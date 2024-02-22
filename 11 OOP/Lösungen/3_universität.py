"""
Aufgabe: Entwickle mit Hilfe objektorientierter Programmierung das Modell einer
Universität. Die Universität soll folgende Klassen mit den entsprechenden Methoden
enthalten:

Person:
+ get_geburtsdatum()

Student:
+ get_matrikelnummer()
(Matrikelnummer setzt sich zusammen aus dem Anfangsbuchstaben des Nachnamens
und 4 zufälligen Zahlen)
+ set_note()
+ wird_verwirrt()

Professor:
+ verwirre_studenten()
+ erteile_note()

Inventar:
+ get_beschaffungspreis()

Tafel:
+ schreibe()
+ loesche()

Hinweis: Mache dir im Vorfeld Gedanken, welche Klasse von welcher erben könnte und
welche Attribute die Klassen brauchen.
"""
import random

class Person:

    def __init__(self, vorname, nachname, geburtstag):
        self.vorname = vorname
        self.nachname = nachname
        self.geburtstag = geburtstag

    def get_geburtsdatum(self):
        return self.geburtstag


class Student(Person):

    def __init__(self, vorname, nachname, geburtstag):
        Person.__init__(self, vorname, nachname, geburtstag)
        self.matrikelnummer = ""
        self.noten = {}
        self.ist_verwirrt = False
        self.erzeuge_matrikelnummer()

    def erzeuge_matrikelnummer(self):
        self.matrikelnummer += self.nachname[0]
        for _ in range(4):
            self.matrikelnummer += str(random.randint(0, 9))
    
    def get_matrikelnummer(self):
        return self.matrikelnummer

    def set_note(self, fach, note):
        self.noten[fach] = note

    def wird_verwirrt(self):
        self.ist_verwirrt = True



class Professor(Person):

    def __init__(self, vorname, nachname, geburtstag, fachgebiet):
        Person.__init__(self, vorname, nachname, geburtstag)
        self.fachgebiet = fachgebiet

    def erteile_note(self, student, fach, note):
        student.set_note(fach, note)

    def verwirre_studenten(self, student, verwirrungsgrad=1):
        x = [False]
        # mit steigendem Verwirrungsgrad steigt die Wahrscheinlichkeit, dass der
        # Student verwirrt wird
        for _ in range(verwirrungsgrad):
            x.append(True)
        if random.choice(x):
            student.wird_verwirrt()
            print("Lerne stets, was es zu lernen gilt.")


class Inventar:

    def __init__(self, beschaffungspreis):
        self.beschaffungspreis = beschaffungspreis

    def get_beschaffungspreis(self):
        return self.beschaffungspreis


class Tafel(Inventar):

    def __init__(self, beschaffungspreis):
        Inventar.__init__(self, beschaffungspreis)
        self.aufschrieb = []

    def schreibe(self, inhalt):
        self.aufschrieb.append(inhalt)

    def loesche(self):
        self.aufschrieb.clear()


if __name__ == "__main__":
    s = Student("Daniel", "Schmidt", "12.13.1914")
    p = Professor("Herbert", "Klausen", "02.03.1804", "Abwasserwirtschaft")
    t = Tafel(5030)

    print(s.get_matrikelnummer())
    print(p.get_geburtsdatum())

    print(s.ist_verwirrt)
    p.erteile_note(s, "Abwasser I", 2.3)

    t.schreibe("Heutiges Thema: Abwasserrohre, Teil 7")
    print(t.aufschrieb)
    p.verwirre_studenten(s, 4)
    print(s.ist_verwirrt)

    t.loesche()

    print(t.aufschrieb)
