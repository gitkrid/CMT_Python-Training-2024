"""
Aufgabe: Erzeuge eine zweidimensionale Liste, die dir die "kleine Einmaleins-Tafel" ausgibt.
In der ersten Spalte sollen die Zahlen mal 1 stehen, in der zweiten Spalte mal 2 usw.
Bsp.:
[ 1 2 3 4 ...]
[ 2 4 6 8 ...]
[ ...        ]
"""
N = 10
einmaleins = []

# Werte berechnen
for i in range(N):
    einmaleins.append([])
    for j in range(N):
        wert = (i+1)*(j+1)
        einmaleins[i].append(wert)

# Ergebnis: N x N Matrix

# Werte schön ausgeben
# Möglichkeit 1:
for row in einmaleins:
    print(row)

# Möglichkeit 2:
import numpy as np
einmaleins = np.array(einmaleins)
print(einmaleins)