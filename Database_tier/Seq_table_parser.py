#!/usr/bin/env python3

import time
import re

t0 = time.time()

DATA = '/home/greg/Documents/Bioinformatics MSc/biocomp_2/Database_tier/processed_records.txt'
OUT = '/home/greg/Documents/Bioinformatics MSc/biocomp_2/Database_tier/seq_table.dat'

# reads raw genbank file and creates list of records based on delimiter '//'
with open(DATA, 'r') as file:
    records = file.read().split('\n//\n')

# gets rid of empty record at the end
records = records[:-1]

# 'p' refers to pattern
p_acc = re.compile(r'\nACCESSION\s{3}(\w+?)[\n|\s]')
p_CDS = re.compile(r'CDS\s{13}(?:[\w\W]+?)\/translation="[A-Z\n\s]+?"')
p_CDS_simple = re.compile(r'CDS\s{13}(?:complement\()?(\d+)\.\.(\d+)')
p_CDS_partial = re.compile(r'CDS\s{13}(?:complement\()?<?(\d+)\.\.>?(\d+)')
p_CDS_partial_5 = re.compile(r'CDS\s{13}(?:complement\()?<(\d+)\.\.>?(\d+)')
p_CDS_partial_3 = re.compile(r'CDS\s{13}(?:complement\()?<?(\d+)\.\.>(\d+)')
p_CDS_join = re.compile(r'CDS\s{13}(?:complement\()?join\(([\w\W]+?)\)')
p_CDS_complement = re.compile(r'CDS\s{13}complement')
p_codon_start = re.compile(r'CDS\s{13}[\w\W]+?\n\s+\/codon_start=(\d+)')
p_trans = re.compile(r'CDS[\w\W]+?\/translation="([\w\W]+?)"')
p_ori = re.compile(r'ORIGIN[\s\n]+1([\w\W]+)')

# includes ambiguous nucleotide letters
    # e.g. 'r' (purine: 'a' or 'g') pairs with 'y' (pyrimidine: 't' or 'c')
basepair_dict = {'a': 't', 'c': 'g', 'g': 'c', 't': 'a',
                 'n': 'n', 'r': 'y', 'y': 'r', 'k': 'm', 'm': 'k', 's': 's', 'w': 'w',
                 'b': 'v', 'v': 'b', 'd': 'h', 'h': 'd'}

stop_codons = ['taa', 'tga', 'tag']

# TO DO:
# extract string of cds positions (e.g. '1..10,30..40,60..65') for every record - all ' <>\n' stripped
# this can be a column in the table - middle layer operations on the full seq string can use indices from here
# extract simple yes/no info for partial 5', partial 3', complement - these can be columns in table
# include checks in the parser that warn of inconsistent / wrong format of data

max_len = 0
inconsistencies = 0

output = open(OUT, 'w')

for gene in records:
    accession = p_acc.search(gene).group(1)
    # captures the first splice variant; all subsequent re searches regarding the CDS feature are carried out on CDS
    # rather than gene, to ensure all of the matches come from the first splice variant
    CDS = p_CDS.search(gene).group(0)
    raw_seq = p_ori.search(gene).group(1)
    # iteratively removes each unwanted character from raw_seq
    for char in ' 1234567890\n\t':
        seq = raw_seq.replace(char, '')
        raw_seq = seq
    if p_CDS_simple.search(CDS):
        start = int(p_CDS_simple.search(CDS).group(1))
        end = int(p_CDS_simple.search(CDS).group(2))
        coding_seq = seq[start - 1:end]
    elif p_CDS_partial_5.search(CDS) or p_CDS_partial_3.search(CDS):
        start = int(p_CDS_partial.search(CDS).group(1)) + int(p_codon_start.search(CDS).group(1)) - 1
        # alternatively, end = start + (3*len(translation)) - 1
        end = int(p_CDS_partial.search(CDS).group(2))
        coding_seq = seq[start-1:end]
    elif p_CDS_join.search(CDS):
        coding_seq = ''
        match = p_CDS_join.search(CDS).group(1)
        # gets rid of spaces, newlines, '<' and '>'
        for char in ' \n<>':
            trimmed_match = match.replace(char, '')
            match = trimmed_match
        # makes a list of coding position fragments
        split_match = trimmed_match.split(',')
        # splits each list item into [start, end]
        positions = [x.split('..') for x in split_match]
        # first fragment
        start = int(positions[0][0]) + int(p_codon_start.search(CDS).group(1)) - 1
        end = int(positions[0][1])
        first_fragment = seq[start-1:end]
        coding_seq += first_fragment
        # 2nd fragment to last fragment
        for x in positions[1:]:
            start = int(x[0])
            end = int(x[1])
            fragment = seq[start-1:end]
            coding_seq += fragment
    else:
        print('Error: unexpected CDS type for record %s. Not included in output file.' % accession)
        continue

    # create complement strand if needed
    if p_CDS_complement.search(CDS):
        coding_seq = ''.join(basepair_dict[base] for base in coding_seq[::-1])

    # print warnings if dna seq length doesn't match translation length from the record
    translation = p_trans.search(CDS).group(1)
    translation = translation.replace('\n', '').replace(' ', '')
    # in case stop codon has been included in the cds region
    if (coding_seq[-3:] in stop_codons) and (not p_CDS_partial_3.search(CDS)):
        dna_len = len(coding_seq) - 3
        if dna_len != (3 * len(translation)):
            diff = dna_len - (3 * len(translation))
            print('WARNING: DNA for %s is %d bp longer than expected\n' % (accession, diff))
            inconsistencies += 1
    # partial-3' sequences don't necessarily stop at a codon_boundary
    elif p_CDS_partial_3.search(CDS):
        if (len(coding_seq) % 3 == 2) and (coding_seq[-2:] in ['ct', 'gt', 'tc', 'cc', 'ac', 'gc', 'cg', 'gg']):
            dna_len = len(coding_seq) + 1
        else:
            dna_len = len(coding_seq)
        if dna_len // 3 != len(translation):
            diff = (dna_len - (dna_len % 3)) - (3 * len(translation))
            print('WARNING: DNA for %s is %d bp longer than expected\n' % (accession, diff))
            inconsistencies += 1

    # checking maximum length so mysql table can be created correctly
    if len(coding_seq) > max_len:
        max_len = len(coding_seq)

        # format that allows bulk loading to mysql database
    seq_table_format = accession + '|' + coding_seq + '\n'
    output.write(seq_table_format)

output.close()

t1 = time.time()
t_delta = t1-t0
print('time taken: {:.2f} seconds'.format(t_delta))

print('max len: %d' % max_len)

print('dna & protein sequence length do not correspond for %d records' % inconsistencies)
