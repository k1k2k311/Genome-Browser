import Regexes_full

import parser_re

import codoncal

import res

import parser_re

import search



#extract sequences

extract_seq = parser_re.load()[1]

#or

extract_seq= parser_re.p_gene

#or

extract_seq= regexes_full.p_trans


#still, data with regex connection needned.
# make extract_seq as one single line, should be '' form)


def chr3precal_per:
    return codoncal.count_perce_codons (extract_seq)

# expectred result : { 'codon' : percentage, ... } dictionary form


def chr3precal_rev:
    return codoncal.relev_perce_codons (extract_seq)

# expected result" [('codon','AA','rev_per'),(...)....]



