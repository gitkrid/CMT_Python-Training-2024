"""
Aufgabe: Überprüfe, ob ein vorher festgelegtes Jahr ein Schaltjahr ist/war.
Folgende Regeln gelten für Schaltjahre:
1) durch 4 teilbar -> Schaltjahr, aber
2) durch 100 teilbar -> kein Schaltjahr, außer
3) durch 400 teilbar -> Schaltjahr
Bsp.: 2000 ist ein Schaltjahr, aber 2100 nicht wegen der 2. Regel
"""

jahr = 1998

# if jahr%4 == 0:
#     if jahr%100 == 0:
#         print(f"{jahr} ist kein Schaltjahr.")
#     elif jahr%400 == 0:
#         print(f"Ja! {jahr} ist ein Schaltjahr!")
#     else:
#         print(f"Ja! {jahr} ist ein Schaltjahr!")
# else:
#     print(f"{jahr} ist kein Schaltjahr.")

# besser:
if jahr % 400 == 0:
    print(f"Ja! {jahr} ist ein Schaltjahr!")
elif jahr % 100 == 0:
    print(f"{jahr} ist kein Schaltjahr.")
elif jahr % 4 == 0:
    print(f"Ja! {jahr} ist ein Schaltjahr!")
else:
    print(f"{jahr} ist kein Schaltjahr.")
