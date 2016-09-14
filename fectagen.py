#!/usr/bin/env python
# trifecta generator
import itertools
import argparse
parser = argparse.ArgumentParser(description='Generate an Xfecta sheet for betting on the order of multiple outcomes.')
parser.add_argument('-o', '--file', dest='file')
parser.add_argument('-r', '--racers', dest='racers', help='How many elements to choose from')
parser.add_argument('-x', '--fecta-factor', dest='fecta', help='How many choices to make in each permutation.')
parser.add_argument('-c', '--cols', dest='chart_cols', default=8)
parser.add_argument('-R', '--rows', dest='chart_rows', default=10)
parser.add_argument('-b', '--breaks', dest='breaks', default=True)
parser.add_argument('-p', '--paper', dest='paper', choices=['U', 'A'], default='U', help='Choose between US Letter and 8A page formatting.')
parser.add_argument('-t', '--first-ticket', dest='ticket', help='First ticket serial number.', default=00001)
args = parser.parse_args([1:])

outfile = open(args.file, 'w')
racers = range(1, args.racers, 1)
fecta = args.fecta
chart_cols = args.chart_cols
chart_rows = args.chart_rows
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
