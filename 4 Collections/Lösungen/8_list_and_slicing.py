"""
Aufgabe: (mittel) Erstelle eine Liste mit Zahlen von 8 bis 1. Gib als nächstes
nur die Werte mit ungeraden Indizes in umgekehrter Reihenfolge aus. Null kann
als gerade angenommen werden.
Bsp.: [8, 7, 6, 5, 4, 3, 2, 1]
> [1, 3, 5, 7]
"""

x = list(range(9, 0, -1))

# wir starten hinten (Index 7) bis zum Index N (Länge der Liste)
# hinterm letzten Doppelpunkt: - sagt wir gehen rückwärts und
# 2 heißt in 2er Schritten
print(x[-1:-len(x):-2])
