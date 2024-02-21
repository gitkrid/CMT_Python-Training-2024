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

# 1.)
with open("11 file handling/studenten_datensatz.csv", "r", encoding="utf-8") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=";")
    header = next(csv_reader)
    names = list()
    for row in csv_reader:
        names.append(row[0])
    print(sorted(names))


# 2.)
students_list = list()

with open("11 file handling/studenten_datensatz.csv", "r", encoding="utf-8") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=";")
    header = next(csv_reader)
    for row in csv_reader:
        # mit dict comprehension
        zipped = {key: value for key, value in zip(header, row)}
        # alternativ
        # zipped = {}
        # for key, value in zip(header, row):
        #     zipped[key] = value
        students_list.append(zipped)
    print(students_list)


# 3.)
students_3 = dict()
with open("11 file handling/studenten_datensatz.csv", "r", encoding="utf-8") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=";")
    header = next(csv_reader)
    # mit dict comprehension
    students_3 = {key: list() for key in header}
    # alternativ
    # for h in header:
    #     students_3[h] = []
    for row in csv_reader:
        for h, value in zip(header, row):
            students_3[h].append(value)


# 4.)
for d in students_list:
    if d["Studienfach"] == "Biochemie":
        print(d)


# 5.)
farben = dict()
for d in students_list:
    if d["Studienfach"] == "Biochemie":
        if not d["Lieblingsfarbe"] in farben:
            farben[d["Lieblingsfarbe"]] = [d["Matrikelnummer"]]
        else:
            farben[d["Lieblingsfarbe"]].append(d["Matrikelnummer"])
print(farben)


# Zusatz
# key erwartet eine Funktion, die dann auf jedes Listenelement der zu sortierenden Liste
# angewendet wird
sortiert1 = sorted(students_list, key=lambda item: item["Vorname"])
# ohne anonyme Lambda-Funktion
# die Funktion darf nur einen Parameter haben
# dieser ist automatisch das Listenelement selbst (hier also ein dictionary)
def hallo(d):
    return d["Vorname"]
sortiert2 = sorted(students_list, key=hallo)

# überprüfen, ob wirklich das gleiche herauskommt
if sortiert1 == sortiert2:
    print(True)
