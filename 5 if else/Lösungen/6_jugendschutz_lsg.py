"""
Aufgabe: Entwirf eine Schutzregelung für einen Zigarettenautomat und prüfe auch,
ob genug Geld für den Kauf zur Verfügung steht. Überprüfe dein Programm durch verschiedene
Eingaben.
"""
prices = {"1": 5.20, "2": 4.80, "3": 6.00}
money = 5.5

print("Was wollen Sie kaufen?")
print("Bitte wählen: 1 = Marlboro, 2 = Chesterfield, 3 = Lucky Strike")
choice = input() # 1, 2 oder 3

print("Bitte bestätigen Sie ihr Alter:")
age = int(input())

# prüfe Alter
if age >= 18:
    # prüfe Geld
    #if (money - prices[choice]) >= 0:
    if money >= prices[choice]:
        print("Bitteschön, hier sind Ihre Zigaretten.")
        print("WARNUNG: Rauchen kann tötlich sein!")
    else:
        print("Sie haben nicht genug Geld.")
else:
    print("Sie sind nicht alt genug, um Zigaretten zu kaufen.")
