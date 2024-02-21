"""
Aufgabe: Schreibe einen Passwortgenerator. Beachte, dass starke Passwörter Groß- und Klein-
buchstaben, Zahlen und Sonderzeichen haben. Das Passwort sollte zufällig generiert werden
und bei jedem Neuaufruf ein anderes Passwort erzeugen.
"""
import random

symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUFVWXYZ1234567890!§$%&/()=?><#*+^"

def generator(N):
    password = ""
    while len(password) < N:
        i = random.randint(0, len(symbols)-1)
        if symbols[i] not in password:
            password += symbols[i]
    return password

pw = generator(10)
print(pw)

# auch möglich
length = 10
pw = "".join(random.sample(symbols, length))
print(pw)
