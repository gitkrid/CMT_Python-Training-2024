"""
Aufgabe: Schreibe eine Funktion, die dir für eine Anzahl an gefahrenen Kilometern
den Spritpreis berechnet.
"""

# km: gefahrene Kilometer
# verbrauch: wie viel Liter Sprit wird pro km verbraucht (z.B. bei 5 L pro 100 km -> 0,05 L pro km)
# kosten: wie viel kostet 1 Liter Sprit
# rückgabe: Kosten für die Strecke
def spritkosten(km, verbrauch, kosten):
    gesamtverbrauch = km * verbrauch # in Liter
    gesamtkosten = gesamtverbrauch * kosten
    return gesamtkosten

print(spritkosten(100, 0.05, 1.8))
