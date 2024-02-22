"""
"Was schiefgehen kann, wird schief gehen."
Aufgabe: Schau dir die verschiedenen Code-Beispiele an und entscheide,
was schiefgehen kann. Verbessere sie anschließend durch gutes Exception-Handling.
"""

# 1)
# zahlen = [1, 2, 3, 4, 5]

# for i in range(len(zahlen) + 1):
#     print(f"Qudrat von {zahlen[i]}: {zahlen[i]**2}")
zahlen = [1, 2, 3, 4, 5]

try:
    for i in range(len(zahlen)):  # Korrigiert den Indexfehler
        print(f"Quadrat von {zahlen[i]}: {zahlen[i]**2}")
except IndexError:
    print("Zugriffsversuch außerhalb der Listenbereiche. Bitte prüfen Sie die Liste.")


# 2)
# mitarbeiter = {
#     "Max": {"Alter": 30, "Abteilung": "IT"},
#     "Lisa": {"Alter": 25, "Abteilung": "Buchhaltung"}
# }

# name = input("Gib den Namen des Mitarbeiters ein: ")
# print(f"Abteilung: {mitarbeiter[name]['Department']}")
mitarbeiter = {
    "Max": {"Alter": 30, "Abteilung": "IT"},
    "Lisa": {"Alter": 25, "Abteilung": "Buchhaltung"}
}

name = input("Gib den Namen des Mitarbeiters ein: ")
try:
    print(f"Abteilung: {mitarbeiter[name]['Abteilung']}")  # Korrektur des Tippfehlers
except KeyError:
    print(f"Keine Informationen verfügbar für: {name}")


# 3)
# from datetime import datetime


# ereignis_datum_str = input("Gib das Datum des Ereignisses ein (dd.mm.yyyy): ")
# ereignis_datum = datetime.strptime(ereignis_datum_str, "%d.%m.%Y")
# heute = datetime.now()

# tage_bis_ereignis = ereignis_datum - heute
# print("Tage bis zum Ereignis: " + tage_bis_ereignis.days)
from datetime import datetime


ereignis_datum_str = input("Gib das Datum des Ereignisses ein (dd.mm.yyyy): ")
try:
    ereignis_datum = datetime.strptime(ereignis_datum_str, "%d.%m.%Y")
    heute = datetime.now()

    tage_bis_ereignis = ereignis_datum - heute
    print("Tage bis zum Ereignis: " + str(tage_bis_ereignis.days))  # Umwandlung in String
except TypeError:
    print("Es gab einen Fehler bei der Berechnung der Tage bis zum Ereignis.")
except ValueError:
    print("Falsches Datumsformat. Bitte verwenden Sie dd.mm.yyyy")



# 4)
# dateiname = input("Gib den Namen der Datei ein, die du lesen möchtest: ")

# with open(dateiname, "r") as file:
#     inhalt = file.read()
#     wortanzahl = len(inhalt.split(" "))
#     print(f"Anzahl der Wörter in der Datei: {wortanzahl}")
dateiname = input("Gib den Namen der Datei ein, die du lesen möchtest: ")

try:
    with open(dateiname, "r") as file:
        inhalt = file.read()
        wortanzahl = len(inhalt.split())
        print(f"Anzahl der Wörter in der Datei: {wortanzahl}")
except FileNotFoundError:
    print(f"Die Datei {dateiname} wurde nicht gefunden. Bitte prüfen Sie den Dateinamen.")



# 5)
# einwohner = [32000, 67000, 198000, 46000]
# for i in range(-2, 2):
#     print(einwohner / i)

einwohner = [32000, 67000, 198000, 46000]
for i in range(-2, 2):
    try:
        print(einwohner / i)
    except ZeroDivisionError:
        print("0 wird übersprungen")
        continue
