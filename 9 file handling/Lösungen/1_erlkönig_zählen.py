"""
Aufgabe: Schreibe eine Funktion, welche dir die Wörter im Erlkönig zählt.
"""
def count_words(filename):
    count = 0
    with open(filename, "r", encoding="utf-8") as f:
        r = f.read()
        # split teilt ein String in eine Liste entsprechend eines Separators
        # default separator ist " "
        words = r.split()
        for word in words:
            count += 1
    return count

# bei VS Code muss hier der ganze Pfad des working directories übergeben werden
print(count_words("11 file handling/Lösungen/erlkoenig.txt"))
