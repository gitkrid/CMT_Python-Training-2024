"""
Kontext: Sie arbeiten an einem kleinen Projekt zur Verwaltung eines Buchkatalogs
für eine lokale Bibliothek. Die Bibliothek möchte ihre Büchersammlung in einem
digitalen Format speichern, um leichter auf Informationen zu den Büchern zugreifen
und diese verwalten zu können. JSON (JavaScript Object Notation) ist aufgrund
seiner Einfachheit und Lesbarkeit das bevorzugte Format für die Speicherung der
Daten. Ihre Aufgabe ist es, ein Python-Skript zu schreiben, das das Lesen von
Buchdaten aus einer JSON-Datei, das Hinzufügen neuer Bücher und das Aktualisieren
vorhandener Einträge ermöglicht.

Anforderungen:
    - Lesen von Buchdaten: Schreiben Sie eine Funktion, die die Buchdaten aus
    einer JSON-Datei liest und diese in einer für den Benutzer lesbaren Form ausgibt.

    - Hinzufügen eines neuen Buchs: Implementieren Sie eine Funktion, die es
    ermöglicht, ein neues Buch zur JSON-Datei hinzuzufügen. Jedes Buch sollte
    mindestens einen Titel, einen Autor und eine ISBN-Nummer haben.

    - Aktualisieren eines Buchs: Entwickeln Sie eine Funktion, die die Details
    eines vorhandenen Buchs in der JSON-Datei aktualisiert, basierend auf der
    ISBN-Nummer.
"""
import json


def lese_buecher(dateipfad):
    try:
        with open(dateipfad, 'r') as file:
            buecher = json.load(file)
            for buch in buecher:
                print(f"Titel: {buch['titel']}, Autor: {buch['autor']}, ISBN: {buch['isbn']}")
    except FileNotFoundError:
        print(f"Die Datei {dateipfad} wurde nicht gefunden.")


def buch_hinzufuegen(dateipfad, titel, autor, isbn):
    try:
        with open(dateipfad, 'r+') as file:
            buecher = json.load(file)
            buecher.append({"titel": titel, "autor": autor, "isbn": isbn})
            file.seek(0)
            json.dump(buecher, file, indent=4)
            print(f"Buch '{titel}' wurde hinzugefügt.")
    except FileNotFoundError:
        print(f"Die Datei {dateipfad} wurde nicht gefunden.")


def buch_aktualisieren(dateipfad, isbn, neuer_titel=None, neuer_autor=None):
    try:
        with open(dateipfad, 'r+') as file:
            buecher = json.load(file)
            for buch in buecher:
                if buch["isbn"] == isbn:
                    if neuer_titel:
                        buch["titel"] = neuer_titel
                    if neuer_autor:
                        buch["autor"] = neuer_autor
                    break
            else:
                print(f"Kein Buch mit der ISBN {isbn} gefunden.")
                return
            file.seek(0)
            file.truncate()
            json.dump(buecher, file, indent=4)
            print(f"Buch mit der ISBN {isbn} wurde aktualisiert.")
    except FileNotFoundError:
        print(f"Die Datei {dateipfad} wurde nicht gefunden.")


lese_buecher('file handling/buecher.json')

buch_hinzufuegen('file handling/buecher.json', 'Neues Buch', 'Neuer Autor', '1122334455')
buch_aktualisieren('file handling/buecher.json', '1122334455', neuer_titel="Neues Buch Titel Update", neuer_autor="Autor Update")


