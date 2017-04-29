import mysql.connector

dbname = "lg001"
dbhost = "hope"
dbuser = "lg001"
dbpass = "--------"
port = 3306

db = mysql.connector.connect(host=dbhost, port=port,
                             user=dbuser, db=dbname, passwd=dbpass)

sql = "select * from summary"

cursor = db.cursor()
nrows = cursor.execute(sql)

for row in cursor:
    GI = row[0]
    gene = row[1]
    product = row[2]
    accession = row[3]
    locus = row[4]

print(GI[0], gene[0], product[0], accession[0], locus[0])
