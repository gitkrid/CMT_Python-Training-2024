"""
Aufgabe: Schreibe eine Funktion, die dir zu einem gegeben Wort eine Liste
der Indizes zurückgibt, wo das Wort Großbuchstaben beinhaltet.
Bsp.:
hAlLO
-> [1, 3, 4]

Hinweis: Die Funktion .isupper() gibt einen boolschen Wert zurück. True = Buchstabe
ist großgeschrieben, False = Buchstabe ist klein
"""


def capital_indizes(wort):
    # Rückgabeliste
    r = []
    for i, buchstabe in enumerate(wort):
        if buchstabe.isupper():
            r.append(i)
    return r

wort = "hAlLO"
print(capital_indizes(wort))
