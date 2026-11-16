/**
 * ====================================================================
 * +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय, हल्दीपोखर
 * MAIN INTERACTIVITY JAVASCRIPT ENGINE
 * Version 4 — Cinematic Campus Storytelling Edition
 * ====================================================================
 */

document.addEventListener('DOMContentLoaded', () => {
  initStickyNavigation();
  initMobileDrawer();
  initFontSizeResizer();
  initScrollAnimations();
  initHeroParallax();
  initNoticeSearchAndFilter();
  initResultsFilter();
  initContactFormValidation();
  initBackToTop();
  initActiveNav();
  initAutoYear();
  initFaqAccordion();
});

/* ====================================================================
   1. STICKY NAVIGATION
   ==================================================================== */
function initStickyNavigation() {
  const navBar = document.querySelector('.main-nav-bar');
  if (!navBar) return;

  const handleScroll = () => {
    if (window.scrollY > 80) {
      navBar.classList.add('is-sticky');
    } else {
      navBar.classList.remove('is-sticky');
    }
  };

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();
}

/* ====================================================================
   2. MOBILE SLIDE-IN NAVIGATION DRAWER
   ==================================================================== */
function initMobileDrawer() {
  const toggleBtn = document.querySelector('.mobile-drawer-toggle');
  const drawer = document.querySelector('.mobile-drawer');
  const backdrop = document.querySelector('.mobile-drawer-backdrop');
  const closeBtn = document.querySelector('.mobile-drawer-close');

  if (!toggleBtn || !drawer || !backdrop) return;

  const openDrawer = () => {
    drawer.classList.add('open');
    backdrop.classList.add('active');
    document.body.style.overflow = 'hidden';
  };

  const closeDrawer = () => {
    drawer.classList.remove('open');
    backdrop.classList.remove('active');
    document.body.style.overflow = '';
  };

  toggleBtn.addEventListener('click', openDrawer);
  if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
  backdrop.addEventListener('click', closeDrawer);

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && drawer.classList.contains('open')) {
      closeDrawer();
    }
  });
}

/* ====================================================================
   3. ACCESSIBILITY FONT SIZE ADJUSTMENT (A- / A / A+)
   ==================================================================== */
function initFontSizeResizer() {
  const btns = document.querySelectorAll('.font-resizer-btn');
  if (!btns.length) return;

  const currentSize = localStorage.getItem('school_font_size') || 'md';
  applyFontSize(currentSize);

  btns.forEach(btn => {
    btn.addEventListener('click', () => {
      const size = btn.getAttribute('data-size');
      applyFontSize(size);
      localStorage.setItem('school_font_size', size);
    });
  });

  function applyFontSize(size) {
    document.documentElement.classList.remove('font-size-sm', 'font-size-md', 'font-size-lg');
    document.documentElement.classList.add(`font-size-${size}`);

    btns.forEach(b => {
      if (b.getAttribute('data-size') === size) {
        b.classList.add('active');
      } else {
        b.classList.remove('active');
      }
    });
  }
}

/* ====================================================================
   4. SCROLL REVEAL ANIMATIONS (INTERSECTION OBSERVER)
   ==================================================================== */
function initScrollAnimations() {
  const elements = document.querySelectorAll('.reveal-on-scroll');
  if (!elements.length) return;

  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    elements.forEach(el => el.classList.add('is-revealed'));
    return;
  }

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-revealed');
        obs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });

  elements.forEach(el => observer.observe(el));
}

/* ====================================================================
   5. CINEMATIC HERO BACKGROUND MOVEMENT (SUBTLE TILT)
   ==================================================================== */
function initHeroParallax() {
  const heroSection = document.querySelector('.cinematic-hero-section');
  const heroMedia = document.querySelector('.hero-bg-media');
  if (!heroSection || !heroMedia) return;

  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  heroSection.addEventListener('mousemove', (e) => {
    const { clientX, clientY } = e;
    const { innerWidth, innerHeight } = window;
    const xOffset = ((clientX / innerWidth) - 0.5) * 15;
    const yOffset = ((clientY / innerHeight) - 0.5) * 15;

    heroMedia.style.transform = `scale(1.05) translate(${xOffset}px, ${yOffset}px)`;
  });

  heroSection.addEventListener('mouseleave', () => {
    heroMedia.style.transform = 'scale(1.02) translate(0px, 0px)';
  });
}

/* ====================================================================
   6. NOTICE SEARCH & CATEGORY FILTERING
   ==================================================================== */
function initNoticeSearchAndFilter() {
  const filterBtns = document.querySelectorAll('.notice-filter-btn');
  const searchInput = document.querySelector('.notice-search-input');
  const noticeCards = document.querySelectorAll('.notice-row-card');

  if (!noticeCards.length) return;

  let activeCategory = 'all';
  let searchTerm = '';

  const filterCards = () => {
    noticeCards.forEach(card => {
      const cardCategory = card.getAttribute('data-category') || '';
      const cardText = card.textContent.toLowerCase();

      const matchesCat = (activeCategory === 'all' || cardCategory.toLowerCase() === activeCategory.toLowerCase());
      const matchesSearch = (!searchTerm || cardText.includes(searchTerm));

      if (matchesCat && matchesSearch) {
        card.style.display = 'flex';
      } else {
        card.style.display = 'none';
      }
    });
  };

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      activeCategory = btn.getAttribute('data-category') || 'all';
      filterCards();
    });
  });

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchTerm = e.target.value.toLowerCase().trim();
      filterCards();
    });
  }
}

