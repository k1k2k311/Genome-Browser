import collections
codon_aa={'GCA':'A','GCC':'A','GCG':'A',"GCT":'A','TGC':'C','TGT':'C','GAC':'D','GAT':'D',
          'GAA':'E','GAG':'E','TTC':'F','TTT':'F','GGA':'G','GGC':'G','GGG':'G','GGT':'G',
          'CAC':'H','CAT':'H','AAA':'K','AAG':'K','ATA':'I','ATC':'I','ATT':'I',
          'CTA':'L','CTC':'L','CTG':'L','CTT':'L','TTA':'L','TTG':'L','ATG':'M','AAC':'N','AAT':'N',
          'CCA':'P','CCC':'P','CCG':'P','CCT':'P','CAA':'Q','CAG':'Q',
          'AGA':'R','AGG':'R','CGA':'R','CGC':'R','CGG':'R','CGT':'R',
          'AGC':'S','AGT':'S','TCA':'S','TCC':'S','TCG':'S','TCT':'S','ACA':'T','ACC':'T','ACG':'T','ACT':'T',
          'GTA':'V','GTC':'V','GTG':'V','GTT':'V','TGG':'W','TAC':'Y','TAT':'Y',
          'TAA':'Z','TAG':'Z','TGA':'Z'}

def upper(cds):
    return cds.upper()

# remove the codons which contains ambiguous nucleotide
# for more information about ambioguous nucleotide, https://genomevolution.org/wiki/index.php/Ambiguous_nucleotide

store=[]
def rem_vague(cds):
    for i in range(0,len(cds),3):
        codon=cds[i:i+3]
        if  codon in codon_aa:
            store.append(codon)
    return "".join(store)
    
    # this function will be used for when we calculate count_relev_perce_codons
    # for count_codons and count_perce_codons, it has own function that 


def count_codons(cds):
    vague=0
    counts = collections.defaultdict(int)
    for i in range(0,len(cds),3):
       codon = cds[i:i+3]
       if codon in codon_aa:
           counts[codon] += 1
       else:    
           vague+=1
    return counts

def translate(cds, codon_aa):
        return "".join((codon_aa[cds[i:i+3]] for i in range(0, len(cds), 3)))


def count_relev_perce_codons(cds):
    codon_counts = count_codons(cds)
    trans_seq = translate(rem_vague(cds),codon_aa)
    return [(codon, codon_aa[codon], float(codon_counts[codon])/trans_seq.count(codon_aa[codon])) for codon in codon_counts.keys()]


def count_perce_codons(cds):
    counts = collections.defaultdict(int)
    for i in range(0,len(cds),3):
       codon = cds[i:i+3]
       if codon in codon_aa:
           counts[codon] +=(1/(len(cds)/3))*100
    return counts

# test 1: testing with long seqeucne

cds='AAATTCACATCAAAAGTAGACGATCAGTGGGAGTTAGGTAAGCCGTTAGTACCGATGACGTTTTTACCCGATCTT'

print(count_relev_perce_codons(cds))
print(count_perce_codons(cds))

# test 2 : testing with ambigous nucleotides

cds='AAATTCACATCAAAAGTAGANNXNANTCCA'



print(count_relev_perce_codons(cds))
print(count_perce_codons(cds))

