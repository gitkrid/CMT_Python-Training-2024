"""
Aufgabe: Schreibe ein Programm, welches dir aus dem gegebenen Dictionary
nur die keys ausgibt, die mit einem Vokal starten.
"""

d = {
    "Niederlande": "Amsterdam",
    "Deutschland": "Berlin",
    "Spanien": "Madrid",
    "Norwegen": "Oslo",
    "Italien": "Rom"
}

vokale = ("A", "E", "I", "O", "U")

for land in d:
    stadt = d[land]
    if stadt[0] in vokale:
        print(stadt)
