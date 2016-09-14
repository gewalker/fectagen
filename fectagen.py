#!/usr/bin/env python
# trifecta generator
import itertools
outfile = open('trifecta_chart.html', 'w')
racers = range(1, 9, 1)
fecta = 3
chart_cols = 8
chart_rows = 10
trifecta_iterator = itertools.permutations(tuple(racers), fecta)
tri = list(trifecta_iterator)
tricellcount = len(tri) + 1
trirows = []
for rowstart in range(0, len(tri), chart_cols):
    trirows.append(tri[rowstart:rowstart + chart_cols])

outfile.write('<html>\n<head>\n<title>"RoboRally Trifecta 2016"</title>\n')
outfile.write('<style>body {font-size: 100%} table, th, td {border: 1px solid black;padding: 2px;text-align: center;vertical-align: middle;border-spacing: 2px} td {height: 1in;width: 1in;font-size: 1em} #pb{page-break-after: always} #count {vertical-align: top;text-align: left;font-size: 0.5em}</style>\n</head>\n')
outfile.write('<body>\n<table>\n')
curcell = 1
currow = 1
for row in trirows:
    outfile.write("<tr>")
    for cell in row:
        cell = str(cell).translate(None, '(),')
        outfile.write("<td><p id=count>" + str(curcell) + "</p>" + str(cell) + "</td>")
        curcell += 1
    outfile.write("</tr>\n")
    if currow % 10 == 0:
        outfile.write("</table>\n<p id='pb'><!-- PAGEBREAK --></p>\n<table>\n")
    currow += 1
outfile.write("</table>\n")
outfile.write("</body>\n</html>")
