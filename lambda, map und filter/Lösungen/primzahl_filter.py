"""
Aufgabe: Schreibe eine Funktion "is_prime", welche dir zurückgibt, ob es sich bei
einer Zahl um eine Primzahl handelt. Filtere anschließend die Liste unten, sodass
nur noch die Primzahlen übrig bleiben.
"""

def is_prime(x):
    if x < 2:
        return False
    else:
        # Start von 2, weil jede Zahl durch 1 teilbar ist
        # bis x, weil jede Zahl durch sich selbst teilbar ist
        for i in range(2, x):
            # aber nur auf Primzahlen trifft ausschließlich das o.g. zu
            if x % i == 0:
                return False
    return True

zahlen = [4, 2, 9, 7, 13, 0, -8, 68, 8, 731]
primzahlen = filter(is_prime, zahlen)
print(list(primzahlen))
