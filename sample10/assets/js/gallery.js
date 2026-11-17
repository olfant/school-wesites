/* Gallery: render, category filter, lightbox with prev/next */
(function () {
  'use strict';
  var S = window.SCHOOL || {};

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    var grid = document.getElementById('galleryGrid');
    if (!grid) return;
    var root = document.body.getAttribute('data-root') || '';
    var base = root + 'assets/img/';
    var limit = parseInt(grid.getAttribute('data-limit'), 10) || 0;
    var fixedCat = grid.getAttribute('data-cat') || '';
    var all = (S.gallery || []).filter(function (g) { return !fixedCat || g.cat === fixedCat; });
    if (limit) all = all.slice(0, limit);

    grid.innerHTML = all.map(function (g, i) {
      return '<div class="gal-wrap ' + esc(g.size || '') + '" data-cat="' + esc(g.cat) + '">' +
        '<button type="button" class="gal-item" data-i="' + i + '" aria-label="Open image: ' + esc(g.cap) + '">' +
        '<span class="lab">' + esc(g.cat) + '</span>' +
        '<img src="' + base + esc(g.src) + '" alt="' + esc(g.cap) + '" loading="lazy">' +
        '<span class="cap">' + esc(g.cap) + '</span></button></div>';
    }).join('');

    var visible = all.slice();
    var current = 0;
    var lb = document.getElementById('lightbox');
    var lbImg = document.getElementById('lbImg');
    var lbCap = document.getElementById('lbCap');
    var lastFocus = null;

    function filter(cat) {
      grid.querySelectorAll('.gal-wrap').forEach(function (w) {
        w.classList.toggle('hide', cat !== 'All' && w.getAttribute('data-cat') !== cat);
      });
      visible = all.filter(function (g) { return cat === 'All' || g.cat === cat; });
    }
    document.querySelectorAll('.gal-filter').forEach(function (b) {
      b.addEventListener('click', function () {
        document.querySelectorAll('.gal-filter').forEach(function (x) { x.classList.remove('active'); x.setAttribute('aria-pressed', 'false'); });
        b.classList.add('active'); b.setAttribute('aria-pressed', 'true');
        filter(b.getAttribute('data-cat'));
      });
    });

    function show(i) {
      if (!visible.length) return;
      current = (i + visible.length) % visible.length;
      var g = visible[current];
      lbImg.src = base + g.src; lbImg.alt = g.cap;
      lbCap.textContent = g.cat + ' — ' + g.cap + '  (' + (current + 1) + '/' + visible.length + ')';
    }
    function open(g) {
      lastFocus = document.activeElement;
      var idx = visible.indexOf(g);
      show(idx < 0 ? 0 : idx);
      lb.classList.add('open'); lb.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
      lb.querySelector('.lb-close').focus();
    }
    function close() {
      lb.classList.remove('open'); lb.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
      if (lastFocus) lastFocus.focus();
    }

    grid.addEventListener('click', function (e) {
      var btn = e.target.closest('.gal-item');
      if (btn) open(all[parseInt(btn.getAttribute('data-i'), 10)]);
    });
    if (lb) {
      lb.querySelector('.lb-close').addEventListener('click', close);
      lb.querySelector('.lb-prev').addEventListener('click', function () { show(current - 1); });
      lb.querySelector('.lb-next').addEventListener('click', function () { show(current + 1); });
      lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
      document.addEventListener('keydown', function (e) {
        if (!lb.classList.contains('open')) return;
        if (e.key === 'Escape') close();
        else if (e.key === 'ArrowLeft') show(current - 1);
        else if (e.key === 'ArrowRight') show(current + 1);
      });
    }
  });
})();
