"""
Aufgabe: Oma Erna braucht immer ziemlich lange an der Kasse, da sie Münzen in ihrem
Geldbeutel nicht schnell genug zusammensuchen kann.
Hilf ihr (und allen Leuten nach ihr)!
Gib eine Liste zurück, die für einen Cent-Betrag die Münzkombination für Oma Erna
zurückgibt.
Bsp.: 1553 Cent = ["2 Euro", "2 Euro", "2 Euro", "2 Euro", "2 Euro", "2Euro", "2 Euro",
"1 Euro", "50 Cent", "2 Cent", "1 Cent"]
Hinweis: Verwende keine Fließkommazahlen.

Zusatz 1: Sie zahlt auch mit Geldscheinen.

Zusatz 2: Gib die Münzen nicht einzeln zurück, sondern die Anzahl.
"""
geld = 1553
muenzen = []


# Hinweis: Die folgende Lösung ist nur im Rahmen der Übung "richtig". Es gibt elegantere
# Möglichkeiten!

geld = 1553
muenzen = []

while geld / 200 >= 1:
# while geld > 200: -> geht auch
    geld -= 200
    muenzen.append("2 Euro")

while geld / 100 >= 1:
    geld -= 100
    muenzen.append("1 Euro")

while geld / 50 >= 1:
    geld -= 50
    muenzen.append("50 Cent")

while geld / 20 >= 1:
    geld -= 20
    muenzen.append("20 Cent")

while geld / 10 >= 1:
    geld -= 10
    muenzen.append("10 Cent")

while geld / 5 >= 1:
    geld -= 5
    muenzen.append("5 Cent")

while geld / 2 >= 1:
    geld -= 2
    muenzen.append("2 Cent")

while geld / 1 >= 1:
    geld -= 1
    muenzen.append("1 Cent")

print(geld)
print(muenzen)

# Zusatz 1: selbes Verfahren, nur oben weitere while-loops anbauen

# Zusatz 2:
muenzen.clear()
geld = 1553
count = 0

while geld / 200 >= 1:
    geld -= 200
    count += 1
if count != 0:
    muenzen.append(f"{count} mal 2 Euro")
    count = 0

while geld / 100 >= 1:
    geld -= 100
    count += 1
muenzen.append(f"{count} mal 1 Euro")
count = 0

while geld / 50 >= 1:
    geld -= 50
    count += 1
if count != 0:
    muenzen.append(f"{count} mal 50 Cent")
    count = 0

while geld / 20 >= 1:
    geld -= 20
    count += 1
if count != 0:
    muenzen.append(f"{count} mal 20 Cent")
    count = 0

while geld / 10 >= 1:
    geld -= 10
    count += 1
if count != 0:
    muenzen.append(f"{count} mal 10 Cent")
    count = 0

while geld / 5 >= 1:
    geld -= 5
    count += 1
if count != 0:
    muenzen.append(f"{count} mal 5 Cent")
    count = 0

while geld / 2 >= 1:
    geld -= 2
    count += 1
if count != 0:
    muenzen.append(f"{count} mal 2 Cent")
    count = 0

while geld / 1 >= 1:
    geld -= 1
    count += 1
if count != 0:
    muenzen.append(f"{count} mal 1 Cent")
    count = 0

print(muenzen)

# noch besser:
anzahl = geld // 200
geld -= anzahl * 200
muenzen.append(f"{anzahl} mal 2 Euro")

# usw.
