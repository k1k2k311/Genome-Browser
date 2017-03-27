#!/usr/bin/env python3

import cgi;

#Debugging output
import cgitb

#Send errors to browser
cgitb.enable	

#Grab form contents
form = cgi.FieldStorage()

#Get data from fields:
#Radio button search
search_type = form.getvalue("search_type")
#Entered dataif form.getvalue("data"):
    data = form.getvalue("data")
else:
    data = "None entered"

#Entered sequenceif form.getvalue("seq"):
    seq = form.getvalue("seq")
else:
    seq = "None entered"


#analysis type checkbox 
an_type  = form.getlist("an_type")

#Print HTML MIME-TYPE header
print ("Content-type:text/html\n")
print()
html = "<html>\n"
html += "<head>\n"
html += "<title>RGR3 Genome Browser</title>\n"
html += "</head>\n\n"
html += "<body>\n"
html += "<h2>RGR3 Genome Browser Results</h2>\n"

html += "<p>You searched on: <b>" + search_type + "</b></p>\n"
html += "<p>Value entered: <b>" + data + "</b></p>\n"

#sequence textarea
html += "<h2>Your sequence was:</h2>\n"html += "<pre>\n"html += seq html += "</pre>\n"





html += "<p><b>The following types of analysis were performed:</b></p>\n"

#Return unordered list of analysis type chosen
html += "<ul>"for a in an_type:    if a == "dna_seq":        html += "<li>Compete DNA sequence</li>\n"    if a == "aa_seq":        html += "<li>Amino acid sequence</li>\n"    if a == "codon":        html += "<li>Codon frequencies</li>\n"
    if a == "EcoRI":        html += "<li>EcoRI</li>\n"
    if a == "BamHI":        html += "<li>BamHI</li>\n"
    if a == "BsuMI":        html += "<li>BsuMI</li>\n" html += "</ul>\n"

html += "</body>\n"
html += "</html>\n"

print(html)
