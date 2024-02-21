"""
Aufgabe: Entscheide VOR dem Ausführen, welche Antwortmöglichkeit die
richtige ist.
"""

# 1
x = {}
x[2] = 5
x[1] = [2, 3, 4]
print(x[1][1])

# a) 2
# b) 3
# c) [2, 3, 4]
# d) Error


# 2
l = [5, 4, 3, 2, 1]
l.extend(tuple(l))
print(l)

# a) [5, 4, 3, 2, 1]
# b) [5, 4, 3, 2, 1, (5, 4, 3, 2, 1)]
# c) [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]
# d) Error
