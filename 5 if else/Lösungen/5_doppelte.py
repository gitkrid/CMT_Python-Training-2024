"""
Aufgabe: (mittel) Schreibe ein Programm, welches dir ausgibt, ob die Liste
doppelte Elemente enthält. Entferne diese anschließend.
"""

zahlen = [3, 9, 2, 4, 1, 3, 1, 8]

# es sind ganz viele Lösungen möglich
# z.B.:
zahlen.sort()
doppelte = 0
for i in range(len(zahlen) - 1):
    if zahlen[i] == zahlen[i + 1]:
        doppelte += 1

print(f"Liste enthält {doppelte} doppelte Elemente [Methode 1]")

# entfernen
zahlen_ohne_doppelte = list(set(zahlen))


# man kann auch beides in einem machen:
zahlen_ohne_doppelte = list(set(zahlen))
# n = Länge der Liste nach dem Entfernen
N = len(zahlen)
# N = Länge der Liste vor Entfernen der Doppelten
n = len(zahlen_ohne_doppelte)

if N != n: # if Answeisung kann man hier theoretisch auch weglassen
    print(f"Liste enthält {N-n} doppelte Elemente [Methode 2]")


# weitere Möglichkeiten
# in Operator nutzen: if i in list
# list.count() verwenden: list.count(i)
