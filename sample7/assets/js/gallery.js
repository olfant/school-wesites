/**
 * Gallery Rendering, Category Filtering & Lightbox Controller
 * CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR
 */

(function () {
  "use strict";

  let activeGalleryItems = [];
  let currentLightboxIndex = 0;

  function initGallery() {
    const galleryGrid = document.getElementById("galleryGrid");
    const filterButtons = document.querySelectorAll(".gallery-filter-btn");

    if (!galleryGrid || !window.SCHOOL_DATA || !window.SCHOOL_DATA.gallery) {
      return;
    }

    activeGalleryItems = [...window.SCHOOL_DATA.gallery];
    renderGallery(activeGalleryItems);

    filterButtons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        filterButtons.forEach(b => b.classList.remove("active"));
        this.classList.add("active");

        const category = this.getAttribute("data-filter");
        if (category === "all") {
          activeGalleryItems = [...window.SCHOOL_DATA.gallery];
        } else {
          activeGalleryItems = window.SCHOOL_DATA.gallery.filter(item => item.category === category);
        }

        renderGallery(activeGalleryItems);
      });
    });

    initLightboxEvents();
  }

  function renderGallery(items) {
    const galleryGrid = document.getElementById("galleryGrid");
    if (!galleryGrid) return;

    if (items.length === 0) {
      galleryGrid.innerHTML = `
        <div class="col-12 text-center py-5">
          <div class="p-4 bg-light rounded-4 border">
            <i class="bi bi-images text-muted fs-1 mb-2 d-block"></i>
            <p class="text-muted mb-0">No photographs found under this category.</p>
          </div>
        </div>
      `;
      return;
    }

    let html = "";
    items.forEach(function (item, index) {
      // Determine if on inner page or homepage to adjust relative asset path
      const isInPagesDir = window.location.pathname.includes("/pages/");
      const assetPrefix = isInPagesDir ? "../" : "";

      html += `
        <div class="col-md-6 col-lg-4 gallery-card-col reveal-up" style="animation-delay: ${index * 0.05}s">
          <div class="organic-gallery-card h-100" data-index="${index}" role="button" tabindex="0" aria-label="View photo: ${item.title}">
            <div class="organic-img-wrap">
              <img src="${assetPrefix}${item.src}" alt="${item.title}" class="img-fluid gallery-thumb" loading="lazy">
              <span class="gallery-category-pill">${item.category.toUpperCase()}</span>
              <div class="gallery-overlay">
                <span class="zoom-btn"><i class="bi bi-zoom-in"></i></span>
              </div>
            </div>
            <div class="gallery-info p-3">
              <h3 class="h6 fw-bold text-deep-green mb-1">${item.title}</h3>
              <p class="small text-secondary-green mb-0 text-truncate">${item.caption}</p>
            </div>
          </div>
        </div>
      `;
    });

    galleryGrid.innerHTML = html;

    // Attach click events to freshly rendered cards
    const cards = galleryGrid.querySelectorAll(".organic-gallery-card");
    cards.forEach(function (card) {
      card.addEventListener("click", function () {
        const idx = parseInt(this.getAttribute("data-index"), 10);
        openLightbox(idx);
      });
      card.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          const idx = parseInt(this.getAttribute("data-index"), 10);
          openLightbox(idx);
        }
      });
    });
  }

  function openLightbox(index) {
    if (activeGalleryItems.length === 0) return;
    currentLightboxIndex = index;
    updateLightboxContent();

    const lightboxModalEl = document.getElementById("galleryLightboxModal");
    if (lightboxModalEl && typeof bootstrap !== "undefined") {
      const modal = bootstrap.Modal.getOrCreateInstance(lightboxModalEl);
      modal.show();
    }
  }

  function updateLightboxContent() {
    const item = activeGalleryItems[currentLightboxIndex];
    if (!item) return;

    const isInPagesDir = window.location.pathname.includes("/pages/");
    const assetPrefix = isInPagesDir ? "../" : "";

    const titleEl = document.getElementById("lbTitle");
    const imgEl = document.getElementById("lbImg");
    const captionEl = document.getElementById("lbCaption");
    const counterEl = document.getElementById("lbCounter");
    const badgeEl = document.getElementById("lbBadge");

    if (titleEl) titleEl.textContent = item.title;
    if (imgEl) {
      imgEl.src = assetPrefix + item.src;
      imgEl.alt = item.title;
    }
    if (captionEl) captionEl.textContent = item.caption;
    if (badgeEl) badgeEl.textContent = item.category.toUpperCase();
    if (counterEl) counterEl.textContent = `${currentLightboxIndex + 1} / ${activeGalleryItems.length}`;
  }

  function nextImage() {
    if (activeGalleryItems.length === 0) return;
    currentLightboxIndex = (currentLightboxIndex + 1) % activeGalleryItems.length;
    updateLightboxContent();
  }

  function prevImage() {
    if (activeGalleryItems.length === 0) return;
    currentLightboxIndex = (currentLightboxIndex - 1 + activeGalleryItems.length) % activeGalleryItems.length;
    updateLightboxContent();
  }

  function initLightboxEvents() {
    const nextBtn = document.getElementById("lbNextBtn");
    const prevBtn = document.getElementById("lbPrevBtn");

    if (nextBtn) {
      nextBtn.addEventListener("click", function (e) {
        e.preventDefault();
        nextImage();
      });
    }

    if (prevBtn) {
      prevBtn.addEventListener("click", function (e) {
        e.preventDefault();
        prevImage();
      });
    }

    // Keyboard navigation
    document.addEventListener("keydown", function (e) {
      const lightboxModalEl = document.getElementById("galleryLightboxModal");
      if (lightboxModalEl && lightboxModalEl.classList.contains("show")) {
        if (e.key === "ArrowRight") {
          nextImage();
        } else if (e.key === "ArrowLeft") {
          prevImage();
        }
      }
    });
  }

  // Self-initialize on DOM ready
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initGallery);
  } else {
    initGallery();
  }
})();
