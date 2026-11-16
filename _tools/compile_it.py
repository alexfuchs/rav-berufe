# Baut das Feld «IT & Digital» in assets/berufe.json aus: BFS Zuweisungsschlüssel CH-ISCO-19 (V1.2), ESCO, jobs.ch.
import json, re, sys, collections, openpyxl
sys.stdout.reconfigure(encoding='utf-8')
Q = '../_quellen/'
wb = openpyxl.load_workbook(Q + 'do-t-00.07-ch-isco-19-02.xlsx', read_only=True)
rows = list(wb['V1.2_102022'].iter_rows(values_only=True))[1:]
jobs = json.load(open(Q + 'jobs-ch-2026-11-16.json', encoding='utf-8'))
esco = json.load(open(Q + 'esco-2026-11-16.json', encoding='utf-8'))
ABRUF = '2026-11-16'

# Gruppen: code -> (unterfeld, isco, ISCO-08 englisch, Beschreibung deutsch [sinngemäss], ESCO-Suchbegriffe)
G = {
'13300': ('Leitung & Vertrieb', '1330', 'ICT service managers', 'Leitung Informatik / ICT-Dienste', ['chief information officer', 'ICT project manager']),
'24340': ('Leitung & Vertrieb', '2434', 'ICT sales professionals', 'Vertrieb von ICT-Produkten und -Dienstleistungen', ['ICT account manager', 'ICT presales engineer']),
'25100': ('Entwicklung & Architektur', '251', 'Software and applications developers and analysts', 'Software-/Applikationsfachleute, allgemein', []),
'25101': ('Entwicklung & Architektur', '251', 'Software and applications developers and analysts', 'Informatikingenieur/in (Ingenieur-/Diplomtitel)', []),
'25111': ('Analyse & Beratung', '2511', 'Systems analysts', 'Systemanalyse und Business-Analyse', ['ICT business analyst', 'ICT system analyst']),
'25112': ('Analyse & Beratung', '2511', 'Systems analysts', 'IT-Beratung und Applikationsberatung', ['ICT consultant']),
'25121': ('Entwicklung & Architektur', '2512', 'Software developers', 'Software-Entwicklung und -Architektur', ['software developer', 'software architect']),
'25122': ('Entwicklung & Architektur', '2512', 'Software developers', 'Wirtschaftsinformatik und IT-Lösungen', ['ICT system architect']),
'25123': ('Entwicklung & Architektur', '2512', 'Software developers', 'Systementwicklung / System Engineering', []),
'25124': ('Projekt & Test', '2512', 'Software developers', 'IT-Projektleitung und Produktverantwortung (Scrum, Product Owner)', ['ICT project manager']),
'25130': ('Entwicklung & Architektur', '2513', 'Web and multimedia developers', 'Web- und Multimedia-Entwicklung', ['web developer', 'digital media designer']),
'25140': ('Entwicklung & Architektur', '2514', 'Applications programmers', 'Applikationsprogrammierung und Entwicklung (inkl. DevOps, Data Science)', ['ICT application developer', 'data scientist']),
'25191': ('Projekt & Test', '2519', 'Software and applications developers and analysts not elsewhere classified', 'Software-Test und Qualitätssicherung', ['ICT test analyst', 'software tester']),
'25210': ('Daten', '2521', 'Database designers and administrators', 'Datenbanken, Data Engineering, Data Warehouse', ['database administrator', 'database developer']),
'25220': ('Betrieb & Infrastruktur', '2522', 'Systems administrators', 'Systemadministration und -betrieb', ['ICT system administrator']),
'25230': ('Betrieb & Infrastruktur', '2523', 'Computer network professionals', 'Netzwerk-Engineering und -Betrieb', ['ICT network engineer', 'ICT network administrator']),
'25291': ('Sicherheit', '2529', 'Database and network professionals not elsewhere classified', 'IT-Sicherheit / Cyber Security', ['ICT security administrator', 'ethical hacker']),
'35100': ('Support', '351', 'ICT operations and user support technicians', 'ICT-Fachpersonen, allgemein (Informatiker/in, Spezialist/in)', []),
'35110': ('Betrieb & Infrastruktur', '3511', 'ICT operations technicians', 'ICT-Betrieb (Techniker/in)', []),
'35120': ('Support', '3512', 'ICT user support technicians', 'Anwenderunterstützung / Helpdesk / Service Desk', ['ICT help desk agent']),
'35130': ('Betrieb & Infrastruktur', '3513', 'Computer network and systems technicians', 'Netzwerk- und Systemtechnik (Techniker/in, Telematik)', ['ICT network technician']),
'35140': ('Web', '3514', 'Web technicians', 'Web-Technik (Webmaster, Web Publishing)', ['webmaster']),
'35220': ('Telekommunikation', '3522', 'Telecommunications engineering technicians', 'Telekommunikationstechnik (Fernmelde, Telematik)', []),
'74220': ('Telekommunikation', '7422', 'ICT installers and servicers', 'Installation und Service von ICT-/Telekommunikationsanlagen', ['telecommunications technician']),
}
# Titel im Internet: (Anzeige, Regex); nur übernommen, wenn in den gesichteten Ausschreibungen gefunden
W = {
'13300': [('Head of IT', 'head of it'), ('Leiter/in IT bzw. Informatik', r'leiter\S* (it|informatik)|(ict|it)-leiter'), ('IT-/ICT-Verantwortliche/r', r'(it|ict)-verantwortliche')],
'24340': [('Account Manager (ICT)', 'account manager'), ('Sales Engineer IT Security', 'sales engineer'), ('Channel Partner Manager', r'channel (sales|partner)')],
'25101': [('Cloud Engineer', 'cloud engineer'), ('ICT Engineer', r'ict .*engineer'), ('AI Engineer', 'ai engineer')],
'25111': [('Business Analyst', 'business analyst'), ('Systems Analyst', r'systems? analyst')],
'25112': [('SAP Consultant', r'sap .*consultant|consultant.*sap'), ('IT Consultant', r'it consultant'), ('ICT-Berater/-in', r'ict-berater|systemberater')],
'25121': [('Software Engineer', 'software engineer'), ('Fullstack Software Engineer', 'fullstack software engineer'), ('Embedded Software Engineer', 'embedded software'), ('Tech Lead', 'tech lead')],
'25122': [('Wirtschaftsinformatiker/in', 'wirtschaftsinformatiker')],
'25123': [('System Engineer', 'system engineer'), ('IT System Engineer', 'it system engineer')],
'25124': [('Product Owner', 'product owner'), ('IT-Projektleiter/in', r'it-?projektleiter|projektleiter\S* it|technischer projektleiter it|it project manager')],
'25130': [('Web Developer / Webentwickler/in', r'web developer|webentwickler|web-/software'), ('Frontend Developer / Engineer', 'frontend'), ('Full-Stack Developer', r'full ?stack')],
'25140': [('Java Developer / Entwickler', r'java (developer|entwickler)'), ('DevOps Engineer', 'devops engineer'), ('Mobile Developer / Applications', r'mobile (developer|applications)')],
'25191': [('Software Test Engineer / Tester', r'test engineer|software tester'), ('Test Manager', r'test ?manager|testmanagement'), ('Teamleiter Testing', r'test und release|teamleader testing')],
'25210': [('Data Engineer', 'data engineer'), ('Datenbank-Administrator/in', r'datenbank-administrator|database administrator')],
'25220': [('IT-Systemadministrator/in', r'systemadministrator|system administrator|system-administrator|netzwerkadministrator'), ('System Engineer (Microsoft / Citrix)', 'system engineer'), ('M365 / Modern Workplace Engineer', r'm365|modern workplace')],
'25230': [('Network Engineer', r'network engineer|netzwerk engineer'), ('Netzwerk-Spezialist/in', 'netzwerk-spezialist'), ('Ingénieur réseau', 'ingénieur réseau')],
'25291': [('Cyber Security Engineer / Analyst', r'cyber security (engineer|analyst)'), ('IT-/ICT-Security-Spezialist/in', r'(it|ict)[- ]security[- ]spezialist'), ('Information Security Officer', 'information security officer'), ('Penetration Testing / Red Teaming', r'penetration|red team')],
'35100': [('IT Spezialist', 'it spezialist'), ('Informatiker/in', r'^informatiker'), ('ICT Servicedesk Mitarbeiter/in', 'servicedesk')],
'35110': [('Technicien IT', r'technicien.* it|it-techniker'), ('IT Coordinator / Koordinator', r'it coordinator|it koordinator')],
'35120': [('IT-/ICT-Supporter/in', r'(it|ict)[- ]?supporter'), ('Service Desk', r'service ?desk'), ('2nd Level Support', '2nd level'), ('Support Specialist', 'support specialist')],
'35130': [('Network Engineer', r'network engineer'), ('ICT System & Network Engineer', r'system & network engineer|system-/ network'), ('Netzwerktechniker/in', 'netzwerktechniker')],
'35140': [('Webmaster', 'webmaster'), ('Content & Channel Manager Web', 'content & channel manager')],
'35220': [('Systemtechniker', 'systemtechniker')],
'74220': [('Monteur Wireless Outdoor', 'wireless outdoor'), ('Monteur Kupfer / LWL Telekommunikation', r'lwl|kupfer')],
}

