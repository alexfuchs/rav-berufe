# Nachlauf: Verweise zwischen Feldern (gleiche ISCO-08-Untergruppe) und Meta-Angaben.
import json, collections, datetime
ABRUF = '2026-11-18'
d = json.load(open('../assets/berufe.json', encoding='utf-8'))
lab = {c['id']: c['de'] for c in d['cluster']}
bykey = collections.defaultdict(list)
for b in d['berufe']:
    if b['isco08'].isdigit() and len(b['isco08']) >= 3: bykey[b['isco08'][:3]].append(b)
added = 0
for b in d['berufe']:
    have = {n['id'] for n in b['nachbar_felder']}
    if b['cluster'] in have: pass
    seen = set(have)
    for o in bykey.get(b['isco08'][:3], []):
        if o['cluster'] == b['cluster'] or o['cluster'] in seen: continue
        if len(b['nachbar_felder']) >= 3: break
        b['nachbar_felder'].append({'id': o['cluster'], 'grund': 'gleiche ISCO-08-Untergruppe %s: %s (%s)' % (b['isco08'][:3], o['gruppe'].replace(' [ESCO-Gruppenname]', ''), o['ch_isco19'])})
        seen.add(o['cluster']); added += 1
for b in d['berufe']:
    if b['id'].split('-')[0] not in ('it', 'bu'): b['status'] = 'entwurf'
filled = [c['id'] for c in d['cluster'] if any(b['cluster'] == c['id'] for b in d['berufe'])]
d['meta']['version'] = '%d-alle' % len(filled)
d['meta']['stand'] = ABRUF
d['meta']['hinweis'] = ('Alle 17 Berufsfelder sind befüllt (%d Berufsarten der CH-ISCO-19 (5-stellig); Zuweisungsschlüssel V1.2, ESCO, jobs.ch, jobup.ch, job-room.ch). '
    'Die Felder IT und Büro wurden von Hand geprüft (Status «geprüft»); die übrigen 15 Felder wurden regelbasiert erzeugt und tragen den Status «entwurf»: Zuordnung der ISCO-Gruppen zu Feldern und Unterfeldern ist eine Setzung des Projekts, Internettitel sind automatisch bereinigte Ausschreibungstitel (Stichprobe je Suchbegriff), Verweise zwischen Feldern beruhen nur auf gleicher ISCO-08-Untergruppe.' % len(d['berufe']))
qs = [x for x in d['meta']['quellen'] if not x.startswith('jobs.ch')]
d['meta']['quellen'] = qs + ['Stellenportale (öffentliche Suche, Stichprobe je Suchbegriff, Abruf %s): https://www.jobs.ch, https://www.jobup.ch, https://www.job-room.ch (RAV/SECO)' % ABRUF,
    'ISCO-08-Gruppennamen de/en: ESCO-API, https://ec.europa.eu/esco/api (Abruf %s)' % ABRUF]
json.dump(d, open('../assets/berufe.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('Feldverweise ergänzt:', added, '| Felder:', len(filled), '| Gruppen:', len(d['berufe']))
print(json.dumps(d['meta'], ensure_ascii=False, indent=1)[:1500])
