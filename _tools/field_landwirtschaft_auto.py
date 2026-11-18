# Automatisch erzeugt (gen_fields.py) aus BFS-Zuweisungsschlüssel V1.2 und ESCO-ISCO-Gruppennamen
CLUSTER = 'landwirtschaft'
PREFIX = 'la'
APPEND = False
BESCHREIBUNG = 'Landwirtschaft, Gartenbau, Forst, Fischerei. Basis: CH-ISCO-19, zugeordnet nach ISCO-08-Gruppen; Gruppennamen aus ESCO (de).'
UNTERFELDER = ['Leitung Land- & Forstwirtschaft', 'Beratung & Technik', 'Landwirtschaft, Gartenbau & Forst']
W = 'auto'
NF = {}
G = {
'13110': ('Leitung Land- & Forstwirtschaft', '1311', 'Agricultural and forestry production managers', 'Führungskräfte in der Produktion in Land- und Forstwirtschaft [ESCO-Gruppenname]', ['agricultural estate owner'], ['Gutsbesitzer', 'Gutsverwalter', 'Forstverwalter', 'Agricultural estate owner']),
'21320': ('Beratung & Technik', '2132', 'Farming, forestry and fisheries advisers', 'Agrar-, Forst- und Fischereiwissenschaftler und -berater [ESCO-Gruppenname]', ['oenologist'], ['Önologe', 'Agronom', 'Pedologe', 'Oenologist']),
'31420': ('Beratung & Technik', '3142', 'Agricultural technicians', 'Agrartechniker [ESCO-Gruppenname]', ['fieldman'], ['Fieldman', 'Baumexperte', 'Zootechniker']),
'31430': ('Beratung & Technik', '3143', 'Forestry technicians', 'Forsttechniker [ESCO-Gruppenname]', ['forest warden'], ['Förster', 'Oberförster', 'Sägemeister', 'Forest warden']),
'61100': ('Landwirtschaft, Gartenbau & Forst', '611', 'Sammelgruppe 61100 (ohne eigene ISCO-08-Gattung)', 'Sammelgruppe: Agrarpraktiker EBA, Spezialkulturen, Agrarpraktiker, Spezialkulturen', [], ['Agrarpraktiker']),
'61110': ('Landwirtschaft, Gartenbau & Forst', '6111', 'Field crop and vegetable growers', 'Ackerbauern und Gemüseanbauer [ESCO-Gruppenname]', ['horticulturist (vegetable grower)'], ['Gemüsebauer', 'Gemüsegärtner', 'Hopfenanbauer', 'Horticulturist (vegetable grower)']),
'61121': ('Landwirtschaft, Gartenbau & Forst', '6112', 'Tree and shrub crop growers', 'Baum- und Strauchfrüchteanbauer [ESCO-Gruppenname]', ['pomologist'], ['Pomologe', 'Obstbauer', 'Obstzüchter', 'Pomologist']),
'61122': ('Landwirtschaft, Gartenbau & Forst', '6112', 'Tree and shrub crop growers', 'Baum- und Strauchfrüchteanbauer [ESCO-Gruppenname]', ['winegrower'], ['Winzer', 'Rebmann', 'Rebbauer', 'Winegrower']),
'61130': ('Landwirtschaft, Gartenbau & Forst', '6113', 'Gardeners, horticultural and nursery growers', 'Gärtner, Saat- und Pflanzenzüchter [ESCO-Gruppenname]', ['gardener'], ['Gärtner', 'Obergärtner', 'Gärtnermeister', 'Gardener']),
'61131': ('Landwirtschaft, Gartenbau & Forst', '6113', 'Gardeners, horticultural and nursery growers', 'Gärtner, Saat- und Pflanzenzüchter [ESCO-Gruppenname]', ['horticulturist'], ['Begrüner', 'Ziergärtner', 'Gartenbauer', 'Horticulturist']),
'61132': ('Landwirtschaft, Gartenbau & Forst', '6113', 'Gardeners, horticultural and nursery growers', 'Gärtner, Saat- und Pflanzenzüchter [ESCO-Gruppenname]', ['mushroom grower'], ['Baumwärter', 'Pilzzüchter', 'Bio-Gärtner', 'Mushroom grower']),
'61211': ('Landwirtschaft, Gartenbau & Forst', '6121', 'Livestock and dairy producers', 'Nutztierhalter (ohne Geflügel) und Milchproduzenten [ESCO-Gruppenname]', ['herdsman'], ['Hirt', 'Senn', 'Alphirt', 'Herdsman']),
'61212': ('Landwirtschaft, Gartenbau & Forst', '6121', 'Livestock and dairy producers', 'Nutztierhalter (ohne Geflügel) und Milchproduzenten [ESCO-Gruppenname]', ['equestrian'], ['Reiter', 'Bereiter', 'Pferdewirt', 'Equestrian']),
'61220': ('Landwirtschaft, Gartenbau & Forst', '6122', 'Poultry producers', 'Geflügelhalter [ESCO-Gruppenname]', ['bird breeder'], ['Vogelzüchter', 'Geflügelhalter', 'Geflügelfarmer', 'Bird breeder']),
'61230': ('Landwirtschaft, Gartenbau & Forst', '6123', 'Apiarists and sericulturists', 'Imker und Seidenraupenzüchter [ESCO-Gruppenname]', ['apiarist'], ['Imker', 'Bienenhalter', 'Imkermeister', 'Apiarist']),
'61290': ('Landwirtschaft, Gartenbau & Forst', '6129', 'Animal producers not elsewhere classified', 'Tierhalter, anderweitig nicht genannt [ESCO-Gruppenname]', ['breeder'], ['Züchter', 'Falkner', 'Hundezüchter', 'Breeder']),
'61300': ('Landwirtschaft, Gartenbau & Forst', '6130', 'Mixed crop and animal producers', 'Landwirte mit Ackerbau und Tierhaltung (ohne ausgeprägten Schwerpunkt) [ESCO-Gruppenname]', ['farmer'], ['Bauer', 'Farmer', 'Pächter']),
'62100': ('Landwirtschaft, Gartenbau & Forst', '6210', 'Forestry and related workers', 'Forstarbeitskräfte und verwandte Berufe [ESCO-Gruppenname]', ['forest manager'], ['Roder', 'Köhler', 'Bannwart', 'Forest manager']),
'62210': ('Landwirtschaft, Gartenbau & Forst', '6221', 'Aquaculture workers', 'Fachkräfte im Bereich Aquakultur [ESCO-Gruppenname]', ['pond keeper (fish farming)'], ['Teichwärter', 'Fischzüchter', 'Austernzüchter', 'Pond keeper (fish farming)']),
'62220': ('Landwirtschaft, Gartenbau & Forst', '6222', 'Inland and coastal waters fishery workers', 'Binnen- und Küstenfischer [ESCO-Gruppenname]', ['fisherman'], ['Fischer', 'Seefischer', 'Netzfischer', 'Fisherman']),
'62240': ('Landwirtschaft, Gartenbau & Forst', '6224', 'Hunters and trappers', 'Jäger und Fallensteller [ESCO-Gruppenname]', ['hunter'], ['Jäger', 'Hunter']),
'83410': ('Landwirtschaft, Gartenbau & Forst', '8341', 'Mobile farm and forestry plant operators', 'Führer von mobilen land- und forstwirtschaftlichen Maschinen [ESCO-Gruppenname]', ['thresher'], ['Drescher', 'Traktorführer', 'Torfmaschinenführer', 'Thresher']),
'92110': ('Landwirtschaft, Gartenbau & Forst', '9211', 'Crop farm labourers', 'Hilfsarbeiter im Ackerbau [ESCO-Gruppenname]', ['picker'], ['Pflücker', 'Weinleser', 'Rebarbeiter', 'Picker']),
'92120': ('Landwirtschaft, Gartenbau & Forst', '9212', 'Livestock farm labourers', 'Hilfsarbeiter in der Tierhaltung [ESCO-Gruppenname]', ['milker'], ['Melker', 'Viehknecht', 'Stallknecht', 'Milker']),
'92130': ('Landwirtschaft, Gartenbau & Forst', '9213', 'Mixed crop and livestock farm labourers', 'Hilfsarbeiter in Ackerbau und Tierhaltung (ohne ausgeprägten Schwerpunkt) [ESCO-Gruppenname]', ['farm hand'], ['Knecht', 'Karrer', 'Fuhrknecht', 'Farm hand']),
'92140': ('Landwirtschaft, Gartenbau & Forst', '9214', 'Garden and horticultural labourers', 'Hilfsarbeiter im Gartenbau [ESCO-Gruppenname]', ['arborist'], ['Gartenhilfe', 'Baumpfleger', 'Rasenpfleger', 'Arborist']),
'92150': ('Landwirtschaft, Gartenbau & Forst', '9215', 'Forestry labourers', 'Hilfsarbeiter in der Forstwirtschaft [ESCO-Gruppenname]', ['forestry assistant'], ['Forstgehilfe', 'Rander in Holzindustrie', 'Forestry assistant']),
'92160': ('Landwirtschaft, Gartenbau & Forst', '9216', 'Fishery and aquaculture labourers', 'Hilfsarbeiter in der Fischerei und Aquakultur [ESCO-Gruppenname]', ['fishing assistant'], ['Fischer-Gehilfe', 'Fishing assistant']),
}
