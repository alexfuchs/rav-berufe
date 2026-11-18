# Automatisch erzeugt (gen_fields.py) aus BFS-Zuweisungsschlüssel V1.2 und ESCO-ISCO-Gruppennamen
CLUSTER = 'finanzen'
PREFIX = 'fi'
APPEND = False
BESCHREIBUNG = 'Banken, Versicherungen, Finanzanalyse, Treuhand. Basis: CH-ISCO-19, zugeordnet nach ISCO-08-Gruppen; Gruppennamen aus ESCO (de).'
UNTERFELDER = ['Leitung Finanz & Versicherung', 'Finanzen, Versicherung & Analyse']
W = 'auto'
NF = {}
G = {
'12110': ('Leitung Finanz & Versicherung', '1211', 'Finance managers', 'Führungskräfte im Bereich Finanzen [ESCO-Gruppenname]', ['authorised signatory'], ['Prokurist', 'Finanzchef', 'Finanzmanager', 'Authorised signatory']),
'13461': ('Leitung Finanz & Versicherung', '1346', 'Financial and insurance services branch managers', 'Führungskräfte auf Filialebene in der Erbringung von Finanz- und Versicherungsdienstleistungen [ESCO-Gruppenname]', ['banker'], ['Bankier', 'Bankleiter', 'Bankmanager', 'Banker']),
'13462': ('Leitung Finanz & Versicherung', '1346', 'Financial and insurance services branch managers', 'Führungskräfte auf Filialebene in der Erbringung von Finanz- und Versicherungsdienstleistungen [ESCO-Gruppenname]', ['bank branch manager'], ['Kassenverwalter', 'Bankfilialleiter', 'Krankenkassenführer', 'Bank branch manager']),
'24110': ('Finanzen, Versicherung & Analyse', '2411', 'Accountants', 'Wirtschaftsprüfer, Steuerberater und verwandte Berufe [ESCO-Gruppenname]', ['auditor'], ['Revisor', 'Treasurer', 'Buchprüfer', 'Auditor']),
'24120': ('Finanzen, Versicherung & Analyse', '2412', 'Financial and investment advisers', 'Finanz- und Anlageberater [ESCO-Gruppenname]', ['bank advisor'], ['Financier', 'Bankberater', 'Fondsmanager', 'Bank advisor']),
'24130': ('Finanzen, Versicherung & Analyse', '2413', 'Financial analysts', 'Finanzanalysten [ESCO-Gruppenname]', ['risk manager'], ['Fondsanalyst', 'Risk Manager', 'Finanzexperte', 'Risk manager']),
'33100': ('Finanzen, Versicherung & Analyse', '331', 'Sammelgruppe 33100 (ohne eigene ISCO-08-Gattung)', 'Sammelgruppe: Finanztechniker, Bankfach-Experte, dipl. HFP', ['bachelor in banking and finance'], ['Finanztechniker', 'Bankfachexperte', 'Bankfach-Experte', 'Bachelor in banking and finance']),
'33110': ('Finanzen, Versicherung & Analyse', '3311', 'Securities and finance dealers and brokers', 'Wertpapierhändler, -makler und Finanzmakler [ESCO-Gruppenname]', ['broker'], ['Broker', 'Bankmakler', 'Börsenchef']),
'33120': ('Finanzen, Versicherung & Analyse', '3312', 'Credit and loans officers', 'Kreditsachbearbeiter [ESCO-Gruppenname]', ['leaser'], ['Leaser', 'Kreditchef', 'Kreditprüfer']),
'33130': ('Finanzen, Versicherung & Analyse', '3313', 'Accounting associate professionals', 'Nicht akademische Fachkräfte im Rechnungswesen [ESCO-Gruppenname]', ['accountant'], ['Quästor', 'Buchhalter', 'Controller', 'Accountant']),
'33140': ('Finanzen, Versicherung & Analyse', '3314', 'Statistical, mathematical and related associate professionals', 'Nicht akademische statistische, mathematische und verwandte Fachkräfte [ESCO-Gruppenname]', ['data processor'], ['Mecanograph', 'EDV-Auswerter', 'Datenverarbeiter', 'Data processor']),
'33150': ('Finanzen, Versicherung & Analyse', '3315', 'Valuers and loss assessors', 'Schätzer und Schadensgutachter [ESCO-Gruppenname]', ['gemologist'], ['Taxator', 'Schätzer', 'Gemmologe', 'Gemologist']),
'33210': ('Finanzen, Versicherung & Analyse', '3321', 'Insurance representatives', 'Versicherungsvertreter [ESCO-Gruppenname]', ['underwriter'], ['Underwriter', 'Generalagent', 'Assekuranzagent']),
}
