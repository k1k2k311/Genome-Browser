import database.data_access as data_access
import re

# Eznyme lists are stored as dictionary

enzymes= {'BamHI':r"GGATCC",'EcoRI':r"GAATTC",'BsuMI':r"CTCGAG"}

sequence = data_access.get_full_seq_and_positions()[0]


# Finding whole restriction enzyme site

store_list = []

def giveme_res (sequence):
    for k in enzymes.keys():
        find=re.finditer(enzymes[k],sequence)
        for match in find:
            find_st=match.start()
            find_end=match.end()
            store_list.append((k,str(find_st),str(find_end)))
    return store_list

    # Format will be (('enzyme','start number of restriction enzyme site in seuqnece','end number of restriction enzyme site') ....)
            


# For single enzyme finding usage,

store_list_single=[]
def single_res(enzyme, sequence):
	find=re.finditer(enzymes[enzyme],sequence)
	for match in find:
		find_st=match.start()
		find_end=match.end()
		store_list_single.append((enzyme,str(find_st),str(find_end)))
	return store_list_single


# For custom search

store_list_custom=[]  

def custom_search_res(res_seq,sequence):
	pattern = re.compile(res_seq)
	find= pattern.finditer(sequence)
	for match in find:
		find_st=match.start()
		find_end=match.end()
		store_list_custom.append((res_seq,str(find_st),str(find_end)))
	return stroe_list_custom

        # res_seq is a custom sequence which the user will type, it is their own restriction enzyme site.


#test					 
sequence = 'AAGGATCCAGAATTCAAGGATCCAAC'

print(giveme_res(sequence))
print(single_res('BamHI',sequence))
print(custom_search_res('TTCAAG',sequence))
