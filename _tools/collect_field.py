# Sammelt für ein Berufsfeld: Titel aus jobs.ch (öffentliche Stellensuche) und ESCO-Treffer.
# Aufruf: python collect_field.py field_buero
import importlib, json, sys, time, datetime, urllib.request, urllib.parse
sys.stdout.reconfigure(encoding='utf-8')
cfg = importlib.import_module(sys.argv[1])
today = datetime.date.today().isoformat()
UA = {"User-Agent": "Mozilla/5.0 (Berufsliste-Recherche)"}

def get(u):
    return json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30))

jobs = {"abruf": today, "quelle": "https://www.jobs.ch/api/v1/public/search?query=<Begriff>&rows=20", "gruppen": {}}
esco = {"abruf": today, "quelle": "https://ec.europa.eu/esco/api (Sprache en)", "treffer": {}}
for g, (uf, isco, en, gl, eq, jq) in cfg.G.items():
    jobs["gruppen"][g] = {}
    for t in jq:
        u = "https://www.jobs.ch/api/v1/public/search?rows=20&query=" + urllib.parse.quote_plus(t)
        try:
            d = get(u)
            jobs["gruppen"][g][t] = {"titel": [x["title"] for x in d["documents"]]}
        except Exception as e:
            jobs["gruppen"][g][t] = {"fehler": str(e)}
        time.sleep(1.2)
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
        except Exception as e:
            esco["treffer"][g].append({"suche": q, "fehler": str(e)})
        time.sleep(0.4)
    print(g, "ok", flush=True)
json.dump(jobs, open("../_quellen/jobs-%s-%s.json" % (cfg.CLUSTER, today), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(esco, open("../_quellen/esco-%s-%s.json" % (cfg.CLUSTER, today), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("fertig")
