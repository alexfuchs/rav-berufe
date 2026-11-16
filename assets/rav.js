/* Berufsliste: lädt berufe.json, Suche, Filter nach Berufsfeld, Export als CSV. */
(function(){
  var d = document, $ = function(s){ return d.querySelector(s); };
  var out = $('#out'), q = $('#q'), chips = $('#chips'), info = $('#info');
  var data = null, active = null;

  function esc(s){ return String(s == null ? '' : s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'); }
  function norm(s){ return String(s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, ''); }

  function hay(b){
    var w = (b.web || []).map(function(x){ return x.titel; });
    return norm([].concat(b.de || [], b.fr || [], b.it || [], b.en || [], w, [b.isco08, b.ch_isco19, b.unterfeld, b.niveau]).join(' | '));
  }
  function list(arr){ return arr && arr.length ? '<ul>' + arr.map(function(x){ return '<li>' + x + '</li>'; }).join('') + '</ul>' : '<span class="empty">–</span>'; }

  function jobRow(b, byId){
    var de = list((b.de || []).map(esc).concat((b.fr || []).map(function(x){ return esc(x) + ' <small>(fr)</small>'; }), (b.it || []).map(function(x){ return esc(x) + ' <small>(it)</small>'; })));
    var en = list((b.en || []).map(esc));
    var web = list((b.web || []).map(function(x){ return esc(x.titel) + (x.quelle ? '<span class="src">' + esc(x.quelle) + '</span>' : ''); }));
    var nb = (b.nachbarn || []).map(function(n){
      var t = byId[n.id]; var label = t ? (t.de && t.de[0]) : n.id;
      return '<a href="#' + esc(n.id) + '">' + esc(label) + '</a>' + (n.grund ? ' <small>(' + esc(n.grund) + ')</small>' : '');
    });
    var code = (b.ch_isco19 ? 'CH-ISCO-19 ' + esc(b.ch_isco19) + '<br>' : '') + (b.isco08 ? 'ISCO-08 ' + esc(b.isco08) : '');
    return '<tr id="' + esc(b.id) + '">' +
      '<td class="code" data-l="Code">' + (code || '–') + '</td>' +
      '<td data-l="Amtlich / Deutsch">' + de + (b.niveau ? '<span class="src">Niveau: ' + esc(b.niveau) + '</span>' : '') + '</td>' +
      '<td data-l="English">' + en + '</td>' +
      '<td data-l="Im Internet">' + web + '</td>' +
      '<td data-l="Nachbarberufe" class="nb">' + (nb.length ? nb.join('<br>') : '–') + (b.quereinstieg ? '<span class="src">Quereinstieg: ' + esc(b.quereinstieg) + '</span>' : '') + '<br><span class="st ' + esc(b.status) + '">' + esc((b.status || '').replace('_', ' ')) + '</span></td>' +
      '</tr>';
  }

  function render(){
    if (!data) return;
    var term = norm(q.value.trim()), byId = {};
    data.berufe.forEach(function(b){ byId[b.id] = b; });
    var shown = 0, html = '';
    data.cluster.forEach(function(c){
      if (active && active !== c.id) return;
      var jobs = data.berufe.filter(function(b){ return b.cluster === c.id && (!term || hay(b).indexOf(term) >= 0); });
      if (term && !jobs.length) return;
      shown += jobs.length;
      var rel = (c.verwandt || []).map(function(r){
        var t = data.cluster.filter(function(x){ return x.id === r.id; })[0];
        return '<a href="#c-' + esc(r.id) + '" title="' + esc(r.grund) + '">' + esc(t ? t.de : r.id) + '</a>';
      }).join('');
      html += '<section class="cl" id="c-' + esc(c.id) + '"><h2>' + esc(c.de) + '</h2><div class="en">' + esc(c.en) + '</div>' +
        (c.beschreibung ? '<p class="desc">' + esc(c.beschreibung) + '</p>' : '') +
        (rel ? '<div class="rel">Verwandte Felder: ' + rel + '</div>' : '');
      if (!jobs.length) {
        html += '<p class="empty">Noch keine Berufe erfasst. Dieses Feld wird mit dem Prompt befüllt.</p>';
      } else {
        var subs = {}; jobs.forEach(function(b){ (subs[b.unterfeld || ''] = subs[b.unterfeld || ''] || []).push(b); });
        Object.keys(subs).forEach(function(s){
          if (s) html += '<h3 class="sub-h">' + esc(s) + '</h3>';
          html += '<table><thead><tr><th>Code</th><th>Amtlich / Deutsch</th><th>English</th><th>Im Internet</th><th>Nachbarn</th></tr></thead><tbody>' + subs[s].map(function(b){ return jobRow(b, byId); }).join('') + '</tbody></table>';
        });
      }
      html += '</section>';
    });
    out.innerHTML = html || '<p class="empty">Keine Treffer.</p>';
    info.textContent = shown + ' Berufe angezeigt, ' + data.berufe.length + ' erfasst, Stand ' + data.meta.stand + ' (' + data.meta.version + ')';
  }

  function drawChips(){
    var n = {}; data.berufe.forEach(function(b){ n[b.cluster] = (n[b.cluster] || 0) + 1; });
    chips.innerHTML = '<button class="chip" type="button" aria-pressed="true" data-id="">Alle</button>' + data.cluster.map(function(c){
      return '<button class="chip" type="button" aria-pressed="false" data-id="' + esc(c.id) + '">' + esc(c.de) + '<small>' + (n[c.id] || 0) + '</small></button>';
    }).join('');
    chips.addEventListener('click', function(e){
      var b = e.target.closest('.chip'); if (!b) return;
      active = b.getAttribute('data-id') || null;
      chips.querySelectorAll('.chip').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      render();
    });
  }

  function csv(){
    var rows = [['Berufsfeld','Unterfeld','ISCO-08','CH-ISCO-19','Deutsch','Franzoesisch','Italienisch','English','Titel im Internet','Niveau','Status','Quellen']];
    data.berufe.forEach(function(b){
      var c = data.cluster.filter(function(x){ return x.id === b.cluster; })[0];
      rows.push([c ? c.de : b.cluster, b.unterfeld, b.isco08, b.ch_isco19, (b.de||[]).join(' | '), (b.fr||[]).join(' | '), (b.it||[]).join(' | '), (b.en||[]).join(' | '), (b.web||[]).map(function(x){ return x.titel; }).join(' | '), b.niveau, b.status, (b.quellen||[]).join(' | ')]);
    });
    var t = rows.map(function(r){ return r.map(function(v){ return '"' + String(v == null ? '' : v).replace(/"/g,'""') + '"'; }).join(';'); }).join('\r\n');
    var a = d.createElement('a'); a.href = URL.createObjectURL(new Blob(['﻿' + t], {type:'text/csv;charset=utf-8'})); a.download = 'berufsliste.csv';
    d.body.appendChild(a); a.click(); a.remove();
  }

  q.addEventListener('input', render);
  $('#csv').addEventListener('click', function(){ if (data) csv(); });
  fetch('assets/berufe.json').then(function(r){ return r.json(); }).then(function(j){
    data = j; $('#hint').textContent = j.meta.hinweis || ''; $('#notice').hidden = !j.meta.hinweis; drawChips(); render();
  }).catch(function(){ out.innerHTML = '<p class="empty">Die Berufsdaten konnten nicht geladen werden.</p>'; });
})();
