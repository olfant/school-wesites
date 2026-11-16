/**
 * +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय, हल्दीपोखर
 * Main Interactive Features & Architectural Controller
 * Version 2.0 (Modern Green Educational Institution)
 */

document.addEventListener('DOMContentLoaded', () => {
  initAccessibilityControls();
  initStickyNavbar();
  initActiveNav();
  initScrollReveal();
  initBackToTop();
  initDynamicCopyright();
  initNoticesFilter();
  initLightbox();
  initGalleryFilter();
  initResultsFilter();
  initContactForm();
});

/* ----------------------------------------------------
   1. Accessibility: Font Size & High Contrast Mode
---------------------------------------------------- */
function initAccessibilityControls() {
  const htmlEl = document.documentElement;
  const bodyEl = document.body;

  // Restore saved preferences
  const savedFontSize = localStorage.getItem('vnhs_font_size') || 'md';
  htmlEl.classList.add(`font-size-${savedFontSize}`);

  const savedContrast = localStorage.getItem('vnhs_high_contrast');
  if (savedContrast === 'true') {
    bodyEl.classList.add('high-contrast');
  }

  // Bind Buttons
  const btnSm = document.getElementById('btnFontDecrease');
  const btnMd = document.getElementById('btnFontReset');
  const btnLg = document.getElementById('btnFontIncrease');
  const btnContrast = document.getElementById('btnHighContrast');

  function setFontSize(size) {
    htmlEl.classList.remove('font-size-sm', 'font-size-md', 'font-size-lg');
    htmlEl.classList.add(`font-size-${size}`);
    localStorage.setItem('vnhs_font_size', size);

    [btnSm, btnMd, btnLg].forEach(btn => btn?.classList.remove('active'));
    if (size === 'sm') btnSm?.classList.add('active');
    if (size === 'md') btnMd?.classList.add('active');
    if (size === 'lg') btnLg?.classList.add('active');
  }

  btnSm?.addEventListener('click', () => setFontSize('sm'));
  btnMd?.addEventListener('click', () => setFontSize('md'));
  btnLg?.addEventListener('click', () => setFontSize('lg'));

  btnContrast?.addEventListener('click', () => {
    bodyEl.classList.toggle('high-contrast');
    const isHigh = bodyEl.classList.contains('high-contrast');
    localStorage.setItem('vnhs_high_contrast', isHigh ? 'true' : 'false');
    btnContrast.classList.toggle('active', isHigh);
  });
}

/* ----------------------------------------------------
   2. Sticky Navigation Bar & Shadow
---------------------------------------------------- */
function initStickyNavbar() {
  const navbar = document.querySelector('.navbar-custom');
  if (!navbar) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  }, { passive: true });
}

/* ----------------------------------------------------
   3. Active Navigation State Detection
---------------------------------------------------- */
function initActiveNav() {
  const currentPath = window.location.pathname.toLowerCase();
  const filename = currentPath.substring(currentPath.lastIndexOf('/') + 1) || 'index.html';

  const navLinks = document.querySelectorAll('.nav-link, .dropdown-item, .mobile-subnav a');
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (!href) return;
    const linkFile = href.substring(href.lastIndexOf('/') + 1);

    if (linkFile === filename || (filename === '' && linkFile === 'index.html')) {
      link.classList.add('active');
      // If it is inside a dropdown, highlight the parent dropdown toggle
      const parentDropdown = link.closest('.dropdown');
      if (parentDropdown) {
        const toggle = parentDropdown.querySelector('.dropdown-toggle');
        if (toggle) toggle.classList.add('active');
      }
    }
  });
}

/* ----------------------------------------------------
   4. Scroll Reveal Animations (IntersectionObserver)
---------------------------------------------------- */
function initScrollReveal() {
  const revealElements = document.querySelectorAll('.reveal-on-scroll');
  if (!revealElements.length) return;

  // Check prefers-reduced-motion
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    revealElements.forEach(el => el.classList.add('is-revealed'));
    return;
  }

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-revealed');
        obs.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.12,
    rootMargin: '0px 0px -40px 0px'
  });

  revealElements.forEach(el => observer.observe(el));
}

/* ----------------------------------------------------
   5. Back to Top Smooth Button
---------------------------------------------------- */
function initBackToTop() {
  const backToTopBtn = document.getElementById('backToTopBtn');
  if (!backToTopBtn) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 400) {
      backToTopBtn.classList.add('visible');
    } else {
      backToTopBtn.classList.remove('visible');
    }
  }, { passive: true });

  backToTopBtn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

/* ----------------------------------------------------
   6. Dynamic Copyright Year
---------------------------------------------------- */
function initDynamicCopyright() {
  const yearEls = document.querySelectorAll('.current-year-placeholder');
  const year = new Date().getFullYear();
  yearEls.forEach(el => {
    el.textContent = year;
  });
}

