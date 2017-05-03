#!/usr/bin/env python3

import parser_module

RECORDS = '/home/greg/Documents/Bioinformatics MSc/biocomp_2/database/src/processed_records.txt'
SUMMARY_TABLE = '/home/greg/Documents/Bioinformatics MSc/biocomp_2/database/src/summary_table.dat'
CODING_SEQ_TABLE = '/home/greg/Documents/Bioinformatics MSc/biocomp_2/database/src/coding_seq_table.dat'
FULL_SEQ_TABLE = '/home/greg/Documents/Bioinformatics MSc/biocomp_2/database/src/full_seq_table.dat'


# reads raw genbank file and creates list of records based on delimiter '//'
with open(RECORDS, 'r') as gbk_file:
        records = gbk_file.read().split('\n//\n')

# removes blank record at the end
records = records[:-1]

# writing summary table data in mysql-readable format for bulk-loading
with open(SUMMARY_TABLE, 'w') as output:
    for gene in records:
        row_data = parser_module.parse_gene(gene) + '|'
        row_data += parser_module.parse_product(gene) + '|'
        row_data += parser_module.parse_accession(gene) + '|'
        row_data += parser_module.parse_locus(gene) + '\n'
        output.write(row_data)

# writing coding_sequence table data in mysql-readable format for bulk-loading
with open(CODING_SEQ_TABLE, 'w') as output:
    max_len = 0
    for gene in records:
        accession = parser_module.parse_accession(gene)
        coding_seq = parser_module.parse_coding_seq(gene)
        # format that allows bulk loading to mysql database
        row_data = accession + '|' + coding_seq + '\n'
        output.write(row_data)

        # checking maximum length so mysql table can be created correctly
        if len(coding_seq) > max_len:
            max_len = len(coding_seq)

print('longest coding sequence: %d' % max_len)

# writing summary table data in mysql-readable format for bulk-loading
with open(FULL_SEQ_TABLE, 'w') as output:
    for gene in records:
        cds = parser_module.parse_cds_feature(gene)
        accession = parser_module.parse_accession(gene) + '|'
        if parser_module.parse_complement_or_not(cds):
            full_seq = parser_module.parse_full_reverse_complement(gene) + '|'
        else:
            full_seq = parser_module.parse_full_dna(gene) + '|'
        coding_start = str(parser_module.parse_coding_boundaries(gene)[0]) + '|'
        coding_end = str(parser_module.parse_coding_boundaries(gene)[1]) + '|'
        partial_5 = parser_module.parse_partial(cds)[0] + '|'
        partial_3 = parser_module.parse_partial(cds)[1] + '|'
        full_coordinates = parser_module.parse_full_cds_coordinates(gene) + '|'
        translation = parser_module.parse_translation(cds)
        row_data = accession + full_seq + coding_start + coding_end + partial_5 + partial_3
        row_data += full_coordinates + translation + '\n'
        output.write(row_data)
