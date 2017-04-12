import re

enzymes= {'BamHI':r"GGATCC",'EcoRI':r"GAATTC"}

sequence = 'AAGGATCCAGAATTCAAGGATCCAAC'


#Main Idea

for k in enzymes.keys():
    find=re.finditer(enzymes[k],sequence)
    for match in find:
        find_st=match.start()
        find_end=match.end()
        print(k,str(find_st),str(find_end))

#Some error occured on "return" function, it does not print out multiple result,

def giveme_res (sequence):
    for k in enzymes.keys():
        find=re.finditer(enzymes[k],sequence)
        for match in find:
            find_st=match.start()
            find_end=match.end()
            return (k,str(find_st),str(find_end)
		    
print(giveme_res('AAGGATCCAGAATTCAAGGATCCAAC'))

#Therefore, I wrote print at the end instead, however "none" result pop up at the end

def giveme_res (sequence):
    for k in enzymes.keys():
        find=re.finditer(enzymes[k],sequence)
        for match in find:
            find_st=match.start()
            find_end=match.end()
            print (k,str(find_st),str(find_end)
		

print(giveme_res('AAGGATCCAGAATTCAAGGATCCAAC'))
		    
		    
		

