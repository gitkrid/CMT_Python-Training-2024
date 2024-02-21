"""
Aufgabe: Schreibe zwei for loops mit denen du alle Farben der Liste unterein-
ander auf der Konsole ausgibst.
Verwende dafür einmal die range Funktion, d.h. greife über den Index auf die
einzelnen Elemente zu.
"""

farben = ["grün", "gelb", "rot", "orange", "magenta", "grau", "blau"]

for farbe in farben:
    print(farbe)

for i in range(len(farben)):
    print(farben[i])
