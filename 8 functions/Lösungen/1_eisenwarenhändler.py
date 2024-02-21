"""
Aufgabe: Schreibe eine Funktion, die für eine gegebene Anzahl Schrauben, Muttern
und Unterlegscheiben den Endpreis berechnet.
Preise:
Schrauben: 7 ct
Muttern 4 ct
Unterlegescheiben: 2 ct
"""

def baumarkt(s, m, u):
    # Schrauben, Muttern, Unterlegescheiben
    return s * 7 + m * 4 + u * 2

endpreis = baumarkt(50, 32, 22)
print(f"Endpreis: {endpreis/100} €")