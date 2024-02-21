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
print(s[1], s[1], s[1]) # Fehler, sets sind nicht indizierbar

# Veränderbarkeit
l.append(4)
l[2] = 5
t.append(4) # Fehler, tuple sind unveränderbar
t[2] = 5 # Fehler, tuple sind unveränderbar
s.append(4) # Fehler, sets sind unveränderbar
s[2] = 5 # Fehler, sets sind unveränderbar

# Mehrfachnennungen
l = [1, 1, 1, 0, 1]
t = (1, 1, 1, 0, 1)
s = {1, 1, 1, 0, 1}
print(l)
print(t)
print(s) # Mehrfachnennungen werden automatisch verworfen
