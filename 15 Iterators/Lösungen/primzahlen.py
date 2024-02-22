"""
Aufgabe: Schreibe einen Iterator, der dir alle Primzahlen bis 50 ausgibt.
"""

def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True


class Primzahlen:
    
    def __init__(self):
        self.stop = 50

    def __iter__(self):
        self.x = 0  # oder gleich mit 2
        return self

    def __next__(self):
        x = self.x
        if x >= 47: # 47 ist die letzte Primzahl bis 50
            raise StopIteration
        for i in range(self.x, self.stop):
            if is_prime(i):
                x = i
                break
        # damit wir nicht immer die selbe Zahl bekommen
        self.x = x + 1
        return x

for i in Primzahlen():
    print(i)
