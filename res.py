import re

enzymes= {'BamHI':r"GGATCC",'EcoRI':r"GAATTC"}

sequence = 'AAGGATCCAGAATTCAAGGATCCAAC'


def giveme_res (sequence):
    for k in enzymes.keys():
        find=re.finditer(enzymes[k],sequence)
        for match in find:
            find_st=match.start()
            find_end=match.end()
            return (k,str(find_st),str(find_end))
		

print(giveme_res('GGATCCGGATCC'))

dna = "ACTGCATTATATCGTACGAAATTATACGCGCG"
runs = re.finditer(r"ATA", dna)
for match in runs:
    run_start = match.start()
    run_end = match.end()
    print("AT rich region from " + str(run_start) + " to " + str(run_end))

$this not works

def giveme_res(sequence):
    find=re.finditer(r"GGATCC",sequence)
    for match in find:
        find_st=match.start()
        find_end=match.end()
        return (str(find_st),str(find_end))
		

print(giveme_res('GGATCCGGATCC'))



#this works

for k in enzymes.keys():
    find=re.finditer(enzymes[k],sequence)
    for match in find:
        find_st=match.start()
        find_end=match.end()
        print(k,str(find_st),str(find_end))

