#!/usr/bin/env python3

import re

RECORDS = '/home/greg/Documents/Bioinformatics MSc/biocomp_2/Database_tier/processed_records.txt'
SUMMARY_TABLE = '/home/greg/Documents/Bioinformatics MSc/biocomp_2/Database_tier/summary_table.dat'

# group(1) == gene
p_gene = re.compile(r'CDS[\w\W]+?\/gene="(.+?)"\n')
# group(1) = product
p_product = re.compile(r'\n\s+CDS[\w\W]+?\/product="(.+?)"')
# group(1) == accession
# only matches first accession no. if there are >1
p_accession = re.compile(r'\nACCESSION\s{3}(\w+?)[\n|\s]')
# group(1) == locus
p_locus = re.compile(r'\nFEATURES[\w\W]+?source[\w\W]+?\/map="(.+?)"\n')

# create list of gene records
with open(RECORDS, 'r') as gbk_file:
        records = gbk_file.read().split('\n//\n')
# removes blank record at the end
records = records[:-1]

# writing table data in mysql-readable format for bulk-loading
with open(SUMMARY_TABLE, 'w') as output:
        for gene in records:
                row_data = ''
                if p_gene.search(gene):
                        row_data += (p_gene.search(gene).group(1) + '|')
                else:
                        row_data += 'NULL|'
                if p_product.search(gene):
                        row_data += (p_product.search(gene).group(1) + '|')
                else:
                        row_data += 'NULL|'
                row_data += (p_accession.search(gene).group(1) + '|')
                if p_locus.search(gene):
                        row_data += (p_locus.search(gene).group(1) + '\n')
                else:
                        row_data += 'NULL\n'
                output.write(row_data)
                # remove last '\n' character from the file?
