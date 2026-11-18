# Prompt: Berufsliste Schweiz für die RAV-Beratung

Diesen Text können Sie unverändert in ein KI-Werkzeug mit Websuche einfügen (zum Beispiel Claude, ChatGPT oder Gemini mit Recherchefunktion). Er ist so gebaut, dass die Arbeit in mehreren Durchgängen weitergeführt werden kann. Am Ende der Datei steht, wie.

---

## 1. Rolle und Ziel

Du unterstützt eine RAV-Beratungsperson in der Schweiz. Baue eine **Berufsliste für die Schweiz**, mit der die Beratungsperson stellensuchenden Personen **alternative Berufe und Suchgebiete** vorschlagen kann.

Die Liste hat drei Perspektiven auf denselben Beruf:

1. **Amtliche Nomenklatur:** Berufsbezeichnung und Code in der aktuellen Schweizer Berufsnomenklatur (CH-ISCO-19) und, wo sinnvoll, der Berufe der beruflichen Grundbildung.
2. **Englische Bezeichnungen:** alle gebräuchlichen englischen Berufsbezeichnungen (ISCO-08 englisch, ESCO, Stellenmarkt).
3. **Bezeichnungen im Internet:** so, wie Arbeitgeber die Stelle tatsächlich ausschreiben (Jobtitel auf Jobportalen, auch Modewörter, Abkürzungen, Mischformen DE/EN).

Die Berufe sind **nach Zusammenhängen** geordnet: in Berufsfelder (Cluster), und innerhalb eines Feldes nach Verwandtschaft. Zusätzlich wird erfasst, **welche Felder und Berufe nahe beieinander liegen**, damit aus «Buchhalter/in» sichtbar wird, was an Nachbarfeldern in Frage kommt.

## 2. Szenario (wofür die Liste gebraucht wird)

Eine stellensuchende Person findet im bisherigen Beruf nichts. Die Beratungsperson will in einem Gespräch:

- zeigen, **wie der bisherige Beruf amtlich und im Markt heisst** (damit in Job-Room und auf Portalen die richtigen Suchbegriffe benutzt werden),
- **verwandte Berufe** nennen, in die man ohne oder mit kurzer Weiterbildung wechseln kann,
- **Suchgebiete** (Berufsfelder) vorschlagen, an die die Person nicht gedacht hat,
- **Suchbegriffe** in Deutsch, Englisch und in der Sprache der Ausschreibungen liefern (auch Französisch und Italienisch, weil die Schweiz mehrsprachig ist).

Die Liste ist ein **Gesprächs- und Suchhilfsmittel**. Sie macht keine Vermittlungsentscheide und keine Aussage über Anspruch oder Eignung einer Person.

## 3. Quellen (in dieser Reihenfolge und mit Quellenangabe)

Verwende nur öffentlich zugängliche Quellen und prüfe deren Nutzungsbedingungen. Gib bei jedem Datensatz die Quelle und das Abrufdatum an.

