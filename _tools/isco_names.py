# Holt ISCO-08-Gruppennamen (en, de) für alle in CH-ISCO-19 vorkommenden Codes aus der ESCO-API.
import json, sys, time, urllib.request, openpyxl
sys.stdout.reconfigure(encoding='utf-8')
wb = openpyxl.load_workbook('../_quellen/do-t-00.07-ch-isco-19-02.xlsx', read_only=True)
rows = list(wb['V1.2_102022'].iter_rows(values_only=True))[1:]
codes = sorted({str(r[13])[:4] for r in rows if r[13] and r[11] == 1 and str(r[13]).isdigit()})
out = {}
def get(u):
    return json.load(urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0 (Berufsliste-Recherche)'}), timeout=30))
for c in codes:
    o = {}
    for l in ('en', 'de'):
        try: o[l] = get('https://ec.europa.eu/esco/api/resource/concept?language=%s&uri=http://data.europa.eu/esco/isco/C%s' % (l, c))['title']
        except Exception as e: o[l] = None
        time.sleep(0.25)
    out[c] = o
json.dump(out, open('../_quellen/isco08-namen.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), sum(1 for v in out.values() if not v['en']), 'ohne en')
