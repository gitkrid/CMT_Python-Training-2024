"""
Aufgabe: Schreibe eine Programm, das den Benutzer auffordert, eine Zahl einzugeben.
Das Programm soll die Eingabe in eine Ganzzahl (int) umwandeln und diese ausgeben.
Wenn die Eingabe keine gültige Zahl ist, soll das Programm eine benutzerfreundliche
Fehlermeldung anzeigen.
Implementiere das Exception Handling für diesen Fall. Nutze den ValueError.
Wenn eine gültige Eingabe erfolgt, soll das Programm beendet werden. Andernfalls
wird der Benutzer solange gefragt, bis eine gültige Eingabe stattfand.

Zusatz: Durch das Wort "exit" kann das Programm zusätzlich verlassen werden.
"""
while True:
    user_input = input("Bitte gib eine Zahl ein (oder 'exit' zum Beenden): ")
    try:
        zahl = int(user_input)
    except ValueError:
        if user_input == "exit":
            break
        else:
            print(f"Bitte gib eine Ganzzahl ein, '{user_input}' ist ungültig.")
    else:
        print(f"Die Zahl ist: {zahl}")
        break