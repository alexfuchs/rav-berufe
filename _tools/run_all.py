# Startet collect_multi.py für alle *_auto-Felder in 5 parallelen Strängen (Pausen pro Anfrage bleiben bestehen).
import glob, os, subprocess, sys, threading
os.chdir(os.path.dirname(os.path.abspath(__file__)))
order = sorted(glob.glob('field_*_auto.py'), key=lambda f: -os.path.getsize(f))
groups = [[] for _ in range(5)]
for i, f in enumerate(order): groups[i % 5].append(f[:-3])
def run(g):
    for m in g:
        with open('../_quellen/collect-%s.log' % m, 'w', encoding='utf-8') as log:
            subprocess.run([sys.executable, 'collect_multi.py', m], stdout=log, stderr=subprocess.STDOUT)
ts = [threading.Thread(target=run, args=(g,)) for g in groups]
[t.start() for t in ts]; [t.join() for t in ts]
print('alle fertig')
