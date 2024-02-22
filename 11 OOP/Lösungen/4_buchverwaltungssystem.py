"""
Kontext: In dieser Aufgabe werden Sie ein objektorientiertes Buchverwaltungssystem
für eine Bibliothek entwickeln. Das System soll es ermöglichen, Bücher in einem
digitalen Katalog zu speichern, zu suchen, hinzuzufügen, zu aktualisieren und
zu entfernen. Jedes Buch wird durch Attribute wie Titel, Autor und ISBN-Nummer
repräsentiert. Die Daten sollen in einer JSON-Datei gespeichert werden, um
Persistenz zu gewährleisten.

Ziele:
    - Anwenden von OOP-Prinzipien zur Strukturierung Ihres Codes.
    - Verwenden von Dateioperationen zum Lesen und Schreiben von JSON-Daten.
    - Implementieren von Methoden zum Hinzufügen, Aktualisieren, Entfernen und
    Suchen von Büchern im Katalog.

Teil 1: Buch- und Katalogklassen
    - Buchklasse (Buch): Diese Klasse repräsentiert ein einzelnes Buch mit den
    Attributen titel, autor und isbn.
    - Katalogklasse (Katalog): Diese Klasse verwaltet eine Sammlung von Büchern.
    Sie enthält Methoden zum Hinzufügen, Aktualisieren, Entfernen und Suchen
    von Büchern sowie zum Laden und Speichern des Katalogs in einer JSON-Datei.

Teil 2: Werden Sie selbst kreativ
    - Überlegen Sie welche Methoden und Attribute solch ein Verwaltungssystem
    haben kann? Erweitern Sie Ihre Klassen entsprechend.
    - Ein paar Inspirationen: Erscheinungsjahr, Genre, Statistiken über die
    verschiedenen Kataloge, ...
"""

import json

class Buch:
    def __init__(self, titel, autor, isbn, erscheinungsjahr=None, genre=None):
        self.titel = titel
        self.autor = autor
        self.isbn = isbn
        self.erscheinungsjahr = erscheinungsjahr
        self.genre = genre

    def als_dict(self):
        return {
            "titel": self.titel,
            "autor": self.autor,
            "isbn": self.isbn,
            "erscheinungsjahr": self.erscheinungsjahr,
            "genre": self.genre
        }

class Katalog:
    def __init__(self, dateipfad):
        self.dateipfad = dateipfad
        self.buecher = []
        self.laden()

    def laden(self):
        try:
            with open(self.dateipfad, 'r', encoding='utf-8') as file:
                buecher_liste = json.load(file)
                # auch mit normaler for loop lösbar
                self.buecher = [Buch(**buch) for buch in buecher_liste]
        except FileNotFoundError:
            print(f"Die Datei {self.dateipfad} wurde nicht gefunden.")

    def speichern(self):
        with open(self.dateipfad, 'w') as file:
            json.dump([buch.als_dict() for buch in self.buecher], file, indent=4)

    def buch_hinzufuegen(self, buch):
        self.buecher.append(buch)
        self.speichern()

    def buch_aktualisieren(self, isbn, neuer_titel=None, neuer_autor=None):
        for buch in self.buecher:
            if buch.isbn == isbn:
                if neuer_titel:
                    buch.titel = neuer_titel
                if neuer_autor:
                    buch.autor = neuer_autor
                self.speichern()
                return
        print("Buch nicht gefunden.")

    def buch_entfernen(self, isbn):
        self.buecher = [buch for buch in self.buecher if buch.isbn != isbn]
        self.speichern()

    def buch_suchen(self, suchbegriff):
        # auch mit normaler for loop realisierbar
        gefundene_buecher = [buch for buch in self.buecher if suchbegriff.lower() in buch.titel.lower() or suchbegriff.lower() in buch.autor.lower()]
        return gefundene_buecher

    def katalog_statistiken(self):
        print(f"Anzahl der Bücher im Katalog: {len(self.buecher)}")
        autoren = set(buch.autor for buch in self.buecher)
        print(f"Anzahl der Autoren im Katalog: {len(autoren)}")
        if self.buecher:
            # auch mit normaler for loop realisierbar
            jahre = [buch.erscheinungsjahr for buch in self.buecher if buch.erscheinungsjahr]
            if jahre:
                print(f"Ältestes Buch erschienen im Jahr: {min(jahre)}")
                print(f"Neuestes Buch erschienen im Jahr: {max(jahre)}")


katalog = Katalog('OOP/buecher.json')
neues_buch = Buch("Neues Buch", "Neuer Autor", "3344556677", 2021, "Fantasy")
katalog.buch_hinzufuegen(neues_buch)
katalog.buch_aktualisieren("3344556677", neuer_titel="Aktualisiertes Neues Buch")

katalog.buch_entfernen("3344556677")
gefundene_buecher = katalog.buch_suchen("Python")
gefundene_buecher = katalog.buch_suchen("Python")
for buch in gefundene_buecher:
    print(buch.als_dict())

katalog.katalog_statistiken()

