"""
Aufgabe: Schreibe ein Spiel in dem der Computer eine Zufallszahl zwischen
0 und 100 wählt. Über eine Benutzereingabe rät der Benutzer. Trifft der Benutzer
die Zahl des Computers soll "Du hast gewonnen!" auf dem Bildschirm erscheinen.
Andernfalls soll der Computer einem sagen, ob man höher oder niedriger raten soll.
Gib dir außerdem die Anzahl der benötigten Schritte aus, die du benötigst, um
die richtige Zahl zu erraten.
Überlege dir eine optimale Ratestrategie!

Zusatz: Ändere dein Programm so, dass du genau 4 Versuche hast, um die Zahl zu
erraten.
"""
import random


computer_zahl = random.randint(0, 100)
count = 0

geratene_zahl = int(input("Na, welche Zahl denkst du ist es? "))

while geratene_zahl != computer_zahl:
    count += 1
    if geratene_zahl > computer_zahl:
        print("Niedriger!")
    else:
        print("Höher!")
    geratene_zahl = int(input("Na, welche Zahl denkst du ist es? "))

print("Du hast gewonnen!")
print(f"Du hast {count} Züge benötigt.")


# Zusatz
for versuch in range(4):
    ...

# oder mit if count == 4: break oder so in der while loop