"""
Für Kim und Manuel.
Zunächst werde ich ein Beispiel zeigen, wie so ein Kassenautomat aussehen
könnte. Danach wird ein Übung folgen, in der ihr euer bisheriges Wissen
testen könnt.
"""

# eine Datenbank (nur ein Dictionary) mit Preisen für Lebensmittel
# alle Preise in CHF natürlich ;)
lebensmittelpreise = {
    "Birchermüsli": 1.25, # 300 g
    "Tirggel": 3.80, # 100 g
    "Käse": 3.00, # 250 g
    "Brot": 4.20, # 400 g
    "Wein": 8.35, # 750 ml
    "Kartoffeln": 2.89, # 1 kg
    "Milch": 2.00, # 1 l
    "Wurst": 3.70, # 100 g
    "Apfel": 2.99, # 1 kg
    "Spargel": 8.99 # 1 kg
}

# eine Liste von Lebensmitteln, die gekauft werden sollen
einkaufsliste = ["Käse", "Brot", "Milch", "Birchermüsli", "Apfel"]

# eine Variable, um den Gesamtpreis zu tracken
gesamtpreis = 0 # wir haben noch nichts gekauft

# wir können das Kassenband und die Kasse mit einer for loop simulieren
# ein Kassenband holt sich nach und nach jedes Lebensmittel, also:
# für jedes Lebensmittel auf der Einkaufsliste ...
for lebensmittel in einkaufsliste:
    # ... gib mir aus dem Dictionary den Preis für dieses Lebensmittel
    preis = lebensmittelpreise[lebensmittel]
    # erhöhe den Gesamtpreis um den preis, den wir uns eben aus der Datenbank
    # geholt haben
    gesamtpreis += preis # Erinnerung: das ist das gleiche wie gesamtpreis = gesamtpreis + preis

# wir nutzen ein f-string, um uns den Gesamtpreis auszugeben
print(f"Gesamtpreis: {gesamtpreis} CHF")


# als nächstes muss der Kunde bezahlen
# dafür erstellen wir zwei Variablen
kartenguthaben = 9.44 # ... der Käufer ist Student und es ist Monatsende
bargeld = 24.98

# wir fragen den Kunden, wie er bezahlen möchte
print("Wie möchten Sie bezahlen? Möglichkeiten: 'bar', 'karte', 'klauen'")
bezahlmethode = input()

# wir prüfen mit if, elif und else, wofür sich der Kunde entschieden hat
if bezahlmethode == "karte":
    # jetzt können wir prüfen, ob Genug Geld vorhanden ist
    if kartenguthaben >= gesamtpreis:
        # wir ziehen den Preis vom Guthaben ab
        kartenguthaben -= gesamtpreis
        # und bestätigen den Kauf
        print("Viel Spaß mit Ihrem Einkauf")
    # falls nicht genug Geld vorhanden ist
    else:
        print("Sie haben nicht genug Geld auf der Karte")
        print("Bitte lassen Sie Ihren Einkauf hier und verlassen Sie den Laden")

elif bezahlmethode == "bar":
    # wieder prüfen, ob Genug Geld vorhanden ist
    if bargeld >= gesamtpreis:
        # Geld abziehen
        bargeld -= gesamtpreis
        # und den Einkauf bestätigen
        print("Viel Spaß mit Ihrem Einkauf")
    else:
        print("Sie haben nicht genug Bargeld")
        print("Bitte lassen Sie Ihren Einkauf hier und verlassen Sie den Laden")

elif bezahlmethode == "klauen":
    print("FASST DEN DIEB!")

# falls die Eingabe vom Benutzer fehlerhaft ist
else:
    print("Diese Bezahlmethode akzeptieren wir nicht.")


print("ENDE BEISPIEL \n")

"""
jetzt folgen die Aufgaben
Aufgaben, die mit einem * markiert sind, können unabhängig gelöst werden

Aufgabe 1: (leicht) Bei der Bezahlmethode 'karte' soll zusätzlich nach einer PIN gefragt
werden. Schreibt mit Hilfe einer zusätzlichen if-else-Abfrage, ob die eingegebene
PIN korrekt ist.
Zusatz: (mittel) Meistens hat man drei Versuche, um die PIN richtig einzugeben. Ergänze
das Programm durch eine for-loop, welche eine PIN-Abfrage genau dreimal zulässt.
Hinweis: das Wort "break" zwingt Python aus einer Schleife (z.B. for-loop)
auszubrechen und diese vorzeitig zu beenden.
Hier nachzulesen: https://www.programiz.com/python-programming/break-continue
"""

