"""
Aufgabe 1: Füge zu den genannten Autoherstellern zwei weitere hinzu. Einen hinten an die Liste
und einen als zweites Element. Sortiere die Liste anschließend alphabetisch und lass sie dir
ausgeben.
Hinweis: Nutze die sort() Funktion.
"""

cars = ["Seat", "Audi", "Mercedes", "Opel"]
cars.append("Ford")
cars.insert(1, "Skoda")
cars.sort()
print(cars)

"""
Aufgabe 2: Ersetze einen Hersteller durch "Toyota".
"""

cars[2] = "Toyota"

