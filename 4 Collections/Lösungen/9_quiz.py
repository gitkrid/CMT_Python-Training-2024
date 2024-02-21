"""
Aufgabe: Entscheide VOR dem Ausführen, welche Antwortmöglichkeit die
richtige ist.
"""

# 1
x = {} # leeres dict wird erstellt
x[2] = 5 # key = 2, value = 5
x[1] = [2, 3, 4] # key = 1, value = [2, 3, 4]
print(x[1][1]) # Wert vom key = 1  und dem value (eine Liste) an der Stelle 1

# a) 2
# b) 3 <-- richtige Antwort
# c) [2, 3, 4]
# d) Error


# 2
li = [5, 4, 3, 2, 1]
li.extend(tuple(li)) # extend ist wie ein mehrfaches "append"
print(li)

# a) [5, 4, 3, 2, 1]
# b) [5, 4, 3, 2, 1, (5, 4, 3, 2, 1)]
# c) [5, 4, 3, 2, 1, 5, 4, 3, 2, 1] <-- richtige Antwort
# d) Error
