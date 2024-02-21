"""
Aufgabe: Schreibe ein Programm, in dem die Summe von 0 bis 20 (inklusive) von allen geraden Zahlen gebildet wird.
Hinweis: 0 darf vereinfacht als gerade Zahl angenommen werden. Die Lösung sollte 110 sein.
"""
summe = 0
for i in range(0, 21, 2):
    summe += i
print(summe)