# Lösungen:
# Aufgabe 1
kartenguthaben = 1302.22 # Zahltag

# wir fragen den Kunden erneut, wie er bezahlen möchte
print("Wie möchten Sie bezahlen? Möglichkeiten: 'bar', 'karte', 'klauen'")
bezahlmethode = input()

if bezahlmethode == "karte":
    # drei Versuche
    for versuch in range(3):
        # PIN eingeben
        print("Bitte geben Sie Ihre PIN ein:")
        pin = input()
        if pin == "1337": # korrekte PIN ist 1337
            print("Erfolgreiche PIN-Eingabe")
            # jetzt können wir prüfen, ob Genug Geld vorhanden ist
            if kartenguthaben >= gesamtpreis:
                # wir ziehen den Preis vom Guthaben ab
                kartenguthaben -= gesamtpreis
                # und bestätigen den Kauf
                print("Viel Spaß mit Ihrem Einkauf")
                # break, weil sonst die PIN erneut abgefragt wird
            # falls nicht genug Geld vorhanden ist
            else:
                print("Sie haben nicht genug Geld auf der Karte")
                print("Bitte lassen Sie Ihren Einkauf hier und verlassen Sie den Laden")
            break
        else:
            print(f"Falsche PIN, Sie haben {2-versuch} Versuche übrig")


print("ENDE AUFGABE 1\n")

"""
Aufgabe 2*: (mittel) Der Kunde ist Mitarbeiter bei der SV Group und möchte
mit seiner Mitarbeiterkarte (Badge) zahlen. Nutzt er diese Bezahlmethode bekommt
er 15% Rabatt auf alle Lebensmittel und sammelt zusätzlich Firmentreuepunkte.
Pro CHF gibt es 10 Punkte auf dem Firmenkonto. Es wird abgerundet, weil man im Leben
nichts geschenkt bekommt. :)
Implementiere die hier beschriebene Funktionalität. Überlege dir, ob es sinnvoll ist,
die Treuepunkte vor oder nach dem Rabatt zu vergeben.
"""

# Aufgabe 2
# wir legen zunächst ein Mitarbeiterkonto in Form eines Dictionaries an
mitarbeiter = {
    "name": "Kim",
    "personalnummer": 59132,
    "treuepunkte": 370,
    "rabatt": 0.15,
    "guthaben": 56.00
}

# wir fragen den Kunden erneut, wie er bezahlen möchte
# klauen geht nicht mehr, weil SV Group-Mitarbeiter ehrliche Menschen sind
print("Wie möchten Sie bezahlen? Möglichkeiten: 'bar', 'karte', 'batch'")
bezahlmethode = input()

# wir prüfen wieder mit if, elif und else, wofür sich der Kunde entschieden hat
# das ist alles nur von oben kopiert, allerdings ohne PIN-Abfrage für eine
# bessere Übersichtlichkeit
if bezahlmethode == "karte":
    # jetzt können wir prüfen, ob Genug Geld vorhanden ist
    if kartenguthaben >= gesamtpreis:
        # wir ziehen den Preis vom Guthaben ab
        kartenguthaben -= gesamtpreis
        # und bestätigen den Kauf
        print("Viel Spaß mit Ihrem Einkauf")
    # falls nicht genug Geld vorhanden ist
    else:
        print("Sie haben nicht genug Geld auf der Karte")
        print("Bitte lassen Sie Ihren Einkauf hier und verlassen Sie den Laden")

elif bezahlmethode == "bar":
    # wieder prüfen, ob Genug Geld vorhanden ist
    if bargeld >= gesamtpreis:
        # Geld abziehen
        bargeld -= gesamtpreis
        # und den Einkauf bestätigen
        print("Viel Spaß mit Ihrem Einkauf")
    else:
        print("Sie haben nicht genug Bargeld")
        print("Bitte lassen Sie Ihren Einkauf hier und verlassen Sie den Laden")

