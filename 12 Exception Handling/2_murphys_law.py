"""
"Was schiefgehen kann, wird schief gehen."
Aufgabe: Schau dir die verschiedenen Code-Beispiele an und entscheide,
was schiefgehen kann. Verbessere sie anschließend durch gutes Exception-Handling.
"""

# 1)
zahlen = [1, 2, 3, 4, 5]

for i in range(len(zahlen) + 1):
    print(f"Qudrat von {zahlen[i]}: {zahlen[i]**2}")


# 2)
mitarbeiter = {
    "Max": {"Alter": 30, "Abteilung": "IT"},
    "Lisa": {"Alter": 25, "Abteilung": "Buchhaltung"}
}

name = input("Gib den Namen des Mitarbeiters ein: ")
print(f"Abteilung: {mitarbeiter[name]['Department']}")


# 3)
from datetime import datetime

ereignis_datum_str = input("Gib das Datum des Ereignisses ein (dd.mm.yyyy): ")
ereignis_datum = datetime.strptime(ereignis_datum_str, "%d.%m.%Y")
heute = datetime.now()

tage_bis_ereignis = ereignis_datum - heute
print("Tage bis zum Ereignis: " + tage_bis_ereignis.days)


# 4)
dateiname = input("Gib den Namen der Datei ein, die du lesen möchtest: ")

with open(dateiname, "r") as file:
    inhalt = file.read()
    wortanzahl = len(inhalt.split(" "))
    print(f"Anzahl der Wörter in der Datei: {wortanzahl}")


# 5)
einwohner = [32000, 67000, 198000, 46000]
for i in range(-2, 2):
    print(einwohner / i)
