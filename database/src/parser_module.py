import re

# all re patterns that are needed to parse the data
p_accession = re.compile(r'\nACCESSION\s{3}(\w+?)[\n|\s]')
p_CDS = re.compile(r'CDS\s{13}(?:[\w\W]+?)\/translation="[A-Z\n\s]+?"')
p_CDS_complement = re.compile(r'CDS\s{13}complement')
p_CDS_join = re.compile(r'CDS\s{13}(?:complement\()?join\(([\w\W]+?)\)')
# 'simple' coordinates are only cover one range e.g. 50..>148
p_CDS_simple = re.compile(r'CDS\s{13}(?:complement\()?<?(\d+)\.\.>?(\d+)')
p_codon_start = re.compile(r'CDS\s{13}[\w\W]+?\n\s+\/codon_start=(\d+)')
p_gene = re.compile(r'CDS[\w\W]+?\/gene="(.+?)"\n')
p_length = re.compile(r'source\s{10}1\.\.(\d+)')
p_locus = re.compile(r'\nFEATURES[\w\W]+?source[\w\W]+?\/map="(.+?)"\n')
p_partial_3 = re.compile(r'..>\d')
p_partial_5 = re.compile(r'<\d+?..')
p_product = re.compile(r'\n\s+CDS[\w\W]+?\/product="(.+?)"')
p_translation = re.compile(r'CDS[\w\W]+?\/translation="([\w\W]+?)"')

# basepair_dict used to create reverse complements where required
# it includes ambiguous nucleotide letters
# e.g. 'r' (purine: 'a' or 'g') pairs with 'y' (pyrimidine: 't' or 'c')
basepair_dict = {'a': 't', 'c': 'g', 'g': 'c', 't': 'a',
                 'n': 'n', 'r': 'y', 'y': 'r', 'k': 'm', 'm': 'k', 's': 's', 'w': 'w',
                 'b': 'v', 'v': 'b', 'd': 'h', 'h': 'd'}

stop_codons = ['taa', 'tga', 'tag']


# list of functions in alphabetical order

def parse_accession(gene):
    # takes a single genbank record string as input and returns the accession number

    accession = p_accession.search(gene).group(1)
    
    return accession