/* ====================================================================
   7. RESULTS TABLE FILTERING
   ==================================================================== */
function initResultsFilter() {
  const sessionSelect = document.getElementById('resultSessionFilter');
  const classSelect = document.getElementById('resultClassFilter');
  const searchInput = document.getElementById('resultSearchInput');
  const rows = document.querySelectorAll('.result-data-row');

  if (!rows.length) return;

  const applyResultsFilter = () => {
    const selectedSession = sessionSelect ? sessionSelect.value.toLowerCase() : 'all';
    const selectedClass = classSelect ? classSelect.value.toLowerCase() : 'all';
    const query = searchInput ? searchInput.value.toLowerCase().trim() : '';

    rows.forEach(row => {
      const rowSession = (row.getAttribute('data-session') || '').toLowerCase();
      const rowClass = (row.getAttribute('data-class') || '').toLowerCase();
      const rowText = row.textContent.toLowerCase();

      const matchSession = (selectedSession === 'all' || rowSession.includes(selectedSession));
      const matchClass = (selectedClass === 'all' || rowClass.includes(selectedClass));
      const matchSearch = (!query || rowText.includes(query));

      if (matchSession && matchClass && matchSearch) {
        row.style.display = '';
      } else {
        row.style.display = 'none';
      }
    });
  };

  if (sessionSelect) sessionSelect.addEventListener('change', applyResultsFilter);
  if (classSelect) classSelect.addEventListener('change', applyResultsFilter);
  if (searchInput) searchInput.addEventListener('input', applyResultsFilter);
}

/* ====================================================================
   8. CONTACT FORM CLIENT-SIDE VALIDATION
   ==================================================================== */
function initContactFormValidation() {
  const form = document.getElementById('schoolContactForm');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    let isValid = true;
    const requiredInputs = form.querySelectorAll('[required]');

    requiredInputs.forEach(input => {
      const feedbackEl = input.nextElementSibling;
      if (!input.value.trim()) {
        input.classList.add('is-invalid');
        isValid = false;
      } else {
        input.classList.remove('is-invalid');
        input.classList.add('is-valid');
      }
    });

    // Email validation
    const emailInput = form.querySelector('input[type="email"]');
    if (emailInput && emailInput.value.trim()) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(emailInput.value.trim())) {
        emailInput.classList.add('is-invalid');
        isValid = false;
      }
    }

    const alertBox = document.getElementById('formStatusAlert');
    if (isValid) {
      if (alertBox) {
        alertBox.className = 'alert alert-success d-block';
        alertBox.innerHTML = `
          <i class="bi bi-check-circle-fill me-2"></i>
          <strong>Message Received:</strong> Thank you for contacting +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय. Your query has been logged. Our administrative team will review and respond promptly.
        `;
      }
      form.reset();
      form.querySelectorAll('.is-valid').forEach(el => el.classList.remove('is-valid'));
    } else {
      if (alertBox) {
        alertBox.className = 'alert alert-danger d-block';
        alertBox.innerHTML = `
          <i class="bi bi-exclamation-triangle-fill me-2"></i>
          <strong>Please complete all required fields</strong> accurately before submitting.
        `;
      }
    }
  });
}

/* ====================================================================
   9. BACK TO TOP BUTTON
   ==================================================================== */
function initBackToTop() {
  const btn = document.querySelector('.back-to-top-btn');
  if (!btn) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 400) {
      btn.classList.add('visible');
    } else {
      btn.classList.remove('visible');
    }
  }, { passive: true });

  btn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

/* ====================================================================
   10. ACTIVE NAVIGATION STATE DETECTOR
   ==================================================================== */
function initActiveNav() {
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.navbar-nav .nav-link, .dropdown-item, .mobile-nav-links .nav-link');

  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (!href) return;
    const linkPath = href.split('/').pop();

    if (linkPath === currentPath) {
      link.classList.add('active');
      const parentDropdown = link.closest('.dropdown');
      if (parentDropdown) {
        const toggle = parentDropdown.querySelector('.nav-link.dropdown-toggle');
        if (toggle) toggle.classList.add('active');
      }
    }
  });
}

/* ====================================================================
   11. AUTOMATIC COPYRIGHT YEAR
   ==================================================================== */
function initAutoYear() {
  const yearEls = document.querySelectorAll('.auto-year');
  const year = new Date().getFullYear();
  yearEls.forEach(el => el.textContent = year);
}

/* ====================================================================
   12. FAQ ACCORDION
   ==================================================================== */
function initFaqAccordion() {
  const triggers = document.querySelectorAll('.faq-trigger-btn');
  triggers.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.getAttribute('data-target');
      const content = document.getElementById(targetId);
      if (!content) return;

      const isOpen = content.classList.contains('show');
      document.querySelectorAll('.faq-collapse-body').forEach(c => c.classList.remove('show'));
      document.querySelectorAll('.faq-trigger-btn').forEach(b => b.classList.remove('active'));

      if (!isOpen) {
        content.classList.add('show');
        btn.classList.add('active');
      }
    });
  });
}
