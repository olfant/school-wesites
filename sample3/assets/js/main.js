/**
 * ====================================================================
 * MAIN JAVASCRIPT — SWISS GRID & CORE FUNCTIONALITY
 * CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR, हल्दीपोखर
 * Version 5 — Modular Vanilla JS
 * ====================================================================
 */

document.addEventListener('DOMContentLoaded', () => {
  initStickyHeader();
  initMobileDrawer();
  initFontSizeControls();
  initActiveNavHighlight();
  initScrollReveal();
  initLearningJourneyObserver();
  initBackToTop();
  initCurrentYear();
  initContactFormValidation();
  initSwissAccordions();
});

/**
 * Sticky Navigation Bar
 */
function initStickyHeader() {
  const navBar = document.querySelector('.site-navigation-bar');
  if (!navBar) return;

  const handleScroll = () => {
    if (window.scrollY > 140) {
      navBar.classList.add('is-sticky');
    } else {
      navBar.classList.remove('is-sticky');
    }
  };

  window.addEventListener('scroll', handleScroll, { passive: true });
}

/**
 * Mobile Drawer Navigation
 */
function initMobileDrawer() {
  const toggleBtn = document.querySelector('.mobile-nav-toggle');
  const drawer = document.querySelector('.mobile-drawer');
  const overlay = document.querySelector('.mobile-drawer-overlay');
  const closeBtn = document.querySelector('.drawer-close-btn');

  if (!toggleBtn || !drawer || !overlay) return;

  const openDrawer = () => {
    drawer.classList.add('is-active');
    overlay.classList.add('is-active');
    document.body.style.overflow = 'hidden';
  };

  const closeDrawer = () => {
    drawer.classList.remove('is-active');
    overlay.classList.remove('is-active');
    document.body.style.overflow = '';
  };

  toggleBtn.addEventListener('click', openDrawer);
  if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
  overlay.addEventListener('click', closeDrawer);

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && drawer.classList.contains('is-active')) {
      closeDrawer();
    }
  });

  // Mobile submenu accordions inside drawer
  const submenuToggles = document.querySelectorAll('.drawer-submenu-toggle');
  submenuToggles.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const parent = btn.closest('.drawer-nav-item');
      const submenu = parent.querySelector('.drawer-submenu');
      if (submenu) {
        submenu.classList.toggle('show');
        const icon = btn.querySelector('i');
        if (icon) {
          icon.classList.toggle('bi-chevron-down');
          icon.classList.toggle('bi-chevron-up');
        }
      }
    });
  });
}

/**
 * Font Size Controls (A- / A / A+)
 */
function initFontSizeControls() {
  const fontBtns = document.querySelectorAll('.font-btn');
  if (!fontBtns.length) return;

  // Retrieve saved preference
  const savedSize = localStorage.getItem('rvnhs_font_size') || 'font-md';
  document.body.classList.remove('font-sm', 'font-md', 'font-lg');
  document.body.classList.add(savedSize);

  fontBtns.forEach(btn => {
    const size = btn.getAttribute('data-size');
    if (size === savedSize) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }

    btn.addEventListener('click', () => {
      fontBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      document.body.classList.remove('font-sm', 'font-md', 'font-lg');
      document.body.classList.add(size);
      localStorage.setItem('rvnhs_font_size', size);
    });
  });
}

/**
 * Active Navigation Link Indication
 */
function initActiveNavHighlight() {
  const currentPath = window.location.pathname.toLowerCase();
  const currentFileName = currentPath.substring(currentPath.lastIndexOf('/') + 1) || 'index.html';

  const navLinks = document.querySelectorAll('.nav-link-item, .dropdown-link-item, .drawer-link, .drawer-sublink');
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (!href) return;

    const linkFileName = href.substring(href.lastIndexOf('/') + 1);

    if (linkFileName === currentFileName || (currentFileName === '' && linkFileName === 'index.html')) {
      link.classList.add('active');

      // Also highlight parent nav-item dropdown if inside one
      const parentDropdown = link.closest('.swiss-dropdown-menu');
      if (parentDropdown) {
        const parentNavItem = parentDropdown.closest('.nav-item');
        if (parentNavItem) {
          const parentNavLink = parentNavItem.querySelector('.nav-link-item');
          if (parentNavLink) parentNavLink.classList.add('active');
        }
      }
    }
  });
}

