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


# 1. Datei laden
tree = etree.parse('library.xml')
root = tree.getroot()


# 2. Bücher auflisten
def list_books(root):
    for book in root.xpath('//book'):
        title = book.find('title').text
        author = book.find('author').text
        print(f"Titel: {title}, Autor: {author}")

list_books(root)


# 3. Suche nach Genre
def find_books_by_genre(root, genre):
    books = root.xpath(f"//book[genre='{genre}']")
    for book in books:
        title = book.find('title').text
        author = book.find('author').text
        print(f"Titel: {title}, Autor: {author}")

# Bsp. Suche nach Büchern im Genre "Programming"
find_books_by_genre(root, "Programming")


# 4. Neuestes Buch finden
def find_newest_book(root):
    years = root.xpath('//book/year')
    max_year = max(int(year.text) for year in years)
    newest_books = root.xpath(f'//book[year="{max_year}"]')

    for book in newest_books:
        title = book.find('title').text
        author = book.find('author').text
        print(f"Neuestes Buch: {title}, Autor: {author}, Jahr: {max_year}")

find_newest_book(root)


# 5. Bonus: Bücher nach bestimmten Zeitraum suchen
def find_books_in_period(root, start_year, end_year):
    books = root.xpath(f"//book[year >= '{start_year}' and year <= '{end_year}']")
    for book in books:
        title = book.find('title').text
        author = book.find('author').text
        year = book.find('year').text
        print(f"Titel: {title}, Autor: {author}, Jahr: {year}")

# Bsp. Suche nach Büchern veröffentlicht zwischen 2018 und 2020
find_books_in_period(root, 2018, 2020)

