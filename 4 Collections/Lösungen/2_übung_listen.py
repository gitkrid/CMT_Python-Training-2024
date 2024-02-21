"""
Aufgabe:
a) Erstelle eine Liste mit 5 Zahlen.
b) Sortiere die Liste der Größe nach. Lege dazu eine neue Liste an.
(Hinweis: sorted() kann hier helfen)
c) Finde das Minimum und Maximum der Liste. (Hinweis: min() und max())
d) Prüfe, ob die erste Zahl deiner Liste durch die letzten Zahl restlos
teilbar ist. Restlos teilbar bedeutet es entsteht kein Rest, das Ergebnis
ist kein Bruch.
"""

# a)
liste = [6, 4, 2, 7, 3]

# b)
sortiert = sorted(liste)
print(f"sortierte Liste: {sortiert}")

# c)
# für ganz Schlaue: nach dem Sortieren ist theoretisch das erste Element
# das Minimum und das letzte Element das Maximum
print(f"Minimum: {min(liste)}")
print(f"Maximum: {max(liste)}")

# d)
rest = liste[0] % liste[-1]
print(f"Rest: {rest}")
