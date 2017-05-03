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


def get_coding_seq(accession):

    sql = "select coding_seq from coding_sequence where accession = %s;" % accession
    cursor = db.cursor()
    nrows = cursor.execute(sql)
    data = cursor.fetchone()
    coding_seq = data[0]
    return coding_seq


def get_full_seq_and_positions(accession):

    sql = "select * from full_sequence where accession = %s;" % accession
    cursor = db.cursor()
    nrows = cursor.execute(sql)
    data = cursor.fetchone()
    full_seq = data[1]
    coding_start = data[2]
    coding_end = data[3]
    partial_5 = data[4]
    partial_3 = data[5]
    full_coordinates = data[6]
    return [full_seq, int(coding_start), int(coding_end), partial_5, partial_3, full_coordinates]


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


def search_by_accession(accession):

    sql = "select * from summary where accession = %s;" % accession
    cursor = db.cursor()
    nrows = cursor.execute(sql)
    data = cursor.fetchone()
    gene = data[0]
    product = data[1]
    accession = data[2]
    locus = data[3]
    summary = [gene, product, accession, locus]
    return summary



# use WHERE column LIKE '%search%' for searches on gene, locus or product
# search on locus: take into account ranges (e.g. 3p2.1-3p2.4) - here we would want to return records that match
# 3p2.1, 3p2.2, 3p2.3 and 3p2.4

# get_gene_details(accession) is not yet written
