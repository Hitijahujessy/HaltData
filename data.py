from pathlib import Path
import csv
import matplotlib.pyplot as plt

path = Path('Halt_jongeren__delictgroep__kenmerken.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

periode_totaal, periode_mannen, periode_vrouwen = [], [], []
delicten_totaal, delicten_mannen, delicten_vrouwen = [], [], []

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

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(periode_totaal, delicten_totaal, c='red')
ax.plot(periode_mannen, delicten_mannen)
ax.plot(periode_vrouwen, delicten_vrouwen, c='green')

# Format plot
ax.set_title("Delicten jongeren 12 tot 18 jaar", fontsize=24)
ax.set_xlabel("Periode", fontsize=16)
ax.set_ylabel("Totaal delicten", fontsize=16)
ax.tick_params(labelsize=16)

ax.axis([2005, 2022, 0, 25000])
ax.ticklabel_format(axis='x', useLocale=True)

plt.show()
