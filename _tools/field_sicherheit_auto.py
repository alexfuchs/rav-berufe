# Automatisch erzeugt (gen_fields.py) aus BFS-Zuweisungsschlüssel V1.2 und ESCO-ISCO-Gruppennamen
CLUSTER = 'sicherheit'
PREFIX = 'si'
APPEND = False
BESCHREIBUNG = 'Polizei, Feuerwehr, Armee, Verwaltung, Zoll, Justizvollzug, Politik. Basis: CH-ISCO-19, zugeordnet nach ISCO-08-Gruppen; Gruppennamen aus ESCO (de).'
UNTERFELDER = ['Streitkräfte', 'Behörden & Politik', 'Kontrolle & Inspektion', 'Verwaltung, Zoll & Polizei']
W = 'auto'
NF = {}
G = {
'01100': ('Streitkräfte', '0110', 'Commissioned armed forces officers', 'Offiziere in regulären Streitkräften [ESCO-Gruppenname]', ['military pilot'], ['Oberst', 'Brigadier', 'Divisionär', 'Military pilot']),
'02100': ('Streitkräfte', '0210', 'Non-commissioned armed forces officers', 'Unteroffiziere in regulären Streitkräften [ESCO-Gruppenname]', ['military police officer'], ['Adjutant', 'Militärpolizist', 'Berufsunteroffizier', 'Military police officer']),
'03100': ('Streitkräfte', '0310', 'Armed forces occupations, other ranks', 'Angehörige der regulären Streitkräfte in sonstigen Rängen. [ESCO-Gruppenname]', ['professional soldier'], ['Zeugwart', 'Zeitsoldat', 'AMP-Beamter', 'Professional soldier']),
'11110': ('Behörden & Politik', '1111', 'Legislators', 'Angehörige gesetzgebender Körperschaften [ESCO-Gruppenname]', ['city councillor'], ['Stadtrat', 'Bundesrat', 'Staatsrat', 'City councillor']),
'11120': ('Behörden & Politik', '1112', 'Senior government officials', 'Leitende Verwaltungsbedienstete [ESCO-Gruppenname]', ['consul'], ['Konsul', 'Präfekt', 'Attaché', 'Consul']),
'11140': ('Behörden & Politik', '1114', 'Senior officials of special-interest organisations', 'Leitende Bedienstete von Interessenorganisationen [ESCO-Gruppenname]', ['party secretary'], ['Parteichef', 'Parteisekretär', 'Bauernsekretär', 'Party secretary']),
'32570': ('Kontrolle & Inspektion', '3257', 'Environmental and occupational health inspectors and associates', 'Nicht akademische Kontrolleure und Beauftragte in den Bereichen Umwelt- und Arbeitsmedizin sowie verwandte Berufe [ESCO-Gruppenname]', ['cattle inspector'], ['Viehinspektor', 'Seuchenwärter', 'Läusefachmann', 'Cattle inspector']),
'33510': ('Verwaltung, Zoll & Polizei', '3351', 'Customs and border inspectors', 'Fachkräfte im Zolldienst und Grenzschutz [ESCO-Gruppenname]', ['customs agent'], ['Zollagent', 'Zollexperte', 'Zollbeamter', 'Customs agent']),
'33520': ('Verwaltung, Zoll & Polizei', '3352', 'Government tax and excise officials', 'Fachkräfte in der Steuerverwaltung [ESCO-Gruppenname]', ['tax officer'], ['Tarifchef', 'Tarifbeamter', 'Steuerbeamter', 'Tax officer']),
'33530': ('Verwaltung, Zoll & Polizei', '3353', 'Government social benefits officials', 'Fachkräfte in Sozialverwaltung und -versicherung [ESCO-Gruppenname]', ['youth secretary'], ['AHV-Beamter', 'Amtsvormund', 'AHV-Fachmann', 'Youth secretary']),
'33540': ('Verwaltung, Zoll & Polizei', '3354', 'Government licensing officials', 'Fachkräfte bei staatlichen Pass-, Lizenz- und Genehmigungsstellen [ESCO-Gruppenname]', ['civil register officer'], ['Patentagent', 'Asylkoordinator', 'Zulassungsbeamter', 'Civil register officer']),
'33550': ('Verwaltung, Zoll & Polizei', '3355', 'Police inspectors and detectives', 'Polizeikommissare und Kriminalbeamte [ESCO-Gruppenname]', ['investigator (detective)'], ['Fahnder', 'Cybercop', 'Inspektor', 'Investigator (detective)']),
'33590': ('Verwaltung, Zoll & Polizei', '3359', 'Regulatory government associate professionals not elsewhere classified', 'Fachkräfte in der öffentlichen Verwaltung, anderweitig nicht genannt [ESCO-Gruppenname]', ['assayer (precious metal tester)'], ['Eichmeister', 'Waagmeister', 'Zuchtexperte', 'Assayer (precious metal tester)']),
'54110': ('Verwaltung, Zoll & Polizei', '5411', 'Fire-fighters', 'Feuerwehrleute [ESCO-Gruppenname]', ['fire policeman'], ['Pionierchef', 'Brandwächter', 'Feuerpolizist', 'Fire policeman']),
'54120': ('Verwaltung, Zoll & Polizei', '5412', 'Police officers', 'Polizisten (ohne Polizeikommissare) [ESCO-Gruppenname]', ['policeman'], ['Polizist', 'Landjäger', 'Politesse', 'Policeman']),
'54130': ('Verwaltung, Zoll & Polizei', '5413', 'Prison guards', 'Gefängnisaufseher [ESCO-Gruppenname]', ['prison officer'], ['Anstaltswärter', 'Gefängniswärter', 'Anstaltsaufseher', 'Prison officer']),
'54140': ('Verwaltung, Zoll & Polizei', '5414', 'Security guards', 'Sicherheitswachpersonal [ESCO-Gruppenname]', ['guard'], ['Wächter', 'Aufseher', 'Burgwart', 'Guard']),
'54190': ('Verwaltung, Zoll & Polizei', '5419', 'Protective services workers not elsewhere classified', 'Schutzkräfte und Sicherheitsbedienstete, anderweitig nicht genannt [ESCO-Gruppenname]', ['ranger'], ['Ranger', 'Rollwart', 'Badewart']),
}
