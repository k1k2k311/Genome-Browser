#v1

def cal(dna):
    counts = {}
    for base1 in ['A', 'T', 'G', 'C']:
        for base2 in ['A', 'T', 'G', 'C']:
            for base3 in ['A', 'T', 'G', 'C']:
                triplet = base1 + base2 + base3
                count = dna.count(triplet)
                counts[triplet] = count
 
print(cal("AGGATAGCTAGCTCC"))


#v2

dna="AGGATAGCTAGCTCC"
counts = {}
for base1 in ['A', 'T', 'G', 'C']:
    for base2 in ['A', 'T', 'G', 'C']:
        for base3 in ['A', 'T', 'G', 'C']:
            triplet = base1 + base2 + base3
            count = dna.count(triplet)
            counts[triplet] = count

print(counts)

#v3

codon_aa={'A':['GCA','GCC','GCG',"GCT"], 'C':['TGC','TGT'], 'D':['GAC','GAT'],
          'E':['GAA','GAG'],'F':['TTC','TTT'], 'G':['GGA','GGC','GGG','GGT'],
          'H':['CAC','CAT'],'K':['AAA','AAG'], 'I':['ATA','ATC','ATT'],
          'L':['CTA','CTC','CTG','CTT','TTA','TTG'],'M':['AUG'],'N':['AAC','AAT'],
          'P':['CCA','CCC','CCG','CCT'],'Q':['CAA','CAG'],
          'R':['AGA','AGG','CGA','CGC','CGG','CGT'],
          'S':['AGC','AGT','TCA','TCC','TCG','TCT'],'T':['ACA','ACC','ACG','ACT'],
          'V':['GTA','GTC','GTG','GTT'],'W':['TGG'],'Y':['TAC','TAT'],
          'Z':['TAA','TAG','TGA']}
          


dna = ""
counts = {}
for base1 in ['A', 'T', 'G', 'C']:
    for base2 in ['A', 'T', 'G', 'C']:
        for base3 in ['A', 'T', 'G', 'C']:
            trinucleotide = base1 + base2 + base3
            count = dna.count(triplet)
            counts[triplet] = count
 

def codoncal(dna):
    count_all={}
    for aa in codon_aa.keys():
        n=0
        for codon in codon_aa[aa]:
            n = n + count[codon]
        count_all[aa] = float(n)
    for aa in codon_aa.keys():
        for codon in codon_aa[aa]:
            if count_all != 0.0:
                freq=count[codon]/all_count[aa]
            else:
                freq=0.0
print(codoncal('AAGAATAAC'))
 



