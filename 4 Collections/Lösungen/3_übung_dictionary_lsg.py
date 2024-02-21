"""
Aufgabe 1: Erstelle einen Steckbrief (Dictionary), welches Informationen über dich enthält.
"""

steckbrief = {
    "Name": "Max Schmidt",
    "Lieblingsfarbe": "blau",
    "Alter": 31,
    "Note im Abi": 2.3,
    "Name des Haustiers": "Hugo"
}


"""
Aufgabe 2: Lass dir nur eine bestimmte, von dir gewählte Informationen auf dem Bildschirm ausgeben.
Bsp.: Name, Lieblingsfarbe
"""
print(steckbrief["Alter"])


"""
Aufgabe 3: Nutze diesmal die get() Funktion, um Aufgabe 2 zu wiederholen.
"""
print(steckbrief.get("Alter"))


"""
Aufgabe 4: Erkläre, was du für einen Output erwarten würdest.
"""
bundeslaender = {
    "Bayern": {
        "Hauptstadt": "München",
        "Einwohner [Mio.]": 13.08
    },
    "Hessen": {
        "Hauptstadt": "Wiesbaden",
        "Einwohner [Mio.]": 6.27
    },
    "Sachsen": {
        "Haupstadt": "Dresden",
        "Einwohner [Mio.]": 4.08
    }
}

# Liste der Keys, hier: [Bayern, Hessen, Sachsen]
print(bundeslaender.keys())
# Liste der Values, hier eine Liste von Dictionaries, weil die
# Values in der ersten Ebene selbst wieder Dictionaries sind
print(bundeslaender.values())
# output: München, hier haben wir get und die [] kombiniert
print(bundeslaender.get("Bayern")["Hauptstadt"])
# Liste von Tupels mit dem Key und dem Value
print(bundeslaender.items())
