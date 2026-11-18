# Automatisch erzeugt (gen_fields.py) aus BFS-Zuweisungsschlüssel V1.2 und ESCO-ISCO-Gruppennamen
CLUSTER = 'medien'
PREFIX = 'me'
APPEND = False
BESCHREIBUNG = 'Journalismus, Gestaltung, Kunst, Kultur, Druck, Marketing und Kommunikation. Basis: CH-ISCO-19, zugeordnet nach ISCO-08-Gruppen; Gruppennamen aus ESCO (de).'
UNTERFELDER = ['Marketing & Kommunikation', 'Design & Gestaltung', 'Kultur, Archiv & Bibliothek', 'Schreiben, Sprache & Übersetzung', 'Kunst, Musik & Darstellung', 'Ton, Bild & Druck']
W = 'auto'
NF = {}
G = {
'12220': ('Marketing & Kommunikation', '1222', 'Advertising and public relations managers', 'Führungskräfte in Werbung und Öffentlichkeitsarbeit [ESCO-Gruppenname]', ['pr manager'], ['PR-Manager', 'Markenchef', 'Reklamechef', 'Pr manager']),
'21630': ('Design & Gestaltung', '2163', 'Product and garment designers', 'Produkt- und Textildesigner [ESCO-Gruppenname]', ['designer'], ['Stylist', 'Stilist', 'Designer']),
'21660': ('Design & Gestaltung', '2166', 'Graphic and multimedia designers', 'Grafik- und Multimediadesigner [ESCO-Gruppenname]', ['graphic designer'], ['Grafiker', 'Graphiker', 'Webdesigner', 'Graphic designer']),
'24310': ('Marketing & Kommunikation', '2431', 'Advertising and marketing professionals', 'Akademische und vergleichbare Fachkräfte in Werbung und Marketing [ESCO-Gruppenname]', ['advertiser'], ['Werber', 'Marketer', 'Fundraiser', 'Advertiser']),
'24320': ('Marketing & Kommunikation', '2432', 'Public relations professionals', 'Akademische und vergleichbare Fachkräfte in der Öffentlichkeitsarbeit [ESCO-Gruppenname]', ['public relations consultant'], ['PR-Attaché', 'PR-Berater', 'Presseagent', 'Public relations consultant']),
'26210': ('Kultur, Archiv & Bibliothek', '2621', 'Archivists and curators', 'Archiv- und Museumswissenschaftler [ESCO-Gruppenname]', ['archivist'], ['Archivar', 'Museologe', 'Konservator', 'Archivist']),
'26220': ('Kultur, Archiv & Bibliothek', '2622', 'Librarians and related information professionals', 'Bibliothekswissenschaftler und verwandte Informationswissenschaftler [ESCO-Gruppenname]', ['media center librarian'], ['Mediothekar', 'Diskothekar', 'Videothekar', 'Media center librarian']),
'26410': ('Schreiben, Sprache & Übersetzung', '2641', 'Authors and related writers', 'Autoren und verwandte schriftstellerische Berufe [ESCO-Gruppenname]', ['author'], ['Autor', 'Texter', 'Literat', 'Author']),
'26420': ('Schreiben, Sprache & Übersetzung', '2642', 'Journalists', 'Journalisten [ESCO-Gruppenname]', ['editor'], ['Redaktor', 'Reporter', 'Kritiker', 'Editor']),
'26430': ('Schreiben, Sprache & Übersetzung', '2643', 'Translators, interpreters and other linguists', 'Übersetzer, Dolmetscher und andere Linguisten [ESCO-Gruppenname]', ['anglicist'], ['Anglist', 'Arabist', 'Romanist', 'Anglicist']),
'26500': ('Kunst, Musik & Darstellung', '265', 'Sammelgruppe 26500 (ohne eigene ISCO-08-Gattung)', 'Sammelgruppe: Freier Künstler, Künstler', [], ['Künstler', 'Kunstexperte', 'Freier Künstler']),
'26510': ('Kunst, Musik & Darstellung', '2651', 'Visual artists', 'Bildende Künstler [ESCO-Gruppenname]', ['sculptor'], ['Kolorist', 'Radierer', 'Colorist', 'Sculptor']),
'26520': ('Kunst, Musik & Darstellung', '2652', 'Musicians, singers and composers', 'Musiker, Sänger und Komponisten [ESCO-Gruppenname]', ['contralto'], ['Altus', 'Tenor', 'Kantor', 'Contralto']),
'26530': ('Kunst, Musik & Darstellung', '2653', 'Dancers and choreographers', 'Tänzer und Choreografen [ESCO-Gruppenname]', ['dancer'], ['Tänzer', 'Eintänzer', 'Vortänzer', 'Dancer']),
'26540': ('Kunst, Musik & Darstellung', '2654', 'Film, stage and related directors and producers', 'Regisseure und Produzenten im Film- und Bühnenbereich sowie in verwandten Bereichen [ESCO-Gruppenname]', ['dramatic adviser'], ['Dramaturg', 'Regisseur', 'Realisator', 'Dramatic adviser']),
'26550': ('Kunst, Musik & Darstellung', '2655', 'Actors', 'Schauspieler [ESCO-Gruppenname]', ['mime'], ['Mime', 'Komiker', 'Imitator']),
'26560': ('Kunst, Musik & Darstellung', '2656', 'Announcers on radio, television and other media', 'Sprecher im Rundfunk, Fernsehen und sonstigen Medien [ESCO-Gruppenname]', ['host (radio/tv)'], ['Ansager', 'Speaker', 'Sprecher', 'Host (radio/tv)']),
'26590': ('Kunst, Musik & Darstellung', '2659', 'Creative and performing artists not elsewhere classified', 'Bildende und darstellende Künstler, anderweitig nicht genannt [ESCO-Gruppenname]', ['clown'], ['Clown', 'Fakir', 'Artist']),
'34310': ('Kunst, Musik & Darstellung', '3431', 'Photographers', 'Fotografen [ESCO-Gruppenname]', ['photographer'], ['Fotograf', 'Fotostylist', 'Fachfotograf', 'Photographer']),
'34320': ('Design & Gestaltung', '3432', 'Interior designers and decorators', 'Raumgestalter und Dekorateure [ESCO-Gruppenname]', ['decorator'], ['Kinomaler', 'Szenograf', 'Standbauer', 'Decorator']),
'34330': ('Kultur, Archiv & Bibliothek', '3433', 'Gallery, museum and library technicians', 'Fachkräfte in Kunstgalerien, Museen und Bibliotheken [ESCO-Gruppenname]', ['museum technician'], ['Präparator', 'Ausstopfer', 'Kunstberater', 'Museum technician']),
'34350': ('Kunst, Musik & Darstellung', '3435', 'Other artistic and cultural associate professionals', 'Sonstige Fachkräfte in Gestaltung und Kultur [ESCO-Gruppenname]', ['scriptgirl/scriptboy'], ['Script', 'Statist', 'Figurant', 'Scriptgirl/scriptboy']),
'35210': ('Ton, Bild & Druck', '3521', 'Broadcasting and audiovisual technicians', 'Techniker für Rundfunk und audiovisuelle Medien [ESCO-Gruppenname]', ['cutter (film)'], ['Cutter', 'Videast', 'Vertoner', 'Cutter (film)']),
'52410': ('Kunst, Musik & Darstellung', '5241', 'Fashion and other models', 'Mannequins/Dressmen und sonstige Modelle [ESCO-Gruppenname]', ['model'], ['Model', 'Dressman', 'Coverboy']),
'73100': ('Kultur, Archiv & Bibliothek', '731', 'Sammelgruppe 73100 (ohne eigene ISCO-08-Gattung)', 'Sammelgruppe: Restaurator, HFG, Kunstrestaurator', ['artisan/craftsman'], ['Kunstgewerbler', 'Kunsthandwerker', 'Kunstrestaurator', 'Artisan/craftsman']),
'73210': ('Ton, Bild & Druck', '7321', 'Pre-press technicians', 'Techniker in der Druckvorstufe [ESCO-Gruppenname]', ['typographer'], ['Ätzer', 'Metteur', 'Clicheur', 'Typographer']),
'73220': ('Ton, Bild & Druck', '7322', 'Printers', 'Drucker [ESCO-Gruppenname]', ['printer'], ['Faktor', 'Kopist', 'Pauser', 'Printer']),
'73230': ('Ton, Bild & Druck', '7323', 'Print finishing and binding workers', 'Berufe in der Druckweiterverarbeitung und Buchbinder [ESCO-Gruppenname]', ['bookbinder'], ['Linierer', 'Buchbinder', 'Perforateur', 'Bookbinder']),
}
