"""
Aufgabe: Nutze die map() Funktion mit der lambda Funktion, um aus
jedem String in der Liste alles in GROßBUCHSTABEN zu machen.
Hinweis: string.upper() könnte helfen.
"""

farben = ["rot", "gelb", "blau", "lila"]

farben_gross = list(map(lambda x: x.upper(), farben))
print(farben_gross)
