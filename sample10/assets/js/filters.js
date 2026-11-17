/* Notice board + examination results filtering */
(function () {
  'use strict';
  var S = window.SCHOOL || {};

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  /* ---------- Notices ---------- */
  function initNotices() {
    var list = document.getElementById('noticeList');
    if (!list) return;
    var prefix = document.body.getAttribute('data-root') || '';
    var empty = document.getElementById('noticeEmpty');
    var search = document.getElementById('noticeSearch');
    var buttons = document.querySelectorAll('.notice-filter');
    var viewAll = document.getElementById('noticeViewAll');
    var limit = parseInt(list.getAttribute('data-limit'), 10) || 4;
    var showAll = false, cat = 'All';

    function render() {
      var q = (search ? search.value : '').trim().toLowerCase();
      var items = (S.notices || []).filter(function (n) {
        var okCat = cat === 'All' || n.cat === cat;
        var okQ = !q || (n.title + ' ' + n.desc + ' ' + n.cat).toLowerCase().indexOf(q) > -1;
        return okCat && okQ;
      });
      var shown = showAll ? items : items.slice(0, limit);
      list.innerHTML = shown.map(function (n) {
        return '<article class="notice-item"><div class="notice-date">' + esc(n.date) + '</div><div>' +
          '<span class="chip">' + esc(n.cat) + '</span> <span class="placeholder-tag">SAMPLE</span>' +
          '<h3>' + esc(n.title) + '</h3><p class="mb-1">' + esc(n.desc) + '</p>' +
          '<a href="' + prefix + esc(n.link) + '" class="fw-bold">Read More →</a></div></article>';
      }).join('');
      if (empty) empty.hidden = items.length > 0;
      if (viewAll) {
        viewAll.hidden = items.length <= limit;
        viewAll.textContent = showAll ? 'Show Fewer' : 'View All';
      }
    }
    buttons.forEach(function (b) {
      b.addEventListener('click', function () {
        buttons.forEach(function (x) { x.classList.remove('active'); x.setAttribute('aria-pressed', 'false'); });
        b.classList.add('active'); b.setAttribute('aria-pressed', 'true');
        cat = b.getAttribute('data-cat');
        render();
      });
    });
    if (search) search.addEventListener('input', render);
    if (viewAll) viewAll.addEventListener('click', function () { showAll = !showAll; render(); });
    render();
  }

  /* ---------- Results ---------- */
  function initResults() {
    var body = document.getElementById('resultBody');
    if (!body) return;
    var msg = document.getElementById('resultMessage');
    var exam = document.getElementById('resExam');
    var session = document.getElementById('resSession');
    var klass = document.getElementById('resClass');
    var search = document.getElementById('resSearch');
    var docs = document.getElementById('resultDocs');
    var records = S.results || [];

    function fillSelect(sel, key) {
      if (!sel) return;
      var vals = [];
      records.forEach(function (r) { if (vals.indexOf(r[key]) < 0) vals.push(r[key]); });
      vals.forEach(function (v) { var o = document.createElement('option'); o.value = v; o.textContent = v; sel.appendChild(o); });
    }
    fillSelect(exam, 'exam'); fillSelect(session, 'session'); fillSelect(klass, 'class');

    function render() {
      var q = (search ? search.value : '').trim().toLowerCase();
      var rows = records.filter(function (r) {
        return (!exam || !exam.value || r.exam === exam.value) &&
          (!session || !session.value || r.session === session.value) &&
          (!klass || !klass.value || r.class === klass.value) &&
          (!q || JSON.stringify(r).toLowerCase().indexOf(q) > -1);
      });
      body.innerHTML = rows.map(function (r, i) {
        return '<tr><td>' + (i + 1) + '</td><td>' + esc(r.exam) + '</td><td>' + esc(r.session) + '</td><td>' + esc(r.class) + '</td><td>' + esc(r.title || '') + '</td><td>' +
          (r.file ? '<a href="' + esc(r.file) + '">Open</a>' : '—') + '</td></tr>';
      }).join('');
      if (msg) msg.hidden = rows.length > 0;
    }
    [exam, session, klass].forEach(function (el) { if (el) el.addEventListener('change', render); });
    if (search) search.addEventListener('input', render);

    if (docs) {
      var d = S.resultDocuments || [];
      docs.innerHTML = d.length ? d.map(function (x) {
        return '<li><a href="' + esc(x.file) + '">' + esc(x.title) + '</a></li>';
      }).join('') : '<li class="placeholder-tag">No verified result documents uploaded yet. Add files to assets/documents/results/ and list them in site-data.js.</li>';
    }
    render();
  }

  document.addEventListener('DOMContentLoaded', function () { initNotices(); initResults(); });
})();
