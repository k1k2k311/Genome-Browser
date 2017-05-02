import collections

# Store codons and its counterpart of amino acids into codon_aa dictionary.
# It is by alphabetical order and 'Z' indicates Stop codon

codon_aa={'GCA':'A','GCC':'A','GCG':'A',"GCT":'A','TGC':'C','TGT':'C','GAC':'D','GAT':'D',
          'GAA':'E','GAG':'E','TTC':'F','TTT':'F','GGA':'G','GGC':'G','GGG':'G','GGT':'G',
          'CAC':'H','CAT':'H','AAA':'K','AAG':'K','ATA':'I','ATC':'I','ATT':'I',
          'CTA':'L','CTC':'L','CTG':'L','CTT':'L','TTA':'L','TTG':'L','ATG':'M','AAC':'N','AAT':'N',
          'CCA':'P','CCC':'P','CCG':'P','CCT':'P','CAA':'Q','CAG':'Q',
          'AGA':'R','AGG':'R','CGA':'R','CGC':'R','CGG':'R','CGT':'R',
          'AGC':'S','AGT':'S','TCA':'S','TCC':'S','TCG':'S','TCT':'S','ACA':'T','ACC':'T','ACG':'T','ACT':'T',
          'GTA':'V','GTC':'V','GTG':'V','GTT':'V','TGG':'W','TAC':'Y','TAT':'Y',
          'TAA':'Z','TAG':'Z','TGA':'Z'}

# the given database(cds) will be written in lowercase, so I need to change it into uppercase first, to calculate.

def upper(cds):
    return cds.upper()



# In our database Ambiguous nucleotides (mostly N) has appeared in sequences , which is not in 4 alphabets-format,nucleotides (A,C,T,G).

# Remove the codons which contains ambiguous nucleotide (we will calculate them seperately later, calling them "unknown amino acids")
# for more information about ambioguous nucleotide, https://genomevolution.org/wiki/index.php/Ambiguous_nucleotide

store=[]
def rem_vague(cds):
    for i in range(0,len(cds),3):
        codon=cds[i:i+3]
        if  codon in codon_aa:
            store.append(codon)
    return "".join(store)
    
    # this function will be used for when we calculate count_relev_perce_codons
    # for count_codons and count_perce_codons, it has own function that exclude codons with ambigous nucleotides.
          


          
# Counts how many each codons appeared in the sequences

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

    # If codon in codon_aa :  <- this line will removes any errors occured with ambigous nucleotides.
          
          
# translation of codons into amino acid seuqnces

def translate(cds, codon_aa):
        return "".join((codon_aa[cds[i:i+3]] for i in range(0, len(cds), 3)))



# calculation of percentage of each codons in sequences

def count_perce_codons(cds):
    counts = collections.defaultdict(int)
    for i in range(0,len(cds),3):
       codon = cds[i:i+3]
       if codon in codon_aa:
           counts[codon] +=(1/(len(cds)/3))*100
    return counts

    # If codon in codon_aa :  <- this line will removes any errors occured with ambigous nucleotides.
    # the reults will be ('codon1': percentage,'codon2':percentage ....)




# calculation of relative ratio of each codons in each amino acids

def count_relev_perce_codons(cds):
    codon_counts = count_codons(cds)
    trans_seq = translate(rem_vague(cds),codon_aa)
    return [(codon, codon_aa[codon], float(codon_counts[codon])/trans_seq.count(codon_aa[codon])) for codon in codon_counts.keys()

     # the reults will be (('codon','Amino Acid','relative ratio'),('codon2','Amino Acid','relative raio')....)



            
# test 1: testing with long seqeucne

cds='AAATTCACATCAAAAGTAGACGATCAGTGGGAGTTAGGTAAGCCGTTAGTACCGATGACGTTTTTACCCGATCTT'

print(count_relev_perce_codons(cds))
print(count_perce_codons(cds))

# test 2 : testing with ambigous nucleotides

cds='AAATTCACATCAAAAGTAGANNXNANTCCA'


print(count_relev_perce_codons(cds))
print(count_perce_codons(cds))

