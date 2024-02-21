"""
Aufgabe: Ziel dieser Übung ist es das Slicing (und Indexing) in Python
zu verinnerlichen. Löse dazu die folgenden Teilaufgaben.
"""

numbers = [2, 5, -4, 7, 1, 0, 4, 2, -9, 3]

# 1 - das dritte Element
print(numbers[2])

# 2 - die letzten 4 Elemente
print(numbers[-4:])

# 3 - vom 2. bis zum 6. Element (inklusive)
print(numbers[1:6])

# 4 - jedes 2. Element
print(numbers[::2])

# 5 - jedes 3. Element, beginnend mit dem ersten
print(numbers[1::3])

# 6 - die Liste "umdrehen", ohne externe Funktion
print(numbers[::-1])

# 7 - ersetze die ersten drei Werte durch (9, 2, 5)
numbers[:3] = (9, 2, 5)
print(numbers)


# gute Quelle:
# https://python-reference.readthedocs.io/en/latest/docs/brackets/slicing.html
