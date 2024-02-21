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

Die Funktionen 'split' und 'strip' könnten hilfreich sein.
"""
def lese_kontakte(dateipfad):
    pass

def kontakt_hinzufuegen(dateipfad, name, telefon, email):
    pass

def kontakt_aktualisieren(dateipfad, name, neues_telefon=None, neue_email=None):
    pass
