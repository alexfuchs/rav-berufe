# Erzeugt aus BFS-Zuweisungsschlüssel + ISCO-08-Namen (ESCO) die Feld-Konfigurationen field_<cluster>_auto.py für alle noch leeren Felder.
import json, sys, collections, openpyxl, re
sys.stdout.reconfigure(encoding='utf-8')
names = json.load(open('../_quellen/isco08-namen.json', encoding='utf-8'))
d = json.load(open('../assets/berufe.json', encoding='utf-8'))
done = {b['ch_isco19'] for b in d['berufe']}
rows = list(openpyxl.load_workbook('../_quellen/do-t-00.07-ch-isco-19-02.xlsx', read_only=True)['V1.2_102022'].iter_rows(values_only=True))[1:]
by = collections.defaultdict(list)
for r in rows:
    if r[13] and r[11] == 1: by[str(r[13])].append(r)

# Zuordnung ISCO-08 / CH-ISCO-19 (Präfix) -> (Feld, Unterfeld); längster Präfix gewinnt
M = {}
def m(cl, uf, *codes):
    for c in codes: M[c] = (cl, uf)

m('recht', 'Leitung & Geschäftsführung', '10', '11', '12', '13', '-999')
m('finanzen', 'Leitung Finanz & Versicherung', '1211', '1346')
m('recht', 'Personal, Strategie & Organisation', '1212', '1213', '1219', '1120', '1349', '1300', '12100')
m('handel', 'Leitung Verkauf & Handel', '1221', '1420')
m('medien', 'Marketing & Kommunikation', '1222')
m('wissenschaft', 'Leitung Forschung', '1223')
m('landwirtschaft', 'Leitung Land- & Forstwirtschaft', '1311', '1312')
m('industrie', 'Leitung Produktion', '1321', '1322', '13200')
m('bau', 'Leitung Bau', '1323')
m('logistik', 'Leitung Logistik', '1324')
m('gesundheit', 'Leitung Gesundheit', '1342', '13400')
m('soziales', 'Leitung Soziales & Bildung', '1341', '1343', '1344', '1345')
m('technik', 'Leitung Technik', '13000')
m('gastro', 'Leitung Gastgewerbe & Freizeit', '1411', '1412', '1431', '1439')
m('sicherheit', 'Streitkräfte', '01', '02', '03')
m('sicherheit', 'Behörden & Politik', '1111', '1112', '1114')
m('wissenschaft', 'Naturwissenschaften', '2111', '2112', '2113', '2114', '2120', '2131', '2133', '21000', '2100')
m('landwirtschaft', 'Beratung & Technik', '2132', '3142', '3143')
m('technik', 'Ingenieurwesen & Technik', '2143', '2149', '2151', '2152', '2153', '2165', '21400', '20000', '2000', '31', '3118', '3119', '3113', '3114', '30', '3100')
m('industrie', 'Ingenieurwesen & Produktionstechnik', '2141', '2145', '2146', '3115', '3116', '3117', '3121', '3122', '31200', '31300', '2144')
m('bau', 'Ingenieurwesen, Architektur & Planung', '2142', '2161', '2162', '2164', '3112', '3123')
m('medien', 'Design & Gestaltung', '2163', '2166', '3432')
m('gesundheit', 'Medizin, Therapie & Assistenz', '22', '3211', '3212', '3213', '3214', '3221', '3222', '3230', '3240', '3251', '3252', '3253', '3254', '3255', '3256', '3258', '3259', '5321', '5322', '5329', '2634')
m('gesundheit', 'Sport & Fitness', '3421', '3422', '3423')
m('gesundheit', 'Körperpflege & Wellness', '5141', '5142')
m('sicherheit', 'Kontrolle & Inspektion', '3257')
m('soziales', 'Bildung & Erziehung', '23', '5311', '5312', '23000')
m('soziales', 'Soziale Arbeit & Seelsorge', '2635', '2636', '3412', '3413')
m('finanzen', 'Finanzen, Versicherung & Analyse', '2411', '2412', '2413', '3311', '3312', '3313', '3314', '3315', '3321', '33100')
m('recht', 'Beratung, Organisation & Personal', '2421', '2422', '2423', '2424', '24000', '3333')
m('medien', 'Marketing & Kommunikation', '2431', '2432')
m('handel', 'Verkauf, Einkauf & Vermittlung', '2433', '3322', '3323', '3324', '3334', '3339', '33000', '33300', '50000')
m('it', 'Informatik (Ergänzung)', '25', '2519', '25000')
m('recht', 'Recht & Justiz', '2611', '2612', '2619', '26100', '2600', '3411')
m('wissenschaft', 'Geistes- und Sozialwissenschaften', '2631', '2632', '2633', '26300', '26000', '2630')
m('medien', 'Kultur, Archiv & Bibliothek', '2621', '2622', '3433', '73100')
m('medien', 'Schreiben, Sprache & Übersetzung', '2641', '2642', '2643')
m('medien', 'Kunst, Musik & Darstellung', '2651', '2652', '2653', '2654', '2655', '2656', '2659', '2650', '26500', '3435', '5241', '3431')
m('medien', 'Ton, Bild & Druck', '3521', '7321', '7322', '7323')
m('gastro', 'Veranstaltung & Küche', '3332', '3434')
m('logistik', 'Spedition & Verkehrsleitung', '3331', '3151', '3152', '3153', '3154', '3155', '31500')
m('sicherheit', 'Verwaltung, Zoll & Polizei', '3351', '3352', '3353', '3354', '3355', '3359', '5411', '5412', '5413', '5414', '5419')
m('buero', 'Sachbearbeitung (Ergänzung)', '4000', '40000')
m('logistik', 'Material, Transport & Post', '4320', '4321', '4322', '4323', '4412', '43200', '8311', '8312', '8321', '8322', '8331', '8332', '8344', '8350', '83000', '9331', '9332', '9333', '9621', '9623')
m('gastro', 'Reise, Küche & Service', '5111', '5112', '5113', '5120', '5131', '5132', '5246', '9411', '9412')
m('reinigung', 'Reinigung & Hauswirtschaft', '5151', '5152', '5153', '9111', '9112', '9121', '9122', '9123', '9129', '9611', '9612', '9613', '9622', '9629', '96100', '7544')
m('reinigung', 'Persönliche Dienste', '5161', '5162', '5163', '5164', '5165', '5169')
m('handel', 'Verkauf & Kasse', '5211', '5212', '5221', '5222', '5223', '5230', '5242', '5243', '5244', '5245', '5249', '9334', '9510', '9520')
m('landwirtschaft', 'Landwirtschaft, Gartenbau & Forst', '61', '62', '6224', '8341', '9211', '9212', '9213', '9214', '9215', '9216')
m('bau', 'Rohbau & Ausbau', '7110', '7111', '7112', '7113', '7114', '7115', '7119', '7120', '7121', '7122', '7123', '7124', '7125', '7126', '7127', '7131', '7132', '7133', '71100', '71200', '70000', '7000', '7542', '7541')
m('bau', 'Elektro & Installation', '7411', '7413', '74000')
m('bau', 'Baumaschinen & Hilfsarbeit', '8342', '8343', '9312', '9313', '93100')
m('technik', 'Elektronik & Feinwerk', '7421', '7412')
m('industrie', 'Metall & Maschinen', '72', '7200', '7210', '7211', '7212', '7213', '7214', '7215', '7220', '7221', '7222', '7223', '7224', '7230', '7231', '7232', '7233', '7234')
m('industrie', 'Handwerk & Kunsthandwerk', '7311', '7312', '7313', '7314', '7315', '7316', '7317', '7318', '7319', '7310')
m('industrie', 'Holz, Textil & Leder', '7520', '7521', '7522', '7523', '7530', '7531', '7532', '7533', '7534', '7535', '7536', '75200', '75300')
m('industrie', 'Lebensmittel', '7510', '7511', '7512', '7513', '7514', '7515', '7516', '75100', '94100')
m('industrie', 'Prüfung & übrige Berufe', '7543', '7549')
m('industrie', 'Anlagen & Maschinenbedienung', '3130', '3131', '3132', '3133', '3134', '3135', '3139', '80', '81', '82')
m('industrie', 'Hilfsarbeit Produktion & Bergbau', '90', '9310', '9311', '9321', '9329')

