#!/usr/bin/env python3

import cgi;

#Debugging output
import cgitb

#Send errors to browser
cgitb.enable

#Print HTML MIME-TYPE header
print ('Content-type:text/html\n')
print()
html ='<!DOCTYPE html>\n'
html += '<html>\n'
html += '<head>\n'
html += '<meta charset="utf-8">\n'
html += '<title>RGR3 Genome Browser</title>\n'

#css stylesheet
html += '<link type="text/css" rel="stylesheet" href="http://student.cryst.bbk.ac.uk/~sr002/css/codon.css">\n'
html += '</head>\n\n'
html += '<body>\n'

#Create table, title
html += '<table>\n'
html += '<caption>CODON USAGE IN HOMO SAPIENS CHROMOSOME 3</caption>\n'
html += '<tr>\n'
#...and coloumn headings
html += '<th> </th>\n'
html += '<th>Codon</th>\n'
html += '<th>Amino Acid</th>\n'
html += '<th>%</th>\n'
html += '<th>Ratio</th>\n'
html += '<th>Codon</th>\n'
html += '<th>Amino Acid</th>\n'
html += '<th>%</th>\n'
html += '<th>Ratio</th>\n'
html += '<th>Codon</th>\n'
html += '<th>Amino Acid</th>\n'
html += '<th>%</th>\n'
html += '<th>Ratio</th>\n'
html += '<th>Codon</th>\n'
html += '<th>Amino Acid</th>\n'
html += '<th>%</th>\n'
html += '<th>Ratio</th>\n'
html += '<th> </th>\n'
html += '</tr>\n'

#Create table row 1 UUU,UCU,UAU,UGU
html += '<tr>\n'
html += '<td class="ucag"><b>U</b></td>\n'
html += '<td rowspan="2">UUU</td>\n'
html += '<td rowspan="2">Phe(F)</td>\n'
html += '<td>%</td>\n'
html += '<td class="ratio">ratio</td>\n'
html += '<td rowspan="2">UCU</td>\n'
html += '<td rowspan="2">Ser(S)</td>\n'
html += '<td>%</td>\n'
html += '<td class="ratio">ratio</td>\n'
html += '<td rowspan="2">UAU</td>\n'
html += '<td rowspan="2">Tyr(Y)</td>\n'
"WWW/cgi-bin/codon.py" 649L, 19356C                                                                                                                                                       1,1           Top
