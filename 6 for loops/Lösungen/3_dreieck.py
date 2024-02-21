"""
Aufgabe: Schreibe ein Programm, welches dir folgenden Output liefert:
*
**
***
****
*****

Zusatz: Erweitere dein Programm für solch einen Output:
    *
   ***
  *****
 *******
*********

Hinweis: Versuche die Muster zu erkennen.
"""
""""
# Aufgabe 1:
# N = 5 Stufen
for i in range(1, 6):
    print(i*"*")

# Alternative, credits to Andreas
x = ""
for _ in range(1, 6):
    x += "*"
    print(x)

# credits to Florian Baatz
for i in range(N):
    for j in range(i+1):
        print("*", end="")
    print()

# Zusatz:
# N = 5 Stufen
N = 5
for i in range(1, 2*N, 2):
    space = N - i//2 - 1
    print(space*" " + i*"*")

# einfacher
N = 5
space = N
for i in range(1, 2*N, 2):
    space -= 1
    print(space*" " + i*"*")


# oder die center Funktion nutzen, für ganz faule Menschen :P

# Pyramide umdrehen
space = -1
for i in range(2*N, 1, -2):
    space += 1
    print(space*" " + i*"*")
"""

# Weihnachtsbaum
N = 10
space = N
for i in range(1, 2*N, 2):
    space -= 1
    print(space*" " + i*"*")
print(int(i/2)*" " + "|")

