#!/usr/bin/env python3

import re

CHROM_3_PATH = '/home/greg/Documents/Bioinformatics MSc/biocomp_2/Database_tier/chrom_CDS_3'
OUT = '/home/greg/Documents/Bioinformatics MSc/biocomp_2/Database_tier/processed_records.txt'
REPORT = '/home/greg/Documents/Bioinformatics MSc/biocomp_2/Database_tier/processing_report.txt'

# matches records with remote joins
p_remote_join = re.compile(r'CDS\s{13}join\([<\d\.,\n\s]*?[A-Z]{1,2}\d{3,8}\.\d:')
# matches records with non-functional (pseudo) genes
p_pseudo = re.compile(r'\/pseudo')
# translation
p_trans = re.compile(r'CDS[\w\W]+?\/translation="([\w\W]+?)"')
# accession number
p_acc = re.compile(r'\nACCESSION\s{3}(\w+?)[\n|\s]')

with open(CHROM_3_PATH, 'r') as gbk_data:
    records = gbk_data.read().split('\n//\n')
# gets rid of the blank record at the end (created by the split)
records = records[:-1]

print('starting number of records: ', len(records))
removed_records = []

new_records = []
for gene in records:
    if p_remote_join.search(gene) is None and p_pseudo.search(gene) is None and p_trans.search(gene) is not None:
        new_records.append(gene)
    else:
        removed_records.append(p_acc.search(gene).group(1))

print('number of records after processing: ', len(new_records))
print('number of removed records: ', len(removed_records))

# writing 'report' of removed records
with open(REPORT, 'w') as file:
    file.write('Removed records:\n\n')
    for accession in removed_records:
        file.write(accession)
        file.write('\n')

# writing output file (this will be the input for the parsing script)
with open(OUT, 'w') as file:
    for gene in new_records:
        file.write(gene)
        file.write('\n//\n')
