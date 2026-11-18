# Automatisch erzeugt (gen_fields.py) aus BFS-Zuweisungsschlüssel V1.2 und ESCO-ISCO-Gruppennamen
CLUSTER = 'soziales'
PREFIX = 'so'
APPEND = False
BESCHREIBUNG = 'Erziehung, Unterricht, soziale Arbeit, Betreuung. Basis: CH-ISCO-19, zugeordnet nach ISCO-08-Gruppen; Gruppennamen aus ESCO (de).'
UNTERFELDER = ['Leitung Soziales & Bildung', 'Bildung & Erziehung', 'Soziale Arbeit & Seelsorge']
W = 'auto'
NF = {}
G = {
'13410': ('Leitung Soziales & Bildung', '1341', 'Child care services managers', 'Führungskräfte in der Erbringung von Dienstleistungen der Kinderbetreuung [ESCO-Gruppenname]', ['creche director'], ['Hortleiter', 'Waisenvater', 'Kita-Leiter', 'Creche director']),
'13430': ('Leitung Soziales & Bildung', '1343', 'Aged care services managers', 'Führungskräfte in der Erbringung von Dienstleistungen der Altenbetreuung [ESCO-Gruppenname]', ['retirement home director'], ['Altersheimleiter', 'Alterssiedlungsverwalter', 'Retirement home director']),
'13440': ('Leitung Soziales & Bildung', '1344', 'Social welfare managers', 'Führungskräfte in der Erbringung von Dienstleistungen der Sozialfürsorge [ESCO-Gruppenname]', ['dwelling group manager'], ['Hospizdirektor', 'Wohnheimleiter', 'AHV-Kassenleiter', 'Dwelling group manager']),
'13450': ('Leitung Soziales & Bildung', '1345', 'Education managers', 'Führungskräfte in der Erbringung von Dienstleistungen des Bildungswesens [ESCO-Gruppenname]', ['dean (ecclesiastical function)'], ['Dekan', 'Prorektor', 'Konrektor', 'Dean (ecclesiastical function)']),
'23000': ('Bildung & Erziehung', '230', 'Sammelgruppe 23000 (ohne eigene ISCO-08-Gattung)', 'Sammelgruppe: Erwachsenenbildner, Erwachsenenbildner', ['trainer'], ['Ausbilder', 'Kursleiter', 'Ausbildner', 'Trainer']),
'23100': ('Bildung & Erziehung', '2310', 'University and higher education teachers', 'Universitäts- und Hochschullehrer [ESCO-Gruppenname]', ['professor'], ['Dozent', 'Vorleser', 'Professor']),
'23200': ('Bildung & Erziehung', '2320', 'Vocational education teachers', 'Lehrkräfte im Bereich Berufsbildung [ESCO-Gruppenname]', ['teacher at a vocational commercial school'], ['KV-Lehrer', 'Nählehrer', 'Kochlehrer', 'Teacher at a vocational commercial school']),
'23300': ('Bildung & Erziehung', '2330', 'Secondary education teachers', 'Lehrkräfte im Sekundarbereich [ESCO-Gruppenname]', ['physics teacher'], ['Werklehrer', 'Hauslehrer', 'Kunstlehrer', 'Physics teacher']),
'23301': ('Bildung & Erziehung', '2330', 'Secondary education teachers', 'Lehrkräfte im Sekundarbereich [ESCO-Gruppenname]', ['grammar school teacher'], ['Gymnasiallehrer', 'Mittelschullehrer', 'Kantonsschullehrer', 'Grammar school teacher']),
'23302': ('Bildung & Erziehung', '2330', 'Secondary education teachers', 'Lehrkräfte im Sekundarbereich [ESCO-Gruppenname]', ['secondary-school teacher (secondary education level i)'], ['Reallehrer', 'Bezirkslehrer', 'Sekundarlehrer', 'Secondary-school teacher (secondary education level i)']),
'23410': ('Bildung & Erziehung', '2341', 'Primary school teachers', 'Lehrkräfte im Primarbereich [ESCO-Gruppenname]', ['primary teacher'], ['Lehrer', 'Meister', 'Primarlehrer', 'Primary teacher']),
'23420': ('Bildung & Erziehung', '2342', 'Early childhood educators', 'Lehrkräfte und Erzieher im Vorschulbereich [ESCO-Gruppenname]', ['nursery teacher'], ['Kindergärtner', 'Vorschullehrer', 'Kinderhortlehrer', 'Nursery teacher']),
'23421': ('Bildung & Erziehung', '2342', 'Early childhood educators', 'Lehrkräfte und Erzieher im Vorschulbereich [ESCO-Gruppenname]', ['child development worker'], ['Kindererzieher', 'Child Dramaleiter', 'Kindheitspädagoge', 'Child development worker']),
'23510': ('Bildung & Erziehung', '2351', 'Education methods specialists', 'Pädagogik- und Didaktikspezialisten [ESCO-Gruppenname]', ['pedagogue'], ['Schulrat', 'Pädagoge', 'Andragoge', 'Pedagogue']),
'23520': ('Bildung & Erziehung', '2352', 'Special needs teachers', 'Lehrkräfte im Bereich Sonderpädagogik [ESCO-Gruppenname]', ['remedial teacher'], ['Audioagoge', 'Heilpädagoge', 'Lerntherapeut', 'Remedial teacher']),
'23530': ('Bildung & Erziehung', '2353', 'Other language teachers', 'Sonstige Sprachlehrer [ESCO-Gruppenname]', ['language teacher'], ['Sprachlehrer', 'Lateinlehrer', 'Deutschlehrer', 'Language teacher']),
'23540': ('Bildung & Erziehung', '2354', 'Other music teachers', 'Sonstige Musiklehrer [ESCO-Gruppenname]', ['voice teacher'], ['Singlehrer', 'Orgellehrer', 'Cellolehrer', 'Voice teacher']),
'23550': ('Bildung & Erziehung', '2355', 'Other arts teachers', 'Sonstige Kunstlehrer [ESCO-Gruppenname]', ['dancing instructor'], ['Mallehrer', 'Tanzlehrer', 'Tanzmeister', 'Dancing instructor']),
'23560': ('Bildung & Erziehung', '2356', 'Information technology trainers', 'Ausbilder im Bereich Informationstechnologie [ESCO-Gruppenname]', ['edp teacher'], ['EDV-Trainer', 'EDV-Ausbildner', 'EDV-Instruktor', 'EDP teacher']),
'23590': ('Bildung & Erziehung', '2359', 'Teaching professionals not elsewhere classified', 'Lehrkräfte, anderweitig nicht genannt [ESCO-Gruppenname]', ['bible teacher'], ['Bibellehrer', 'Koranlehrer', 'Zoopädagoge', 'Bible teacher']),
'26350': ('Soziale Arbeit & Seelsorge', '2635', 'Social work and counselling professionals', 'Sozialarbeiter [ESCO-Gruppenname]', ['mediator'], ['Mediator', 'Fürsorger', 'Eheberater']),
'26360': ('Soziale Arbeit & Seelsorge', '2636', 'Religious professionals', 'Geistliche Seelsorger [ESCO-Gruppenname]', ['abbot'], ['Imam', 'Vikar', 'Prior', 'Abbot']),
'34120': ('Soziale Arbeit & Seelsorge', '3412', 'Social work associate professionals', 'Nicht akademische sozialpflegerische Fachkräfte [ESCO-Gruppenname]', ['educator'], ['Erzieher', 'Animator', 'Job coach', 'Educator']),
'34130': ('Soziale Arbeit & Seelsorge', '3413', 'Religious associate professionals', 'Ordensbrüder/-schwestern und Seelsorgehelfer [ESCO-Gruppenname]', ['mother superior'], ['Mönch', 'Novize', 'Oberin', 'Mother superior']),
'53110': ('Bildung & Erziehung', '5311', 'Child care workers', 'Kinderbetreuer [ESCO-Gruppenname]', ['parental assistant'], ['Amme', 'Hausvater', 'Tagesvater', 'Parental assistant']),
'53120': ('Bildung & Erziehung', '5312', 'Teachers’ aides', 'Lernbetreuer [ESCO-Gruppenname]', ['teaching assistant'], ['Hilfslehrer', 'Schulhelfer', 'Aufgabenhilfe', 'Teaching assistant']),
}
