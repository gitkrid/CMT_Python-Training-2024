"""
Aufgaben:
1.) Schreibe eine Funktion, welche dir zu einer gegebenen Zeile
die nächste Zeile des Pascalschen Dreiecks zurückgibt. Das Pascalsche Dreieck
ist wie folgt aufgebaut:
     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1
Die Ausgabe soll eine Liste sein.

2.) Schreibe eine weitere Funktion, die dir die ersten N Stufen des Pascalschen
Dreiecks mit Hilfe der Funktion aus 1.) berechnet.
Hinweis: Nutze eine zweidimensionale Liste zum Speichern der Zeilen.
"""

# nächste Zeile zu einer gegebenen Zeile berechnen
def next_pascal_from_row(row):
    next_row = [row[0]] # man kann auch 1 schreiben, weil am Rand immer 1 steht
    for i in range(len(row)-1):
        next_row.append(row[i] + row[i+1])
    next_row.append(row[-1]) # man kann auch 1 schreiben, weil am Rand immer 1 steht
    return next_row


# Pascalsches Dreieck für N Stufen berechnen.
def pascal_triangle(N):
    pascal = [[1]]
    for i in range(N-1):
        next_row = next_pascal_from_row(pascal[i])
        pascal.append(next_row)
    return pascal

# Code testen
print(next_pascal_from_row([1, 2, 1]))
print(pascal_triangle(10))
