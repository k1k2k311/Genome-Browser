#!/usr/bin/env python3

import re

p1 = re.compile(r'\nVERSION.+?GI:([0-9]+?)\n')     # group(1) == GI
p2 = re.compile(r'CDS(.|\n)+?\/gene="(.+?)"\n')    # group(2) == gene
p3 = re.compile(r'\n\s+CDS(.|\n)+?\/product="(.+?)"')    # group(2) = product
p4 = re.compile(r'\nACCESSION(\s){3}(\w+?)(\n|\s)')    # group(2) == accession
        # only taking first accession no. if there are >1
p5 = re.compile(r'\nFEATURES(.|\n)+?source(.|\n)+?\/map="(.+?)"\n')    # group(3) = locus

# create iterator of gene records
with open('./chrom_CDS_3', 'r') as gbk_data:
        records = gbk_data.read().split('\n//\n')

#test:
#print(records[1])
#print(records[2])

# for some reason there is one extra empty record (no. 387) at the end,
# which translates to a row of NULLS in the summary_table.dat file

# open empty data file for writing table attributes
fo = open('./summary_table.dat', 'w')
for gene in records:
        if p1.search(gene):
                fo.write(p1.search(gene).group(1) + '|')
        else:
                fo.write('NULL|')
        if p2.search(gene):
                fo.write(p2.search(gene).group(2) + '|')
        else:
                fo.write('NULL|')
        if p3.search(gene):
                fo.write(p3.search(gene).group(2) + '|')
        else:
                fo.write('NULL|')
        if p4.search(gene):
                fo.write(p4.search(gene).group(2) + '|')
        else:
                fo.write('NULL|')
        if p5.search(gene):
                fo.write(p5.search(gene).group(3))
        else:
                fo.write('NULL')
        fo.write('\n')

fo.close()


# TABLE 2
#fo = open("chrom_3_table_2.dat", "w")



# LOAD DATA INFILE "chrom_3_summary.dat" INTO TABLE genome
# FIELDS TERMINATED BY '|'
# LINES TERMINATED BY '\n';
