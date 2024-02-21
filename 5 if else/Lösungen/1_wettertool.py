"""
Ziel: Schreiben Sie ein Python-Programm, das den Benutzer nach der aktuellen
Temperatur fragt und basierend auf dieser Eingabe unterschiedliche Empfehlungen
ausspricht.

Anweisungen:
    - Das Programm sollte den Benutzer auffordern, die aktuelle Temperatur in
    Grad Celsius einzugeben.
    - Basierend auf der eingegebenen Temperatur soll das Programm entscheiden
    und ausgeben:
        - Ist die Temperatur unter 0 Grad Celsius, soll das Programm empfehlen,
        nicht nach draußen zu gehen, da es zu kalt ist.
        - Liegt die Temperatur zwischen 0 und 15 Grad Celsius, soll das Programm
        empfehlen, eine Jacke anzuziehen.
        - Bei Temperaturen zwischen 16 und 25 Grad Celsius soll das Programm
        sagen, dass das Wetter angenehm ist.
        - Bei Temperaturen über 25 Grad Celsius soll das Programm empfehlen,
        einen Sonnenhut zu tragen, da es warm ist.
"""
temperatur = float(input("Bitte geben Sie die aktuelle Temperatur in Grad Celsius ein: "))

if temperatur < 0:
    print("Es ist zu kalt, um nach draußen zu gehen.")
elif 0 <= temperatur <= 15:
    print("Es ist kühl. Vergessen Sie nicht, eine Jacke anzuziehen!")
elif 16 <= temperatur <= 25:
    print("Das Wetter ist angenehm.")
else:
    print("Es ist warm draußen. Tragen Sie einen Sonnenhut!")
