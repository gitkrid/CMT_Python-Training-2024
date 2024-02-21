"""
Aufgabe: Schreibe einen kleinen Übersetzer, der die folgenden Wörter übersetzen
kann:
Baum = jikar
Wald = iljikarem
ich = tix
sehen = valser
vor = olyip
lauter = wagonsk

Zusatz: Versuche mit Hilfe einer if-Anweisung eine schönere Rückgabe zu erzeugen,
falls ein Wort nicht übersetzt werden kann.
"""

uebersetzung = {
    "baum": "jikar",
    "wald": "iljikarem",
    "ich": "tix",
    "sehen": "valser",
    "vor": "olyip",
    "lauter": "wagonsk"
}

eingabe = input("Bitte geben Sie ein Wort ein, dass Sie übersetzen möchten: ")
uebersetzt = uebersetzung.get(eingabe.lower())

if uebersetzt is not None:
    print(uebersetzt)
else:
    print(f"Keine Übersetzung gefunden für: {eingabe}")
