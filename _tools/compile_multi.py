# Baut ein Berufsfeld in assets/berufe.json aus: BFS Zuweisungsschlüssel CH-ISCO-19 (V1.2), ESCO und drei Stellenportalen (jobs.ch, jobup.ch, job-room.ch).
# Aufruf: python compile_multi.py field_technik_auto 2026-11-18
import importlib, json, re, sys, collections, openpyxl
sys.stdout.reconfigure(encoding='utf-8')
cfg = importlib.import_module(sys.argv[1]); ABRUF = sys.argv[2]
Q = '../_quellen/'
rows = list(openpyxl.load_workbook(Q + 'do-t-00.07-ch-isco-19-02.xlsx', read_only=True)['V1.2_102022'].iter_rows(values_only=True))[1:]
jobs = json.load(open(Q + 'jobs-%s-%s.json' % (cfg.CLUSTER, ABRUF), encoding='utf-8'))
esco = json.load(open(Q + 'esco-%s-%s.json' % (cfg.CLUSTER, ABRUF), encoding='utf-8'))
G = cfg.G
APPEND = getattr(cfg, 'APPEND', False)

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

EN_WORDS = set('manager engineer specialist assistant officer developer technician operator driver consultant advisor adviser sales service head lead senior junior agent clerk worker supervisor analyst coordinator administrator nurse teacher director designer mechanic electrician cleaner cook chef warehouse logistics customer support and the for'.split())
def sprache(t):
    w = re.findall(r'[a-zäöü]+', t.lower())
    n = sum(1 for x in w if x in EN_WORDS)
    return 'en' if w and n * 2 >= len(w) else ('de/en' if n else 'de')

def norm(t):
    t = re.sub(r'<[^>]+>', '', t)
    t = re.sub(r'\(\s*[mwfdx*:/]{1,8}(\s*[/,]\s*[mwfdx*:]{1,3})*\s*\)|\b[mwfd]\s*/\s*[mwfd](\s*/\s*[mwfdx])?\b|\[[^\]]*\]|\(\d.*?%\)', ' ', t, flags=re.I)
    t = re.sub(r'\b\d{1,3}\s*(-|–|bis)?\s*\d{0,3}\s*%', ' ', t)
    t = re.split(r'\s+[|–—]\s+|\s+-\s+', t)[0] if len(re.split(r'\s+[|–—]\s+|\s+-\s+', t)[0]) >= 8 else t
    t = re.sub(r'\s+(in|bei|at|im|region)\s+[A-ZÄÖÜ][\w\.\-]+(\s+[A-ZÄÖÜ][\w\.\-]+)*\s*$', '', t)
    if t.count('(') > t.count(')'): t = t.split('(')[0]
    t = re.sub(r'[\s,;:/\-–]+$', '', re.sub(r'\s+', ' ', t)).strip(' ,;:/-–')
    return t

STOP = set('manag engin agent assis speci senio junio mitar leite leitu offic techn fachp fachm sachb chef head lead group globa inter prakt apprent verwa projek custo clien'.split())
def stems(strs):
    s = set()
    for x in strs:
        for w in re.findall(r'[A-Za-zÄÖÜäöüéèàç]{5,}', x.lower()):
            if w[:5] not in STOP: s.add(w[:5])
    return s

by = collections.defaultdict(list)
for r in rows:
    if r[13] and str(r[13]) in G and r[11] == 1: by[str(r[13])].append(r)

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
        if t['isco'] and not any(i and (i.startswith(isco[:3]) or isco.startswith(i[:3])) for i in t['isco']):
            print('ESCO-Treffer verworfen (ISCO passt nicht):', g, q, t['titel'], t['isco']); continue
        escos.append(t); ev += [t['titel']] + t['alt']
    ev = clean(ev, 10)
    # Titel im Internet: bereinigte Ausschreibungstitel aus drei Portalen, nur mit Bezug zu BFS-Titeln oder Suchbegriffen
    st = stems([r[1] or '' for r in rs] + [r[7] or '' for r in rs] + jq)
    cnt = collections.Counter(); disp = {}; ports = collections.defaultdict(set); raw_n = 0
    for qy, e in jobs['gruppen'].get(g, {}).items():
        for p, l in e.get('portale', {}).items():
            if not isinstance(l, list): continue
            for t in l:
                raw_n += 1
                c = norm(t)
                if len(c) < 4 or len(c) > 70: continue
                if not (stems([c]) & st): continue
                k = c.lower(); cnt[k] += 1; disp.setdefault(k, c); ports[k].add(p)
    web = []
    for k, n in sorted(cnt.items(), key=lambda kv: (-kv[1], len(kv[0])))[:8]:
        web.append({'titel': disp[k], 'sprache': sprache(disp[k]), 'haeufigkeit': n, 'portale': sorted(ports[k]),
                    'quelle': '%s, Abruf %s: %d Treffer in %d gesichteten Titeln' % (', '.join(sorted(ports[k])), ABRUF, n, raw_n)})
    quellen = ['BFS Zuweisungsschlüssel CH-ISCO-19 V1.2 (10/2022), Code %s: %d aktive Titel' % (g, len(rs))]
    quellen += ['ESCO «%s» %s (Abruf %s)' % (t['titel'], t['uri'], ABRUF) for t in escos]
    if web: quellen.append('jobs.ch, jobup.ch, job-room.ch öffentliche Stellensuche, Abruf ' + ABRUF)
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
for b in berufe: b.pop('_skills')

d = json.load(open('../assets/berufe.json', encoding='utf-8'))
if APPEND:
    ids = {b['id'] for b in berufe}
    d['berufe'] = [b for b in d['berufe'] if b['id'] not in ids] + berufe
else:
    d['berufe'] = [b for b in d['berufe'] if b['cluster'] != cfg.CLUSTER] + berufe
order = {c['id']: i for i, c in enumerate(d['cluster'])}
d['berufe'].sort(key=lambda b: order.get(b['cluster'], 99))
for c in d['cluster']:
    if c['id'] == cfg.CLUSTER:
        if APPEND: c['unterfelder'] = list(dict.fromkeys(c.get('unterfelder', []) + cfg.UNTERFELDER))
        else:
            c['unterfelder'] = cfg.UNTERFELDER; c['beschreibung'] = cfg.BESCHREIBUNG
json.dump(d, open('../assets/berufe.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(cfg.CLUSTER, len(berufe), 'Gruppen; mit Internettiteln:', sum(1 for b in berufe if b['web']))
