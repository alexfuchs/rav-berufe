# Automatisch erzeugt (gen_fields.py) aus BFS-Zuweisungsschlüssel V1.2 und ESCO-ISCO-Gruppennamen
CLUSTER = 'gastro'
PREFIX = 'ga'
APPEND = False
BESCHREIBUNG = 'Küche, Service, Hotellerie, Reise, Veranstaltungen. Basis: CH-ISCO-19, zugeordnet nach ISCO-08-Gruppen; Gruppennamen aus ESCO (de).'
UNTERFELDER = ['Leitung Gastgewerbe & Freizeit', 'Veranstaltung & Küche', 'Reise, Küche & Service']
W = 'auto'
NF = {}
G = {
'14110': ('Leitung Gastgewerbe & Freizeit', '1411', 'Hotel managers', 'Führungskräfte in Hotels [ESCO-Gruppenname]', ['landlord (public house)'], ['Gerant', 'Gastwirt', 'Hotelier', 'Landlord (public house)']),
'14120': ('Leitung Gastgewerbe & Freizeit', '1412', 'Restaurant managers', 'Führungskräfte in Restaurants [ESCO-Gruppenname]', ['cafe/restaurant owner'], ['Wirt', 'Cafetier', 'Gastronom', 'Cafe/restaurant owner']),
'14310': ('Leitung Gastgewerbe & Freizeit', '1431', 'Sports, recreation and cultural centre managers', 'Führungskräfte in der Erbringung von Dienstleistungen im Bereich Sport, Erholung und Kultur [ESCO-Gruppenname]', ['zoo director'], ['Clubleiter', 'Kurdirektor', 'Zoodirektor', 'Zoo director']),
'14390': ('Leitung Gastgewerbe & Freizeit', '1439', 'Services managers not elsewhere classified', 'Führungskräfte in der Erbringung von Dienstleistungen, anderweitig nicht genannt [ESCO-Gruppenname]', ['garage owner'], ['Garagist', 'Garagechef', 'Garagedirektor', 'Garage owner']),
'33320': ('Veranstaltung & Küche', '3332', 'Conference and event planners', 'Konferenz- und Veranstaltungsplaner [ESCO-Gruppenname]', ['event manager'], ['Messeplaner', 'Event Manager', 'Weddingplaner', 'Event manager']),
'34340': ('Veranstaltung & Küche', '3434', 'Chefs', 'Küchenchefs [ESCO-Gruppenname]', ['chef cook'], ['Chefkoch', 'Küchenchef', 'Kochberater', 'Chef cook']),
'51110': ('Reise, Küche & Service', '5111', 'Travel attendants and travel stewards', 'Reisebegleiter und Stewards [ESCO-Gruppenname]', ['purser'], ['Purser', 'Steward', 'Airliner']),
'51120': ('Reise, Küche & Service', '5112', 'Transport conductors', 'Schaffner [ESCO-Gruppenname]', ['train manager'], ['Zugchef', 'Zugführer', 'Schaffner', 'Train manager']),
'51130': ('Reise, Küche & Service', '5113', 'Travel guides', 'Reiseleiter/Fremdenführer [ESCO-Gruppenname]', ['guide'], ['Führer', 'Zooführer', 'Tourguide', 'Guide']),
'51200': ('Reise, Küche & Service', '5120', 'Cooks', 'Köche [ESCO-Gruppenname]', ['cook'], ['Koch', 'Saucier', 'Traiteur', 'Cook']),
'51311': ('Reise, Küche & Service', '5131', 'Waiters', 'Kellner [ESCO-Gruppenname]', ['head waiter'], ['Demi-chef', 'Hotelküfer', 'Saalmeister', 'Head waiter']),
'51312': ('Reise, Küche & Service', '5131', 'Waiters', 'Kellner [ESCO-Gruppenname]', ['server (waiter)'], ['Servierer', 'Sommelier', 'Weinkellner', 'Server (waiter)']),
'51313': ('Reise, Küche & Service', '5131', 'Waiters', 'Kellner [ESCO-Gruppenname]', ['boy waiter'], ['Piccolo', 'Buffetier', 'Saalkellner', 'Boy waiter']),
'51320': ('Reise, Küche & Service', '5132', 'Bartenders', 'Barkeeper [ESCO-Gruppenname]', ['barman'], ['Barman', 'Barista', 'Barmixer']),
'52460': ('Reise, Küche & Service', '5246', 'Food service counter attendants', 'Imbissverkäufer [ESCO-Gruppenname]', ['kebab seller'], ['Glacéverkäufer', 'Kebabverkäufer', 'Eiscremeverkäufer', 'Kebab seller']),
'94110': ('Reise, Küche & Service', '9411', 'Fast food preparers', 'Zubereiter von Fast Food und anderen Imbissen [ESCO-Gruppenname]', ['pizzaiolo'], ['Pizzaiolo', 'Kebab-Koch', 'Crêpehersteller']),
'94121': ('Reise, Küche & Service', '9412', 'Kitchen helpers', 'Küchenhilfen [ESCO-Gruppenname]', ['kitchen ancillary'], ['Hilfskoch', 'Kochgehilfe', 'Kochassistent', 'Kitchen ancillary']),
'94122': ('Reise, Küche & Service', '9412', 'Kitchen helpers', 'Küchenhilfen [ESCO-Gruppenname]', ['kitchen porter/dish washer'], ['Abwascher', 'Officeherr', 'Casserolier', 'Kitchen porter/dish washer']),
}
