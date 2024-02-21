"""
Aufgabe: Erstelle eine Liste mit den Fibonacci-Zahlen bis N = 10 mit Hilfe einer
for-Schleife.
Hinweis: Die Fibonacci-Zahlen sind folgendermaßen definiert:
f(n) = f(n-1) + f(n-2), f(0) = 0, f(1) = 1
(Es gibt mehrere mögliche Lösungen.)
"""

N = 10
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
fib = [0, 1]

# erzeuge Fibonacci-Zahlen hier
for n in range(N-2):
    fib_next = fib[n] + fib[n+1]
    fib.append(fib_next)

# alternativ
# for n in range(N):
#     fib.append(fib[-2] + fib[-1])


print(fib)