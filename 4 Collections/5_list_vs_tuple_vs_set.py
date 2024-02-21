"""
Aufgabe: Prüfe und überzeuge dich selbst von den Eigenschaften der
verschiedenen Typen. Wo entstehen Fehler? Erkläre deine Beobachtung.
"""

l = [1, 7, 3]
t = (1, 7, 3)
s = {1, 7, 3}

# Indizierung/Ordnung
print(l[1], l[1], l[1])
print(t[1], t[1], t[1])
print(s[1], s[1], s[1])

# Veränderbarkeit
l.append(4)
l[2] = 5
t.append(4)
t[2] = 5
s.append(4)
s[2] = 5

# Mehrfachnennungen
l = [1, 1, 1, 0, 1]
t = (1, 1, 1, 0, 1)
s = {1, 1, 1, 0, 1}
print(l)
print(t)
print(s)
