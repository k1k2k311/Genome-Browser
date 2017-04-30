import codoncal

import res

import search

import data_access


data_access.get_all_coding_seqs() = extract_seq


def chr3precal_per:
    return codoncal.count_perce_codons (extract_seq)

# expectred result : { 'codon' : percentage, ... } dictionary form


def chr3precal_rev:
    return codoncal.relev_perce_codons (extract_seq)

# expected result" [('codon','AA','rev_per'),(...)....]



