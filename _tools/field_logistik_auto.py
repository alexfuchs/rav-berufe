# Automatisch erzeugt (gen_fields.py) aus BFS-Zuweisungsschlüssel V1.2 und ESCO-ISCO-Gruppennamen
CLUSTER = 'logistik'
PREFIX = 'lo'
APPEND = False
BESCHREIBUNG = 'Transport, Lager, Post, Schiene, Luftfahrt, Schiff, Spedition. Basis: CH-ISCO-19, zugeordnet nach ISCO-08-Gruppen; Gruppennamen aus ESCO (de).'
UNTERFELDER = ['Leitung Logistik', 'Spedition & Verkehrsleitung', 'Material, Transport & Post']
W = 'auto'
NF = {}
G = {
'13240': ('Leitung Logistik', '1324', 'Supply, distribution and related managers', 'Führungskräfte in der Beschaffung, Logistik und in verwandten Bereichen [ESCO-Gruppenname]', ['shipowner'], ['Reeder', 'Carhalter', 'Lead Buyer', 'Shipowner']),
'31500': ('Spedition & Verkehrsleitung', '315', 'Sammelgruppe 31500 (ohne eigene ISCO-08-Gattung)', 'Sammelgruppe: Schiffsexperte, Besatzungsplaner', ['traffic expert'], ['Schiffsexperte', 'Verkehrsexperte', 'Besatzungsplaner', 'Traffic expert']),
'31510': ('Spedition & Verkehrsleitung', '3151', 'Ships’ engineers', 'Technische Schiffsoffiziere [ESCO-Gruppenname]', ['boat machinist'], ['Bootsmaschinist', 'Maschinenoffizier', 'Schiffsmaschinist', 'Boat machinist']),
'31520': ('Spedition & Verkehrsleitung', '3152', "Ships' deck officers and pilots", 'Schiffsführer, nautische Schiffsoffiziere und Schiffslotsen [ESCO-Gruppenname]', ['ship pilot'], ['Lotse', 'Kapitän', 'Fährmann', 'Ship pilot']),
'31530': ('Spedition & Verkehrsleitung', '3153', 'Aircraft pilots and related associate professionals', 'Flugzeugführer und verwandte Berufe [ESCO-Gruppenname]', ['pilot'], ['Pilot', 'Flieger', 'Copilot']),
'31540': ('Spedition & Verkehrsleitung', '3154', 'Air traffic controllers', 'Flugverkehrslotsen [ESCO-Gruppenname]', ['control tower operator'], ['Flugagent', 'Fluglotse', 'Flugleiter', 'Control tower operator']),
'31550': ('Spedition & Verkehrsleitung', '3155', 'Air traffic safety electronics technicians', 'Flugsicherungstechniker [ESCO-Gruppenname]', ['air traffic safety technician'], ['Fallschirmwart', 'Luftfahrtinspektor', 'Fachkontrolleur BAMF', 'Air traffic safety technician']),
'33310': ('Spedition & Verkehrsleitung', '3331', 'Clearing and forwarding agents', 'Fachkräfte für Abrechnungs- und Speditionsdienstleistungen [ESCO-Gruppenname]', ['haulier'], ['Fergger', 'Expedient', 'Spediteur', 'Haulier']),
'43200': ('Material, Transport & Post', '432', 'Sammelgruppe 43200 (ohne eigene ISCO-08-Gattung)', 'Sammelgruppe: Logistiker, Logistiksachbearbeiter', ['managing clerk'], ['Disponent', 'Logistiker', 'Logismatiker', 'Managing clerk']),
'43210': ('Material, Transport & Post', '4321', 'Stock clerks', 'Fachkräfte in der Lagerwirtschaft [ESCO-Gruppenname]', ['stockkeeper'], ['Ausgeber', 'Lagerist', 'Lagerchef', 'Stockkeeper']),
'43220': ('Material, Transport & Post', '4322', 'Production clerks', 'Bürokräfte in der Material- und Fertigungsplanung und verwandte Berufe [ESCO-Gruppenname]', ['order planner'], ['Terminchef', 'Terminbeamter', 'Einsatzplaner', 'Order planner']),
'43230': ('Material, Transport & Post', '4323', 'Transport clerks', 'Bürokräfte in der Transportwirtschaft und verwandte Berufe [ESCO-Gruppenname]', ['gate agent'], ['Deklarant', 'Güterchef', 'Gate Agent', 'Gate agent']),
'44120': ('Material, Transport & Post', '4412', 'Mail carriers and sorting clerks', 'Postverteiler und -sortierer [ESCO-Gruppenname]', ['mailman'], ['Postbote', 'Briefbote', 'Zusteller', 'Mailman']),
'83000': ('Material, Transport & Post', '830', 'Sammelgruppe 83000 (ohne eigene ISCO-08-Gattung)', 'Sammelgruppe: Chauffeur-Magaziner, Chauffeur-Servicemann', ['chauffeur'], ['Chauffeur', 'Schlepper', 'Testfahrer']),
'83110': ('Material, Transport & Post', '8311', 'Locomotive engine drivers', 'Lokomotivführer [ESCO-Gruppenname]', ['locomotive driver'], ['Lokführer', 'Lokomotivführer', 'Lokomotivheizer', 'Locomotive driver']),
'83120': ('Material, Transport & Post', '8312', 'Railway brake, signal and switch operators', 'Bediener von Sicherungs-, Signal- und Leittechnik im Schienennetzbetrieb [ESCO-Gruppenname]', ['braker (railway)'], ['Bremser', 'Blockwärter', 'Manövrierer', 'Braker (railway)']),
'83210': ('Material, Transport & Post', '8321', 'Motorcycle drivers', 'Kraftradfahrer [ESCO-Gruppenname]', [], ['Motorradkurier', 'Chauffeur Kat. A', 'Pizzakurier']),
'83220': ('Material, Transport & Post', '8322', 'Car, taxi and van drivers', 'Personenkraftwagen-, Taxi-, Kleintransporter- und Kleinbusfahrer [ESCO-Gruppenname]', ['breakdown mechanic'], ['Lieferer', 'Taxifahrer', 'Blumenbote', 'Breakdown mechanic']),
'83310': ('Material, Transport & Post', '8331', 'Bus and tram drivers', 'Busfahrer und Straßenbahnführer [ESCO-Gruppenname]', ['motorman (driver)'], ['Busfahrer', 'Tramführer', 'Wagenführer', 'Motorman (driver)']),
'83320': ('Material, Transport & Post', '8332', 'Heavy truck and lorry drivers', 'Fahrer schwerer Lastkraftwagen [ESCO-Gruppenname]', ['long-haul truck driver'], ['Camionist', 'Fernfahrer', 'Camionneur', 'Long-haul truck driver']),
'83440': ('Material, Transport & Post', '8344', 'Lifting truck operators', 'Gabelstaplerfahrer und verwandte Berufe [ESCO-Gruppenname]', ['fork-lift operator'], ['Clark-Fahrer', 'Staplerfahrer', 'Hubstaplerfahrer', 'Fork-lift operator']),
'83500': ('Material, Transport & Post', '8350', 'Ships’ deck crews and related workers', 'Deckspersonal auf Schiffen und verwandte Berufe [ESCO-Gruppenname]', ['seaman'], ['Ländter', 'Seemann', 'Matrose', 'Seaman']),
'93310': ('Material, Transport & Post', '9331', 'Hand and pedal vehicle drivers', 'Führer von Handwagen und pedalbetriebenen Fahrzeugen [ESCO-Gruppenname]', ['bicycle courier'], ['Velokurier', 'Bicycle courier']),
'93320': ('Material, Transport & Post', '9332', 'Drivers of animal-drawn vehicles and machinery', 'Führer von Fahrzeugen und Maschinen mit Zugtierantrieb [ESCO-Gruppenname]', ['coachman'], ['Kutscher', 'Postkutscher', 'Hotelkutscher', 'Coachman']),
'93330': ('Material, Transport & Post', '9333', 'Freight handlers', 'Frachtarbeiter und verwandte Berufe [ESCO-Gruppenname]', ['removal man'], ['Säumer', 'Zügler', 'Belader', 'Removal man']),
'96210': ('Material, Transport & Post', '9621', 'Messengers, package deliverers and luggage porters', 'Boten, Paketauslieferer und Gepäckträger [ESCO-Gruppenname]', ['courier (messenger)'], ['Kurier', 'Eilbote', 'Bankbote', 'Courier (messenger)']),
'96230': ('Material, Transport & Post', '9623', 'Meter readers and vending-machine collectors', 'Zählerableser, Automatenbefüller und -kassierer [ESCO-Gruppenname]', ['vending machine technician'], ['Wassermesser', 'Standaufnehmer', 'Gasstandableser', 'Vending machine technician']),
}
