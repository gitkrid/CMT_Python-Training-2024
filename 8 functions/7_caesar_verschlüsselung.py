"""
Aufgabe: Schreibe eine Funktion, die einen String und eine Zahl k als Parameter
entgegennimmt und die sog. Caesar-Verschlüsselung zurückliefert.
Bei diesem einfachen Verschlüsselungsverfahren wird jeder Buchstabe zyklisch mit dem
Buchstaben ersetzt, der im Alphabet k Buchstaben weiter hinten steht.
Bsp.: caesar, k = 3 ---> fdhvdu

Hinweis: Stelle mit str.lower() sicher, dass immer Kleinbuchstaben verwendet werden.
Was passiert, wenn das Alphabet überschritten wird?

Zusatz 1: Programmiere auch das "Decoding".

Zusatz 2: Kann man auch beides in einer Funktion kombinieren?
"""

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

"""
oder mit folgendem Code:
import string
alphabet = list(string.ascii_lowercase)
"""
