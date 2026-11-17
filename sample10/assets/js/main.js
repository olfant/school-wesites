/* Global interactions */
(function () {
  'use strict';
  document.documentElement.classList.remove('no-js');

  function safeGet(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function safeSet(k, v) { try { localStorage.setItem(k, v); } catch (e) { /* ignore */ } }

  // Active navigation highlighting
  function markActiveNav() {
    var page = document.body.getAttribute('data-page');
    if (!page) return;
    document.querySelectorAll('[data-nav]').forEach(function (el) {
      if (el.getAttribute('data-nav') === page) {
        el.classList.add('active');
        el.setAttribute('aria-current', 'page');
        var parent = el.closest('.dropdown');
        if (parent) {
          var t = parent.querySelector('.nav-link.dropdown-toggle');
          if (t) t.classList.add('active');
        }
      }
    });
  }

  // Font size A- / A / A+
  function initFontSize() {
    var scale = parseFloat(safeGet('fsScale')) || 1;
    function apply(s) {
      scale = Math.min(1.3, Math.max(0.85, s));
      document.documentElement.style.setProperty('--fs-scale', scale);
      safeSet('fsScale', scale);
    }
    apply(scale);
    document.querySelectorAll('[data-fs]').forEach(function (b) {
      b.addEventListener('click', function () {
        var a = b.getAttribute('data-fs');
        if (a === 'down') apply(scale - 0.1);
        else if (a === 'up') apply(scale + 0.1);
        else apply(1);
      });
    });
  }

  // Back to top
  function initBackTop() {
    var btn = document.getElementById('backTop');
    if (!btn) return;
    window.addEventListener('scroll', function () {
      btn.classList.toggle('show', window.scrollY > 400);
    }, { passive: true });
    btn.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: 'smooth' }); });
  }

  // Smooth scroll for in-page anchors
  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(function (a) {
      a.addEventListener('click', function (e) {
        var id = a.getAttribute('href');
        if (id.length < 2) return;
        var t = document.querySelector(id);
        if (t) { e.preventDefault(); t.scrollIntoView({ behavior: 'smooth' }); }
      });
    });
  }

  // Scroll reveal
  function initReveal() {
    var els = document.querySelectorAll('.reveal,.reveal-left');
    if (!('IntersectionObserver' in window)) { els.forEach(function (e) { e.classList.add('in'); }); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { threshold: 0.12 });
    els.forEach(function (e) { io.observe(e); });
  }

  // Copyright year
  function initYear() {
    document.querySelectorAll('.js-year').forEach(function (e) { e.textContent = new Date().getFullYear(); });
  }

  // Contact form validation + mailto fallback
  function initContactForm() {
    var form = document.getElementById('contactForm');
    if (!form) return;
    var status = document.getElementById('formStatus');
    var emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    function setErr(id, msg) {
      var el = document.getElementById(id);
      var err = document.getElementById(id + 'Err');
      if (!el || !err) return;
      err.textContent = msg;
      el.classList.toggle('is-invalid', !!msg);
      el.setAttribute('aria-invalid', msg ? 'true' : 'false');
    }
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var name = form.cName.value.trim(), email = form.cEmail.value.trim();
      var subject = form.cSubject.value.trim(), message = form.cMessage.value.trim();
      var ok = true;
      setErr('cName', name.length < 2 ? 'Please enter your name (min 2 characters).' : ''); if (name.length < 2) ok = false;
      setErr('cEmail', !emailRe.test(email) ? 'Please enter a valid email address.' : ''); if (!emailRe.test(email)) ok = false;
      setErr('cSubject', subject.length < 3 ? 'Please enter a subject (min 3 characters).' : ''); if (subject.length < 3) ok = false;
      setErr('cMessage', message.length < 10 ? 'Please write a message (min 10 characters).' : ''); if (message.length < 10) ok = false;
      if (!ok) {
        status.className = 'demo-note mt-3';
        status.textContent = 'Please correct the highlighted fields.';
        return;
      }
      var body = 'Name: ' + name + '\nEmail: ' + email + '\n\n' + message;
      var href = 'mailto:' + window.SCHOOL.email + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
      status.className = 'demo-note mt-3';
      status.innerHTML = 'No backend is connected. Your email app should open with a prepared message. If it does not, <a href="' + href + '">click here to send by email</a>.';
      window.location.href = href;
    });
  }

  // Offcanvas: close when a leaf link is chosen
  function initMobileNav() {
    var oc = document.getElementById('mainMenu');
    if (!oc || !window.bootstrap) return;
    oc.querySelectorAll('a.nav-link:not(.dropdown-toggle), a.dropdown-item').forEach(function (a) {
      a.addEventListener('click', function () {
        var inst = window.bootstrap.Offcanvas.getInstance(oc);
        if (inst && window.innerWidth < 1200) inst.hide();
      });
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    markActiveNav(); initFontSize(); initBackTop(); initSmoothScroll();
    initReveal(); initYear(); initContactForm(); initMobileNav();
  });
})();
