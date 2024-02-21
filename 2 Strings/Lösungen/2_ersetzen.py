"""
Aufgabe: Schreibe ein Programm, welches einen bestimmten Buchstaben durch ? ersetzt,
außer dem letzten Buchstaben.
Bsp.: Buchstabe a, Valhalla -> V?lh?lla
"""

def ersetzen(wort, buchstabe):
    new = wort[:-1].replace(buchstabe, "?") +  wort[-1]
    return new

print(ersetzen("Valhalla", "a"))



wort = "Valhalla"
new = wort[:-1].replace("a", "?") +  wort[-1]

print(new)


# andere Idee:
# Buchstaben zählen und N - 1 ersetzen
anzahl = wort.count("a")
new = wort.replace("a", "?", anzahl-1)
print(new)
