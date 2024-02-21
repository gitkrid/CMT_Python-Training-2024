"""
Aufgabe: Importiere die csv-Datei (csv = comma separated values) "studenten_datensatz.csv".

1.) Importiere die Namen der Studenten und sortiere sie in einer Liste alphabetisch.

2.) Importiere die Informationen aus der csv-Datei in ein dictionary. Lege dazu eine Liste
der verschiedenen dictionaries an.
Bsp.: [{"name": "Hanson", "vorname": "Hans", ...}, {"name": "Peterson", "vorname": "Peter", ...}]
Hinweis: Nutze die zip()-Funktion und nicht die csv.DictReader()-Methode.

3.) Erstelle ein dictionary mit den Kategorien als keys und den Daten als Liste für die values.
Bsp.: {"name":["Hanson", "Meyer", ...], "vorname": ...}
Hinweis: Nutze die zip()-Funktion.

4.) Nutze die Liste aus 2.) und gib die Studenten aus, welche Biochemie studieren.

5.) Nutze 3.), um herauszufinden, ob es Studenten gibt, die Biochemie studieren und die
gleiche Lieblingsfarbe haben.
"""

import csv