**A. Amtliche Nomenklatur und Berufe**
- Bundesamt für Statistik (BFS): Schweizer Berufsnomenklatur **CH-ISCO-19** (Codes, Bezeichnungen, Gruppen; DE/FR/IT/EN). Sie baut auf der internationalen ISCO-08 auf (4 Stellen) und ergänzt eine 5. Stelle für die Schweiz. Prüfe, ob eine neuere Fassung existiert, und nenne die benutzte Version.
  - **Beste Datenquelle:** der **Zuweisungsschlüssel** als Excel-Datei (rund 23'000 aktive Berufsbezeichnungen mit Code, DE/FR/IT/EN, männlich/weiblich). Version 1.2 (Oktober 2022): https://dam-api.bfs.admin.ch/hub/api/dam/assets/23530845/master. Spalte `CH_ISCO_19` ist der 5-stellige Code, `ACTIVE` = 1 heisst aktive Bezeichnung. Die Datei nennt nur Einzeltitel, keine Gruppennamen; Gruppennamen sind dann sinngemäss zu formulieren und als solche zu kennzeichnen.
  - Die Datei ist die Quelle für Code und amtlichen Titel. Prüfe zuerst, ob damit der Eintrag schon belegt ist, bevor du weitere Quellen heranziehst.
- **Job-Room / AVAM** (SECO): die Berufsauswahl im Stellenportal der Arbeitsvermittlung. Sie zeigt, unter welchen Bezeichnungen Stellen und Profile in der RAV-Praxis erfasst werden.
- **berufsberatung.ch** (SDBB): Berufe, Berufsfelder, Weiterbildungen, Verwandte Berufe.
- **SBFI-Berufsverzeichnis** und Bildungsverordnungen: Berufe der beruflichen Grundbildung (EFZ, EBA) mit offiziellem Titel.
- Berufe der höheren Berufsbildung (eidgenössische Berufsprüfung, höhere Fachprüfung, höhere Fachschule) und Fachhochschul-/Universitätsabschlüsse, soweit sie zu einem Beruf führen.

**B. Englisch und Zusammenhänge**
- **ISCO-08** (ILO), englische Titel.
- **ESCO** (EU): Berufe mit **alternativen Bezeichnungen** in mehreren Sprachen und mit **Fähigkeiten und Wissen pro Beruf**. Daraus lassen sich Verwandtschaften ableiten (gemeinsame Fähigkeiten). Öffentliche Schnittstelle: `https://ec.europa.eu/esco/api/search?language=en&type=occupation&text=<Begriff>` und `https://ec.europa.eu/esco/api/resource/occupation?language=en&uri=<URI>` (liefert `alternativeLabel`, ISCO-Gruppe und Fähigkeiten). Prüfe, dass die ISCO-Gruppe des Treffers zur gesuchten Gruppe passt; nimm sonst den Treffer nicht.
- **O*NET OnLine** (USA): «Related Occupations» und «Alternate Titles» als Hinweis auf Verwandtschaft; Hinweis auf die US-Herkunft in der Quelle.

**C. Bezeichnungen im Internet**
- Jobportale der Schweiz, zum Beispiel jobs.ch, jobup.ch, jobscout24.ch, indeed.ch, x28.ch, LinkedIn, Job-Room. Prüfe Titel in **echten, aktuellen Ausschreibungen** und notiere Titel, die vom amtlichen Titel abweichen.
  - Technischer Hinweis: die öffentliche Stellensuche von jobs.ch lässt sich per `https://www.jobs.ch/api/v1/public/search?rows=20&query=<Begriff>` abfragen (Parameter `query`, höchstens 20 Treffer pro Anfrage). Mit wenigen Anfragen und Pausen arbeiten, Nutzungsbedingungen beachten, Rohdaten nicht weitergeben, nur Titel mit Quelle und Datum übernehmen.
  - Mehrere Suchbegriffe pro Berufsgruppe verwenden (deutsch und englisch) und nur Titel übernehmen, die tatsächlich in den Treffern vorkommen. Häufigkeit in der Stichprobe angeben, nicht als Marktanteil darstellen.
- Branchen- und Berufsverbände und Lohnportale (zum Beispiel Salarium des BFS) für gebräuchliche Titel.

Wenn zwei Quellen sich widersprechen, **nenne beide** und markiere den Eintrag als «zu klären». Erfinde nichts.

## 4. Vollständigkeit: was «alle» hier heisst

«Alle Berufe» ist nicht abschliessend aufzählbar, weil Jobtitel im Internet unbegrenzt variieren. Arbeite daher mit zwei klaren Massstäben:

1. **Amtliche Vollständigkeit:** jede Berufsart (5-Steller) der CH-ISCO-19 ist **mindestens einmal** als Eintrag erfasst, entsprechend den 4-stelligen Berufsgattungen der ISCO-08. Ein Eintrag ist eine Berufsgruppe mit allen ihren Bezeichnungen (im Beispielfeld IT: 24 Einträge). Berufe der beruflichen Grundbildung sind den passenden Gruppen zugeordnet.
2. **Marktabdeckung:** pro Beruf die **häufigsten** Titel aus Stellenausschreibungen (Richtwert: bis zu 10 pro Beruf, nach Häufigkeit), nicht jede Schreibvariante.

Führe eine **Abdeckungstabelle** (siehe Abschnitt 8), damit sichtbar ist, was erledigt ist und was fehlt.

## 5. Ordnung nach Zusammenhängen

Verwende diese **Berufsfelder** als Grundordnung (anpassen, wenn die Quellen es nahelegen, und jede Anpassung begründen):

IT & Digital · Technik & Ingenieurwesen · Industrie & Produktion · Bau & Handwerk · Gesundheit & Pflege · Soziales & Bildung · Büro & Administration · Finanzen & Versicherung · Handel & Verkauf · Gastgewerbe & Tourismus · Logistik & Verkehr · Sicherheit & Öffentliche Dienste · Land- & Forstwirtschaft · Medien, Kreation & Kommunikation · Recht, Beratung & Management · Reinigung & Hauswirtschaft · Wissenschaft & Forschung

Für jedes Feld:
- **Verwandte Felder** mit Begründung in einem Satz (zum Beispiel «Logistik ↔ Handel: gemeinsame Warenkenntnis, Lagersysteme»).
- Innerhalb des Feldes **Unterfelder** (zum Beispiel IT: Entwicklung, Betrieb/Infrastruktur, Support, Daten, Sicherheit).
- Pro Beruf **Nachbarberufe** (ID anderer Berufe), mit dem Grund der Verwandtschaft (gemeinsame Fähigkeiten, gleiche Branche, Aufstieg, Quereinstieg).

Ergänze pro Beruf, wenn die Quelle es hergibt:
- **Zugang/Niveau:** ohne Lehre, EBA, EFZ, höhere Berufsbildung, FH/Uni (nur was die Quelle sagt).
- **Quereinstieg:** typischer Weg aus Nachbarberufen oder nötige kurze Weiterbildung, mit Quelle.

## 6. Datenformat (verbindlich)

Liefere JSON, das direkt in die Seite übernommen werden kann (Schema entspricht der Datei `berufe.json` der Seite).

```json
{
  "meta": { "version": "1", "stand": "JJJJ-MM-TT", "nomenklatur": "CH-ISCO-19 (Version nennen)", "quellen": ["Name, URL, Abrufdatum"] },
  "cluster": [
    { "id": "it", "de": "IT & Digital", "en": "IT & Digital", "beschreibung": "…", "unterfelder": ["Entwicklung", "Betrieb"],
      "verwandt": [ { "id": "technik", "grund": "…" } ] }
  ],
  "berufe": [
    {
      "id": "it-25121",
      "cluster": "it",
      "unterfeld": "Entwicklung & Architektur",
      "gruppe": "Software-Entwicklung und -Architektur (sinngemässe Beschreibung)",
      "isco08": "2512",
      "isco08_en": "Software developers",
      "ch_isco19": "25121",
      "de": ["Softwareentwickler/in", "Informatiker/in EFZ (Applikationsentwicklung)"],
      "fr": [], "it": [],
      "en": ["Software developer"],
      "en_esco": ["software developer", "application programmer"],
      "web": [ { "titel": "Fullstack Software Engineer", "sprache": "de/en", "haeufigkeit": 3, "quelle": "jobs.ch Stellensuche, Abruf 2026-11-16: 3 von 53 gesichteten Titeln" } ],
      "niveau": "Titel im Zuweisungsschlüssel nennen: FH, BP",
      "anzahl_titel": 35,
      "nachbarn": [ { "id": "it-25130", "grund": "gemeinsame ESCO-Kernfähigkeiten: computer programming" } ],
      "nachbar_felder": [ { "id": "wissenschaft", "grund": "Beleg in einem Satz, nur mit Quelle" } ],
      "quereinstieg": "",
      "quellen": ["BFS Zuweisungsschlüssel CH-ISCO-19 V1.2 (10/2022), Code 25121: 35 aktive Titel", "ESCO «software developer» <URI> (Abruf 2026-11-16)"],
      "status": "geprüft | entwurf | zu_klären"
    }
  ]
}
```

Regeln:
- `id` ist stabil, klein geschrieben, ohne Umlaute und Leerzeichen.
- **Codes nur eintragen, wenn die Quelle sie nennt.** Sonst `null`. Keine geschätzten Codes.
- `status: "geprüft"` nur, wenn der Titel und der Code in einer amtlichen Quelle gesehen wurden. Jobtitel aus dem Internet sind immer mit Quelle und Datum versehen.
- Weibliche und männliche Form wie in der Quelle («Koch/Köchin»).
- Keine Personendaten, keine Lohnangaben ohne Quelle, keine Aussagen zu Arbeitslosenversicherung oder Anspruch.

## 7. Arbeitsweise

1. **Plan zuerst:** Lege die Reihenfolge fest: zuerst das Gerüst (Felder und Unterfelder), dann Feld für Feld die Berufe. Nenne, welches Feld du jetzt bearbeitest.
2. **Pro Durchgang ein Feld oder höchstens 25 Berufe**, damit nichts abgeschnitten wird. Liefere am Ende des Durchgangs das JSON **nur für diesen Durchgang** (neue und geänderte Einträge) und die aktualisierte Abdeckungstabelle.
3. **Prüfe jeden Eintrag gegen mindestens eine amtliche Quelle** und, für `web`, gegen mindestens zwei aktuelle Ausschreibungen.
4. **Dubletten:** Prüfe vor dem Hinzufügen, ob ein Beruf schon unter einem anderen Titel erfasst ist. Fasse zusammen und liste die Varianten unter `de`, `en`, `web`.
5. **Unsicherheit offen sagen:** wenn du etwas nicht findest oder nicht lesen kannst, schreibe «nicht gefunden», setze `status: "zu_klären"` und fahre fort. Nicht raten.
6. **Am Schluss jedes Durchgangs** drei Zeilen: erledigt, offen, nächster Schritt.

## 8. Abdeckungstabelle (mitführen und jedes Mal aktualisieren)

| Berufsfeld | CH-ISCO-19 Einheitsgruppen im Feld | davon erfasst | davon geprüft | offen / zu klären |
| --- | --- | --- | --- | --- |
| IT & Digital | … | … | … | … |

Zähle die Einheitsgruppen aus der Quelle, nicht aus dem Gedächtnis.

## 9. Qualitätsprüfung vor der Abgabe

- Stimmt jeder Code mit der Quelle überein?
- Hat jeder Eintrag Quelle und Status?
- Gibt es Berufe ohne Nachbarn? (Mindestens zwei Nachbarn pro Beruf, ausser die Quelle gibt weniger her.)
- Sind englische Titel wirklich gebräuchlich (nicht wörtlich übersetzt)?
- Sind Titel aus dem Internet echt und aktuell (nicht erfunden)?
- Kommen Hilfsberufe, Lehrberufe, höhere Berufsbildung und akademische Berufe gleichermassen vor, unabhängig vom Geschlecht, das der Beruf traditionell hatte?

## 10. Weiterarbeiten in einem neuen Gespräch

Wenn das Gespräch zu lang wird oder abbricht, starten Sie ein neues. Fügen Sie dort **diesen Prompt** ein und hängen Sie an:

> Stand: Hier ist die bisherige `berufe.json` und die Abdeckungstabelle. Mache beim Feld **<Name>** weiter, ohne bestehende Einträge zu ändern ausser bei Fehlern (diese nennen).

So bleibt die Arbeit zusammenhängend. Die fertige `berufe.json` kann in die Seite eingefügt werden; sie zeigt Suche, Berufsfelder, die drei Spalten (amtlich, Englisch, Internet) und die Nachbarberufe.

## 11. Hinweis

Das Ergebnis ist ein Hilfsmittel und ersetzt weder die amtlichen Berufsverzeichnisse noch die Fachberatung. Die Beratungsperson prüft Einträge, bevor sie sie weitergibt.

## 12. Stand der Arbeit und Referenzbeispiel

- **Erledigt:** Alle 17 Berufsfelder sind befüllt: 549 Berufsarten der CH-ISCO-19 (V1.2, aktive Titel). **IT & Digital** und **Büro & Administration** wurden von Hand geprüft (Status «geprüft») und dienen als Referenz für Format und Tiefe: https://alexfuchs.github.io/rav-berufe/ (Daten: `assets/berufe.json`).
- **Regelbasiert erzeugt (Status «entwurf»):** die übrigen 15 Felder. Die Zuordnung der ISCO-Gruppen zu Feldern und Unterfeldern ist eine Setzung des Projekts, die Gruppennamen stammen aus ESCO (de), die Internettitel aus jobs.ch, jobup.ch und job-room.ch (bereinigt, Allerweltswörter gefiltert, Stichprobe je Suchbegriff), die Verweise zwischen Feldern nur aus gleicher ISCO-08-Untergruppe. **Offen:** diese Einträge von Hand prüfen und auf «geprüft» setzen, Quereinstiege mit Beleg ergänzen, Gruppen ohne Internettitel (rund 100) mit weiteren Suchbegriffen abfragen.
- **Nicht erfasst im Referenzfeld:** Berufe, die die CH-ISCO-19 anderen Feldern zuordnet (zum Beispiel Grafik und UX unter Medien). Sie gehören ins jeweilige Feld, im IT-Feld nur als `nachbar_felder` mit Beleg.
- **Vorgehen, das sich bewährt hat:** (1) Gruppen und Titel aus dem BFS-Zuweisungsschlüssel ziehen, (2) pro Gruppe ESCO-Treffer mit passender ISCO-Gruppe suchen, (3) pro Gruppe 3 bis 6 Suchbegriffe auf jobs.ch abfragen und nur tatsächlich gefundene Titel eintragen, (4) Nachbarn aus gemeinsamen ESCO-Kernfähigkeiten, sonst aus derselben ISCO-Untergruppe, (5) Quellen pro Eintrag festhalten. Die Skripte dazu liegen im Repository unter `_tools/` (pro Feld eine Konfigurationsdatei `field_*.py`; von Hand: `collect_field.py` und `compile_field.py`; automatisch: `gen_fields.py` erzeugt `field_*_auto.py`, `collect_multi.py` fragt drei Portale ab, `compile_multi.py` baut den Eintrag, `finish.py` ergänzt Feldverweise und Meta; ESCO-Treffer mit nicht passender ISCO-Gruppe werden verworfen).
