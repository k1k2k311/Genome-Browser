#!/usr/bin/env python3

PATH = '/home/greg/Documents/Bioinformatics MSc/biocomp_2/processed_records_1.txt'

with open(PATH, 'r') as file:
    records = file.read().split('\n//\n')

import re

# NB: use regex101.com to check efficiency/speed (no.of steps)
# e.g. [\w\W] is much better than (.|\n)
# it seems more specific patterns often take fewer 'steps' and are quicker
    # e.g. starting with 'source[\w\W]+?' rather than just '\/db_xref...'
# only 1 capturing group used in each pattern
# where possible, use quantifiers like abc[\w\W]{,20}?def instead of abd[\w\W]+?def
    # otherwise ALL of the characters after abc will be checked to see if they match 'def'

# not the cytogenetic band; often the same as accession
p_locus = re.compile(r'LOCUS\s+([A-Z0-9_]+)\s')

# Sequence length in bp (whole record, not just CDS)
p_len = re.compile(r'LOCUS\s+[A-Z0-9_]+\s+(\d+)\sbp')

# Modification date
p_date = re.compile(r'LOCUS.+?\s(.+)$', re.MULTILINE)

# Definition
# (.+) is enough to capture, as no record has a definition longer than 1 line
p_def = re.compile(r'\nDEFINITION\s+(.+)$', re.MULTILINE)

# Accession
p_acc = re.compile(r'\nACCESSION\s{3}(\w+?)[\n|\s]')

# Version
p_vers = re.compile(r'\nVERSION\s+([A-Z0-9\.]+?)\s')

# GI
p_gi = re.compile(r'\nVERSION.+?GI:([0-9]+?)\n')

# Keywords
p_kwds = re.compile(r'\nKEYWORDS\s+(.+)$', re.MULTILINE)

# REFERENCE
p_ref = re.compile(r'')

# FEATURES ##################

# source (always same as p_len i.e. seq len from the LOCUS row)
# use whichever one is quicker? This one is according to regex101.com
p_src = re.compile(r'source\s{10}1\.\.(\d+)')

# source /organism
p_org = re.compile(r'source[\w\W]+?\/organism="(.+?)"')

# source /mol_type="genomic DNA"
p_moltype = re.compile(r'source[\w\W]+?\/mol_type="genomic DNA"')

# source /db_xref="taxon:____"
p_taxon = re.compile(r'source[\w\W]+?\/db_xref="taxon:(.+?)"')

# source /chromosome="3"
p_chrom = re.compile(r'source[\w\W]+?\/chromosome="[3|III]"')

# source /map="__"
p_map = re.compile(r'source[\w\W]+?\/map="(.+?)"')

# source /clone="__"
p_clone = re.compile(r'source[\w\W]+?\/clone="([\w\W]+?)"')

# source /cell_line="__"
p_cell_line = re.compile(r'source[\w\W]+?\/cell_line="([\w\W]+?)"')

# CDS ########
# NB: need to ignore any CDS features after the first one (alt splice variants)

# CDS region - several regexes best?
p_CDS = re.compile(r'CDS\s{13}([\w\W]+?)\n\s+\/')
p_CDS_simple = re.compile(r'CDS\s{13}(\d+)\.\.(\d+)')
p_CDS_partial5 = re.compile(r'CDS\s{13}<?(\d+)\.\.>?(\d+)')
p_CDS_join = re.compile(r'CDS\s{13}([\w\W]+?)\n\s+\/')
p_CDS_complement = re.compile(r'CDS\s{13}([\w\W]+?)\n\s+\/')


# codon start qualifier - the first position AFTER the start codon
p_codon_start = re.compile(r'CDS\s{13}[\w\W]+?\n\s+\/codon_start=(\d+)')

# 
p_ = re.compile(r'')

# /translation (amino acid 1-letter seq)
p_trans = re.compile(r'CDS[\w\W]+?\/translation="([\w\W]+?)"')

# 
p_ = re.compile(r'')

