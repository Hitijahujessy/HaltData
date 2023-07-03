from pathlib import Path
import csv

path= Path('Halt_jongeren__delictgroep__kenmerken.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

periode_totaal, periode_mannen, periode_vrouwen = [], [], []
delicten_totaal, delicten_mannen, delicten_vrouwen = [], [], []

for index, column_header in enumerate(header_row):
    print(index, column_header)

for row in reader:
    geslacht = str(row[0])
    periode = int(row[3])
    delict = int(row[4])

    if geslacht == 'Totaal mannen en vrouwen':
       periode_totaal.append(periode)
       delicten_totaal.append(delict)
    
    elif geslacht == 'Mannen':
        periode_mannen.append(periode)
        delicten_mannen.append(delict)

    elif geslacht == 'Vrouwen':
        periode_vrouwen.append(periode)
        delicten_vrouwen.append(delict)
    
print(periode_totaal)
print(delicten_totaal) 
print(periode_mannen)
print(delicten_mannen)
print(periode_vrouwen)
print(delicten_vrouwen)