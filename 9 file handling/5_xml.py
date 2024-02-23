"""
Kontext: Du bist ein Softwareentwickler, der für eine kleine Bibliothek arbeitet.
Die Bibliothek möchte eine neue Funktion in ihrem Bibliotheksverwaltungssystem
einführen, um Informationen über Bücher leichter abrufen zu können.
Die Informationen zu den Büchern sind in einer XML-Datei gespeichert, die library.xml
genannt wird. Deine Aufgabe ist es, ein Python-Skript zu schreiben, das diese
XML-Datei liest und bestimmte Informationen extrahiert und darstellt.

Aufgabenstellung:

    1. XML-Datei Laden: Lade die library.xml Datei mit Python und parse sie, um
    auf die Daten zugreifen zu können.
    2. Bücher Auflisten: Erstelle eine Funktion, die alle Bücher in der Bibliothek
    auflistet. Für jedes Buch sollen der Titel und der Autor ausgegeben werden.
    3. Suche nach Genre: Erstelle eine Funktion, die es ermöglicht, Bücher anhand
    ihres Genres zu suchen. Die Funktion soll das Genre als Parameter
    entgegennehmen und eine Liste aller Bücher dieses Genres ausgeben (Titel, Autor, Jahr).
    4. Neuestes Buch Finden: Schreibe eine Funktion, die das Buch (oder die Bücher)
    mit dem neuesten Erscheinungsjahr findet. Gib den Titel, Autor und das Jahr
    des Buches aus.
    5. Bonus: Erweitere das Bibliotheksverwaltungssystem, indem du eine Funktion
    hinzufügst, die es ermöglicht, Bücher nach einem bestimmten Zeitraum zu suchen
    (z.B. alle Bücher, die zwischen 2018 und 2020 veröffentlicht wurden).
"""
# pip install lxml
# oder
# conda install lxml
from lxml import etree