elif bezahlmethode == "badge":
    # nun wenden wir den Rabatt an, weil der Kunde offensichtlich ein
    # Mitarbeiter ist
    discount = gesamtpreis * mitarbeiter["rabatt"]
    gesamtpreis_neu = gesamtpreis - discount
    # prüfen, ob genug Guthaben vorhanden ist
    if mitarbeiter["guthaben"] >= gesamtpreis_neu:
        # Geld vom Guthaben abziehen
        mitarbeiter["guthaben"] -= gesamtpreis_neu
        print("Viel Spaß mit Ihren Produkten!")
        # wir erhöhen die Treuepunkte des Mitarbeiters (vor dem Rabatt natürlich)
        # um den entsprechenden Preis, den wir bezahlen müssen
        treuepunkte = int(gesamtpreis * 10) # Erinnerung: bei int wird alles nach dem Komma abgeschnitten
        mitarbeiter["treuepunkte"] += treuepunkte
        print(f"Sie haben durch diesen Einkauf {treuepunkte} Treuepunkte erhalten.")
    else:
        print("Bitte laden Sie Ihre Karte auf.")

# falls die Eingabe vom Benutzer fehlerhaft ist
else:
    print("Diese Bezahlmethode akzeptieren wir nicht.")

print("ENDE AUFGABE 2\n")


"""
Aufgabe 3*: (leicht) Erstelle eine Datenbank mit Produkten, die der Mitarbeiter
mit Treuepunkten erwerben kann. Der Hauptpreis ist ein Abendessen mit Kim und Manuel.
Erstelle anschließend 3 verschiedene Mitarbeiterkonten, die unterschiedliche Lebensmittel
einkaufen. Die 3 Mitarbeiter könnten Kim, Manuel und Marc sein. Weil Marc
als Externer beschäftigt ist, erhält er nur 60% der Treuepunkte, die ein
vollwertiger Mitarbeiter bekäme. Berechne die Treuepunkte der Mitarbeiter
entsprechend ihrer Einkaufslisten.
"""

# Aufgabe 3
# Datenbank (Dictionary) mit Preisen für Treuepunkte
treue_preise = {
    "Bodensee-Bootsfahrt": 600,
    "Abendessen": 1000, # Hauptgewinn
    "Sprachkurs-Schwyzerdütsch": 300
}

# drei Mitarbeiter anlegen
mitarbeiter_manuel = {
    "name": "Manuel",
    "personalnummer": 48291,
    "treuepunkte": 410,
    "rabatt": 0.15,
    "guthaben": 34.00,
    "einkaufsliste": ["Brot", "Wurst", "Kartoffeln", "Käse"]
}

mitarbeiter_kim = {
    "name": "Kim",
    "personalnummer": 68575,
    "treuepunkte": 230,
    "rabatt": 0.15,
    "guthaben": 79.00,
    "einkaufsliste": ["Birchermüsli", "Apfel", "Tirggel", "Spargel"]
}

externer_marc = {
    "name": "Marc",
    "treuepunkte": 40,
    "rabatt": 0.05,
    "guthaben": 62.00,
    "einkaufsliste": ["Wein", "Wein", "Wein", "Wein"]
}

# wir brauchen 3 for-loops, für jeden Mitarbeiter eine
# diese simulieren sozusagen wieder das Kassenband
preis_manuel = 0
for lebensmittel in mitarbeiter_manuel["einkaufsliste"]:
    preis = lebensmittelpreise[lebensmittel]
    preis_manuel += preis

# Treuepunkte berechnen
treuepunkte_manuel = int(preis_manuel * 10)

# Mitarbeiterkonto aktualisieren
mitarbeiter_manuel["treuepunkte"] += treuepunkte_manuel


preis_kim = 0
for lebensmittel in mitarbeiter_kim["einkaufsliste"]:
    preis = lebensmittelpreise[lebensmittel]
    preis_kim += preis

# Treuepunkte berechnen
treuepunkte_kim = int(preis_kim * 10)

# Mitarbeiterkonto aktualisieren
mitarbeiter_kim["treuepunkte"] += treuepunkte_kim


preis_marc = 0
for lebensmittel in externer_marc["einkaufsliste"]:
    preis = lebensmittelpreise[lebensmittel]
    preis_marc += preis

# Treuepunkte berechnen
treuepunkte_marc = int(preis_marc * 6) # 60% von 10 = 6

# Mitarbeiterkonto aktualisieren
externer_marc["treuepunkte"] += treuepunkte_marc


# zum Schluss, alle Treuepunkte vergleichen
print(f"Treuepunkte von Manuel: {mitarbeiter_manuel['treuepunkte']}")
print(f"Treuepunkte von Kim: {mitarbeiter_kim['treuepunkte']}")
print(f"Treuepunkte von Marc: {externer_marc['treuepunkte']}")
