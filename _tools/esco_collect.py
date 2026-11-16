import json,urllib.request,urllib.parse,sys,time,datetime
sys.stdout.reconfigure(encoding='utf-8')
Q={"13300":["chief information officer","ICT project manager"],"24340":["ICT account manager","ICT sales"],
"25111":["ICT business analyst","ICT system analyst"],"25112":["ICT consultant"],"25121":["software developer","software architect"],
"25122":["ICT solutions architect","business informatics"],"25123":["ICT system architect"],"25124":["ICT project manager","scrum master"],
"25130":["web developer","multimedia developer"],"25140":["application developer","DevOps engineer","data scientist"],
"25191":["ICT test analyst","software tester"],"25210":["database administrator","data engineer","database developer"],
"25220":["ICT system administrator"],"25230":["ICT network engineer","ICT network administrator"],
"25291":["ICT security specialist","ICT security administrator","penetration tester"],"35120":["ICT help desk agent","ICT application support"],
"35130":["ICT network technician"],"35140":["web administrator","webmaster"],"74220":["ICT installer"],"35220":["telecommunications technician"]}
out={"abruf":datetime.date.today().isoformat(),"quelle":"https://ec.europa.eu/esco/api (ESCO v1.x, Sprache en)","treffer":{}}
def get(u):
    return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=30))
for g,qs in Q.items():
    out["treffer"][g]=[]
    for q in qs:
        try:
            r=get("https://ec.europa.eu/esco/api/search?language=en&type=occupation&limit=1&full=false&text="+urllib.parse.quote(q))
            h=r["_embedded"]["results"][0]
            d=get("https://ec.europa.eu/esco/api/resource/occupation?language=en&uri="+urllib.parse.quote(h["uri"],safe=""))
            alts=d.get("alternativeLabel",{}).get("en",[])
            iscos=[x.get("code") for x in d.get("_links",{}).get("broaderIscoGroup",[]) if isinstance(x,dict)]
            out["treffer"][g].append({"suche":q,"titel":d["title"],"uri":h["uri"],"alt":alts,"isco":iscos,"skills":[s["title"] for s in d.get("_links",{}).get("hasEssentialSkill",[])][:12]})
        except Exception as e:
            out["treffer"][g].append({"suche":q,"fehler":str(e)})
        time.sleep(0.4)
    print(g,[ (t.get("titel"),t.get("isco")) for t in out["treffer"][g]],flush=True)
json.dump(out,open(sys.argv[1],"w",encoding="utf-8"),ensure_ascii=False,indent=1)
