# Konfiguration Berufsfeld «Büro & Administration» (CH-ISCO-19: 334xx, 41xxx, 42xxx, 431xx, 441xx ohne 44120)
CLUSTER = 'buero'
PREFIX = 'bu'
BESCHREIBUNG = ('Sekretariat und Assistenz, Sachbearbeitung, Rechnungswesen und Personal, Kundendienst und Empfang, Archiv und Bibliothek. '
                'Basis: CH-ISCO-19 Gruppen 334, 41, 42, 431 und 441. Material- und Transportsachbearbeitung (432) sowie Postzustellung (44120) '
                'gehören ins Feld Logistik & Verkehr.')
UNTERFELDER = ['Sekretariat & Assistenz', 'Bürobetrieb & Sachbearbeitung', 'Rechnungswesen & Personal', 'Kundendienst & Empfang', 'Archiv, Bibliothek & Dokumente']

# code -> (unterfeld, isco, ISCO-08 englisch, Beschreibung deutsch [sinngemäss], ESCO-Suchbegriffe, Suchbegriffe jobs.ch)
G = {
'33400': ('Sekretariat & Assistenz', '334', 'Administrative and specialized secretaries', 'Verwaltungsfachleute, allgemein', [], ['Sachbearbeiter Verwaltung']),
'33410': ('Sekretariat & Assistenz', '3341', 'Office supervisors', 'Büroleitung / Teamleitung Administration', ['office manager'], ['Büroleiter', 'Office Manager', 'Teamleiter Administration']),
'33420': ('Sekretariat & Assistenz', '3342', 'Legal secretaries', 'Rechts- und Notariatssekretariat', ['legal secretary'], ['Rechtsanwaltsassistent', 'Notariatsangestellte', 'Legal Assistant']),
'33430': ('Sekretariat & Assistenz', '3343', 'Administrative and executive secretaries', 'Verwaltungs- und Direktionssekretariat', ['executive assistant'], ['Assistent Geschäftsleitung', 'Executive Assistant', 'Direktionsassistent']),
'33440': ('Sekretariat & Assistenz', '3344', 'Medical secretaries', 'Medizinisches Sekretariat', ['medical secretary'], ['Medizinische Praxisassistentin Sekretariat', 'Medizinische Sekretärin', 'Spitalsekretärin']),
'41100': ('Bürobetrieb & Sachbearbeitung', '4110', 'General office clerks', 'Allgemeine Büro- und Sachbearbeitung (inkl. Kaufmann/-frau EFZ)', ['office clerk'], ['Sachbearbeiter', 'Kaufmann EFZ', 'Sachbearbeiter Backoffice', 'Administrator', 'Office Administrator']),
'41200': ('Sekretariat & Assistenz', '4120', 'Secretaries (general)', 'Sekretariat, allgemein', ['secretary'], ['Sekretärin', 'Sekretariat', 'Assistenz Sekretariat']),
'41310': ('Bürobetrieb & Sachbearbeitung', '4131', 'Typists and word processing operators', 'Schreibdienst und Textverarbeitung', ['typist'], ['Schreibkraft', 'Textverarbeitung']),
'41320': ('Bürobetrieb & Sachbearbeitung', '4132', 'Data entry clerks', 'Datenerfassung', ['data entry clerk'], ['Datenerfassung', 'Dateneingabe', 'Data Entry']),
'42110': ('Kundendienst & Empfang', '4211', 'Bank tellers and related clerks', 'Schalterdienst Bank und Post', ['bank teller'], ['Schalterbeamter', 'Kundenberater Schalter', 'Postschalter']),
'42111': ('Kundendienst & Empfang', '4211', 'Bank tellers and related clerks', 'Schalterdienst Post (Postangestellte)', ['post office clerk'], ['Postagent', 'Kundenberater Poststelle', 'Postangestellter Schalter']),
'42112': ('Kundendienst & Empfang', '4211', 'Bank tellers and related clerks', 'Schalterdienst Bank (Kassier)', ['bank teller'], ['Bankkassier', 'Kundenberater Bank Schalter', 'Bank Teller']),
'42120': ('Kundendienst & Empfang', '4212', 'Bookmakers, croupiers and related gaming workers', 'Spielbank und Wetten (Croupier)', ['croupier'], ['Croupier', 'Casino Dealer']),
'42130': ('Kundendienst & Empfang', '4213', 'Pawnbrokers and money-lenders', 'Pfand- und Kleinkreditgeschäft', [], ['Pfandleiher']),
'42140': ('Kundendienst & Empfang', '4214', 'Debt-collectors and related workers', 'Inkasso', ['debt collector'], ['Inkasso', 'Inkassosachbearbeiter', 'Debitorenmanagement Inkasso']),
'42210': ('Kundendienst & Empfang', '4221', 'Travel consultants and clerks', 'Reiseberatung und Reisebüro', ['travel agent'], ['Reiseberater', 'Travel Consultant', 'Reisebüro']),
'42220': ('Kundendienst & Empfang', '4222', 'Contact centre information clerks', 'Contact Center und Telefonberatung', ['call centre agent'], ['Call Center Agent', 'Customer Service Agent', 'Kundenberater Telefon', 'Contact Center']),
'42230': ('Kundendienst & Empfang', '4223', 'Telephone switchboard operators', 'Telefonzentrale', ['switchboard operator'], ['Telefonist', 'Telefonzentrale']),
'42240': ('Kundendienst & Empfang', '4224', 'Hotel receptionists', 'Hotelempfang', ['hotel receptionist'], ['Rezeptionist Hotel', 'Night Auditor', 'Front Office Hotel']),
'42250': ('Kundendienst & Empfang', '4225', 'Inquiry clerks', 'Auskunft und Beschwerdemanagement', [], ['Complaint Manager', 'Kundenservice Auskunft']),
'42260': ('Kundendienst & Empfang', '4226', 'Receptionists (general)', 'Empfang und Réception', ['receptionist'], ['Receptionist', 'Empfang', 'Réception', 'Front Desk']),
'42270': ('Kundendienst & Empfang', '4227', 'Survey and market research interviewers', 'Befragung und Marktforschung (Interviewer)', ['market research interviewer'], ['Interviewer', 'Telefoninterviewer']),
'42290': ('Kundendienst & Empfang', '4229', 'Client information workers not elsewhere classified', 'Kundeninformation, übrige', [], ['Kundeninformation']),
'43110': ('Rechnungswesen & Personal', '4311', 'Accounting and bookkeeping clerks', 'Buchhaltung und Rechnungswesen (Sachbearbeitung)', ['accounting clerk', 'bookkeeper'], ['Buchhalter', 'Sachbearbeiter Buchhaltung', 'Debitorenbuchhalter', 'Kreditorenbuchhalter', 'Accounts Payable']),
'43120': ('Rechnungswesen & Personal', '4312', 'Statistical, finance and insurance clerks', 'Sachbearbeitung Finanz, Versicherung und Statistik', ['insurance clerk'], ['Sachbearbeiter Versicherung', 'Sachbearbeiter Bank', 'Sachbearbeiter Finanzen']),
'43130': ('Rechnungswesen & Personal', '4313', 'Payroll clerks', 'Lohnbuchhaltung', ['payroll clerk'], ['Lohnbuchhalter', 'Payroll Specialist', 'Lohnsachbearbeiter']),
'44100': ('Archiv, Bibliothek & Dokumente', '441', 'Other clerical support workers', 'Bürohilfe, übrige (allgemein)', [], ['Bürohilfe']),
'44110': ('Archiv, Bibliothek & Dokumente', '4411', 'Library clerks', 'Bibliotheksassistenz', ['library assistant'], ['Bibliotheksassistent', 'Fachperson Information und Dokumentation']),
'44130': ('Archiv, Bibliothek & Dokumente', '4413', 'Coding, proof-reading and related clerks', 'Kodierung und Korrektorat', ['proofreader'], ['Korrektor', 'Lektor', 'Medizinischer Kodierer']),
'44140': ('Archiv, Bibliothek & Dokumente', '4414', 'Scribes and related workers', 'Schreibservice', [], ['Schreibservice']),
'44150': ('Archiv, Bibliothek & Dokumente', '4415', 'Filing and copying clerks', 'Archiv, Registratur und Dokumentation', ['filing clerk'], ['Archivar', 'Registratur', 'Dokumentalist', 'Records Manager']),
'44160': ('Rechnungswesen & Personal', '4416', 'Personnel clerks', 'Personalsachbearbeitung und HR-Assistenz', ['human resources assistant'], ['HR Assistent', 'Personalsachbearbeiter', 'HR Administrator']),
'44190': ('Bürobetrieb & Sachbearbeitung', '4419', 'Clerical support workers not elsewhere classified', 'Büro-Sachbearbeitung, übrige (Verlag, Einkauf, Redaktion)', [], ['Einkaufsassistent', 'Redaktionsassistent', 'Verlagsassistent']),
'44191': ('Bürobetrieb & Sachbearbeitung', '4419', 'Clerical support workers not elsewhere classified', 'Sachbearbeitung Marketing und Werbung', ['marketing assistant'], ['Marketing Assistent', 'Marketing Sachbearbeiter', 'Werbeadministration']),
'44192': ('Bürobetrieb & Sachbearbeitung', '4419', 'Clerical support workers not elsewhere classified', 'Kundenbetreuung und Verkaufsinnendienst', ['sales support'], ['Kundenberater', 'Verkaufsinnendienst', 'Kundenbetreuer', 'Customer Service']),
}
# Titel im Internet: Anzeige und Regex (nur übernommen, wenn in den gesichteten Ausschreibungen gefunden)
W = {
'33400': [('Sachbearbeiter/in (öffentliche Verwaltung)', 'sachbearbeit')],
'33410': [('Office Manager', r'office.?manag'), ('Back-Office Manager', 'back-office manager'), ('Administration & Office Management', 'office management')],
'33420': [('Partnerassistent/in', 'partnerassistent'), ('Notariatsassistent/in', 'notariatsassistent'), ('Paralegal / Legal Assistant', r'paralegal|legal .*assistant'), ('Secrétaire juridique', 'secrétaire juridique'), ('Staatsanwaltsassistent/in', 'staatsanwaltsassistent')],
'33430': [('Executive Assistant', 'executive assistant'), ('Direktionsassistent/in', r'direktionsassist|assistant de direction'), ('Assistenz der Geschäftsleitung / GL-Assistenz', r'geschäftsleitung|gl-assist')],
'33440': [('MPA / Arztsekretär/in', r'arztsekret|mpa'), ('Medizinische/r Sekretär/in', r'med\. sekret|medizinische/n sekret|secrétaire médical|kliniksekret')],
'41100': [('Kauffrau / Kaufmann', r'kauffrau|kaufmann'), ('Sachbearbeiter/in Kundenservice', 'sachbearbeiter kundenservice'), ('Administrator (Office, Finance, Project)', r'(finance|office|project|supply chain) administrator')],
'41200': [('Sekretär/in', r'sekretär:in|sekretärin'), ('Mitarbeiter/in Sekretariat', r'mitarbeiter\S* (administration (und|&) )?sekretariat'), ('Sachbearbeiter/in Sekretariat', r'sachbearbeiter.*sekretariat')],
'42110': [('Front Office Agent', 'front office agent'), ('Front Office (Empfang, Schalter)', 'front office')],
'42120': [('Croupier / Croupière', 'croupier')],
'42140': [('Sachbearbeiter/in Inkasso', 'inkasso')],
'42210': [('Reisespezialist/in / Reiseberater/in', r'reisespezialist|reiseberater|conseiller.*voyages'), ('Corporate Travel Agent', 'travel agent')],
'42220': [('Customer Service Specialist / Representative', r'customer service (specialist|representative)'), ('Call Agent / Telefonmarketing', r'call agent|telefonmarketing')],
'42230': [('Telefonist/in', r'telefonist|téléphoniste')],
'42240': [('Front Office Agent', 'front office agent'), ('Rezeptionist/in', r'rezeption|réceptionniste|receptionist')],
'42260': [('Receptionist/in / Empfang', r'receptionist|empfang|réceptionniste'), ('Nachtportier/in', 'nachtportier')],
'43110': [('Buchhalter/in', 'buchhalter'), ('Sachbearbeiter/in Buchhaltung / Rechnungswesen', r'sachbearbeiter\S* (buchhaltung|rechnungswesen)'), ('Accountant', 'accountant')],
'43120': [('Sachbearbeiter/in Rechnungswesen', r'sachbearbeiter.*rechnungswesen'), ('Versicherungssachbearbeiter/in', r'versicherungssachbearbeiter|sachbearbeiter\S* versicherung')],
'43130': [('Payroll Specialist', 'payroll'), ('Lohnbuchhalter/in', 'lohnbuchhalt')],
'44110': [('Records Manager / Agent d’information documentaire', r'records manager|information documentaire')],
'44130': [('Medizinische/r Kodierer/in', r'kodier|codier|codeur')],
'44150': [('Archivar/in', r'archivar|archiviste'), ('Records Manager', 'records manager'), ('Technical Documentation Specialist', 'documentation')],
'44160': [('HR-Assistent/in', r'hr-assistent|hr assistant'), ('HR Administration Specialist', r'hr administration|hr-admin'), ('HR-Sachbearbeiter/in', 'hr-sachbearbeiter')],
'44190': [('Sachbearbeiter/in Einkauf', r'sachbearbeiter.* einkauf|gestionnaire achats'), ('Junior Buyer / Assistent Beschaffung', r'buyer|beschaffung')],
'44191': [('Marketing Assistant / Assistenz Marketing', r'marketing assist|assistenz marketing')],
'44192': [('Sachbearbeiter/in Verkaufsinnendienst', 'verkaufsinnendienst'), ('Kundenberater/in', 'kundenberater'), ('Customer Service Representative', 'customer service representative')],
}
# Verweise auf andere Felder, nur mit Beleg
NF = {
'33420': [('recht', 'Titel Paralegal, Notariats- und Staatsanwaltsassistent/in in Ausschreibungen; ESCO «legal secretary»')],
'33440': [('gesundheit', 'Ausschreibungen «MPA / Arztsekretär/in» in Spitälern und Praxen')],
'42110': [('finanzen', 'Titel wie Bankkassier und Bankbeamter im BFS-Zuweisungsschlüssel (Code 42112)')],
'42210': [('gastro', 'Ausschreibungen Reisebüro und Tourismus (Corporate Travel, Sachbearbeiter Tourismus)')],
'42240': [('gastro', 'Hotelempfang: Titel wie Night Butler und Portier in den Ausschreibungen')],
'43110': [('finanzen', 'Ausschreibungen Accountant und Financial Accountant')],
'43130': [('finanzen', 'ESCO «payroll clerk»: Rechnungswesen')],
'44190': [('logistik', 'Ausschreibungen Einkauf: Assistant Supply Chain & Procurement')],
}
