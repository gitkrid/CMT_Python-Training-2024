"""
Aufgabe: Erweitere das Modul "my_module", um die folgenden Funktionen:
- rest: berechnet den Rest der Division zweier Werte a und b
- quadratische Funktionen: berechnet die y Werte einer quadratischen Funktion
mit gegebenen Parametern a, b, c und einem interval
- beliebige Funktionen: eine Funktion, die abhängig von der gegebenen Anzahl an
Parametern die Funktionswerte der entsprechenden Ordnung bestimmt. (Bsp.:
2 Parameter = linear, 3 Parameter = quadratisch usw.)
"""
import numpy as np


# in my_module.calculate
def rest(a, b):
    return a % b


# in my_module.math_functions
def quadratic_function(a, b, c, interval):
    x_values = np.linspace(interval[0], interval[1], 100)
    return a * x_values**2 + b * x_values + c


# in my_module.math_functions
def order_n_function(*args, interval=[0, 1]):
    x_values = np.linspace(interval[0], interval[1], 100)
    result = 0
    for i, param in enumerate(args, start=1):
        result += param * x_values ** (len(args) - i)
    return result

# f(x) = x^2
print(quadratic_function(1, 0, 0, [0, 3]))
# f(x) = x^3 + 1
print(order_n_function(1, 0, 0, 1, interval=[0, 3]))
