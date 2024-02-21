"""
Aufgabe 1: Erstelle einen Steckbrief (Dictionary), welcher Informationen über dich enthält.
"""

steckbrief = {}


"""
Aufgabe 2: Lass dir nur eine bestimmte, von dir gewählte Informationen auf dem Bildschirm ausgeben.
Bsp.: Name, Lieblingsfarbe
"""


"""
Aufgabe 3: Nutze diesmal die get() Funktion, um Aufgabe 2 zu wiederholen.
"""


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

# ?
print(bundeslaender.keys())
# ?
print(bundeslaender.values())
# ?
print(bundeslaender.get("Bayern")["Hauptstadt"])
# ?
print(bundeslaender.items())
