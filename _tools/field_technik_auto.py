# Automatisch erzeugt (gen_fields.py) aus BFS-Zuweisungsschlüssel V1.2 und ESCO-ISCO-Gruppennamen
CLUSTER = 'technik'
PREFIX = 'te'
APPEND = False
BESCHREIBUNG = 'Ingenieurwesen und technische Berufe ausserhalb IT, Bau und Produktion. Basis: CH-ISCO-19, zugeordnet nach ISCO-08-Gruppen; Gruppennamen aus ESCO (de).'
UNTERFELDER = ['Leitung Technik', 'Ingenieurwesen & Technik', 'Elektronik & Feinwerk']
W = 'auto'
NF = {}
G = {
'13000': ('Leitung Technik', '130', 'Sammelgruppe 13000 (ohne eigene ISCO-08-Gattung)', 'Sammelgruppe: Direktor Technisches Büro, Betriebsverantwortlicher (nicht Direktionsmitglied)', [], ['Direktor Technisches Büro', 'Technischer Manager', 'Betriebsverantwortlicher']),
'20000': ('Ingenieurwesen & Technik', '200', 'Sammelgruppe 20000 (ohne eigene ISCO-08-Gattung)', 'Sammelgruppe: Dr. sc. tech., dipl. Ingenieur, Wissenschaftlicher Adjunkt (Privatwirtschaft)', ['consultant'], ['Berater', 'Experte', 'Forscher', 'Consultant']),
'21400': ('Ingenieurwesen & Technik', '214', 'Sammelgruppe 21400 (ohne eigene ISCO-08-Gattung)', 'Sammelgruppe: Dr. Ingenieur, Berechnungsingenieur', ['engineer'], ['Ingenieur', 'Prüfingenieur', 'Chefingenieur', 'Engineer']),
'21430': ('Ingenieurwesen & Technik', '2143', 'Environmental engineers', 'Umweltschutzingenieure [ESCO-Gruppenname]', ['environmental technologist'], ['Umweltingenieur', 'Umwelttechnologe', 'Umweltanalytiker', 'Environmental technologist']),
'21490': ('Ingenieurwesen & Technik', '2149', 'Engineering professionals not elsewhere classified', 'Ingenieure, anderweitig nicht genannt [ESCO-Gruppenname]', ['timber construction engineer'], ['Bioingenieur', 'Atomingenieur', 'Glasingenieur', 'Timber construction engineer']),
'21510': ('Ingenieurwesen & Technik', '2151', 'Electrical engineers', 'Ingenieure im Bereich Elektrotechnik [ESCO-Gruppenname]', ['electrical engineer'], ['Lichtingenieur', 'Elektroingenieur', 'Leitungsingenieur', 'Electrical engineer']),
'21520': ('Ingenieurwesen & Technik', '2152', 'Electronics engineers', 'Ingenieure im Bereich Elektronik [ESCO-Gruppenname]', ['chip designer'], ['Chipdesigner', 'Messingenieur', 'Radaringenieur', 'Chip designer']),
'21530': ('Ingenieurwesen & Technik', '2153', 'Telecommunications engineers', 'Ingenieure im Bereich Telekommunikationstechnik [ESCO-Gruppenname]', ['radio engineer'], ['Funkingenieur', 'Radioingenieur', 'Video-Ingenieur', 'Radio engineer']),
'21650': ('Ingenieurwesen & Technik', '2165', 'Cartographers and surveyors', 'Kartografen und Vermessungsingenieure [ESCO-Gruppenname]', ['geodesist'], ['Geodät', 'Topograf', 'Geometer', 'Geodesist']),
'30000': ('Ingenieurwesen & Technik', '300', 'Sammelgruppe 30000 (ohne eigene ISCO-08-Gattung)', 'Sammelgruppe: Technischer Supporter, Technischer Beamter', ['technical supporter'], ['Spezialist', 'Fachmeister', 'Technischer Beamter', 'Technical supporter']),
'30001': ('Ingenieurwesen & Technik', '300', 'Sammelgruppe 30001 (ohne eigene ISCO-08-Gattung)', 'Sammelgruppe: Projekttechniker, Projektmanager (Direktionsmitglied)', ['project leader'], ['Projektleiter', 'Projektmanager', 'Projekttechniker', 'Project leader']),
'30002': ('Ingenieurwesen & Technik', '300', 'Sammelgruppe 30002 (ohne eigene ISCO-08-Gattung)', 'Sammelgruppe: Gemeindewerkmeister, Arbeitsvorarbeiter', [], ['Souschef', 'Teamleiter', 'Gruppenführer']),
'31000': ('Ingenieurwesen & Technik', '310', 'Sammelgruppe 31000 (ohne eigene ISCO-08-Gattung)', 'Sammelgruppe: Ingenieurassistent, Techniker', ['technician'], ['Techniker', 'Ingenieurassistent', 'Technikmitarbeiter', 'Technician']),
'31100': ('Ingenieurwesen & Technik', '311', 'Sammelgruppe 31100 (ohne eigene ISCO-08-Gattung)', 'Sammelgruppe: Entwicklungskonstrukteur', [], ['Entwicklungskonstrukteur']),
'31110': ('Ingenieurwesen & Technik', '3111', 'Chemical and physical science technicians', 'Chemo- und Physikotechniker [ESCO-Gruppenname]', ['laboratory assistant'], ['Laborist', 'Laborant', 'Laborassistent', 'Laboratory assistant']),
'31111': ('Ingenieurwesen & Technik', '3111', 'Chemical and physical science technicians', 'Chemo- und Physikotechniker [ESCO-Gruppenname]', ['chemical laboratory worker'], ['Lacklaborant', 'Chemiemeister', 'Analysenzieher', 'Chemical laboratory worker']),
'31112': ('Ingenieurwesen & Technik', '3111', 'Chemical and physical science technicians', 'Chemo- und Physikotechniker [ESCO-Gruppenname]', ['metallographer'], ['Radiometrist', 'Metallograph', 'Physiklaborant', 'Metallographer']),
'31130': ('Ingenieurwesen & Technik', '3113', 'Electrical engineering technicians', 'Elektrotechniker [ESCO-Gruppenname]', ['lighting planner'], ['Ampelbauer', 'Lichtplaner', 'Elektroplaner', 'Lighting planner']),
'31140': ('Ingenieurwesen & Technik', '3114', 'Electronics engineering technicians', 'Techniker im Bereich Elektronik [ESCO-Gruppenname]', ['hardware technician'], ['Optroniker', 'Netzplaner', 'Radartechniker', 'Hardware technician']),
'31180': ('Ingenieurwesen & Technik', '3118', 'Draughtspersons', 'Technische Zeichner [ESCO-Gruppenname]', ['draughtsperson'], ['Zeichner', 'Entwerfer', 'Skizzierer', 'Draughtsperson']),
'31181': ('Ingenieurwesen & Technik', '3118', 'Draughtspersons', 'Technische Zeichner [ESCO-Gruppenname]', ['watch draughtsman'], ['Konstrukteur', 'Mikrozeichner', 'Uhrenzeichner', 'Watch draughtsman']),
'31182': ('Ingenieurwesen & Technik', '3118', 'Draughtspersons', 'Technische Zeichner [ESCO-Gruppenname]', ['structural draughtsman'], ['Bauzeichner', 'Neonzeichner', 'Betonzeichner', 'Structural draughtsman']),
'31183': ('Ingenieurwesen & Technik', '3118', 'Draughtspersons', 'Technische Zeichner [ESCO-Gruppenname]', ['refrigeration systems draughtsman'], ['Sanitärplaner', 'Kältezeichner', 'Heizungsplaner', 'Refrigeration systems draughtsman']),
'31184': ('Ingenieurwesen & Technik', '3118', 'Draughtspersons', 'Technische Zeichner [ESCO-Gruppenname]', ['geoinformation technologist'], ['Geomatiker', 'Katasterzeichner', 'Katasteroperateur', 'Geoinformation technologist']),
'31190': ('Ingenieurwesen & Technik', '3119', 'Physical and engineering science technicians not elsewhere classified', 'Material- und ingenieurtechnische Fachkräfte, anderweitig nicht genannt [ESCO-Gruppenname]', ['production calculator'], ['Planer', 'Visiteur', 'Kalkulator', 'Production calculator']),
'31410': ('Ingenieurwesen & Technik', '3141', 'Life science technicians (excluding medical)', 'Biotechniker (ohne medizinische Fachberufe) [ESCO-Gruppenname]', ['biological laboratory worker'], ['Biotechniker', 'Phytotechniker', 'Probeentnehmer', 'Biological laboratory worker']),
'74120': ('Elektronik & Feinwerk', '7412', 'Electrical mechanics and fitters', 'Elektromechaniker und verwandte Berufe [ESCO-Gruppenname]', ['lift installer'], ['Umwickler', 'Liftmonteur', 'Liftrevisor', 'Lift installer']),
'74210': ('Elektronik & Feinwerk', '7421', 'Electronics mechanics and servicers', 'Elektroniker und Elektronik-Servicetechniker [ESCO-Gruppenname]', ['electronic technician'], ['Avioniker', 'Radiomonteur', 'Elektroniker', 'Electronic technician']),
}
