"""
Kontext: Sie entwickeln ein einfaches Kontaktbuch-Verwaltungssystem für einen
kleinen Unternehmer, der seine geschäftlichen Kontakte effizient speichern,
abrufen und aktualisieren möchte. Das System soll die Kontakte in einer Textdatei
speichern, wodurch die Notwendigkeit einer komplexen Datenbankinfrastruktur entfällt.
Jeder Kontakt besteht aus einem Namen, einer Telefonnummer und einer E-Mail-Adresse.
Die Aufgabe umfasst das Lesen von Kontaktdaten aus einer Datei, das Hinzufügen
neuer Kontakte und das Aktualisieren bestehender Kontakte.

Anforderungen:

    - Lesen von Kontakten: Schreiben Sie eine Funktion, die die Kontaktdaten
    aus einer Datei liest und jede Kontaktinformation als Eintrag in einer Liste
    zurückgibt. Jeder Eintrag sollte ein Dictionary sein, das Name, Telefonnummer
    und E-Mail enthält.

    - Hinzufügen eines neuen Kontakts: Implementieren Sie eine Funktion, die es
    ermöglicht, einen neuen Kontakt der Datei hinzuzufügen. Stellen Sie sicher,
    dass die neue Kontaktinformation korrekt formatiert und am Ende der Datei
    hinzugefügt wird.

    - Aktualisieren eines Kontakts: Entwickeln Sie eine Funktion, die einen
    bestehenden Kontakt aktualisiert. Wenn der Benutzer einen Kontakt
    aktualisieren möchte, sucht die Funktion nach dem Namen des Kontakts in der
    Datei und ermöglicht es, die Telefonnummer und/oder die E-Mail-Adresse zu
    aktualisieren.

Hinweise:
    Verwenden Sie eine einfache Textdatei (kontakte.txt) als Speicher für die Kontakte.
    Für jeden Kontakt sollten die Informationen in einer Zeile gespeichert werden,
    getrennt durch ein spezifisches Trennzeichen, z.B. Name;Telefonnummer;E-Mail.
    Stellen Sie sicher, dass Ihre Funktionen robust sind und Fehler, wie z.B. das
    Hinzufügen eines Kontakts, der bereits existiert, oder das Aktualisieren
    eines Kontakts, der nicht gefunden wurde, angemessen behandeln.

Die Funktionen 'split' und 'strip' könnten hilfreich sein.
"""
def lese_kontakte(dateipfad):
    kontakte = []
    try:
        with open(dateipfad, 'r') as datei:
            for zeile in datei:
                name, telefon, email = zeile.strip().split(';')
                kontakte.append({'Name': name, 'Telefonnummer': telefon, 'E-Mail': email})
    except FileNotFoundError:
        print(f"Die Datei {dateipfad} wurde nicht gefunden.")
    return kontakte


def kontakt_hinzufuegen(dateipfad, name, telefon, email):
    with open(dateipfad, 'a') as datei:
        datei.write(f"{name};{telefon};{email}\n")
    print(f"Kontakt {name} wurde hinzugefügt.")


def kontakt_aktualisieren(dateipfad, name, neues_telefon=None, neue_email=None):
    kontakte_gefunden = False
    try:
        with open(dateipfad, 'r') as datei:
            zeilen = datei.readlines()
        
        with open(dateipfad, 'w') as datei:
            for zeile in zeilen:
                aktueller_name, telefon, email = zeile.strip().split(';')
                if aktueller_name == name:
                    if neues_telefon:
                        telefon = neues_telefon
                    if neue_email:
                        email = neue_email
                    kontakte_gefunden = True
                datei.write(f"{aktueller_name};{telefon};{email}\n")
        
        if kontakte_gefunden:
            print(f"Kontakt {name} wurde aktualisiert.")
        else:
            print(f"Kontakt {name} wurde nicht gefunden.")
    except FileNotFoundError:
        print(f"Die Datei {dateipfad} wurde nicht gefunden.")


# Test Code
kontakte = lese_kontakte('file handling/Lösungen/kontakte.txt')
for kontakt in kontakte:
    print(kontakt)

kontakt_hinzufuegen('file handling/Lösungen/kontakte.txt', 'Neuer Kontakt', '1234567890', 'neuer@beispiel.de')
kontakte = lese_kontakte('file handling/Lösungen/kontakte.txt')
print(kontakte[-1])

kontakt_aktualisieren('kontakte.txt', 'Max Mustermann',
                      neues_telefon='000111222',
                      neue_email='max.neu@beispiel.de')
kontakte = lese_kontakte('file handling/Lösungen/kontakte.txt')
for kontakt in kontakte:
    if kontakt['Name'] == 'Max Mustermann':
        print(kontakt)