def lookup(g):
    for l in range(len(g), 1, -1):
        if g[:l] in M: return M[g[:l]]
    return None

def q(s): return (s or '').strip()

res = collections.defaultdict(dict); unmapped = []
for g in sorted(by):
    if g in done: continue
    t = lookup(g)
    if not t: unmapped.append(g); continue
    cl, uf = t
    rs = by[g]
    n = names.get(g[:4], {})
    en = n.get('en') or 'Sammelgruppe %s (ohne eigene ISCO-08-Gattung)' % g
    de = (n.get('de') + ' [ESCO-Gruppenname]') if n.get('de') else 'Sammelgruppe: ' + ', '.join(q(r[1]) for r in rs[:2])
    ms = sorted([r for r in rs if r[1]], key=lambda r: (r[12] != 1, len(r[1])))
    jq = []
    for r in ms:
        x = re.sub(r'\b(dipl\.|eidg\.|Dr\.|HF|FH|EFZ|EBA|ETH|HTL|HFG)\b|\(.*?\)|,.*', '', r[1]).strip()
        if x and len(x) > 3 and x.lower() not in [j.lower() for j in jq]: jq.append(x)
        if len(jq) == 3: break
    ens = [q(r[7]) for r in ms if q(r[7]) and ',' not in q(r[7]) and len(q(r[7])) > 3]
    eqs = [ens[0].lower()] if ens else []
    if ens and ens[0] not in jq: jq.append(ens[0])
    res[cl][g] = (uf, g[:4] if g[:4] in names and names[g[:4]].get('en') else g[:3], en, de, eqs, jq)
