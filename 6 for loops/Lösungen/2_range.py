"""
Aufgabe: Schreibe ein Programm, dass dir
a) Zahlen von 0 bis 20 ausgibt.
b) Zahlen von 20 bis 50 in Dreierschritten ausgibt.
c) Zahlen von 10 bis 0 herunterzählt.
"""

# a)
for i in range(21):
    print(i)

# b)
for i in range(20, 51, 3):
    print(i)

# c)
for i in range(10, -1, -1):
    print(i)
