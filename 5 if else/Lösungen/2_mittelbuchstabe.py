"""
Aufgabe: (einfach) Schreibe ein Programm, welches dir zu einem String den mittleren
Buchstaben zurückgibt. Sollte es keine Mitte geben, gib ein "?" zurück.
Bsp.:
"Schranken" -> "a"
"Autobahn" -> "?"
"""

wort1 = "Schranken"
wort2 = "Autobahn"

laenge1 = len(wort1)
if laenge1 % 2 == 0:
    print("?")
else:
    print(wort1[int((laenge1 - 1) / 2)])

laenge2 = len(wort2)
if laenge2 % 2 == 0:
    print("?")
else:
    print(wort2[int((laenge2 - 1) / 2)])
