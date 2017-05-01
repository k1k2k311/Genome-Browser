#!/usr/bin/env python3

import mysql.connector

dbname = "lg001"
dbhost = "hope"
dbuser = "lg001"
dbpass = "i-tf7on%8"
port = 3306

db = mysql.connector.connect(host=dbhost, port=port,
                             user=dbuser, db=dbname, passwd=dbpass)

def get_all_coding_seqs():

        sql = "select coding_seq from coding_sequence;"
        cursor = db.cursor()
        nrows = cursor.execute(sql)
        all_coding_seqs = ''
        data = cursor.fetchone()
        while data is not None:
                coding_seq = data[0]
                all_coding_seqs += coding_seq
                data = cursor.fetchone()
        return all_coding_seqs

# test:
# all_cds = get_all_coding_seqs()
# print(len(all_cds))


def get_coding_seq(accession):

    sql = "select coding_seq from coding_sequence where accession = %s;" % accession
    cursor = db.cursor()
    nrows = cursor.execute(sql)
    data = cursor.fetchone()
    coding_seq = data[0]
    return coding_seq


def get_summary_table_as_list():

    summary_list = []
    sql = "select * from summary;"
    cursor = db.cursor()
    nrows = cursor.execute(sql)
    data = cursor.fetchone()
    while data is not None:
        gene = data[0]
        product = data[1]
        accession = data[2]
        locus = data[3]
        summary_list.append([gene, product, accession, locus])
        data = cursor.fetchone()
    return summary_list


def search_by_accession(acc):

    sql = "select * from summary where accession = %s;" % acc
    cursor = db.cursor()
    nrows = cursor.execute(sql)
    data = cursor.fetchone()
    gene = data[0]
    product = data[1]
    accession = data[2]
    locus = data[3]
    summary = [gene, product, accession, locus]
    return summary

print(search_by_accession('AB065665'))
