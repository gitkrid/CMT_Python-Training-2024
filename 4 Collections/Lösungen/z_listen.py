"""
Wiederholung & Übung zu Listen
"""

farben = ["rot", "gelb", "blau"]

# neues Element hinten anhängen
farben.append("grün")

# neues Element an bestimmter Stelle (Index) einfügen
farben.insert(1, "lila")

# Element entfernen
farben.remove("rot")

# Element an bestimmter Stelle (Index) entfernen
entfernte_farbe = farben.pop(0) # Achtung: .pop() gibt das entfernte Element zurück

# ein bestimmtes Element finden
print(farben[1])

# bestimmtes Element an einer Stelle ändern
farben[1] = "orange"
print(farben[1])

# for loop über Liste
for farbe in farben:
    print(farbe)

# for loop mit Index
for i, farbe in enumerate(farben):
    print(f"Index: {i}, Farbe: {farbe}")



"""
Aufgabe: Gegeben ist eine Liste mit Zahlen.
1) Füge eine beliebige Zahl hinten und vorne an die Liste hinzu.
2) Entferne die dritte Zahl der Liste.
3) Ändere die letzte Zahl der Liste zu 2. (Hinweis: letztes Element hat Index -1)
4) Lass dir alle geraden Zahlen der Liste ausgeben. (Hinweis: gerade Zahlen sind
restlos durch 2 teilbar, verwende for und if)
"""

zahlen = [4, 9, 11, 42, 67, 3, 14]

# 1)
zahlen.append(8)
zahlen.insert(0, 7)

# 2)
zahlen.pop(2)

# 3)
zahlen[-1] = 2

# 4)
for zahl in zahlen:
    if zahl % 2 == 0:
        print(f"{zahl} ist eine gerade Zahl")
    else:
        print(f"{zahl} ist eine ungerade Zahl")
