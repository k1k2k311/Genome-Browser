#!/usr/bin/env python3

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
html += '<caption>CHROMOSOME 3</caption>\n'^Mhtml += '<tr>\n'^Mhtml += '<th>Gene name</th>\n'^Mhtml += '<th>Protein product</th>\n'^Mhtml += '<th>GenBank Accession</th>\n'^Mhtml += '<th>Chromosomal location</th>\n'^Mhtml += '</tr>\n'^M
for row in data:
    html += '<tr>\n'^M    html += '<td>' + gene + '</td>\n'^M    html += '<td>' + product + '</td>\n'^M    html += '<td>' + accession + '</td>\n'^M    html += '<td>' + locus + '</td>\n'^M    html += '</tr>\n'
^Mhtml += '</table>\n'
html += '</body>\n'
html += '</html>\n'^Mprint(html)
                                                                                                                                                     19,1          All
