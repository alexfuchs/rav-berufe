/* Berufsliste: gruppiert nach Berufsfeld > Unterfeld > Beruf. Suche, Filter, alles öffnen/schliessen, CSV-Export. */
(function(){
  var d = document, $ = function(s){ return d.querySelector(s); };
  var out = $('#out'), q = $('#q'), chips = $('#chips'), info = $('#info'), toggleBtn = $('#toggle');
  var data = null, active = null, allOpen = false;

  function esc(s){ return String(s == null ? '' : s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'); }
  function norm(s){ return String(s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, ''); }
  function byIdOf(list){ var m = {}; list.forEach(function(x){ m[x.id] = x; }); return m; }

  function hay(b){
    return norm([].concat(b.de || [], b.fr || [], b.it || [], b.en || [], b.en_esco || [], [b.gruppe, b.isco08, b.isco08_en, b.ch_isco19, b.unterfeld, b.niveau]).join(' | '));
  }
  function hl(text, term){
    var t = esc(text);
    if (!term) return t;
    var n = norm(text), i = n.indexOf(term);
    if (i < 0 || n.length !== String(text).length) return t;
    var s = String(text);
    return esc(s.slice(0, i)) + '<mark>' + esc(s.slice(i, i + term.length)) + '</mark>' + esc(s.slice(i + term.length));
  }
  function ul(items){ return items.length ? '<ul>' + items.map(function(x){ return '<li>' + x + '</li>'; }).join('') + '</ul>' : '<span class="none">–</span>'; }

  function jobHtml(b, byId, term, open){
    var de = (b.de || []).map(function(x){ return hl(x, term); });
    var fi = (b.fr || []).map(function(x){ return hl(x, term) + ' <small>(fr)</small>'; }).concat((b.it || []).map(function(x){ return hl(x, term) + ' <small>(it)</small>'; }));
    var fiHtml = fi.length ? '<details class="srcs"' + (term ? ' open' : '') + '><summary>Französisch, Italienisch (' + fi.length + ')</summary>' + ul(fi) + '</details>' : '';
    var en = (b.en || []).map(function(x){ return hl(x, term); }).concat((b.en_esco || []).map(function(x){ return hl(x, term) + ' <small>(ESCO)</small>'; }));
    var nb = (b.nachbarn || []).map(function(n){
      var t = byId[n.id]; var label = t ? (t.gruppe || (t.de && t.de[0])) : n.id;
      return '<a href="#' + esc(n.id) + '" data-go="' + esc(n.id) + '">' + esc(label) + '</a>' + (n.grund ? ' <small>(' + esc(n.grund) + ')</small>' : '');
    }).concat((b.nachbar_felder || []).map(function(n){
      var c = data.cluster.filter(function(x){ return x.id === n.id; })[0];
      return 'Feld: <a href="#c-' + esc(n.id) + '" data-go="c-' + esc(n.id) + '">' + esc(c ? c.de : n.id) + '</a>' + (n.grund ? ' <small>(' + esc(n.grund) + ')</small>' : '');
    }));
    var srcs = (b.quellen || []).length ? '<details class="srcs"><summary>Quellen (' + b.quellen.length + ')</summary><ul>' + b.quellen.map(function(x){ return '<li>' + esc(x) + '</li>'; }).join('') + '</ul></details>' : '';
    var preview = (b.de || []).slice(0, 4).join(' · ');
    var code = b.ch_isco19 || b.isco08 || '–';
    return '<details class="job" id="' + esc(b.id) + '"' + (open ? ' open' : '') + '><summary>' +
      '<span class="caret" aria-hidden="true">›</span><span class="code">' + esc(code) + '</span><span class="gn">' + hl(b.gruppe || (b.de && b.de[0]) || b.id, term) + '</span>' +
      '<span class="pv">' + esc(preview) + '</span></summary>' +
      '<div class="job-body">' +
        '<div class="col"><h4>Amtlich / Deutsch</h4>' + ul(de) + fiHtml + (b.anzahl_titel ? '<span class="src">Auswahl aus ' + b.anzahl_titel + ' amtlichen Titeln</span>' : '') + '</div>' +
        '<div class="col"><h4>English</h4>' + ul(en) + '</div>' +
        '<div class="job-foot"><div class="col"><h4>Nachbarn</h4>' + (nb.length ? ul(nb) : '<span class="none">–</span>') + (b.quereinstieg ? '<span class="src">Quereinstieg: ' + esc(b.quereinstieg) + '</span>' : '') + '</div>' +
        '<div class="col"><h4>Einordnung</h4><span class="src">CH-ISCO-19: ' + esc(b.ch_isco19 || '–') + '</span><span class="src">ISCO-08: ' + esc(b.isco08 || '–') + (b.isco08_en ? ' (' + esc(b.isco08_en) + ')' : '') + '</span>' + (b.niveau ? '<span class="src">' + esc(b.niveau) + '</span>' : '') + srcs + '</div></div>' +
      '</div></details>';
  }

  function render(){
    if (!data) return;
    var term = norm(q.value.trim()), byId = byIdOf(data.berufe), shown = 0, html = '';
    var populated = data.cluster.filter(function(c){ return data.berufe.some(function(b){ return b.cluster === c.id; }); }).length;
    data.cluster.forEach(function(c){
      if (active && active !== c.id) return;
      var all = data.berufe.filter(function(b){ return b.cluster === c.id; });
      var jobs = all.filter(function(b){ return !term || hay(b).indexOf(term) >= 0; });
      if (term && !jobs.length) return;
      if (!all.length) {
        html += '<div class="field empty" id="c-' + esc(c.id) + '"><div class="eh"><h2>' + esc(c.de) + '</h2><span class="cnt">noch leer</span></div></div>';
        return;
      }
      shown += jobs.length;
      var fieldOpen = !!term || !!active || populated <= 2;
      var rel = (c.verwandt || []).map(function(r){
        var t = data.cluster.filter(function(x){ return x.id === r.id; })[0];
        return '<a href="#c-' + esc(r.id) + '" data-go="c-' + esc(r.id) + '" title="' + esc(r.grund) + '">' + esc(t ? t.de : r.id) + '</a>';
      }).join('');
      var order = (c.unterfelder || []).slice();
      jobs.forEach(function(b){ if (order.indexOf(b.unterfeld || '') < 0) order.push(b.unterfeld || ''); });
      var subsHtml = order.map(function(s){
        var js = jobs.filter(function(b){ return (b.unterfeld || '') === s; });
        if (!js.length) return '';
        return '<details class="sub-g"' + ((term || active || allOpen) ? ' open' : '') + '><summary><span class="caret" aria-hidden="true">›</span><h3>' + esc(s || 'Weitere') + '</h3><span class="cnt">' + js.length + ' ' + (js.length === 1 ? 'Gruppe' : 'Gruppen') + '</span></summary>' +
          js.map(function(b){ return jobHtml(b, byId, term, allOpen || (!!term && js.length <= 3)); }).join('') + '</details>';
      }).join('');
      html += '<details class="field" id="c-' + esc(c.id) + '"' + ((fieldOpen || allOpen) ? ' open' : '') + '><summary><span class="caret" aria-hidden="true">›</span><h2>' + esc(c.de) + '</h2><span class="en">' + esc(c.en) + '</span><span class="cnt">' + jobs.length + (term ? ' von ' + all.length : '') + ' Gruppen</span></summary>' +
        '<div class="field-body">' + (c.beschreibung ? '<p class="desc">' + esc(c.beschreibung) + '</p>' : '') + (rel ? '<div class="rel">Verwandte Felder: ' + rel + '</div>' : '') + subsHtml + '</div></details>';
    });
    out.innerHTML = html || '<p class="none">Keine Treffer.</p>';
    info.textContent = shown + (shown === 1 ? ' Berufsgruppe angezeigt' : ' Berufsgruppen angezeigt') + ' · ' + data.berufe.length + ' erfasst · Stand ' + data.meta.stand + ' (' + data.meta.version + ')';
  }

  function drawChips(){
    var n = {}; data.berufe.forEach(function(b){ n[b.cluster] = (n[b.cluster] || 0) + 1; });
    chips.innerHTML = '<button class="chip" type="button" aria-pressed="true" data-id="">Alle</button>' + data.cluster.map(function(c){
      return '<button class="chip' + (n[c.id] ? '' : ' zero') + '" type="button" aria-pressed="false" data-id="' + esc(c.id) + '">' + esc(c.de) + '<small>' + (n[c.id] || 0) + '</small></button>';
    }).join('');
    chips.addEventListener('click', function(e){
      var b = e.target.closest('.chip'); if (!b) return;
      active = b.getAttribute('data-id') || null;
      chips.querySelectorAll('.chip').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      render();
    });
  }

  /* Sprung zu einem Beruf oder Feld: Eltern öffnen, dann scrollen */
  function goTo(id){
    var el = d.getElementById(id); if (!el) return;
    for (var p = el; p; p = p.parentElement) if (p.tagName === 'DETAILS') p.open = true;
    el.scrollIntoView({block:'start'});
    el.classList.remove('flash'); void el.offsetWidth; el.classList.add('flash');
    if (history.replaceState) history.replaceState(null, '', '#' + id);
  }
  out.addEventListener('click', function(e){
    var a = e.target.closest('a[data-go]'); if (!a) return;
    e.preventDefault();
    var id = a.getAttribute('data-go');
    if (!d.getElementById(id)) { active = null; q.value = ''; chips.querySelectorAll('.chip').forEach(function(x){ x.setAttribute('aria-pressed', x.getAttribute('data-id') ? 'false' : 'true'); }); render(); }
    goTo(id);
  });

  toggleBtn.addEventListener('click', function(){
    allOpen = !allOpen;
    out.querySelectorAll('details').forEach(function(x){ x.open = allOpen; });
    toggleBtn.textContent = allOpen ? 'Alles schliessen' : 'Alles öffnen';
  });

  /* Drucken: alles aufklappen, danach Zustand zurück */
  var wasOpen = [];
  window.addEventListener('beforeprint', function(){ wasOpen = []; out.querySelectorAll('details').forEach(function(x){ wasOpen.push([x, x.open]); x.open = true; }); });
  window.addEventListener('afterprint', function(){ wasOpen.forEach(function(p){ p[0].open = p[1]; }); });

  function csv(){
    var rows = [['Berufsfeld','Unterfeld','Gruppe','ISCO-08','CH-ISCO-19','Deutsch','Franzoesisch','Italienisch','English','English (ESCO)','Niveau','Quellen']];
    data.berufe.forEach(function(b){
      var c = data.cluster.filter(function(x){ return x.id === b.cluster; })[0];
      rows.push([c ? c.de : b.cluster, b.unterfeld, b.gruppe, b.isco08, b.ch_isco19, (b.de||[]).join(' | '), (b.fr||[]).join(' | '), (b.it||[]).join(' | '), (b.en||[]).join(' | '), (b.en_esco||[]).join(' | '), b.niveau, (b.quellen||[]).join(' | ')]);
    });
    var t = rows.map(function(r){ return r.map(function(v){ return '"' + String(v == null ? '' : v).replace(/"/g,'""') + '"'; }).join(';'); }).join('\r\n');
    var a = d.createElement('a'); a.href = URL.createObjectURL(new Blob(['﻿' + t], {type:'text/csv;charset=utf-8'})); a.download = 'berufsliste.csv';
    d.body.appendChild(a); a.click(); a.remove();
  }

  q.addEventListener('input', render);
  $('#csv').addEventListener('click', function(){ if (data) csv(); });
  fetch('assets/berufe.json').then(function(r){ return r.json(); }).then(function(j){
    data = j; $('#hint').textContent = j.meta.hinweis || ''; $('#notice').hidden = !j.meta.hinweis; drawChips(); render();
    if (location.hash.length > 1) goTo(location.hash.slice(1));
  }).catch(function(){ out.innerHTML = '<p class="none">Die Berufsdaten konnten nicht geladen werden.</p>'; });
})();
