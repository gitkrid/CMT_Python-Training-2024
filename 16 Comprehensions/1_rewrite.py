"""
Aufgabe: Schreibe für die hier aufgeführten Beispiele eine entsprechende
Comprehension. Kontrolliere dein Ergebnis.
"""

# einfach
even_numbers = []
for i in range(2, 11, 2):
    even_numbers.append(i)
print(even_numbers)


# einfach
cities = ("Paris", "Rome", "Berlin", "Sofia")
metro_populations = (13.0, 4.3, 6.1, 1.7)
cities_to_populations = {}
for c, p in zip(cities, metro_populations):
    cities_to_populations[c] = p
print(cities_to_populations)


# mittel
div_by_3_set = set()
for num in range(10):
    if num % 3 == 0:
        div_by_3_set.add(num)
print(div_by_3_set)


# mittel
fruits = ["apple", "banana", "pineapple", "strawberry", "melon"]
e_fruits = []
for fruit in fruits:
    if fruit.count("e") >= fruit.count("a"):
        e_fruits.append(fruit)
print(e_fruits)
# additional task: try to implement this functionality with the filter() function
# interesting discussion about comprehension vs filter() + lambda:
# https://stackoverflow.com/questions/3013449/list-comprehension-vs-lambda-filter


# mittel
import math

sqrts = []
for i in range(10):
    if math.sqrt(i) > 2 and math.sqrt(i) < 2.5:
        sqrts.append(1)
    else:
        sqrts.append(0)
print(sqrts)


# schwer
mult_table = {}
for i in range(1, 11):
    table = []
    for j in range(1, 11):
        table.append(i*j)
    mult_table[i] = table
print(mult_table)