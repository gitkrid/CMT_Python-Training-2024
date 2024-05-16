class Person:

    # Konstruktur
    def __init__(self, name, position):
        self.name = name
        self.position = position


class Tier:

    # Konstruktor
    def __init__(self, name, ernährungsweise, tierart):
        self.name = name
        self.ernährungsweise = ernährungsweise
        self.tierart = tierart
        if self.ernährungsweise == "fleisch":
            self.ist_hungrig = True
        else:
            self.ist_hungrig = False

    def füttern(self, futtermenge, person):
        if person.position != "Pfleger":
            print("Du darfst mich nicht füttern, du wirst gefressen!! :)")
            print(f"{person.name} ist tot")
            # del person
            return
        
        if self.ernährungsweise == "fleisch":
            if futtermenge > 20:
                self.ist_hungrig = False
                print("Danke, bin nicht mehr hungrig")
            else:
                print("ZU WENIG FUTTER!!!")
        elif self.ernährungsweise == "pflanzlich":
            if futtermenge > 5:
                self.ist_hungrig = False
                print("Danke, bin nicht mehr hungrig")
            else:
                print("ZU WENIG FUTTER!!")

    def streicheln(self, person):
        print(f"{person.name} streichelt das Tier")
        print("Ich bin ein glückliches Tier")
    
p1 = Person("Hans", "Pfleger")
p2 = Person("Barbara", "Direktorin")
p3 = Person("Johannes", "Besucher")

t1 = Tier("Krok", "fleisch", "Krokodil")
t2 = Tier("Lucy", "pflanzlich", "Affe")
t3 = Tier("Simba", "fleisch", "Löwe")

t1.füttern(25, p2)
t2.streicheln(p1)
