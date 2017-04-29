#!/usr/bin/env python3
#file for index and sequence page on gene summary list table creation
import cgi;

#Debugging output
import cgitb

#Send errors to browser
cgitb.enable

#Print HTML MIME-TYPE header
print ('Content-type:text/html\n')
print()


gene=("gene")
product=("product")
accession=("accession")
locus=("locus")

data=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

#Create summary list table
html ='<!DOCTYPE html>\n'
html += '<html>\n'
html += '<head>\n'
html += '<title>RGR3 Genome Browser</title>\n'
html += '<link type="text/css" rel="stylesheet" href="http://student.cryst.bbk.ac.uk/~sr002/css/sumlist.css">\n'
html += '</head>\n\n'
html += '<body>\n'
html += '<table>\n'
html += '<caption>CHROMOSOME 3</caption>\n'
html += '<tr>\n'
html += '<th>Gene name</th>\n'
html += '<th>Protein product</th>\n'
html += '<th>GenBank Accession</th>\n'
html += '<th>Chromosomal location</th>\n'
html += '</tr>\n'
for row in data:
    html += '<tr>\n'
    html += '<td>' + gene + '</td>\n'
    html += '<td>' + product + '</td>\n'
    html += '<td>' + accession + '</td>\n'
    html += '<td>' + locus + '</td>\n'
    html += '</tr>\n'

html += '</table>\n'
html += '</body>\n'
html += '</html>\n'
print(html)
                                                                                                19,1          All
