# Automatisch erzeugt (gen_fields.py) aus BFS-Zuweisungsschlüssel V1.2 und ESCO-ISCO-Gruppennamen
CLUSTER = 'reinigung'
PREFIX = 'rg'
APPEND = False
BESCHREIBUNG = 'Reinigung, Hauswirtschaft, Abfall, persönliche Dienste. Basis: CH-ISCO-19, zugeordnet nach ISCO-08-Gruppen; Gruppennamen aus ESCO (de).'
UNTERFELDER = ['Reinigung & Hauswirtschaft', 'Persönliche Dienste']
W = 'auto'
NF = {}
G = {
'51511': ('Reinigung & Hauswirtschaft', '5151', 'Cleaning and housekeeping supervisors in offices, hotels and other establishments', 'Reinigungs- und Hauswirtschaftsleiter in Büros, Hotels und anderen Einrichtungen [ESCO-Gruppenname]', ['butler'], ['Butler', 'Etagenchef', 'Gouvernante']),
'51512': ('Reinigung & Hauswirtschaft', '5151', 'Cleaning and housekeeping supervisors in offices, hotels and other establishments', 'Reinigungs- und Hauswirtschaftsleiter in Büros, Hotels und anderen Einrichtungen [ESCO-Gruppenname]', ['hotel housekeeping specialist'], ['Tournant', 'Hotelfachmann', 'Hotelassistent', 'Hotel housekeeping specialist']),
'51520': ('Reinigung & Hauswirtschaft', '5152', 'Domestic housekeepers', 'Hauswirtschafter in Privathaushalten [ESCO-Gruppenname]', ['private domestic servant'], ['Pfarrhausangestellter', 'Bäuerlicher Haushälter', 'Bäuerlicher Hausangestellter', 'Private domestic servant']),
'51530': ('Reinigung & Hauswirtschaft', '5153', 'Building caretakers', 'Hauswarte [ESCO-Gruppenname]', ['caretaker'], ['Abwart', 'Pedell', 'Küster', 'Caretaker']),
'51610': ('Persönliche Dienste', '5161', 'Astrologers, fortune-tellers and related workers', 'Astrologen, Wahrsager und verwandte Berufe [ESCO-Gruppenname]', ['palmist'], ['Pendler', 'Handleser', 'Hellseher', 'Palmist']),
'51620': ('Persönliche Dienste', '5162', 'Companions and valets', 'Gesellschafter und Zofen/Kammerdiener [ESCO-Gruppenname]', [], ['Kammerdiener', 'Gesellschaftsherr']),
'51630': ('Persönliche Dienste', '5163', 'Undertakers and embalmers', 'Bestatter und Einbalsamierer [ESCO-Gruppenname]', ['mortician'], ['Bestatter', 'Totengräber', 'Leichenwärter', 'Mortician']),
'51640': ('Persönliche Dienste', '5164', 'Pet groomers and animal care workers', 'Tierpfleger und -betreuer [ESCO-Gruppenname]', ['animal keeper'], ['Dresseur', 'Zoowärter', 'Tierwärter', 'Animal keeper']),
'51650': ('Persönliche Dienste', '5165', 'Driving instructors', 'Fahrschullehrer [ESCO-Gruppenname]', ['driving instructor'], ['Fahrlehrer', 'Autofahrlehrer', 'Fahrschulleiter', 'Driving instructor']),
'51690': ('Persönliche Dienste', '5169', 'Personal services workers not elsewhere classified', 'Berufe im Bereich personenbezogener Dienstleistungen, anderweitig nicht genannt [ESCO-Gruppenname]', ['prostitute'], ['Caddy-Man', 'Golfgehilfe', 'Prostituierter', 'Prostitute']),
'75440': ('Reinigung & Hauswirtschaft', '7544', 'Fumigators and other pest and weed controllers', 'Kammerjäger und andere Schädlingsbekämpfungsberufe [ESCO-Gruppenname]', ['mouse catcher'], ['Mauser', 'Kammerjäger', 'Desinfekteur', 'Mouse catcher']),
'91110': ('Reinigung & Hauswirtschaft', '9111', 'Domestic cleaners and helpers', 'Reinigungspersonal und Hilfskräfte in Privathaushalten [ESCO-Gruppenname]', ['domestic help'], ['Putzmann', 'Haushelfer', 'Hausbursche', 'Domestic help']),
'91120': ('Reinigung & Hauswirtschaft', '9112', 'Cleaners and helpers in offices, hotels and other establishments', 'Reinigungspersonal und Hilfskräfte in Büros, Hotels und anderen Einrichtungen [ESCO-Gruppenname]', ['bellman'], ['Diener', 'Etagier', 'Bellman']),
'91210': ('Reinigung & Hauswirtschaft', '9121', 'Hand launderers and pressers', 'Handwäscher und Handbügler [ESCO-Gruppenname]', ['clothing presser'], ['Bügler', 'Glätter', 'Wäscher', 'Clothing presser']),
'91220': ('Reinigung & Hauswirtschaft', '9122', 'Vehicle cleaners', 'Fahrzeugreiniger [ESCO-Gruppenname]', ['car washer'], ['Autowäscher', 'Autopolierer', 'Autoreiniger', 'Car washer']),
'91230': ('Reinigung & Hauswirtschaft', '9123', 'Window cleaners', 'Fensterputzer [ESCO-Gruppenname]', ['window cleaner'], ['Fensterputzer', 'Fensterreiniger', 'Window cleaner']),
'91290': ('Reinigung & Hauswirtschaft', '9129', 'Other cleaning workers', 'Sonstiges Reinigungspersonal [ESCO-Gruppenname]', ['compressed air cleaning technician'], ['Entgifter', 'Fassputzer', 'Düsenputzer', 'Compressed air cleaning technician']),
'96100': ('Reinigung & Hauswirtschaft', '961', 'Sammelgruppe 96100 (ohne eigene ISCO-08-Gattung)', 'Sammelgruppe: Abfallverbrennungsarbeiter, Abfallbelader', ['waste disposer'], ['Abfallbelader', 'Hadernmeister', 'Abfuhrarbeiter', 'Waste disposer']),
'96110': ('Reinigung & Hauswirtschaft', '9611', 'Garbage and recycling collectors', 'Arbeiter in der Abfall- und Wertstoffsammlung [ESCO-Gruppenname]', ['rag dealer'], ['Verschrotter', 'Dosenpresser', 'Wasenmeister', 'Rag dealer']),
'96120': ('Reinigung & Hauswirtschaft', '9612', 'Refuse sorters', 'Arbeiter in der Abfallsortierung [ESCO-Gruppenname]', ['renderer'], ['Abdecker', 'Recyclist', 'Deponiewart', 'Renderer']),
'96130': ('Reinigung & Hauswirtschaft', '9613', 'Sweepers and related labourers', 'Straßenkehrer und verwandte Berufe [ESCO-Gruppenname]', ['flusher'], ['Wegknecht', 'Kanalreiniger', 'Kanalarbeiter', 'Flusher']),
'96220': ('Reinigung & Hauswirtschaft', '9622', 'Odd job persons', 'Gelegenheitsarbeiter [ESCO-Gruppenname]', [], ['Taglöhner', 'Reparaturarbeiter', 'Gelegenheitsarbeiter']),
'96290': ('Reinigung & Hauswirtschaft', '9629', 'Elementary workers not elsewhere classified', 'Hilfsarbeitskräfte, anderweitig nicht genannt [ESCO-Gruppenname]', ['car-park attendant'], ['Liftboy', 'Anweiser', 'Billeteur', 'Car-park attendant']),
}
