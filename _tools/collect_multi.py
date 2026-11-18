# Sammelt für ein Berufsfeld Titel aus drei öffentlichen Schweizer Stellenportalen (jobs.ch, jobup.ch, job-room.ch der RAV/SECO) und ESCO-Treffer.
# Aufruf: python collect_multi.py field_technik_auto
import importlib, json, re, sys, time, datetime, urllib.request, urllib.parse
sys.stdout.reconfigure(encoding='utf-8')
cfg = importlib.import_module(sys.argv[1])
today = datetime.date.today().isoformat()
UA = {"User-Agent": "Mozilla/5.0 (Berufsliste-Recherche)"}

def get(u, data=None):
    h = dict(UA)
    if data: h['Content-Type'] = 'application/json'
    return json.load(urllib.request.urlopen(urllib.request.Request(u, headers=h, data=data), timeout=30))

def portal(name, t):
    if name == 'jobs.ch':
        return [x['title'] for x in get('https://www.jobs.ch/api/v1/public/search?rows=20&query=' + urllib.parse.quote_plus(t))['documents']]
    if name == 'jobup.ch':
        return [x['title'] for x in get('https://www.jobup.ch/api/v1/public/search?rows=20&query=' + urllib.parse.quote_plus(t))['documents']]
    if name == 'job-room.ch':
        d = get('https://www.job-room.ch/jobadservice/api/jobAdvertisements/_search?page=0&size=20&sort=score', json.dumps({"keywords": [t]}).encode())
        return [re.sub(r'</?em>', '', j['title']) for a in d for j in a['jobAdvertisement']['jobContent']['jobDescriptions'][:1]]

jobs = {"abruf": today, "quelle": "jobs.ch, jobup.ch, job-room.ch (öffentliche Suche, je Begriff 20 Treffer)", "gruppen": {}}
esco = {"abruf": today, "quelle": "https://ec.europa.eu/esco/api (Sprache en)", "treffer": {}}
for g, (uf, isco, en, gl, eq, jq) in cfg.G.items():
    jobs["gruppen"][g] = {}
    for t in jq:
        e = {"titel": [], "portale": {}}
        for p in ('jobs.ch', 'jobup.ch', 'job-room.ch'):
            try:
                l = portal(p, t); e["portale"][p] = l; e["titel"] += l
            except Exception as ex:
                e["portale"][p] = {"fehler": str(ex)}
            time.sleep(0.8)
        jobs["gruppen"][g][t] = e
    esco["treffer"][g] = []
    for q in eq:
        try:
            r = get("https://ec.europa.eu/esco/api/search?language=en&type=occupation&limit=1&full=false&text=" + urllib.parse.quote(q))
            h = r["_embedded"]["results"][0]
            d = get("https://ec.europa.eu/esco/api/resource/occupation?language=en&uri=" + urllib.parse.quote(h["uri"], safe=""))
            esco["treffer"][g].append({"suche": q, "titel": d["title"], "uri": h["uri"],
                "alt": d.get("alternativeLabel", {}).get("en", []),
                "isco": [x.get("code") for x in d.get("_links", {}).get("broaderIscoGroup", []) if isinstance(x, dict)],
                "skills": [s["title"] for s in d.get("_links", {}).get("hasEssentialSkill", [])][:12]})
        except Exception as ex:
            esco["treffer"][g].append({"suche": q, "fehler": str(ex)})
        time.sleep(0.4)
    print(g, "ok", flush=True)
json.dump(jobs, open("../_quellen/jobs-%s-%s.json" % (cfg.CLUSTER, today), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(esco, open("../_quellen/esco-%s-%s.json" % (cfg.CLUSTER, today), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("fertig")