/* ----------------------------------------------------
   7. Notices Search & Live Category Filter
---------------------------------------------------- */
function initNoticesFilter() {
  const noticesContainer = document.getElementById('noticesContainer');
  const searchInput = document.getElementById('noticeSearchInput');
  const filterPills = document.querySelectorAll('[data-notice-category]');

  if (!noticesContainer || typeof SITE_DATA === 'undefined') return;

  let currentCategory = 'all';
  let searchQuery = '';

  function renderNotices() {
    const filtered = SITE_DATA.notices.filter(notice => {
      const matchCat = (currentCategory === 'all' || notice.category.toLowerCase() === currentCategory.toLowerCase());
      const matchQuery = notice.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
                         notice.summary.toLowerCase().includes(searchQuery.toLowerCase()) ||
                         notice.category.toLowerCase().includes(searchQuery.toLowerCase());
      return matchCat && matchQuery;
    });

    if (filtered.length === 0) {
      noticesContainer.innerHTML = `
        <div class="col-12 text-center py-5">
          <div class="p-4 bg-white rounded-3 border">
            <i class="bi bi-info-circle text-success fs-1 mb-3 d-block"></i>
            <h5 class="fw-bold text-dark">No Notices Found</h5>
            <p class="text-muted mb-0">No official updates matched your search query or selected category filter.</p>
          </div>
        </div>
      `;
      return;
    }

    noticesContainer.innerHTML = filtered.map(notice => {
      const [day, month, yr] = notice.date.split(' ');
      return `
        <div class="col-12 reveal-on-scroll is-revealed">
          <div class="editorial-notice-card">
            <div class="notice-date-box">
              <span class="notice-day">${day}</span>
              <span class="notice-month">${month}</span>
            </div>
            <div class="notice-content-area">
              <div class="d-flex align-items-center gap-2 mb-1">
                <span class="badge-notice-tag ${notice.categoryClass}">${notice.category}</span>
                ${notice.isNew ? '<span class="badge bg-danger rounded-pill px-2" style="font-size:0.7rem;">NEW</span>' : ''}
              </div>
              <h5 class="fw-bold mb-1 text-dark">${notice.title}</h5>
              <p class="mb-0 text-muted small">${notice.summary}</p>
            </div>
            <div class="flex-shrink-0 text-end">
              <span class="btn btn-sm btn-outline-success rounded-pill px-3 fw-bold" onclick="alert('Notice Reference: ${notice.id}\\n\\n${notice.title}\\n\\nPlease refer to the school physical notice board for signed official gazette copy.')">
                View Notice <i class="bi bi-arrow-right ms-1"></i>
              </span>
            </div>
          </div>
        </div>
      `;
    }).join('');
  }

  // Initial render
  renderNotices();

  // Category Pill Click
  filterPills.forEach(pill => {
    pill.addEventListener('click', () => {
      filterPills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      currentCategory = pill.getAttribute('data-notice-category') || 'all';
      renderNotices();
    });
  });

  // Search Input
  searchInput?.addEventListener('input', (e) => {
    searchQuery = e.target.value.trim();
    renderNotices();
  });
}

/* ----------------------------------------------------
   8. Lightbox Image Viewer
---------------------------------------------------- */
let currentLightboxIndex = 0;
let currentLightboxList = [];

function initLightbox() {
  const modal = document.getElementById('lightboxModal');
  if (!modal) return;

  const imgEl = modal.querySelector('.lightbox-img-el');
  const captionEl = modal.querySelector('.lightbox-caption-text');
  const closeBtn = modal.querySelector('.lightbox-close-btn');
  const prevBtn = modal.querySelector('.lightbox-prev-btn');
  const nextBtn = modal.querySelector('.lightbox-next-btn');

  function openLightbox(list, index) {
    currentLightboxList = list;
    currentLightboxIndex = index;
    updateLightbox();
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }

  function updateLightbox() {
    if (!currentLightboxList.length) return;
    const item = currentLightboxList[currentLightboxIndex];
    imgEl.src = item.src;
    imgEl.alt = item.title;
    captionEl.textContent = `${item.title} — ${item.caption || ''}`;
  }

  closeBtn?.addEventListener('click', closeLightbox);
  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeLightbox();
  });

  prevBtn?.addEventListener('click', (e) => {
    e.stopPropagation();
    currentLightboxIndex = (currentLightboxIndex - 1 + currentLightboxList.length) % currentLightboxList.length;
    updateLightbox();
  });

  nextBtn?.addEventListener('click', (e) => {
    e.stopPropagation();
    currentLightboxIndex = (currentLightboxIndex + 1) % currentLightboxList.length;
    updateLightbox();
  });

  document.addEventListener('keydown', (e) => {
    if (!modal.classList.contains('active')) return;
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowLeft') prevBtn?.click();
    if (e.key === 'ArrowRight') nextBtn?.click();
  });

  // Attach to triggerable gallery items
  document.querySelectorAll('[data-lightbox-trigger]').forEach((el, idx, all) => {
    el.addEventListener('click', (e) => {
      e.preventDefault();
      const list = Array.from(all).map(item => ({
        src: item.getAttribute('data-img-src') || item.querySelector('img')?.src,
        title: item.getAttribute('data-img-title') || item.querySelector('img')?.alt || 'Campus Photo',
        caption: item.getAttribute('data-img-caption') || ''
      }));
      openLightbox(list, idx);
    });
  });
}

