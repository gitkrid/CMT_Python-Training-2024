"""
Kontext: Sie arbeiten als Entwickler in einem Unternehmen, das eine große Menge
an Webserver-Logdateien analysiert, um Informationen über Zugriffe auf die Webseite
zu gewinnen. Diese Logdateien sind sehr groß, manchmal mehrere Gigabyte pro Datei.
Sie müssen eine effiziente Methode entwickeln, um bestimmte Daten aus diesen Dateien
zu extrahieren, ohne den gesamten Dateiinhalt auf einmal in den Speicher zu laden.
Dies ist ein perfekter Anwendungsfall für Generatoren in Python, da sie es
ermöglichen, die Datei zeilenweise zu verarbeiten, wodurch der Speicherverbrauch
erheblich reduziert wird.

Aufgabe: Aufgabe: Schreiben Sie einen Generator in Python, der durch eine
Logdatei iteriert und nur die Einträge zurückgibt, die einen HTTP-Statuscode
200 haben. Der Generator soll flexibel genug sein, um nach anderen Statuscodes
oder Kriterien filtern zu können, falls gewünscht.
"""