/**
 * Intersection Observer for Smooth Scroll Reveal
 */
function initScrollReveal() {
  const revealElements = document.querySelectorAll('.reveal-on-scroll');
  if (!revealElements.length || !('IntersectionObserver' in window)) return;

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-revealed');
        obs.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.15,
    rootMargin: '0px 0px -40px 0px'
  });

  revealElements.forEach(el => observer.observe(el));
}

/**
 * SECTION 08: Student Development Journey Animation
 */
function initLearningJourneyObserver() {
  const journeySection = document.querySelector('.section-learning-journey');
  const progressBar = document.querySelector('.timeline-track-progress');
  const nodes = document.querySelectorAll('.journey-node .node-marker');

  if (!journeySection || !('IntersectionObserver' in window)) return;

  const journeyObserver = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        if (progressBar) progressBar.style.width = '100%';
        nodes.forEach((node, idx) => {
          setTimeout(() => {
            node.style.transform = 'scale(1.06)';
            setTimeout(() => { node.style.transform = 'scale(1)'; }, 250);
          }, idx * 150);
        });
        obs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.25 });

  journeyObserver.observe(journeySection);
}

/**
 * Back to Top Smooth Button
 */
function initBackToTop() {
  const btn = document.querySelector('.back-to-top-btn');
  if (!btn) return;

  btn.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
}

/**
 * Auto Copyright Year
 */
function initCurrentYear() {
  const yearEls = document.querySelectorAll('.current-year');
  const year = new Date().getFullYear();
  yearEls.forEach(el => { el.textContent = year; });
}

/**
 * Contact Form Client-side Validation & Feedback
 */
function initContactFormValidation() {
  const contactForm = document.getElementById('schoolContactForm');
  if (!contactForm) return;

  contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    let isValid = true;

    const name = document.getElementById('contactName');
    const email = document.getElementById('contactEmail');
    const subject = document.getElementById('contactSubject');
    const message = document.getElementById('contactMessage');
    const alertBox = document.getElementById('contactFormAlert');

    // Reset validation states
    [name, email, subject, message].forEach(input => {
      if (input) input.classList.remove('is-invalid');
    });

    if (!name || name.value.trim().length < 2) {
      if (name) name.classList.add('is-invalid');
      isValid = false;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email || !emailRegex.test(email.value.trim())) {
      if (email) email.classList.add('is-invalid');
      isValid = false;
    }

    if (!subject || subject.value.trim().length < 3) {
      if (subject) subject.classList.add('is-invalid');
      isValid = false;
    }

    if (!message || message.value.trim().length < 10) {
      if (message) message.classList.add('is-invalid');
      isValid = false;
    }

    if (!isValid) return;

    // Show demonstration notice as requested in prompt:
    // "Clearly explain that no backend submission service is connected."
    if (alertBox) {
      alertBox.innerHTML = `
        <div class="alert alert-success d-flex align-items-center gap-2" role="alert">
          <i class="bi bi-check-circle-fill fs-5"></i>
          <div>
            <strong>Message Received (Demo Mode):</strong> Thank you, <em>${escapeHTML(name.value.trim())}</em>. 
            This frontend demonstration form validates your inquiry. For official admissions and communications, 
            please contact the school office directly at <strong>vnhs.haldipokhar.e.singhbhum@gmail.com</strong> 
            or visit the school premises at Haldipokhar, Potka.
          </div>
        </div>
      `;
      alertBox.scrollIntoView({ behavior: 'smooth', block: 'center' });
      contactForm.reset();
    }
  });
}

function escapeHTML(str) {
  return str.replace(/[&<>'"]/g, 
    tag => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;' }[tag] || tag)
  );
}

/**
 * Swiss Accordions (e.g. for FAQs and Stream listings)
 */
function initSwissAccordions() {
  const accordionBtns = document.querySelectorAll('.swiss-accordion-btn');
  accordionBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const isExpanded = btn.getAttribute('aria-expanded') === 'true';
      const targetId = btn.getAttribute('data-target');
      const body = document.getElementById(targetId);

      if (body) {
        if (isExpanded) {
          btn.setAttribute('aria-expanded', 'false');
          body.style.display = 'none';
        } else {
          btn.setAttribute('aria-expanded', 'true');
          body.style.display = 'block';
        }
      }
    });
  });
}