/* ----------------------------------------------------
   9. Filterable Gallery Grid (Gallery Page)
---------------------------------------------------- */
function initGalleryFilter() {
  const galleryContainer = document.getElementById('galleryContainer');
  const filterButtons = document.querySelectorAll('[data-gallery-filter]');

  if (!galleryContainer) return;

  filterButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      filterButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const filter = btn.getAttribute('data-gallery-filter');

      const items = galleryContainer.querySelectorAll('.gallery-card-item');
      items.forEach(item => {
        const cat = item.getAttribute('data-category');
        if (filter === 'all' || cat === filter) {
          item.style.display = 'block';
        } else {
          item.style.display = 'none';
        }
      });
    });
  });
}

/* ----------------------------------------------------
   10. Examination Results Search & Filtering
---------------------------------------------------- */
function initResultsFilter() {
  const resultsTableBody = document.getElementById('resultsTableBody');
  const sessionSelect = document.getElementById('resultSessionFilter');
  const classSelect = document.getElementById('resultClassFilter');
  const searchInput = document.getElementById('resultSearchInput');

  if (!resultsTableBody || typeof SITE_DATA === 'undefined') return;

  function renderResults() {
    const selSession = sessionSelect ? sessionSelect.value : 'all';
    const selClass = classSelect ? classSelect.value : 'all';
    const query = searchInput ? searchInput.value.toLowerCase().trim() : '';

    const filtered = SITE_DATA.results.filter(res => {
      const matchSession = (selSession === 'all' || res.session === selSession);
      const matchClass = (selClass === 'all' || res.classGroup.toLowerCase().includes(selClass.toLowerCase()) || res.stream.toLowerCase().includes(selClass.toLowerCase()));
      const matchQuery = res.examName.toLowerCase().includes(query) ||
                         res.classGroup.toLowerCase().includes(query) ||
                         res.session.toLowerCase().includes(query);
      return matchSession && matchClass && matchQuery;
    });

    if (filtered.length === 0) {
      resultsTableBody.innerHTML = `
        <tr>
          <td colspan="6" class="text-center py-4 text-muted">
            <i class="bi bi-folder2-open fs-2 d-block text-secondary mb-2"></i>
            No official examination gazettes match the selected criteria.
          </td>
        </tr>
      `;
      return;
    }

    const basePath = window.location.pathname.includes('/pages/') ? '../' : '';

    resultsTableBody.innerHTML = filtered.map(item => `
      <tr>
        <td class="fw-bold text-dark">${item.examName}</td>
        <td><span class="badge bg-light text-dark border px-2 py-1">${item.session}</span></td>
        <td>${item.classGroup}</td>
        <td>${item.resultDate}</td>
        <td><span class="badge bg-success-subtle text-success border border-success-subtle fw-bold px-2 py-1">${item.passPercentage} Pass</span></td>
        <td class="text-end">
          <a href="${basePath}assets/documents/results/${item.documentName}" target="_blank" class="btn btn-sm btn-outline-success rounded-pill px-3">
            <i class="bi bi-file-earmark-pdf me-1"></i> View Gazette
          </a>
        </td>
      </tr>
    `).join('');
  }

  sessionSelect?.addEventListener('change', renderResults);
  classSelect?.addEventListener('change', renderResults);
  searchInput?.addEventListener('input', renderResults);

  renderResults();
}

/* ----------------------------------------------------
   11. Contact Form Client-side Validation
---------------------------------------------------- */
function initContactForm() {
  const form = document.getElementById('schoolContactForm');
  const alertContainer = document.getElementById('contactFormAlert');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!form.checkValidity()) {
      e.stopPropagation();
      form.classList.add('was-validated');
      return;
    }

    // Success response simulation
    if (alertContainer) {
      alertContainer.innerHTML = `
        <div class="alert alert-success alert-dismissible fade show d-flex align-items-center" role="alert">
          <i class="bi bi-check-circle-fill fs-4 me-3"></i>
          <div>
            <strong>संदेश सफलतापूर्वक प्राप्त हुआ (Inquiry Submitted)!</strong><br>
            Thank you for contacting +2 Rajkiyakrit Vidya Niketan High School, Haldipokhar. The administrative desk will review your inquiry.
          </div>
          <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
      `;
      alertContainer.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }

    form.reset();
    form.classList.remove('was-validated');
  });
}