print('nicht zugeordnet:', unmapped)

BES = {'technik': 'Ingenieurwesen und technische Berufe ausserhalb IT, Bau und Produktion.', 'industrie': 'Metall, Maschinen, Lebensmittelherstellung, Holz, Textil, Anlagen- und Maschinenbedienung, Produktionshilfen.', 'bau': 'Hoch- und Tiefbau, Ausbau, Installation, Planung und Baumaschinen.', 'gesundheit': 'Medizin, Pflege, Therapie, Assistenzberufe, Sport und Körperpflege.', 'soziales': 'Erziehung, Unterricht, soziale Arbeit, Betreuung.', 'finanzen': 'Banken, Versicherungen, Finanzanalyse, Treuhand.', 'handel': 'Detailhandel, Kasse, Vertrieb, Einkauf, Vermittlung.', 'gastro': 'Küche, Service, Hotellerie, Reise, Veranstaltungen.', 'logistik': 'Transport, Lager, Post, Schiene, Luftfahrt, Schiff, Spedition.', 'sicherheit': 'Polizei, Feuerwehr, Armee, Verwaltung, Zoll, Justizvollzug, Politik.', 'landwirtschaft': 'Landwirtschaft, Gartenbau, Forst, Fischerei.', 'medien': 'Journalismus, Gestaltung, Kunst, Kultur, Druck, Marketing und Kommunikation.', 'recht': 'Recht, Unternehmensführung, Beratung, Personal.', 'reinigung': 'Reinigung, Hauswirtschaft, Abfall, persönliche Dienste.', 'wissenschaft': 'Naturwissenschaften, Geistes- und Sozialwissenschaften, Forschung.', 'it': '', 'buero': ''}
PRE = {'technik': 'te', 'industrie': 'in', 'bau': 'ba', 'gesundheit': 'ge', 'soziales': 'so', 'finanzen': 'fi', 'handel': 'ha', 'gastro': 'ga', 'logistik': 'lo', 'sicherheit': 'si', 'landwirtschaft': 'la', 'medien': 'me', 'recht': 're', 'reinigung': 'rg', 'wissenschaft': 'wi', 'it': 'itx', 'buero': 'bux'}
for cl, G in res.items():
    ufs = list(dict.fromkeys(v[0] for v in G.values()))
    append = cl in ('it', 'buero')
    s = "# Automatisch erzeugt (gen_fields.py) aus BFS-Zuweisungsschlüssel V1.2 und ESCO-ISCO-Gruppennamen\nCLUSTER = %r\nPREFIX = %r\nAPPEND = %r\nBESCHREIBUNG = %r\nUNTERFELDER = %r\nW = 'auto'\nNF = {}\nG = {\n" % (cl, PRE[cl], append, (BES[cl] + ' ' if BES[cl] else '') + 'Basis: CH-ISCO-19, zugeordnet nach ISCO-08-Gruppen; Gruppennamen aus ESCO (de).', ufs)
    for g, v in G.items(): s += '%r: %r,\n' % (g, v)
    s += '}\n'
    open('field_%s_auto.py' % cl, 'w', encoding='utf-8').write(s)
    print(cl, len(G), 'Gruppen', len(ufs), 'Unterfelder')
