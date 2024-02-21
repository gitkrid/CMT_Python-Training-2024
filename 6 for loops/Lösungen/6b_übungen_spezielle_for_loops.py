"""
Aufgabe 1: Du arbeitest in einer Firma mit mehreren Angestellten, die nach Tarif
bezahlt werden. Von deinem Vorgesetzten bekommst du zwei Listen mit den neuen
Tarifgruppen und dem entsprechenden Gehalt. Du hättest jedoch gerne ein Dictionary,
um effizienter nach einem Gehalt suchen zu können.
Dein Ziel:
>> gehalt.get("Tarifgruppe A1")
45000 # output
"""

tarifgruppen = ["Tarifgruppe A1", "Tarifgruppe A2", "Tarifgruppe C",
                "Tarifgruppe D1.2", "Tarifgruppe D1.2", "Tarifgruppe M",
                "Tarifgruppe P0"]
gehaelter = [32000, 37000, 66000, 52000, 55000, 80000, 120000]

gehalt = {}
for gr, ge in zip(tarifgruppen, gehaelter):
    gehalt[gr] = ge

print(gehalt.get("Tarifgruppe A1"))


# für die Experten: dict comprehension
gehalt2 = {gr: ge for gr, ge in zip(tarifgruppen, gehaelter)}
print(gehalt2)


"""
Aufgabe 2: Zahltag! Lass dir dein gesamtes Dictionary mit einer for loop ausgeben.
Hänge vor der Ausgabe des Gehaltes eine Null an. Beachte: Ändere nicht das
Dictionary selbst, sondern nur den Wert vor der Ausgabe.
"""

for gr, ge in gehalt.items():
    print("Nach dem Zahltag:")
    print(f"{gr} verdient: {ge*10}")
