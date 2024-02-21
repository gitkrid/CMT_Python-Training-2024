"""
Aufgabe: (leicht) Schreibe ein Programm, welches dir die Steuern für unterschiedliche Einkommen berechnet:
Einkommen - Steuersatz
< 9500€ - 0%
9500€ <= x < 20000€ - 14%
20000€ <= x < 45000€ - 23%
45000€ <= x < 67000€ - 37%
67000€ <= x < 89000€ - 44%
>= 89000€ - 53%
"""

def steuern(einkommen):
    if einkommen < 0: return "Fehler, Einkommen kann nicht negativ sein!"
    if einkommen < 9500:
        return einkommen * 0.14
    elif einkommen >= 9500 and einkommen < 20000:
        return einkommen * 0.23
    elif einkommen >= 20000 and einkommen < 45000:
        return einkommen * 0.37
    elif einkommen >= 45000 and einkommen < 67000:
        return einkommen * 0.44
    else:
        return einkommen * 0.53

print(steuern(192000))
