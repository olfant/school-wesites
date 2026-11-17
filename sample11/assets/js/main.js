/* ==========================================================================
   CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR
   MAIN GLOBAL CONTROLLER (Vanilla JS)
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  initNavbarScroll();
  initTextSizeControls();
  initBackToTop();
  initCopyrightYear();
  initMobileMenuClose();
  initActiveNavLinks();
});

/* Sticky Navigation & Scroll Transparency */
function initNavbarScroll() {
  const nav = document.querySelector('.sticky-floating-nav, .floating-nav');
  if (!nav) return;

  const onScroll = () => {
    if (window.scrollY > 50) {
      nav.classList.add('scrolled');
    } else {
      nav.classList.remove('scrolled');
    }
  };

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}

/* Accessibility: Text Size Adjustment */
function initTextSizeControls() {
  const root = document.documentElement;
  const buttons = document.querySelectorAll('.fs-control-group button');
  if (!buttons.length) return;

  const savedSize = localStorage.getItem('vniketan_fs') || '0';
  applyTextSize(savedSize);

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      const size = btn.getAttribute('data-fs');
      applyTextSize(size);
      localStorage.setItem('vniketan_fs', size);
    });
  });

  function applyTextSize(val) {
    if (val === '0') {
      root.removeAttribute('data-fs');
    } else {
      root.setAttribute('data-fs', val);
    }
    buttons.forEach(b => {
      const isActive = b.getAttribute('data-fs') === val;
      b.classList.toggle('active', isActive);
      b.setAttribute('aria-pressed', isActive ? 'true' : 'false');
    });
  }
}

/* Back to Top Smooth Scroll */
function initBackToTop() {
  const btn = document.getElementById('backToTopBtn');
  if (!btn) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 350) {
      btn.classList.add('visible');
    } else {
      btn.classList.remove('visible');
    }
  }, { passive: true });

  btn.addEventListener('click', () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
}

/* Dynamic Copyright Year */
function initCopyrightYear() {
  const yrSpan = document.getElementById('currentYear');
  if (yrSpan) {
    yrSpan.textContent = new Date().getFullYear();
  }
}

/* Mobile Menu auto-close on link click or outside click */
function initMobileMenuClose() {
  const navCollapse = document.getElementById('navbarSchoolNav');
  if (!navCollapse) return;

  const navLinks = navCollapse.querySelectorAll('.nav-link:not(.dropdown-toggle), .dropdown-item');
  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      if (navCollapse.classList.contains('show')) {
        const bsCollapse = bootstrap.Collapse.getInstance(navCollapse);
        if (bsCollapse) bsCollapse.hide();
      }
    });
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && navCollapse.classList.contains('show')) {
      const bsCollapse = bootstrap.Collapse.getInstance(navCollapse);
      if (bsCollapse) bsCollapse.hide();
    }
  });
}

/* Active Nav Link Detection */
function initActiveNavLinks() {
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.navbar-nav .nav-link, .dropdown-menu .dropdown-item');

  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (!href) return;
    const linkFile = href.split('/').pop();
    if (linkFile === currentPath) {
      link.classList.add('active');
      const parentDropdown = link.closest('.dropdown');
      if (parentDropdown) {
        const toggle = parentDropdown.querySelector('.dropdown-toggle');
        if (toggle) toggle.classList.add('active');
      }
    }
  });
}
