"""
Aufgabe: Für ein gegebenen String, schreibe ein Programm, das dir einen neuen String
aus den ersten zwei und letzten zwei Zeichen erstellt.
Bsp.: Nikolaushaus -> Nius
Wenn ein Wort weniger als 2 Zeichen hat, soll ein leerer String zurückgegeben werden.
"""

wort = "Strandkorbverkäufer"

def kuerzen(s):
    if len(s) > 2:
        return s[:2] + s[-2:]
    return ""

print(kuerzen(wort))
