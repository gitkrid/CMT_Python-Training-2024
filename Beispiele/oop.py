class Auto:
    

    def __init__(self, farbe, max_geschwindigkeit):
        print("init aufgerufen")
        self.farbe = farbe
        self._max_geschwindigkeit = max_geschwindigkeit

    def umlackieren(self, neue_farbe):
        self.farbe = neue_farbe


mein_auto = Auto("grün", 320)
print(mein_auto.farbe)
mein_auto.umlackieren("gelb")
print(mein_auto.farbe)
mein_auto._max_geschwindigkeit = 500
