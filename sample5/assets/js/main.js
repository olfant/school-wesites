/**
 * CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR
 * (+2 राजकीयकृत विद्या निकेतन उच्च विद्यालय, हल्दीपोखर, पूर्वी सिंहभूम)
 * Main Interactive JavaScript Engine
 */

document.addEventListener('DOMContentLoaded', function () {
  'use strict';

  // ========================================================================
  // 1. Accessibility: Font Size Adjuster (A-, A, A+)
  // ========================================================================
  const fontDecBtn = document.getElementById('fontDecBtn');
  const fontResetBtn = document.getElementById('fontResetBtn');
  const fontIncBtn = document.getElementById('fontIncBtn');

  const FONT_KEY = 'vnhs_font_scale';
  const scales = {
    dec: '90%',
    reset: '100%',
    inc: '110%'
  };

  function setFontScale(scaleKey) {
    const val = scales[scaleKey] || '100%';
    document.documentElement.style.setProperty('--font-scale', val);
    try {
      localStorage.setItem(FONT_KEY, scaleKey);
    } catch (e) {
      console.warn('localStorage not available', e);
    }

    // Update active class on buttons
    [fontDecBtn, fontResetBtn, fontIncBtn].forEach(function (btn) {
      if (btn) btn.classList.remove('active');
    });

    if (scaleKey === 'dec' && fontDecBtn) fontDecBtn.classList.add('active');
    if (scaleKey === 'inc' && fontIncBtn) fontIncBtn.classList.add('active');
    if (scaleKey === 'reset' && fontResetBtn) fontResetBtn.classList.add('active');
  }

  // Init font scale from storage
  let savedFontScale = 'reset';
  try {
    savedFontScale = localStorage.getItem(FONT_KEY) || 'reset';
  } catch (e) {}
  setFontScale(savedFontScale);

  if (fontDecBtn) fontDecBtn.addEventListener('click', function () { setFontScale('dec'); });
  if (fontResetBtn) fontResetBtn.addEventListener('click', function () { setFontScale('reset'); });
  if (fontIncBtn) fontIncBtn.addEventListener('click', function () { setFontScale('inc'); });


  // ========================================================================
  // 2. Sticky Navbar Scroll Effect
  // ========================================================================
  const mainNavbar = document.querySelector('.main-navbar');
  window.addEventListener('scroll', function () {
    if (mainNavbar) {
      if (window.scrollY > 60) {
        mainNavbar.classList.add('navbar-scrolled');
      } else {
        mainNavbar.classList.remove('navbar-scrolled');
      }
    }
  }, { passive: true });


  // ========================================================================
  // 3. Active Nav Link Detector
  // ========================================================================
  function highlightActiveNav() {
    const currentPath = window.location.pathname.toLowerCase();
    const navLinks = document.querySelectorAll('.main-navbar .nav-link, .main-navbar .dropdown-item');

    navLinks.forEach(function (link) {
      const href = link.getAttribute('href');
      if (!href) return;

      // Extract file name
      const targetName = href.split('/').pop().toLowerCase();
      const currentFileName = currentPath.split('/').pop().toLowerCase() || 'index.html';

      if (targetName === currentFileName && currentFileName !== '') {
        link.classList.add('active');
        // If it is in a dropdown, also highlight parent dropdown toggle
        const dropdownParent = link.closest('.dropdown');
        if (dropdownParent) {
          const parentToggle = dropdownParent.querySelector('.dropdown-toggle');
          if (parentToggle) parentToggle.classList.add('active');
        }
      }
    });
  }
  highlightActiveNav();


  // ========================================================================
  // 4. Back-to-Top Floating Button
  // ========================================================================
  const backToTopBtn = document.getElementById('backToTopBtn');
  window.addEventListener('scroll', function () {
    if (backToTopBtn) {
      if (window.scrollY > 350) {
        backToTopBtn.classList.add('show');
      } else {
        backToTopBtn.classList.remove('show');
      }
    }
  }, { passive: true });

  if (backToTopBtn) {
    backToTopBtn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }


  // ========================================================================
  // 5. Scroll-Triggered Reveal Animations (IntersectionObserver)
  // ========================================================================
  const revealElements = document.querySelectorAll('.reveal, .reveal-left, .reveal-right');
  if ('IntersectionObserver' in window && revealElements.length > 0) {
    const revealObserver = new IntersectionObserver(function (entries, observer) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
          observer.unobserve(entry.target);
        }
      });
    }, {
      rootMargin: '0px 0px -40px 0px',
      threshold: 0.1
    });

    revealElements.forEach(function (el) {
      revealObserver.observe(el);
    });
  } else {
    // Fallback if IntersectionObserver not supported
    revealElements.forEach(function (el) {
      el.classList.add('active');
    });
  }


  // ========================================================================
  // 6. Dynamic Year in Footer
  // ========================================================================
  const copyrightYearEl = document.getElementById('copyrightYear');
  if (copyrightYearEl) {
    copyrightYearEl.textContent = new Date().getFullYear();
  }


  // ========================================================================
  // 7. Notice Board Live Search & Category Filter
  // ========================================================================
  const noticeSearchInput = document.getElementById('noticeSearchInput');
  const noticeCategoryPills = document.querySelectorAll('.notice-cat-btn');
  const noticeItems = document.querySelectorAll('.notice-item');
  const noticeEmptyState = document.getElementById('noticeEmptyState');

  function filterNotices() {
    if (!noticeItems.length) return;

    const searchTerm = noticeSearchInput ? noticeSearchInput.value.toLowerCase().trim() : '';
    let activeCat = 'all';
    const activePill = document.querySelector('.notice-cat-btn.active');
    if (activePill) activeCat = activePill.getAttribute('data-cat') || 'all';

    let visibleCount = 0;

    noticeItems.forEach(function (item) {
      const title = item.querySelector('.notice-title') ? item.querySelector('.notice-title').textContent.toLowerCase() : '';
      const summary = item.querySelector('.notice-summary') ? item.querySelector('.notice-summary').textContent.toLowerCase() : '';
      const cat = item.getAttribute('data-category') || '';

      const matchesSearch = title.includes(searchTerm) || summary.includes(searchTerm);
      const matchesCategory = activeCat === 'all' || cat === activeCat;

      if (matchesSearch && matchesCategory) {
        item.style.display = 'flex';
        visibleCount++;
      } else {
        item.style.display = 'none';
      }
    });

    if (noticeEmptyState) {
      noticeEmptyState.style.display = visibleCount === 0 ? 'block' : 'none';
    }
  }

  if (noticeSearchInput) {
    noticeSearchInput.addEventListener('input', filterNotices);
  }

  if (noticeCategoryPills.length > 0) {
    noticeCategoryPills.forEach(function (pill) {
      pill.addEventListener('click', function () {
        noticeCategoryPills.forEach(function (p) { p.classList.remove('active'); });
        this.classList.add('active');
        filterNotices();
      });
    });
  }


  // ========================================================================
  // 8. Gallery Category Filter & Lightbox Viewer
  // ========================================================================
  const galleryFilterBtns = document.querySelectorAll('.gallery-filter-btn');
  const galleryCards = document.querySelectorAll('.gallery-grid-col');
  const lightboxModalEl = document.getElementById('galleryLightboxModal');
  const lightboxImg = document.getElementById('lightboxModalImg');
  const lightboxCaption = document.getElementById('lightboxModalCaption');
  const lightboxPrevBtn = document.getElementById('lightboxPrevBtn');
  const lightboxNextBtn = document.getElementById('lightboxNextBtn');

  // Filter functionality
  if (galleryFilterBtns.length > 0 && galleryCards.length > 0) {
    galleryFilterBtns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        galleryFilterBtns.forEach(function (b) { b.classList.remove('active'); });
        this.classList.add('active');

        const selectedCategory = this.getAttribute('data-category');

        galleryCards.forEach(function (card) {
          const itemCategory = card.getAttribute('data-category');
          if (selectedCategory === 'all' || itemCategory === selectedCategory) {
            card.style.display = 'block';
            setTimeout(function () {
              card.style.opacity = '1';
              card.style.transform = 'scale(1)';
            }, 50);
          } else {
            card.style.opacity = '0';
            card.style.transform = 'scale(0.95)';
            setTimeout(function () {
              card.style.display = 'none';
            }, 250);
          }
        });
      });
    });
  }

  // Lightbox functionality
  let currentGalleryIndex = 0;
  const visibleGalleryItems = [];

  function updateVisibleGalleryList() {
    visibleGalleryItems.length = 0;
    const cards = document.querySelectorAll('.gallery-card');
    cards.forEach(function (card) {
      const parent = card.closest('.gallery-grid-col');
      if (!parent || parent.style.display !== 'none') {
        visibleGalleryItems.push({
          src: card.getAttribute('data-img-src') || card.querySelector('img').src,
          caption: card.getAttribute('data-caption') || card.querySelector('h5')?.textContent || ''
        });
      }
    });
  }

  function showLightboxImage(index) {
    if (visibleGalleryItems.length === 0) return;
    if (index < 0) index = visibleGalleryItems.length - 1;
    if (index >= visibleGalleryItems.length) index = 0;
    currentGalleryIndex = index;

    if (lightboxImg) lightboxImg.src = visibleGalleryItems[currentGalleryIndex].src;
    if (lightboxCaption) lightboxCaption.textContent = visibleGalleryItems[currentGalleryIndex].caption;
  }

  const galleryCardElements = document.querySelectorAll('.gallery-card');
  galleryCardElements.forEach(function (card) {
    card.addEventListener('click', function () {
      updateVisibleGalleryList();
      const clickedSrc = card.getAttribute('data-img-src') || card.querySelector('img').src;
      const foundIdx = visibleGalleryItems.findIndex(function (item) {
        return item.src.includes(clickedSrc.split('/').pop());
      });

      showLightboxImage(foundIdx !== -1 ? foundIdx : 0);

      if (lightboxModalEl && typeof bootstrap !== 'undefined') {
        const modal = bootstrap.Modal.getOrCreateInstance(lightboxModalEl);
        modal.show();
      }
    });
  });

  if (lightboxPrevBtn) {
    lightboxPrevBtn.addEventListener('click', function () {
      showLightboxImage(currentGalleryIndex - 1);
    });
  }

  if (lightboxNextBtn) {
    lightboxNextBtn.addEventListener('click', function () {
      showLightboxImage(currentGalleryIndex + 1);
    });
  }


  // ========================================================================
  // 9. Examination Results Interactive Table Filter
  // ========================================================================
  const resultSessionFilter = document.getElementById('resultSessionFilter');
  const resultClassFilter = document.getElementById('resultClassFilter');
  const resultSearchInput = document.getElementById('resultSearchInput');
  const resultTableRows = document.querySelectorAll('.result-data-row');
  const resultEmptyState = document.getElementById('resultEmptyState');

  function filterExamResults() {
    if (!resultTableRows.length) return;

    const sessionVal = resultSessionFilter ? resultSessionFilter.value : 'all';
    const classVal = resultClassFilter ? resultClassFilter.value : 'all';
    const query = resultSearchInput ? resultSearchInput.value.toLowerCase().trim() : '';

    let matchCount = 0;

    resultTableRows.forEach(function (row) {
      const rowSession = row.getAttribute('data-session') || '';
      const rowClass = row.getAttribute('data-class') || '';
      const rowText = row.textContent.toLowerCase();

      const matchesSession = sessionVal === 'all' || rowSession === sessionVal;
      const matchesClass = classVal === 'all' || rowClass === classVal;
      const matchesQuery = query === '' || rowText.includes(query);

      if (matchesSession && matchesClass && matchesQuery) {
        row.style.display = '';
        matchCount++;
      } else {
        row.style.display = 'none';
      }
    });

    if (resultEmptyState) {
      resultEmptyState.style.display = matchCount === 0 ? 'block' : 'none';
    }
  }

  if (resultSessionFilter) resultSessionFilter.addEventListener('change', filterExamResults);
  if (resultClassFilter) resultClassFilter.addEventListener('change', filterExamResults);
  if (resultSearchInput) resultSearchInput.addEventListener('input', filterExamResults);


  // ========================================================================
  // 10. Contact Form Interactive Validation & Mailto Action
  // ========================================================================
  const contactForm = document.getElementById('schoolContactForm');
  const formSuccessAlert = document.getElementById('contactFormSuccessAlert');

  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();

      const nameInput = document.getElementById('contactName');
      const emailInput = document.getElementById('contactEmail');
      const subjectInput = document.getElementById('contactSubject');
      const messageInput = document.getElementById('contactMessage');

      let isValid = true;

      // Validation
      [nameInput, emailInput, subjectInput, messageInput].forEach(function (field) {
        if (!field) return;
        if (!field.value.trim()) {
          field.classList.add('is-invalid');
          isValid = false;
        } else {
          field.classList.remove('is-invalid');
        }
      });

      if (!isValid) return;

      const schoolEmail = 'vnhs.haldipokhar.e.singhbhum@gmail.com';
      const mailSubject = encodeURIComponent(`[विद्यालय पूछताछ] ${subjectInput.value}`);
      const mailBody = encodeURIComponent(
        `प्रेषक का नाम: ${nameInput.value}\nईमेल: ${emailInput.value}\n\nसंदेश:\n${messageInput.value}\n\n---\nSent via School Contact Portal (CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR)`
      );

      const mailtoUrl = `mailto:${schoolEmail}?subject=${mailSubject}&body=${mailBody}`;

      if (formSuccessAlert) {
        formSuccessAlert.style.display = 'block';
        formSuccessAlert.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }

      // Open user email client
      window.location.href = mailtoUrl;

      // Reset form
      contactForm.reset();
    });
  }

});
