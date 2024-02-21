"""
Nachfolgend schauen wir uns ein paar Beispiele zu speziellen for loops an.
"""

# enumerate - zusätzlich zum Element einen Index/Zahl erhalten
cars = ("Mercedes", "Porsche", "BMW", "VW", "Audi")
for i, car in enumerate(cars):
    print(i)
    print(car)


# zip - gleichzeitig über mehrere iterables iterieren
vornamen = ("Andrea", "Markus", "Eileen", "Basti")
namen = ("Müller", "Schwedt", "Schmidt", "Meyer")
for vorname, name in zip(vornamen, namen):
    print(f"Mein Vorname ist: {vorname}")
    print(f"Und mein Nachname ist: {name}")


# über dictionaries iterieren
autohersteller = {
    # Marke : Konzernsitz
    "Mercedes": "Stuttgart",
    "BMW": "München",
    "Audi": "Ingolstadt",
    "Opel": "Rüsselsheim"
}

for key, value in autohersteller.items():
    print(key, ":", value)

for value in autohersteller.values():
    print(value)

for key in autohersteller:
    print(key)


# Kombination aus mehreren, oben genannten Möglichkeiten
for vorname, (marke, sitz) in zip(vornamen, autohersteller.items()):
    print(f"{vorname} fährt einen {marke} und wohnt in {sitz}")
