"""
Aufgabe: Schreibe ein Programm, welches dir die zweitkleinste Nummer
aus einer Liste herausfindet. Überprüfe dein Ergebnis.
Hinweis: Es gibt mehrere Lösungen.
"""

numbers = [0, -2, 5, 7, 8, 5, -3]

unique = list(set(numbers))
unique.sort()
print(unique[1])