def mf(m, f):
    m = (m or '').strip(); f = (f or '').strip()
    if not m: return f
    if f == m or not f: return m
    if f == m + 'in': return m + '/in'
    return m + ' / ' + f

def clean(l, limit):
    seen = set(); out = []
    for t in l:
        k = t.lower()
        if k in seen: continue
        seen.add(k); out.append(t)
    return out[:limit]

def ok(t): return ',' not in t or re.search(r'EFZ|EBA|eidg\.|dipl\.', t)

by = collections.defaultdict(list)
for r in rows:
    if r[13] and str(r[13]) in G and r[11] == 1: by[str(r[13])].append(r)

def raw_titles(g):
    s = set()
    for v in jobs['gruppen'].get(g, {}).values(): s.update(v.get('titel', []))
    return s

berufe = []
for g, (uf, isco, iscoen, gl, eq) in G.items():
    rs = by[g]
    rs_sorted = sorted(rs, key=lambda r: (r[12] != 1, len(r[1] or '')))
    de = clean([mf(r[1], r[2]) for r in rs_sorted if r[1] and ok(r[1])], 14)
    fr = clean([mf(r[3], r[4]) for r in rs_sorted if r[3] and ok(r[3])], 4)
    it = clean([mf(r[5], r[6]) for r in rs_sorted if r[5] and ok(r[5])], 4)
    en = clean([r[7] for r in rs_sorted if r[7] and ok(r[7])], 10)
    alltext = ' '.join((r[1] or '') for r in rs)
    tokens = []
    for tok, pat in [('EBA', r'\bEBA\b'), ('EFZ', r'\bEFZ\b'), ('Berufsprüfung (BP)', r'\bBP\b|eidg\. FA'), ('höhere Fachprüfung (HFP)', r'\bHFP\b'), ('HF/TS', r'\bHF\b|\bTS\b'), ('FH', r'\bFH\b'), ('HTL', r'\bHTL\b'), ('ETH', r'\bETH\b')]:
        if re.search(pat, alltext): tokens.append(tok)
    ev = []; escos = []
    for q in eq:
        t = [x for gg in esco['treffer'].values() for x in gg if x.get('suche') == q and 'titel' in x]
        if not t: continue
        t = t[0]; escos.append(t); ev += [t['titel']] + t['alt']
    ev = clean(ev, 10)
    raws = raw_titles(g); web = []
    for disp, pat in W.get(g, []):
        n = sum(1 for t in raws if re.search(pat, t, re.I))
        if n:
            web.append({'titel': disp, 'sprache': 'de/en', 'haeufigkeit': n, 'quelle': 'jobs.ch Stellensuche, Abruf %s: %d von %d gesichteten Titeln' % (ABRUF, n, len(raws))})
    quellen = ['BFS Zuweisungsschlüssel CH-ISCO-19 V1.2 (10/2022), Code %s: %d aktive Titel' % (g, len(rs))]
    quellen += ['ESCO «%s» %s (Abruf %s)' % (t['titel'], t['uri'], ABRUF) for t in escos]
    if web: quellen.append('jobs.ch öffentliche Stellensuche, Abruf ' + ABRUF)
    berufe.append({'id': 'it-' + g, 'cluster': 'it', 'unterfeld': uf, 'gruppe': gl, 'isco08': isco, 'isco08_en': iscoen, 'ch_isco19': g,
      'de': de, 'fr': fr, 'it': it, 'en': en, 'en_esco': ev, 'web': web,
      'niveau': ('Titel im Zuweisungsschlüssel nennen: ' + ', '.join(tokens)) if tokens else '',
      'anzahl_titel': len(rs), 'nachbarn': [], 'nachbar_felder': [], 'quereinstieg': '', 'quellen': quellen, 'status': 'geprüft',
      '_skills': [s for t in escos for s in t['skills']]})

