"""
Szenario: Ein Programm, das zwei Zahlen von einem Benutzer anfordert und diese dividiert.

Ohne Exception Handling:
"""
numerator = int(input("Geben Sie den Zähler ein: "))
denominator = int(input("Geben Sie den Nenner ein: "))
result = numerator / denominator
print("Das Ergebnis der Division ist:", result)

"""
Wenn der Benutzer als Nenner eine 0 eingibt, führt dies zu einem ZeroDivisionError,
da eine Division durch Null in der Mathematik nicht definiert ist und Python standardmäßig einen Fehler auswirft.

Mit Exception Handling:
"""
try:
    numerator = int(input("Geben Sie den Zähler ein: "))
    denominator = int(input("Geben Sie den Nenner ein: "))
    result = numerator / denominator
except ZeroDivisionError:
    print("Fehler: Division durch Null ist nicht erlaubt.")
except ValueError:
    print("Fehler: Bitte geben Sie eine gültige Zahl ein.")
else:
    print("Das Ergebnis der Division ist:", result)


"""
Weiteres Beispiel:
Beispiel mit finally und else

Szenario: Ein Programm, das versucht, eine Datei zu öffnen, aus ihr zu lesen und
die Datei anschließend sicher zu schließen, unabhängig davon, ob ein Fehler aufgetreten ist oder nicht.

Code:
"""
try:
    file = open("beispiel.txt", "r")
    inhalt = file.read()
    print("Dateiinhalt:", inhalt)
except FileNotFoundError:
    print("Fehler: Die Datei wurde nicht gefunden.")
else:
    print("Die Datei wurde erfolgreich gelesen.")
finally:
    print("Schließe die Datei...")
    file.close()

"""
- Der try-Block versucht, die Datei zu öffnen und zu lesen.
- Der except-Block fängt den Fehler ab, falls die Datei nicht existiert.
- Der else-Block wird ausgeführt, wenn keine Ausnahme auftritt, d.h., die Datei
existiert und wurde erfolgreich gelesen.
- Der finally-Block wird immer ausgeführt, unabhängig davon, ob eine Ausnahme
aufgetreten ist oder nicht. Dies ist ideal, um Ressourcen freizugeben, z.B. Dateien zu schließen.
"""