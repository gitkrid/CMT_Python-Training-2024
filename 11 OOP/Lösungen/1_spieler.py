"""
Aufgabe: Schreibe eine Klasse "Spieler" mit den Attributen
+ name
+ level
+ lebenspunkte
+ angriffs_staerke

und den Methoden
+ verliere_leben()
+ angreifen()

Erstelle anschließend zwei Objekte. Ein Spieler mit dem Level 12 und
ein Spieler mit dem Level 41. (restliche Attribute frei wählbar)
"""

class Spieler:

    def __init__(self, name, level, lebenspunkte, angriffs_staerke):
        self.name = name
        self.level = level
        self.lebenspunkte = lebenspunkte
        self.angriffs_staerke = angriffs_staerke

    def verliere_leben(self, schaden):
        self.lebenspunkte -= schaden
        if self.lebenspunkte < 0:
            print("Aaaaaargh! Ich sterbe!")

    def angreifen(self):
        return self.angriffs_staerke


spieler1 = Spieler("Hamudi", 127, 100, 20)
spieler2 = Spieler("Mini-Banane", 13, 25, 3)

spieler1.verliere_leben(spieler2.angreifen())

# Wie viel Leben hat Spieler "Hamudi" nach diesem Angriff?
print(spieler1.lebenspunkte)
