import database.data_access as data_acess

import codoncal

import res

import csv  

data_access.get_all_coding_seqs() = extract_seq


def chr3precal_per():
    return codoncal.count_perce_codons (extract_seq)

# expectred result : { 'codon' : percentage, ... } dictionary form


percentage_a=chr3precal_per()



def chr3precal_rel():
    return codoncal.count_relev_perce_codons (extract_seq)

# expected result" [('codon','AA','ratio'),(...)....]


ratio_a= chr3precal_rel()
 
    
 #v1

with open('./chromosome_codon_usage.csv', 'wb') as csvfile:
    fieldnames = ['codon', 'percentage','relevant ratio']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'codon':'ratio_a[0]', 'percentage' : 'chr3precal_per[percentage_a[0]]','ratio' : 'ratio_a[2]'})
        

        
#v2

# Storing the ratio first
store=[]
def collect_ratio():
    for c in chr3precal_rel():
        store.append(c[2])
    return store
l= collect_ratio()

# and then put the ratio into csv

with open('./chromosome_codon_usage.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in codoncal.items():
        writer.writerow(key, value,l)

                    
