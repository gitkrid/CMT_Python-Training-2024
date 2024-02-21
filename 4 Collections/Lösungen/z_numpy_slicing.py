import numpy as np


a = np.array([[57, 67, 33, 44, 8, 63, 6, 7, 9, 67],
              [23, 56, 17, 36, 12, 50, 14, 29, 28, 64],
              [31, 41, 21, 37, 26, 45, 40, 51, 24, 43],
              [50, 26, 53, 35, 26, 57, 18, 13, 53, 28],
              [21, 17, 16, 43, 41, 56, 31, 44, 33, 35],
              [57, 56, 63, 43, 64, 20, 48, 22, 5, 24]])

# zweitletzte Spalte, Zeile 2 bis 5 (exklusive)
print(a[2:5, -2])

# Zeilen zwischen 1 und 2 (exklusiv), d.h. nur die erste Zeile, Spalten 2 bis 4 (exklusiv)
# Warum 2D Array? weil wir theoretisch mehrere Zeilen zurückgeben
print(a[1:2, 2:4])

# -6. Zeile und Spalte 3 bis 6 (exklusive), nur 1D Array, weil nur eine Zeile
print(a[-6, 3:6])

# Merkregel: Slices für Zeile und Spalte = 2D Array
# nur einmal Slice = 1D Array
# kein Slice = einzelnes Element

print(a[4][-3])

