# Automatisch erzeugt (gen_fields.py) aus BFS-Zuweisungsschlüssel V1.2 und ESCO-ISCO-Gruppennamen
CLUSTER = 'wissenschaft'
PREFIX = 'wi'
APPEND = False
BESCHREIBUNG = 'Naturwissenschaften, Geistes- und Sozialwissenschaften, Forschung. Basis: CH-ISCO-19, zugeordnet nach ISCO-08-Gruppen; Gruppennamen aus ESCO (de).'
UNTERFELDER = ['Leitung Forschung', 'Naturwissenschaften', 'Geistes- und Sozialwissenschaften']
W = 'auto'
NF = {}
G = {
'12230': ('Leitung Forschung', '1223', 'Research and development managers', 'Führungskräfte in Forschung und Entwicklung [ESCO-Gruppenname]', ['lead researcher'], ['Forschungsleiter', 'Leiter Forschung', 'Entwicklungschef', 'Lead researcher']),
'21000': ('Naturwissenschaften', '210', 'Sammelgruppe 21000 (ohne eigene ISCO-08-Gattung)', 'Sammelgruppe: Universitätslaborant, Technischer Analytiker', ['inventor'], ['Erfinder', 'Metalloge', 'Assistent', 'Inventor']),
'21110': ('Naturwissenschaften', '2111', 'Physicists and astronomers', 'Physiker und Astronomen [ESCO-Gruppenname]', ['astronomer'], ['Astronom', 'Physiker', 'Rheologe', 'Astronomer']),
'21120': ('Naturwissenschaften', '2112', 'Meteorologists', 'Meteorologen [ESCO-Gruppenname]', ['aerologist'], ['Aerologe', 'Wetterwart', 'Klimatologe', 'Aerologist']),
'21130': ('Naturwissenschaften', '2113', 'Chemists', 'Chemiker [ESCO-Gruppenname]', ['chemist'], ['Chemiker', 'Biochemiker', 'Anorganiker', 'Chemist']),
'21140': ('Naturwissenschaften', '2114', 'Geologists and geophysicists', 'Geologen und Geophysiker [ESCO-Gruppenname]', ['geologist'], ['Geologe', 'Hydrologe', 'Petrograf', 'Geologist']),
'21200': ('Naturwissenschaften', '2120', 'Mathematicians, actuaries and statisticians', 'Mathematiker, Versicherungsmathematiker und Statistiker [ESCO-Gruppenname]', ['demographer'], ['Aktuar', 'Demograf', 'Demograph', 'Demographer']),
'21310': ('Naturwissenschaften', '2131', 'Biologists, botanists, zoologists and related professionals', 'Biologen, Botaniker, Zoologen und verwandte Berufe [ESCO-Gruppenname]', ['anatomist'], ['Anatom', 'Biologe', 'Zoologe', 'Anatomist']),
'21330': ('Naturwissenschaften', '2133', 'Environmental protection professionals', 'Umweltwissenschaftler [ESCO-Gruppenname]', ['ecologist'], ['Ökologe', 'Geoökologe', 'Umweltökonom', 'Ecologist']),
'26000': ('Geistes- und Sozialwissenschaften', '260', 'Sammelgruppe 26000 (ohne eigene ISCO-08-Gattung)', 'Sammelgruppe: Dr ès lettres, Lic. ès lettres', ['dr ès lettres'], ['Dr ès lettres', 'Lic. ès lettres', 'Master en lettres']),
'26300': ('Geistes- und Sozialwissenschaften', '263', 'Sammelgruppe 26300 (ohne eigene ISCO-08-Gattung)', 'Sammelgruppe: Doktor in Polizei- und Kriminologiewissenschaft, Prof. Dr. phil I', ['master in social sciences'], ['Dr. phil. I', 'Lic. phil. I', 'Prof. Dr. phil I', 'Master in social sciences']),
'26310': ('Geistes- und Sozialwissenschaften', '2631', 'Economists', 'Volkswirtschaftler [ESCO-Gruppenname]', ['economist'], ['Ökonom', 'Volkswirt', 'Ökonomist', 'Economist']),
'26320': ('Geistes- und Sozialwissenschaften', '2632', 'Sociologists, anthropologists and related professionals', 'Soziologen, Anthropologen und verwandte Wissenschaftler [ESCO-Gruppenname]', ['slavist'], ['Slawist', 'Nordist', 'Geograph', 'Slavist']),
'26330': ('Geistes- und Sozialwissenschaften', '2633', 'Philosophers, historians and political scientists', 'Philosophen, Historiker und Politologen [ESCO-Gruppenname]', ['mythologist'], ['Mythologe', 'Genealoge', 'Mediävist', 'Mythologist']),
}
