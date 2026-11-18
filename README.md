# Berufsliste Schweiz

Hilfsmittel für die RAV-Beratung: Berufe nach Berufsfeldern, mit amtlicher Bezeichnung, englischen Bezeichnungen und Titeln aus dem Internet.

- `index.html`, `assets/`: die Seite (statisch, ohne Server)
- `assets/berufe.json`: die Daten (Schema siehe Prompt)
- `prompt-berufsliste-RAV.md`: Prompt, mit dem die Liste recherchiert und erweitert wird
- `_tools/`: Skripte (BFS-Zuweisungsschlüssel, ESCO, jobs.ch, jobup.ch, job-room.ch); Rohdaten und Quelldateien bleiben lokal (`_quellen/`)

Stand: alle 17 Felder befüllt, 549 Berufsarten (CH-ISCO-19). IT und Büro von Hand geprüft, die übrigen regelbasiert erzeugt (Status «entwurf»).
