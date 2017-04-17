# If you are usign MySQLdb,

import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="john",         # your username
                     passwd="megajonhy",  # your password
                     db="jonhydb")        # name of the data base


cur = db.cursor()

cur.execute("SELECT * FROM YOUR_TABLE_NAME")

for row in cur.fetchall():
    print row[0]

db.close()

# If you are usign MySQL.cooonecter,



import mysql.connector
myConnection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
doQuery( myConnection )
myConnection.close()

hostname = 'localhost'
username = 'USERNAME'
password = 'PASSWORD'
database = 'DBNAME'

def doQuery( conn ) :
    cur = conn.cursor()

    cur.execute( "SELECT fname, lname FROM employee" )

    for firstname, lastname in cur.fetchall() :
        print firstname, lastname




#just in case, using sqlite3

import sqlite 3
def find_details(id2find):
  db=sqlite3.connect( # location or inf)
  db.row_facotry=sqlite3.Row
  cursor= db/cursor()
  cursor.execute("select*from surfers")
  rows=cursor.fetchall()
  
  for row in rows:
    if row['id']==id2find
    s['id']=str(row['id'])
    s['name']=row['name']
    s['cds']=row['cds']
    s['aa']=row['aa]
    cursor.close()
    return(s)
  cursor.close()
  return(s)

# test 
lookup_idint(intput("Enter ID"))
surfer=find_details(lookup_id)
if surfer:
  print("ID:    "+ surfer(['id'])
  print("Name:   "+surfer(['name'])
  

  






# general format


  #!/usr/bin/python

hostname = 'localhost'
username = 'USERNAME'
password = 'PASSWORD'
database = 'DBNAME'

def doQuery( conn ) :
    cur = conn.cursor()

    cur.execute( "SELECT fname, lname FROM employee" )

    for firstname, lastname in cur.fetchall() :
        print firstname, lastname


print "Using MySQLdb…"
import MySQLdb
myConnection = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
doQuery( myConnection )
myConnection.close()

print "Using pymysql…"
import pymysql
myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
doQuery( myConnection )
myConnection.close()

print "Using mysql.connector…"
import mysql.connector
myConnection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
doQuery( myConnection )
myConnection.close()