for b in berufe:
    sc = []
    for o in berufe:
        if o is b or o['anzahl_titel'] <= 6: continue
        sh = sorted(set(b['_skills']) & set(o['_skills']))
        same = (b['isco08'][:3] == o['isco08'][:3])
        if sh: sc.append((len(sh) * 10 + (3 if same else 0), o, 'gemeinsame ESCO-Kernfähigkeiten: ' + '; '.join(sh[:3])))
        elif same: sc.append((1, o, 'gleiche ISCO-08-Untergruppe ' + b['isco08'][:3]))
    sc.sort(key=lambda x: -x[0])
    b['nachbarn'] = [{'id': o['id'], 'grund': gr} for _, o, gr in sc[:3]]

nf = {'25140': [('wissenschaft', '«Data Scientist» führt der BFS-Zuweisungsschlüssel auch unter 21200 (Mathematik/Statistik)')],
 '25130': [('medien', 'ESCO «digital media designer» (ISCO 2166, Grafik/Multimedia); Titel Mediamatiker/in im Zuweisungsschlüssel')],
 '24340': [('handel', 'Vertriebsfähigkeiten laut ESCO «ICT account manager»: sales strategies, customer relationship management')],
 '74220': [('bau', 'Titel wie Elektro-Installateur/in und Netzbaumonteur/in in jobs.ch-Ausschreibungen zur Monteur-Suche')]}
