"""
Problem: Python erlaubt den Zugriff auf Attribute ohne Getter und Setter.
"""
class Person:

    def __init__(self, name, größe):
        self.name = name
        self.größe = größe

p = Person("Claudia", 167)
p.größe = -20 # Körpergröße kann nicht negativ sein


"""
Lösung 1: getter und setter schreiben und Attribute auf privat setzen
"""
class Person:

    def __init__(self, name, größe):
        self.name = name
        self._größe = größe

    def get_größe(self):
        return self._größe
    
    def set_größe(self, wert):
        if wert < 0:
            raise ValueError("Größe einer Person darf nicht negativ sein.")
        self._größe = wert


"""
neues Problem: Code ist nicht backward compatible, jeder Code, der unsere Klasse nutzt muss
jetzt angepasst werden

Lösung: Das ist eine Stärke von Decorators in Python. Sie fügen Funktionalität nachträglich hinzu,
ohne den bestehenden Code zu verändern. Sie "dekorieren" den Code.
Andere Beispiele, die wir noch sehen werden sind z.B. ein nachträgliches logging.
"""
class Person:

    def __init__(self, name, größe):
        self.name = name
        self._größe = größe

    @property
    def größe(self):
        print("rufe getter auf")
        return self._größe
    
    @größe.setter
    def größe(self, wert):
        print("rufe setter auf")
        if wert < 0:
            raise ValueError("Größe einer Person darf nicht negativ sein.")
        self._größe = wert

p = Person("Peter", 187)
print(p.größe)
p.größe = 190

