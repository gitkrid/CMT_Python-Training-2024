"""
Aufgabe: Schreibe ein Programm, welches kontrolliert, ob ein eingegebens Passwort
korrekt ist. Nebenbedingung ist, dass maximal 5 Versuche gewährt werden.
"""

korrektes_passwort = "ExtremSicher123#"

eingabe = input("Bitte geben Sie Ihr Passwort ein: ")
versuche = 1
while eingabe != korrektes_passwort:
    print("Falsches PW. BItte versuchen Sie es erneut.")
    eingabe = input("Bitte geben Sie Ihr Passwort ein: ")
    versuche += 1
    if versuche == 5:
        print("5 Fehlversuche ...")
        break
else:
    print("Sie sind eingeloggt!")
