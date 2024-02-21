"""
Aufgabe: Schreibe ein Programm, welches die Funktionen, die gegeben sind, anwendet,
um einen Bankautomaten zu implementieren.
Hinweis: Auch wenn es nicht schön ist, kann man while True loops verwenden,
um einen "immer aktiven" Ablauf zu programmieren.
"""
def display_menu():
    print("\nWillkommen beim Geldautomaten")
    print("1. Kontostand prüfen")
    print("2. Geld einzahlen")
    print("3. Geld abheben")
    print("4. Beenden")

def check_balance(balance):
    print(f"Ihr aktueller Kontostand beträgt: €{balance}")

def deposit_money(balance):
    amount = float(input("Geben Sie den Einzahlungsbetrag ein: €"))
    return balance + amount

def withdraw_money(balance):
    amount = float(input("Geben Sie den Abhebungsbetrag ein: €"))
    if amount > balance:
        print("Nicht genügend Guthaben für diese Transaktion.")
    else:
        balance -= amount
    return balance

balance = 1000
