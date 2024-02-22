"""
Aufgabe: Entwickle ein Programm, welches dir aus EINER Funktion mehrere neue Funktionen
generieren kann. Am Ende sollst du die Zahl 5 sowohl verdoppeln, verdreifachen als auch
das Quadrat berechnen können.
Hinweis: Nutze die anonyme lambda-Funktion.
"""

def ntimes(n):
    return lambda x: x * n

k = 5

doppler = ntimes(2)
dreifacher = ntimes(3)
fuenffacher = ntimes(k)

print(doppler(k))
print(dreifacher(5))
print(fuenffacher(5))
