"""
Aufgabe: Schreibe eine Funktion, der ein Zahlenbereich (bspw. 0 bis 100) übergeben
wird. Die Funktion soll jedes Mal "fizz" ausgeben, wenn die Zahl durch 3 und jedes Mal
"buzz" ausgeben, wenn die Zahl durch 5 teilbar ist. Ist die Zahl sowohl durch
5 als auch durch 3 teilbar soll "FizzBuzz" ausgegeben werden. Gib sonst die Zahl selbst aus.
"""

def fizz_buzz(f, t):
    for i in range(f, t + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

fizz_buzz(0, 100)
