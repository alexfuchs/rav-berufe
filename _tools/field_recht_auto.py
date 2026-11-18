# Automatisch erzeugt (gen_fields.py) aus BFS-Zuweisungsschlüssel V1.2 und ESCO-ISCO-Gruppennamen
CLUSTER = 'recht'
PREFIX = 're'
APPEND = False
BESCHREIBUNG = 'Recht, Unternehmensführung, Beratung, Personal. Basis: CH-ISCO-19, zugeordnet nach ISCO-08-Gruppen; Gruppennamen aus ESCO (de).'
UNTERFELDER = ['Leitung & Geschäftsführung', 'Personal, Strategie & Organisation', 'Beratung, Organisation & Personal', 'Recht & Justiz']
W = 'auto'
NF = {}
G = {
'-999': ('Leitung & Geschäftsführung', '-99', 'Sammelgruppe -999 (ohne eigene ISCO-08-Gattung)', 'Sammelgruppe: Technischer Bevollmächtigter, Bundesbeamter', [], ['Beamter', 'Assistent', 'Eisenbahner']),
'10000': ('Leitung & Geschäftsführung', '100', 'Sammelgruppe 10000 (ohne eigene ISCO-08-Gattung)', 'Sammelgruppe: Manager, Ingenieurbürodirektor', ['manager'], ['Manager', 'Adjunkt', 'Chefbeamter']),
'11200': ('Personal, Strategie & Organisation', '1120', 'Managing directors and chief executives', 'Geschäftsführer und Vorstände [ESCO-Gruppenname]', ['office owner'], ['Präsident', 'Vizeleiter', 'Inkassochef', 'Office owner']),
'12100': ('Personal, Strategie & Organisation', '121', 'Sammelgruppe 12100 (ohne eigene ISCO-08-Gattung)', 'Sammelgruppe: Kaufmännischer Leiter, Kaufmännischer Direktor', ['trade manager'], ['Verwalter', 'Sektorchef', 'Bereichsleiter', 'Trade manager']),
'12120': ('Personal, Strategie & Organisation', '1212', 'Human resource managers', 'Führungskräfte im Personalwesen [ESCO-Gruppenname]', ['personnel officer'], ['Personalchef', 'Personalleiter', 'Arbeitsdirektor', 'Personnel officer']),
'12130': ('Personal, Strategie & Organisation', '1213', 'Policy and planning managers', 'Führungskräfte in Unternehmenspolitik und -planung [ESCO-Gruppenname]', ['planning manager'], ['Planning Manager', 'Investment Manager', 'Business Developer', 'Planning manager']),
'12190': ('Personal, Strategie & Organisation', '1219', 'Business services and administration managers not elsewhere classified', 'Führungskräfte in der betrieblichen Verwaltung und in unternehmensbezogenen Dienstleistungen, anderweitig nicht genannt [ESCO-Gruppenname]', ['facility manager'], ['Systemchef', 'Wissensmanager', 'Operativdirektor', 'Facility manager']),
'13490': ('Personal, Strategie & Organisation', '1349', 'Professional services managers not elsewhere classified', 'Führungskräfte in der Erbringung von speziellen Dienstleistungen, anderweitig nicht genannt [ESCO-Gruppenname]', ['publisher'], ['Verleger', 'Galerist', 'Laborleiter', 'Publisher']),
'24000': ('Beratung, Organisation & Personal', '240', 'Sammelgruppe 24000 (ohne eigene ISCO-08-Gattung)', 'Sammelgruppe: Analytiker, Analysator', ['analyst (it)'], ['Analytiker', 'Analysator', 'Verwaltungswissenschafter', 'Analyst (IT)']),
'24210': ('Beratung, Organisation & Personal', '2421', 'Management and organisation analysts', 'Akademische und vergleichbare Fachkräfte im Bereich Management- und Organisationsanalyse [ESCO-Gruppenname]', ['organiser'], ['Organizer', 'Methodiker', 'Organisator', 'Organiser']),
'24220': ('Beratung, Organisation & Personal', '2422', 'Policy administration professionals', 'Akademische und vergleichbare Fachkräfte in der strategischen Planung in Politik und Wirtschaft [ESCO-Gruppenname]', ['risk engineer'], ['Risk Engineer', 'Risk Controller', 'Marktorganisator', 'Risk engineer']),
'24230': ('Beratung, Organisation & Personal', '2423', 'Personnel and careers professionals', 'Berufsberater und -analytiker und akademische und vergleichbare Personalfachleute [ESCO-Gruppenname]', ['recruiter'], ['Recruiter', 'HR-Experte', 'HR-Fachmann']),
'24240': ('Beratung, Organisation & Personal', '2424', 'Training and staff development professionals', 'Fachkräfte in Personalschulung und -entwicklung [ESCO-Gruppenname]', ['vocational trainer'], ['Instruktor', 'Lehrmeister', 'Finanztrainer', 'Vocational trainer']),
'26100': ('Recht & Justiz', '261', 'Sammelgruppe 26100 (ohne eigene ISCO-08-Gattung)', 'Sammelgruppe: Lic. iur., Dr. iur.', ['jurist'], ['Jurist', 'Assessor', 'Rechtswissenschafter']),
'26110': ('Recht & Justiz', '2611', 'Lawyers', 'Anwälte [ESCO-Gruppenname]', ['lawyer'], ['Anwalt', 'Advokat', 'Fürsprecher', 'Lawyer']),
'26120': ('Recht & Justiz', '2612', 'Judges', 'Richter [ESCO-Gruppenname]', ['judge'], ['Richter', 'Amtsrichter', 'Oberrichter', 'Judge']),
'26190': ('Recht & Justiz', '2619', 'Legal professionals not elsewhere classified', 'Juristen, anderweitig nicht genannt [ESCO-Gruppenname]', ['criminalist'], ['Syndikus', 'Baujurist', 'Substitut', 'Criminalist']),
'26191': ('Recht & Justiz', '2619', 'Legal professionals not elsewhere classified', 'Juristen, anderweitig nicht genannt [ESCO-Gruppenname]', ['notary'], ['Notar', 'Amtsnotar', 'Staatsnotar', 'Notary']),
'33330': ('Beratung, Organisation & Personal', '3333', 'Employment agents and contractors', 'Arbeits- und Personalvermittler [ESCO-Gruppenname]', ['head hunter'], ['Head hunter', 'Stellenvermittler', 'Arbeitsvermittler']),
'34110': ('Recht & Justiz', '3411', 'Legal and related associate professionals', 'Nicht akademische Fachkräfte für Rechts- und verwandte Angelegenheiten [ESCO-Gruppenname]', ['detective'], ['Weibel', 'Detektiv', 'Referent', 'Detective']),
}
