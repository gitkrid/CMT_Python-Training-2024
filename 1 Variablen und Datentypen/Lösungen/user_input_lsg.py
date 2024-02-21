"""
Aufgabe: Ein Benutzer gibt mehrere Zahlen in die Konsole ein. Diese sind Strings (str).
Wandle diese Zahlen entsprechend ihres "wahren" Typs um und ordne sie der Größe nach.
Hinweis: Mit der Funktion sort() lässt sich eine Liste sortieren: liste.sort()
"""

a = "3"
b = "11"
c = "4.2"
d = "9"
e = "0.5"
f = "6"

# alles in eine Liste packen und in den richtigen Typ konvertieren
zahlen = [int(a), int(b), float(c), int(d), float(e), int(f)]

# Liste sortieren
zahlen.sort()

# Ausgabe
print("Sortiert:", zahlen)
