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
