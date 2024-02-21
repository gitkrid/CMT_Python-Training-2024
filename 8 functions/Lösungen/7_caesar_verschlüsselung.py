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
better solution:
import string
alphabet = list(string.ascii_lowercase)
"""

def caesar_encoding(wort, k):
    # für den Fall, dass k > len(alphabet) sein sollte, erscheint ein IndexError
    # dieser ließe sich sehr einfach mit einer if-Abfrage abfangen:
    # if k > len(alphabet): k = k%len(alphabet)
    wort = wort.lower()
    verschluesselt = ""
    for buchstabe in wort:
        index = alphabet.index(buchstabe)
        neuer_index = index + k - len(alphabet)
        verschluesselt += alphabet[neuer_index]
    return verschluesselt

# Zusatz 1
def caesar_decoding(wort, k):
    unverschluesselt = ""
    for buchstabe in wort:
        index = alphabet.index(buchstabe)
        neuer_index = index - k
        unverschluesselt += alphabet[neuer_index]
    return unverschluesselt


# Zusatz 2
def caesar(wort, k, encoding=True):
    wort = wort.lower()
    rueckgabe = ""
    for buchstabe in wort:
        index = alphabet.index(buchstabe)
        if encoding:
            neuer_index = index + k - len(alphabet)
        else:
            neuer_index = index - k
        rueckgabe += alphabet[neuer_index]
    return rueckgabe


# print(caesar_encoding("HalloPythonWieGehts", 3))
# print(caesar_decoding("kdoorsbwkrqzlhjhkwv", 3))
print(caesar("caesar", 3))
print(caesar("fdhvdu", 3, encoding=False))
