# Sammelt Titel aktueller Stellenausschreibungen von jobs.ch (öffentliche Suche) pro Suchbegriff.
import json, time, urllib.request, urllib.parse, datetime, sys
sys.stdout.reconfigure(encoding='utf-8')
Q = {
 "13300": ["Head of IT","Leiter IT","Leiter Informatik","CIO","IT Manager","Head of Infrastructure"],
 "24340": ["IT Sales","Account Manager IT","Presales Engineer","ICT Sales"],
 "25101": ["Informatikingenieur","Informatik Ingenieur ETH"],
 "25111": ["Business Analyst IT","Systemanalytiker","Requirements Engineer","IT Architekt","Solution Architect"],
 "25112": ["IT Consultant","Applikationsberater","SAP Consultant","Technology Consultant"],
 "25121": ["Software Engineer","Softwareentwickler","Software Architect","Backend Developer"],
 "25122": ["Wirtschaftsinformatiker","IT Solution Engineer","Business Informatiker"],
 "25123": ["System Engineer","Systemingenieur","Platform Engineer"],
 "25124": ["IT Projektleiter","IT Project Manager","Scrum Master","Product Owner"],
 "25130": ["Web Developer","Frontend Developer","Mediamatiker","Webentwickler"],
 "25140": ["Applikationsentwickler","Java Developer","DevOps Engineer","Data Scientist","Mobile Developer","Full Stack Developer"],
 "25191": ["Software Tester","Test Engineer","QA Engineer","Testmanager"],
 "25210": ["Data Engineer","Datenbankadministrator","BI Developer","Data Warehouse"],
 "25220": ["Systemadministrator","Linux Administrator","Windows Systemadministrator","Cloud Engineer","System Engineer Microsoft"],
 "25230": ["Netzwerkingenieur","Network Engineer","Netzwerkspezialist"],
 "25291": ["Information Security","IT Security Engineer","Cyber Security Specialist","Penetration Tester","Security Analyst"],
 "35100": ["IT Operator","Informatik Mitarbeiter","IT Mitarbeiter"],
 "35110": ["IT Techniker","Informatiktechniker","IT Specialist"],
 "35120": ["IT Supporter","Service Desk","Helpdesk","First Level Support","Informatiker EFZ Systemtechnik","2nd Level Support"],
 "35130": ["Netzwerktechniker","Telematiker","Informatiker EFZ Plattformentwicklung"],
 "35140": ["Webmaster","Web Publisher","Content Manager Web"],
 "35220": ["Telekommunikation Techniker","Fernmeldetechniker","Telematiktechniker"],
 "74220": ["ICT Monteur","Glasfaser Monteur","Antennenmonteur","Telematik Monteur"],
}
out = {"abruf": datetime.date.today().isoformat(), "quelle": "https://www.jobs.ch/api/v1/public/search?query=<Begriff>&rows=20", "gruppen": {}}
for g, terms in Q.items():
    out["gruppen"][g] = {}
    for t in terms:
        u = "https://www.jobs.ch/api/v1/public/search?rows=20&query=" + urllib.parse.quote_plus(t)
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (Berufsliste-Recherche)"})
        try:
            d = json.load(urllib.request.urlopen(req, timeout=30))
            out["gruppen"][g][t] = {"treffer_total": d.get("total_hits") or d.get("num_pages"), "titel": [x["title"] for x in d["documents"]]}
        except Exception as e:
            out["gruppen"][g][t] = {"fehler": str(e)}
        time.sleep(1.2)
    print(g, "ok", flush=True)
json.dump(out, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
