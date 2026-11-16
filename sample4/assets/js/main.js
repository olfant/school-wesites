/**
 * +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय | HALDIPOKHAR, JHARKHAND
 * Main Interactive Application Script
 */

document.addEventListener('DOMContentLoaded', function () {
  'use strict';

  // 1. Automatic Copyright Year
  const yearElements = document.querySelectorAll('.auto-current-year');
  const currentYear = new Date().getFullYear();
  yearElements.forEach(el => {
    el.textContent = currentYear;
  });

  // 2. Font Size Accessibility Controls
  const fontControlButtons = document.querySelectorAll('[data-font-size]');
  const savedFontSize = localStorage.getItem('vnhs_font_size') || 'md';

  function applyFontSize(size) {
    document.documentElement.classList.remove('font-size-sm', 'font-size-md', 'font-size-lg');
    document.documentElement.classList.add(`font-size-${size}`);
    localStorage.setItem('vnhs_font_size', size);

    fontControlButtons.forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-font-size') === size);
    });
  }

  applyFontSize(savedFontSize);

  fontControlButtons.forEach(btn => {
    btn.addEventListener('click', function () {
      const size = this.getAttribute('data-font-size');
      applyFontSize(size);
    });
  });

  // 3. Back to Top Button
  const backToTopBtn = document.getElementById('backToTopBtn');
  if (backToTopBtn) {
    window.addEventListener('scroll', function () {
      if (window.scrollY > 350) {
        backToTopBtn.classList.add('is-shown');
      } else {
        backToTopBtn.classList.remove('is-shown');
      }
    });

    backToTopBtn.addEventListener('click', function () {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

  // 4. Active Navigation Link Highlighting
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.navbar-nav .nav-link, .dropdown-menu .dropdown-item');

  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (!href) return;
    const targetFile = href.split('/').pop();

    if (targetFile === currentPath || (currentPath === '' && targetFile === 'index.html')) {
      link.classList.add('active');
      // If it's a dropdown item, highlight its parent dropdown toggle
      const parentDropdown = link.closest('.dropdown');
      if (parentDropdown) {
        const toggle = parentDropdown.querySelector('.dropdown-toggle');
        if (toggle) toggle.classList.add('active');
      }
    }
  });

  // 5. Scroll Reveal with IntersectionObserver
  const revealElements = document.querySelectorAll('.reveal-on-scroll');
  if ('IntersectionObserver' in window && revealElements.length > 0) {
    const revealObserver = new IntersectionObserver(
      (entries, observer) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
          }
        });
      },
      {
        threshold: 0.12,
        rootMargin: '0px 0px -40px 0px'
      }
    );

    revealElements.forEach(el => revealObserver.observe(el));
  } else {
    revealElements.forEach(el => el.classList.add('is-visible'));
  }

  // 6. Notice Center Interactive Search & Filter
  const noticeContainer = document.getElementById('notice-list-container');
  const noticeSearchInput = document.getElementById('noticeSearchInput');
  const noticeFilterButtons = document.querySelectorAll('[data-notice-filter]');

  if (noticeContainer && typeof SchoolData !== 'undefined' && SchoolData.notices) {
    let currentCategory = 'all';
    let currentSearchTerm = '';

    function renderNotices() {
      const filtered = SchoolData.notices.filter(notice => {
        const matchesCategory = currentCategory === 'all' || notice.category.toLowerCase() === currentCategory.toLowerCase();
        const matchesSearch =
          notice.title.toLowerCase().includes(currentSearchTerm.toLowerCase()) ||
          notice.summary.toLowerCase().includes(currentSearchTerm.toLowerCase()) ||
          notice.category.toLowerCase().includes(currentSearchTerm.toLowerCase());
        return matchesCategory && matchesSearch;
      });

      if (filtered.length === 0) {
        noticeContainer.innerHTML = `
          <div class="col-12 text-center py-4 text-muted">
            <i class="bi bi-inbox fs-2 d-block mb-2 text-success"></i>
            <p class="mb-0">No notices found matching the selected criteria.</p>
          </div>
        `;
        return;
      }

      noticeContainer.innerHTML = filtered
        .map(n => `
          <div class="col-12">
            <div class="notice-card">
              <div class="notice-meta">
                <span class="notice-category-badge">${n.category}</span>
                <span class="notice-date"><i class="bi bi-calendar3 me-1"></i>${n.date}</span>
                ${n.isImportant ? '<span class="badge bg-danger">Important</span>' : ''}
              </div>
              <h5 class="notice-title">${n.title}</h5>
              <p class="notice-summary">${n.summary}</p>
              <div class="d-flex justify-content-between align-items-center mt-2">
                <a href="${n.file}" class="btn btn-sm btn-green-outline" target="_blank" rel="noopener">
                  <i class="bi bi-file-earmark-text me-1"></i>View Notice (Placeholder)
                </a>
                <small class="text-muted"><i class="bi bi-shield-check me-1"></i>Official School Record</small>
              </div>
            </div>
          </div>
        `)
        .join('');
    }

    renderNotices();

    if (noticeSearchInput) {
      noticeSearchInput.addEventListener('input', function (e) {
        currentSearchTerm = e.target.value.trim();
        renderNotices();
      });
    }

    noticeFilterButtons.forEach(btn => {
      btn.addEventListener('click', function () {
        noticeFilterButtons.forEach(b => b.classList.remove('active'));
        this.classList.add('active');
        currentCategory = this.getAttribute('data-notice-filter');
        renderNotices();
      });
    });
  }

  // 7. Examination Results Filtering
  const resultsTbody = document.getElementById('results-tbody');
  const sessionSelect = document.getElementById('sessionSelect');
  const classSelect = document.getElementById('classSelect');

  if (resultsTbody && typeof SchoolData !== 'undefined' && SchoolData.results) {
    function filterResults() {
      const selectedSession = sessionSelect ? sessionSelect.value : 'all';
      const selectedClass = classSelect ? classSelect.value : 'all';

      const filtered = SchoolData.results.filter(item => {
        const matchSession = selectedSession === 'all' || item.session === selectedSession;
        const matchClass = selectedClass === 'all' || item.className.toLowerCase().includes(selectedClass.toLowerCase());
        return matchSession && matchClass;
      });

      if (filtered.length === 0) {
        resultsTbody.innerHTML = `
          <tr>
            <td colspan="5" class="text-center py-4 text-muted">
              <i class="bi bi-info-circle me-1"></i>No official records found for the selected filter combination. Official results are published directly via JAC.
            </td>
          </tr>
        `;
        return;
      }

      resultsTbody.innerHTML = filtered
        .map(r => `
          <tr>
            <td class="fw-bold">${r.session}</td>
            <td>${r.exam}</td>
            <td><span class="badge bg-light text-success border border-success">${r.className}</span></td>
            <td><span class="text-success fw-semibold"><i class="bi bi-check-circle-fill me-1"></i>${r.status}</span></td>
            <td>
              <a href="${r.link}" target="_blank" rel="noopener" class="btn btn-sm btn-green-outline py-1 px-2">
                <i class="bi bi-download me-1"></i>Gazette Notice
              </a>
            </td>
          </tr>
        `)
        .join('');
    }

    filterResults();

    if (sessionSelect) sessionSelect.addEventListener('change', filterResults);
    if (classSelect) classSelect.addEventListener('change', filterResults);
  }

  // 8. Gallery Category Filtering & Lightbox Modal
  const galleryFilterBtns = document.querySelectorAll('[data-gallery-filter]');
  const galleryTiles = document.querySelectorAll('[data-gallery-category]');
  const lightboxModal = document.getElementById('lightboxModal');
  const lightboxImg = document.getElementById('lightboxImg');
  const lightboxTitle = document.getElementById('lightboxTitle');
  const lightboxDesc = document.getElementById('lightboxDesc');
  const lightboxClose = document.getElementById('lightboxClose');
  const lightboxPrev = document.getElementById('lightboxPrev');
  const lightboxNext = document.getElementById('lightboxNext');

  let activeGalleryItems = [];
  let currentLightboxIndex = 0;

  function updateActiveGalleryList() {
    activeGalleryItems = [];
    galleryTiles.forEach((tile, index) => {
      if (tile.style.display !== 'none') {
        activeGalleryItems.push({
          index: index,
          src: tile.getAttribute('data-img-src') || tile.querySelector('img').getAttribute('src'),
          title: tile.getAttribute('data-img-title') || 'School Gallery',
          desc: tile.getAttribute('data-img-desc') || ''
        });
      }
    });
  }

  if (galleryFilterBtns.length > 0 && galleryTiles.length > 0) {
    galleryFilterBtns.forEach(btn => {
      btn.addEventListener('click', function () {
        galleryFilterBtns.forEach(b => b.classList.remove('active'));
        this.classList.add('active');
        const filter = this.getAttribute('data-gallery-filter');

        galleryTiles.forEach(tile => {
          const category = tile.getAttribute('data-gallery-category');
          if (filter === 'all' || category === filter) {
            tile.style.display = '';
          } else {
            tile.style.display = 'none';
          }
        });
        updateActiveGalleryList();
      });
    });

    updateActiveGalleryList();
  }

  // Open Lightbox
  galleryTiles.forEach((tile, idx) => {
    tile.addEventListener('click', function () {
      const src = this.getAttribute('data-img-src') || this.querySelector('img').getAttribute('src');
      const title = this.getAttribute('data-img-title') || this.querySelector('h5')?.textContent || 'School Activity';
      const desc = this.getAttribute('data-img-desc') || this.querySelector('p')?.textContent || '';

      updateActiveGalleryList();
      currentLightboxIndex = activeGalleryItems.findIndex(item => item.src === src);
      if (currentLightboxIndex === -1) currentLightboxIndex = 0;

      showLightboxItem(currentLightboxIndex);
    });
  });

  function showLightboxItem(index) {
    if (!lightboxModal || activeGalleryItems.length === 0) return;
    const item = activeGalleryItems[index];
    if (!item) return;

    if (lightboxImg) lightboxImg.src = item.src;
    if (lightboxTitle) lightboxTitle.textContent = item.title;
    if (lightboxDesc) lightboxDesc.textContent = item.desc;
    lightboxModal.classList.add('is-active');
  }

  function closeLightbox() {
    if (lightboxModal) {
      lightboxModal.classList.remove('is-active');
    }
  }

  if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
  if (lightboxModal) {
    lightboxModal.addEventListener('click', function (e) {
      if (e.target === lightboxModal) closeLightbox();
    });
  }

  if (lightboxPrev) {
    lightboxPrev.addEventListener('click', function (e) {
      e.stopPropagation();
      currentLightboxIndex = (currentLightboxIndex - 1 + activeGalleryItems.length) % activeGalleryItems.length;
      showLightboxItem(currentLightboxIndex);
    });
  }

  if (lightboxNext) {
    lightboxNext.addEventListener('click', function (e) {
      e.stopPropagation();
      currentLightboxIndex = (currentLightboxIndex + 1) % activeGalleryItems.length;
      showLightboxItem(currentLightboxIndex);
    });
  }

  document.addEventListener('keydown', function (e) {
    if (!lightboxModal || !lightboxModal.classList.contains('is-active')) return;
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowLeft' && lightboxPrev) lightboxPrev.click();
    if (e.key === 'ArrowRight' && lightboxNext) lightboxNext.click();
  });

  // 9. Contact Form Interactive Validation
  const contactForm = document.getElementById('schoolContactForm');
  const formSuccessAlert = document.getElementById('formSuccessAlert');

  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();

      if (!contactForm.checkValidity()) {
        e.stopPropagation();
        contactForm.classList.add('was-validated');
        return;
      }

      contactForm.classList.add('was-validated');

      // Feedback display without non-existent backend
      if (formSuccessAlert) {
        formSuccessAlert.classList.remove('d-none');
        formSuccessAlert.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }

      contactForm.reset();
      contactForm.classList.remove('was-validated');
    });
  }
});
