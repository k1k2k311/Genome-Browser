#!/usr/bin/env python3

import cgi;

#Debugging output
import cgitb

#Send errors to browser
cgitb.enable

#Print HTML MIME-TYPE header
print ("Content-type:text/html\n")
print()


ID=("ID")
acc=("acc")
prod=("prod")
loc=("loc")

data=[1,2,3,4,5,6,7,8,9]

#Create summary list table
html = "<html>\n"
html += "<head>\n"
html += "<title>RGR3 Genome Browser</title>\n"
html += "</head>\n\n"
html += "<body>\n"
html += "<table>\n"html += "<tr>\n"html += "<th>Gene ID</th>\n"html += "<th>Genbank Accession</th>\n"html += "<th>Protein product</th>\n"html += "<th>Chromosomal location</th>\n"html += "</tr>\n"
for row in data:
    html += "<tr>\n"    html += "<td>" + ID + "</td>\n"    html += "<td>" + acc + "</td>\n"    html += "<td>" + prod + "</td>\n"    html += "<td>" + loc + "</td>\n"    html += "</tr>\n"
html += "</table>\n"
html += "</body>\n"
html += "</html>\n"print(html)