for b in berufe:
    for f, gr in nf.get(b['ch_isco19'], []): b['nachbar_felder'].append({'id': f, 'grund': gr})
    b.pop('_skills')

d = json.load(open('../assets/berufe.json', encoding='utf-8'))
d['berufe'] = [b for b in d['berufe'] if b['cluster'] != 'it'] + berufe
for c in d['cluster']:
    if c['id'] == 'it':
        c['unterfelder'] = ['Leitung & Vertrieb', 'Analyse & Beratung', 'Entwicklung & Architektur', 'Projekt & Test', 'Daten', 'Betrieb & Infrastruktur', 'Sicherheit', 'Support', 'Web', 'Telekommunikation']
        c['beschreibung'] = 'Entwicklung, Betrieb, Support, Daten, Sicherheit und Telekommunikation. Basis: alle ICT-Gruppen der CH-ISCO-19 (133, 2434, 251, 252, 351, 3522, 7422).'
d['meta'].update({'version': '1-it', 'stand': ABRUF, 'nomenklatur': 'CH-ISCO-19, Zuweisungsschlüssel V1.2 (Oktober 2022), BFS',
 'hinweis': 'Berufsfeld «IT & Digital» ist befüllt (geprüft gegen BFS-Zuweisungsschlüssel, ESCO und jobs.ch). Alle anderen Felder sind noch leer.',
 'quellen': ['BFS, Schweizer Berufsnomenklatur CH-ISCO-19, Zuweisungsschlüssel V1.2: https://dam-api.bfs.admin.ch/hub/api/dam/assets/23530845/master (Abruf ' + ABRUF + ')',
  'ESCO (Europäische Kommission): https://esco.ec.europa.eu, API https://ec.europa.eu/esco/api (Abruf ' + ABRUF + ')',
  'jobs.ch öffentliche Stellensuche: https://www.jobs.ch (Abruf ' + ABRUF + ', Stichprobe je Suchbegriff)']})
json.dump(d, open('../assets/berufe.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(berufe), 'Gruppen')
for b in berufe: print(b['ch_isco19'], len(b['de']), len(b['en']), len(b['en_esco']), len(b['web']), [n['id'] for n in b['nachbarn']])
