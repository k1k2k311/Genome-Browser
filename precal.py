import database.data_access as data_acess

import codoncal

import res

import csv  

data_access.get_all_coding_seqs() = extract_seq


def chr3precal_per():
    return codoncal.count_perce_codons (extract_seq)

# expectred result : { 'codon' : percentage, ... } dictionary form


def chr3precal_rev():
    return codoncal.relev_perce_codons (extract_seq)

# expected result" [('codon','AA','rev_per'),(...)....]


with open('./chromosome_codon_usage.csv', 'w') as csvfile:
    fieldnames = ['codon', 'percentage','relevant ratio']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'codon':chr3precal_rev()[0], 'percentage' : 'chr3precal_per[chr3precal_rev()[0]]','ratio' : 'chr3precal_rev[2]})
        


