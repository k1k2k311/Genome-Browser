
import re

enzymes= {'BamHI':r"GGATCC",'EcoRI':r"GAATTC",'BsuMI':r"CTCGAG"}

sequence = 'AAGGATCCAGAATTCAAGGATCCAAC'

store_list = []

def giveme_res (sequence):
    for k in enzymes.keys():
        find=re.finditer(enzymes[k],sequence)
        for match in find:
            find_st=match.start()
            find_end=match.end()
            store_list.append((k,str(find_st),str(find_end)))
    return store_list
            

print(giveme_res(sequence))


#for single enzyme find usage,

store_list_single=[]
def single_res(enzyme, sequence):
	find=re.finditer(enzymes[enzyme],sequence)
	for match in find:
		find_st=match.start()
		find_end=match.end()
		store_list_single.append((enzyme,str(find_st),str(find_end)))
	return store_list_single

store_list_custom=[]  gtagta   r'gtagta
					 
def custom_search_res(res_seq,sequence):
	pattern = re.compile(res_seq)
	find= pattern.finditer(sequence)
	for match in find:
		find_st=match.start()
		find_end=match.end()
		store_list_custom.append((res_seq,str(find_st),str(find_end)))
	return stroe_list_custom
	
	
					 
	