def parse_coding_seq(gene):
    # takes a single genbank record string as input and returns the dna sequence of the coding region
    # involves discriminating between different types of positional information (partial, joins, complements, etc)
    # for partial records, the dna is trimmed so that it's in frame and only includes complete codons

    full_dna = parser_module.parse_full_dna(gene)
    # extracts only the first CDS feature if there is more than one splice variant
    cds = parser_module.parse_CDS_feature(gene).group(0)

    if p_CDS_simple.search(cds):
        start = int(p_CDS_simple.search(cds).group(1))
        end = int(p_CDS_simple.search(cds).group(2))
        coding_seq = full_dna[start - 1:end]
    elif p_CDS_join.search(cds):
        match = p_CDS_join.search(cds).group(1)
        # gets rid of spaces, newlines, '<' and '>'
        for char in ' \n<>':
            trimmed_match = match.replace(char, '')
            match = trimmed_match
        # makes a list of coding position fragments
        split_match = trimmed_match.split(',')
        # splits each list item into [start, end]
        positions = [x.split('..') for x in split_match]
        # first fragment
        start = int(positions[0][0])
        end = int(positions[0][1])
        first_fragment = seq[start - 1:end]
        coding_seq = first_fragment
        # 2nd fragment to last fragment
        for x in positions[1:]:
            start = int(x[0])
            end = int(x[1])
            fragment = seq[start - 1:end]
            coding_seq += fragment
    # If the CDS coordinates are not matched by either of the re patterns
    else:
        accession = p_accession.search(gene).group(1)
        print('Warning: unexpected CDS type for record %s.' % accession)

    # trims incomplete codons (can't be used for codon usage calculation) from partial ends
    # ensures coding_seq length is a multiple of 3 and is in the correct reading frame
    if p_CDS_complement.search(cds):
        # creates reverse complement
        coding_seq = ''.join(basepair_dict[base] for base in coding_seq[::-1])
        # if reverse complement is partial at the 5' end
        if p_partial_3.search(cds):
            coding_seq = coding_seq[(int(p_codon_start.search(cds).group(1)) - 1):]
        # if reverse complement is partial at the 3' end
        if p_partial_5.search(cds):
            if len(coding_seq) % 3 == 1:
                coding_seq = coding_seq[:-1]
            if len(coding_seq) % 3 == 2:
                # these 8 combinations of the first two positions in a codon code for the same amino acid
                # regardless of the 3rd base
                if coding_seq[-2:] in ['ct', 'gt', 'tc', 'cc', 'ac', 'gc', 'cg', 'gg']:
                    # 'n' means any nucleotide
                    coding_seq += 'n'
                else:
                    coding_seq = coding_seq[:-2]
    else:
        if p_partial_5.search(cds):
            coding_seq = coding_seq[(int(p_codon_start.search(cds).group(1)) - 1):]
        if p_partial_3.search(cds):
            if len(coding_seq) % 3 == 1:
                coding_seq = coding_seq[:-1]
            if len(coding_seq) % 3 == 2:
                if coding_seq[-2:] in ['ct', 'gt', 'tc', 'cc', 'ac', 'gc', 'cg', 'gg']:
                    coding_seq += 'n'
                else:
                    coding_seq = coding_seq[:-2]

    # print warnings if dna seq length doesn't match translation length from the record
    # indicates an error in the coding sequence parsing above
    translation = (p_trans.search(cds).group(1)).replace('\n', '').replace(' ', '')
    # in case stop codon has been included in the cds region
    if coding_seq[-3:] in stop_codons:
        dna_len = len(coding_seq) - 3
    else:
        dna_len = len(coding_seq)
    if dna_len != (3 * len(translation)):
            diff = dna_len - (3 * len(translation))
            accession = p_accession.search(gene).group(1)
            print('WARNING: DNA for %s is %d bp longer than expected\n' % (accession, diff))

    return coding_seq


def parse_cds_feature(gene):
    # takes a single genbank record string as input and returns the whole CDS feature
    # captures only the first CDS feature is matched (if there are splice variants);
    # carrying out subsequent re searches on this cds, rather than the whole gene, ensures data integrity

    cds = p_CDS.search(gene).group(0)
    
    return cds


def parse_coding_boundaries(gene):
    # takes a single genbank record string as input and returns the coding region boundaries
    # coordinates for complement records are dealt with

    cds = p_CDS.search(gene).group(0)
    if p_CDS_simple.search(cds):
        coding_start = int(p_CDS_simple.search(cds).group(1))
        coding_end = int(p_CDS_simple.search(cds).group(2))
    elif p_CDS_join.search(cds):
        # this is inefficient; re pattern that matches first and last digits in join coordinates would be better
        match = p_CDS_join.search(cds).group(1)
        # gets rid of spaces, newlines, '<' and '>'
        for char in ' \n<>':
            trimmed_match = match.replace(char, '')
            match = trimmed_match
        # makes a list of coding position fragments
        split_match = trimmed_match.split(',')
        # splits each list item into [start, end]
        positions = [x.split('..') for x in split_match]
        coding_start = int(positions[0][0])
        coding_end = int(positions[-1][1])
    else:
        accession = p_accession.search(gene).group(1)
        print('Warning: unexpected CDS type for record %s.' % accession)
        
    if p_CDS_complement.search(cds):
        dna_length = int(p_length.search(gene).group(1))
        coding_start = (dna_length + 1) - coding_end
        coding_end = (dna_length + 1) - coding_start

    return coding_start, coding_end


def parse_complement_or_not(cds):
    # returns True if complement

    if p_CDS_complement:
        complement = True
    else:
        complement = False
    
    return complement


