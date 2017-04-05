class CodonFrequency

def codoncal()

degen_dict = {}
for codons in degenerated:
    for codon in codons:
        degen_dict[codon] = codons

#query_codons

max_seq = len(seq)
query_codons = [seq[i:i+3] for i in range(0, max_seq, 3)]

#prepare dictio of counts:

counts = defaultdict(int)
for codon in query_codons:
    counts[codon] +=1

#actual calculation of frecuencies

data = {}
for codon in query_codons:
    if codon in  degen_dict:
        totals = sum(counts[deg] for deg in degen_dict[codon])
        frecuency = float(counts[codon]) / totals
    else:
        frecuency = 1.00

    data[codon] = frecuency

#print results

for codon, frecuency in data.iteritems():
    return "%s  -> %.2f" %(codon, frecuency)
