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
