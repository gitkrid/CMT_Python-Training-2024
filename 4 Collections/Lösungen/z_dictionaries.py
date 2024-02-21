"""
Wiederholung & Übung zu Dictionaries
"""

# Dictionary erstellen
autohersteller = {
    # Marke : Konzernsitz
    "Mercedes": "Stuttgart",
    "BMW": "München",
    "Audi": "Ingolstadt",
    "Opel": "Rüsselsheim"
}

# Wert (value) über Schlüssel (key) finden
print(f"Hauptsitz von Mercedes ist: {autohersteller['Mercedes']}")

# Erinnerung: wir können auch .get() verwenden
print(f"Hauptsitz von Mercedes ist: {autohersteller.get('Mercedes')}")

# neues Schlüssel-Werte-Paar hinzufügen
# Achtung: existiert der Schlüssel bereits, wird der entsprechende Wert überschrieben
autohersteller["VW"] = "Wolfsburg"

# Wert mit Hilfe des Schlüssels verändern
# nach der Fusion von FCA und PSA gehört Opel zu Stellantis mit Sitz in Hoofddorp
autohersteller["Opel"] = "Hoofddorp"
print(f"Hauptsitz von Opel ist jetzt {autohersteller['Opel']}")

# for loop über das gesamte Dictionary
for hersteller in autohersteller:
    print(hersteller)

# for loop über Schlüssel und Werte
for key, value in autohersteller.items():
    print(f"Autohersteller {key} hat seinen Hauptsitz in {value}")

# nur die Werte (values)
print(autohersteller.values())

# nur die Schlüssel (keys)
print(autohersteller.keys())


"""
Aufgabe: Gegeben ist ein Dictionary mit Götternamen und ihrer zugehörigen Mythologie.
1) Füge einen Gott deiner Wahl hinzu.
2) Ersetze die Mythologie eines Gottes durch ein Fragezeichen '?'.
3) Lass dir alle nordischen Götter ausgeben. (Hinweis: for und if)
"""

goetter = {
    "Zeus": "griechisch",
    "Hera": "griechisch",
    "Mars": "römisch",
    "Odin": "nordisch",
    "Jupiter": "römisch",
    "Thor": "nordisch"
}

# 1)
goetter["Poseidon"] = "griechisch"

# 2)
goetter["Odin"] = "?"

# 3)
for gott in goetter:
    if goetter[gott] == "griechisch":
        print(gott)
