# Automatisch erzeugt (gen_fields.py) aus BFS-Zuweisungsschlüssel V1.2 und ESCO-ISCO-Gruppennamen
CLUSTER = 'handel'
PREFIX = 'ha'
APPEND = False
BESCHREIBUNG = 'Detailhandel, Kasse, Vertrieb, Einkauf, Vermittlung. Basis: CH-ISCO-19, zugeordnet nach ISCO-08-Gruppen; Gruppennamen aus ESCO (de).'
UNTERFELDER = ['Leitung Verkauf & Handel', 'Verkauf, Einkauf & Vermittlung', 'Verkauf & Kasse']
W = 'auto'
NF = {}
G = {
'12210': ('Leitung Verkauf & Handel', '1221', 'Sales and marketing managers', 'Führungskräfte in Vertrieb und Marketing [ESCO-Gruppenname]', ['head of marketing and sales'], ['Kundendienstinspektor', 'Marketing- und Verkaufsleiter', 'Marketing- und Verkaufsmanager', 'Head of marketing and sales']),
'12211': ('Leitung Verkauf & Handel', '1221', 'Sales and marketing managers', 'Führungskräfte in Vertrieb und Marketing [ESCO-Gruppenname]', ['sales manager'], ['Marktleiter', 'Verkaufschef', 'Salesmanager', 'Sales manager']),
'12212': ('Leitung Verkauf & Handel', '1221', 'Sales and marketing managers', 'Führungskräfte in Vertrieb und Marketing [ESCO-Gruppenname]', ['marketing director'], ['Bid-Manager', 'Marketingleiter', 'Marketingmanager', 'Marketing director']),
'14200': ('Leitung Verkauf & Handel', '1420', 'Retail and wholesale trade managers', 'Führungskräfte in Groß- und Einzelhandel [ESCO-Gruppenname]', ['car dealer'], ['Grossist', 'Autohändler', 'Grosshändler', 'Car dealer']),
'24331': ('Verkauf, Einkauf & Vermittlung', '2433', 'Technical and medical sales professionals (excluding ICT)', 'Akademische und vergleichbare Fachkräfte im Bereich Vertrieb (Technik und Medizin, ohne Informations- und Kommunikationstechnologie) [ESCO-Gruppenname]', ['account engineer'], ['Account Engineer', 'Verkaufsingenieur', 'Verkaufstechniker', 'Account engineer']),
'24332': ('Verkauf, Einkauf & Vermittlung', '2433', 'Technical and medical sales professionals (excluding ICT)', 'Akademische und vergleichbare Fachkräfte im Bereich Vertrieb (Technik und Medizin, ohne Informations- und Kommunikationstechnologie) [ESCO-Gruppenname]', ['pharmaceutical representative'], ['Ärzteberater', 'Arztbesucher', 'Pharmaberater', 'Pharmaceutical representative']),
'33000': ('Verkauf, Einkauf & Vermittlung', '330', 'Sammelgruppe 33000 (ohne eigene ISCO-08-Gattung)', 'Sammelgruppe: Vermittler, Makler', ['agent'], ['Agent', 'Makler', 'Auswerter']),
'33220': ('Verkauf, Einkauf & Vermittlung', '3322', 'Commercial sales representatives', 'Vertriebsagenten [ESCO-Gruppenname]', ['travelling salesman'], ['Reisender', 'Vertreter', 'Reiseagent', 'Travelling salesman']),
'33230': ('Verkauf, Einkauf & Vermittlung', '3323', 'Buyers', 'Einkäufer [ESCO-Gruppenname]', ['buyer'], ['Aufkäufer', 'Einkäufer', 'Beschaffer', 'Buyer']),
'33240': ('Verkauf, Einkauf & Vermittlung', '3324', 'Trade brokers', 'Handelsmakler [ESCO-Gruppenname]', ['merchant'], ['Händler', 'Depositär', 'Negoziant', 'Merchant']),
'33300': ('Verkauf, Einkauf & Vermittlung', '333', 'Sammelgruppe 33300 (ohne eigene ISCO-08-Gattung)', 'Sammelgruppe: Zentralagent, Regionalagent', [], ['Zentralagent', 'Regionalagent']),
'33340': ('Verkauf, Einkauf & Vermittlung', '3334', 'Real estate agents and property managers', 'Immobilienmakler und -verwalter [ESCO-Gruppenname]', ['property manager'], ['Häusermakler', 'Objektleiter', 'Gebäudemakler', 'Property manager']),
'33390': ('Verkauf, Einkauf & Vermittlung', '3339', 'Business services agents not elsewhere classified', 'Fachkräfte für unternehmensbezogene Dienstleistungen, anderweitig nicht genannt [ESCO-Gruppenname]', ['advertising agent'], ['Filmagent', 'Werbeagent', 'Impresario', 'Advertising agent']),
'50000': ('Verkauf, Einkauf & Vermittlung', '500', 'Sammelgruppe 50000 (ohne eigene ISCO-08-Gattung)', 'Sammelgruppe: Dienstleistungsangestellter', [], ['Dienstleistungsangestellter']),
'52110': ('Verkauf & Kasse', '5211', 'Stall and market salespersons', 'Verkaufsstand- und Marktverkäufer [ESCO-Gruppenname]', ['kiosk manager'], ['Marktmann', 'Perronier', 'Kioskleiter', 'Kiosk manager']),
'52120': ('Verkauf & Kasse', '5212', 'Street food salespersons', 'Straßenverkäufer von Lebensmitteln [ESCO-Gruppenname]', ['hot chestnut vendor'], ['Marroniverkäufer', 'Hot chestnut vendor']),
'52210': ('Verkauf & Kasse', '5221', 'Shop keepers', 'Leiter eines Einzelhandelsgeschäftes [ESCO-Gruppenname]', ['junk dealer'], ['Krämer', 'Trödler', 'Antiquar', 'Junk dealer']),
'52220': ('Verkauf & Kasse', '5222', 'Shop supervisors', 'Verkaufsaufsichtskräfte in Handelsgeschäften [ESCO-Gruppenname]', ['shop manager'], ['Rayonchef', 'Möbelagent', 'Chef Rayon', 'Shop manager']),
'52230': ('Verkauf & Kasse', '5223', 'Shop sales assistants', 'Verkäufer und Verkaufshilfskräfte in Handelsgeschäften [ESCO-Gruppenname]', ['salesperson'], ['Verkäufer', 'Blumenmann', 'Modeberater', 'Salesperson']),
'52231': ('Verkauf & Kasse', '5223', 'Shop sales assistants', 'Verkäufer und Verkaufshilfskräfte in Handelsgeschäften [ESCO-Gruppenname]', ['druggist'], ['Drogist', 'Druggist']),
'52300': ('Verkauf & Kasse', '5230', 'Cashiers and ticket clerks', 'Kassierer und Kartenverkäufer [ESCO-Gruppenname]', ['cashier'], ['Kassier', 'Bezüger', 'Einzieher', 'Cashier']),
'52420': ('Verkauf & Kasse', '5242', 'Sales demonstrators', 'Produktvorführer [ESCO-Gruppenname]', ['presenter'], ['Werbemann', 'Vorführer', 'Promoteur', 'Presenter']),
'52430': ('Verkauf & Kasse', '5243', 'Door to door salespersons', 'Haustürverkäufer [ESCO-Gruppenname]', ['pedlar'], ['Hausierer', 'Brothausierer', 'Hausierhändler', 'Pedlar']),
'52440': ('Verkauf & Kasse', '5244', 'Contact centre salespersons', 'Telefonverkäufer [ESCO-Gruppenname]', ['call centre salesperson'], ['Telefonverkäufer', 'Telefonverkaufsberater', 'Telemarketingmitarbeiter', 'Call centre salesperson']),
'52450': ('Verkauf & Kasse', '5245', 'Service station attendants', 'Tankwarte [ESCO-Gruppenname]', ['service station attendant'], ['Tanker', 'Tankwart', 'Pneumonteur', 'Service station attendant']),
'52490': ('Verkauf & Kasse', '5249', 'Sales workers not elsewhere classified', 'Verkaufskräfte, anderweitig nicht genannt [ESCO-Gruppenname]', ['rental agent'], ['Vermieter', 'Verleiher', 'Skiverleiher', 'Rental agent']),
'93340': ('Verkauf & Kasse', '9334', 'Shelf fillers', 'Regalbetreuer und -auffüller [ESCO-Gruppenname]', ['shelf stacker'], ['Auffüller', 'Warenauffüller', 'Shelf stacker']),
'95100': ('Verkauf & Kasse', '9510', 'Street and related service workers', 'Auf der Straße arbeitende Dienstleistungskräfte und verwandte Berufe [ESCO-Gruppenname]', ['shoe cleaner'], ['Schuhputzer', 'Shoe cleaner']),
'95200': ('Verkauf & Kasse', '9520', 'Street vendors (excluding food)', 'Straßenverkäufer (ohne Lebensmittel) [ESCO-Gruppenname]', ['street hawker'], ['Wanderhändler', 'Strassenhändler', 'Ambulanter Händler', 'Street hawker']),
}
