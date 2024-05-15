"""
Aufgabe: Schreibe eine Funktion, die die Gesamtarbeitszeit eines Tages erfasst,
wenn Startuhrzeit und Enduhrzeit gegeben ist. Verwende KEINE externen Module.

Hinweis: Überlege dir, wie du die Uhrzeiten gut erfassen kannst, um leichte Rechnungen
zu haben. Tipp: Du solltest 4 Parameter für deine Funktion haben.
"""

# h - Stunde
# m - Minute
def arbeitszeit(h_start, m_start, h_ende, m_ende):
    delta_stunden = h_ende - h_start
    # delta_minuten = abs(m_ende - m_start) # falsch!
    if m_ende < m_start:
        delta_minuten = 60 - m_start + m_ende
    else:
        delta_stunden += 1
        delta_minuten = m_ende - m_start
    return f"{delta_stunden} h, {delta_minuten} m"

print(arbeitszeit(7, 12, 17, 32))