def parse_full_cds_coordinates(gene):
    # takes a single genbank record string as input and returns the full coding region coordinates
    # coordinates for complement records are dealt with

    cds = p_CDS.search(gene).group(0)
    if p_CDS_simple.search(cds):
        coding_start = p_CDS_simple.search(cds).group(1)
        coding_end = p_CDS_simple.search(cds).group(2)
        positions = [coding_start, coding_end]
        full_coordinates = '..'.join(x for x in positions)
    elif p_CDS_join.search(cds):
        match = p_CDS_join.search(cds).group(1)
        # gets rid of spaces, newlines, '<' and '>'
        for char in ' \n<>':
            trimmed_match = match.replace(char, '')
            match = trimmed_match
        split_match = trimmed_match.split(',')
        full_coordinates = [x.split('..') for x in split_match]
    else:
        accession = p_accession.search(gene).group(1)
        print('Warning: unexpected CDS type for record %s.' % accession)
        
    if p_CDS_complement.search(cds):
        dna_length = int(p_length.search(gene).group(1))
        full_coordinates = [x for x in reversed(full_coordinates)]
        for x in full_coordinates:
            start = (dna_length + 1) - x[1]
            end = (dna_length + 1) - x[0]
            x[0] = start
            x[1] = end
        full_coordinates = ','.join(['..'.join(x) for x in full_coordinates])

    return full_coordinates


def parse_full_dna(gene):
    # takes a single genbank record string as input and returns the whole dna sequence

    raw_dna = p_ori.search(gene).group(1)
    # iteratively removes each unwanted character from raw_seq
    for char in ' 1234567890\n\t':
        pure_dna = raw_dna.replace(char, '')
        raw_dna = pure_dna
    
    return pure_dna


def parse_full_reverse_complement(gene):
    # takes a single genbank record string as input and returns the reverse complement of the whole dna sequence
    # separate from the parse_full_dna function because that is quicker when the reverse complement is only needed
    # for the coding region

    raw_dna = p_ori.search(gene).group(1)
    # iteratively removes each unwanted character from raw_seq
    for char in ' 1234567890\n\t':
        pure_dna = raw_dna.replace(char, '')
        raw_dna = pure_dna
    reverse_complement = ''.join(basepair_dict[base] for base in raw_dna[::-1])
    
    return reverse_complement


def parse_gene(cds):
    # takes a single genbank record string as input and returns the gene name, or 'NULL' if none found

    if p_gene.search(cds):
        gene_name = p_gene.search(cds).group(1)
    else:
        gene_name = 'NULL'
    
    return gene_name


def parse_locus(gene):
    # takes a single genbank record string as input and returns the chromosomal location, or 'NULL' if none found

    if p_locus.search(gene):
        locus = p_locus.search(gene).group(1)
    else:
        locus = 'NULL'
    
    return locus


def parse_partial(cds):
    # takes a single genbank record string as input and returns tuple of partial cds information
    # note that the complement sequences are on the reverse strand, so if the partial_5 pattern matchs,
    # its actually partial at the 3' end of the reverse complement, and vice versa

    partial_5 = 'no'
    partial_3 = 'no'
    if p_CDS_complement.search(cds):
        if p_partial_5.search(cds):
            partial_3 = 'yes'
        if p_partial_3.search(cds):
            partial_5 = 'yes'
    else:
        if p_partial_5.search(cds):
            partial_5 = 'yes'
        if p_partial_3.search(cds):
            partial_3 = 'yes'
    
    return partial_5, partial_3


def parse_product(cds):
    # takes a single genbank record string as input and returns the gene name, or 'NULL' if none found

    if p_product.search(cds):
        product = p_product.search(cds).group(1)
    else:
        product = 'NULL'
    
    return product


def parse_translation(cds):

    translation = p_translation(cds).group(1)
    
    return translation
