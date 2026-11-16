# Baut ein Berufsfeld in assets/berufe.json aus: BFS Zuweisungsschlüssel CH-ISCO-19 (V1.2), ESCO, jobs.ch.
# Aufruf: python compile_field.py field_buero 2026-11-16
import importlib, json, re, sys, collections, openpyxl
sys.stdout.reconfigure(encoding='utf-8')
cfg = importlib.import_module(sys.argv[1]); ABRUF = sys.argv[2]
Q = '../_quellen/'
wb = openpyxl.load_workbook(Q + 'do-t-00.07-ch-isco-19-02.xlsx', read_only=True)
rows = list(wb['V1.2_102022'].iter_rows(values_only=True))[1:]
jobs = json.load(open(Q + 'jobs-%s-%s.json' % (cfg.CLUSTER, ABRUF), encoding='utf-8'))
esco = json.load(open(Q + 'esco-%s-%s.json' % (cfg.CLUSTER, ABRUF), encoding='utf-8'))
G, W, NF = cfg.G, cfg.W, cfg.NF

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
for g, (uf, isco, iscoen, gl, eq, jq) in G.items():
    rs = by[g]
    if not rs: print('WARNUNG keine Titel für', g); continue
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
        t = t[0]
        # nur ESCO-Treffer, deren ISCO-Gruppe zur Gruppe passt
        if t['isco'] and not any(i and (i.startswith(isco[:3]) or isco.startswith(i[:3])) for i in t['isco']):
            print('ESCO-Treffer verworfen (ISCO passt nicht):', g, q, t['titel'], t['isco']); continue
        escos.append(t); ev += [t['titel']] + t['alt']
    ev = clean(ev, 10)
    raws = raw_titles(g); web = []
    for disp, pat in W.get(g, []):
        n = sum(1 for t in raws if re.search(pat, t, re.I))
        if n:
            web.append({'titel': disp, 'sprache': 'de/en', 'haeufigkeit': n, 'quelle': 'jobs.ch Stellensuche, Abruf %s: %d von %d gesichteten Titeln' % (ABRUF, n, len(raws))})
    quellen = ['BFS Zuweisungsschlüssel CH-ISCO-19 V1.2 (10/2022), Code %s: %d aktive Titel' % (g, len(rs))]
    quellen += ['ESCO «%s» %s (Abruf %s)' % (t['titel'], t['uri'], ABRUF) for t in escos]
    if web: quellen.append('jobs.ch öffentliche Stellensuche, Abruf ' + ABRUF)
    berufe.append({'id': '%s-%s' % (cfg.PREFIX, g), 'cluster': cfg.CLUSTER, 'unterfeld': uf, 'gruppe': gl, 'isco08': isco, 'isco08_en': iscoen, 'ch_isco19': g,
      'de': de, 'fr': fr, 'it': it, 'en': en, 'en_esco': ev, 'web': web,
      'niveau': ('Titel im Zuweisungsschlüssel nennen: ' + ', '.join(tokens)) if tokens else '',
      'anzahl_titel': len(rs), 'nachbarn': [], 'nachbar_felder': [], 'quereinstieg': '', 'quellen': quellen, 'status': 'geprüft',
      '_skills': [s for t in escos for s in t['skills']]})

for b in berufe:
    sc = []
    for o in berufe:
        if o is b or o['anzahl_titel'] <= 4: continue
        sh = sorted(set(b['_skills']) & set(o['_skills']))
        same = (b['isco08'][:3] == o['isco08'][:3])
        if sh: sc.append((len(sh) * 10 + (3 if same else 0), o, 'gemeinsame ESCO-Kernfähigkeiten: ' + '; '.join(sh[:3])))
        elif b['isco08'] == o['isco08']: sc.append((3, o, 'gleiche ISCO-08-Berufsgattung ' + b['isco08']))
        elif same: sc.append((2, o, 'gleiche ISCO-08-Untergruppe ' + b['isco08'][:3]))
        elif b['isco08'][:2] == o['isco08'][:2]: sc.append((1, o, 'gleiche ISCO-08-Berufsgruppe ' + b['isco08'][:2]))
    sc.sort(key=lambda x: -x[0])
    b['nachbarn'] = [{'id': o['id'], 'grund': gr} for _, o, gr in sc[:3]]
for b in berufe:
    for f, gr in NF.get(b['ch_isco19'], []): b['nachbar_felder'].append({'id': f, 'grund': gr})
    b.pop('_skills')

d = json.load(open('../assets/berufe.json', encoding='utf-8'))
d['berufe'] = [b for b in d['berufe'] if b['cluster'] != cfg.CLUSTER] + berufe
order = {c['id']: i for i, c in enumerate(d['cluster'])}
d['berufe'].sort(key=lambda b: order.get(b['cluster'], 99))
for c in d['cluster']:
    if c['id'] == cfg.CLUSTER:
        c['unterfelder'] = cfg.UNTERFELDER
        c['beschreibung'] = cfg.BESCHREIBUNG
filled = [c['de'] for c in d['cluster'] if any(b['cluster'] == c['id'] for b in d['berufe'])]
d['meta']['version'] = '%d-%s' % (len(filled), '+'.join(c['id'] for c in d['cluster'] if any(b['cluster'] == c['id'] for b in d['berufe'])))
d['meta']['stand'] = ABRUF
d['meta']['nomenklatur'] = 'CH-ISCO-19, Zuweisungsschlüssel V1.2 (Oktober 2022), BFS'
d['meta']['hinweis'] = 'Befüllt (geprüft gegen BFS-Zuweisungsschlüssel, ESCO und jobs.ch): ' + ', '.join(filled) + '. Alle anderen Felder sind noch leer.'
for s in ['jobs.ch öffentliche Stellensuche: https://www.jobs.ch (Abruf %s, Stichprobe je Suchbegriff)' % ABRUF]:
    qs = [x for x in d['meta']['quellen'] if not x.startswith('jobs.ch')]
    d['meta']['quellen'] = qs + [s]
json.dump(d, open('../assets/berufe.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(berufe), 'Gruppen')
for b in berufe: print(b['ch_isco19'], len(b['de']), len(b['en']), len(b['en_esco']), len(b['web']), [n['id'] for n in b['nachbarn']])
