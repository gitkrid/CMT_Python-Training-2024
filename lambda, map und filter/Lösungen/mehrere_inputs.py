"""
Aufgabe: Nutze die map-Funktion, um folgenden Code zu verbessern.
Hinweis: int() ist eine Funktion, mit der wir in Integer typecasten können.
Außerdem könnte split() hilfreich sein.
"""

eingaben = input("Geben Sie 3 durch Leerzeichen getrennte Zahlen ein: ").split()

a, b, c = map(int, eingaben)

print(a, b, c)
