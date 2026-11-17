/**
 * CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR
 * Prompt 08 - Premium Glassmorphism & Digital Campus Portal
 * Photo Gallery & Lightbox: gallery.js
 */

document.addEventListener("DOMContentLoaded", () => {
  initGalleryFilter();
  initGalleryLightbox();
});

/* 1. Category Filtering */
function initGalleryFilter() {
  const filterBtns = document.querySelectorAll(".gallery-filter-btn");
  const galleryItems = document.querySelectorAll(".gallery-card-item");

  if (!galleryItems.length || !filterBtns.length) return;

  filterBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      filterBtns.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");

      const category = btn.getAttribute("data-filter");

      galleryItems.forEach(item => {
        const itemCat = item.getAttribute("data-category");
        if (category === "all" || itemCat === category) {
          item.style.display = "";
          item.classList.add("fade-in");
        } else {
          item.style.display = "none";
        }
      });
    });
  });
}

/* 2. Full-Screen Glass Lightbox Modal with Controls */
function initGalleryLightbox() {
  const modalEl = document.getElementById("galleryLightboxModal");
  if (!modalEl) return;

  const modalImg = modalEl.querySelector("#lightboxModalImg");
  const modalTitle = modalEl.querySelector("#lightboxModalTitle");
  const modalCat = modalEl.querySelector("#lightboxModalCategory");
  const prevBtn = modalEl.querySelector("#lightboxPrevBtn");
  const nextBtn = modalEl.querySelector("#lightboxNextBtn");

  const galleryItems = Array.from(document.querySelectorAll(".gallery-lightbox-trigger"));
  if (!galleryItems.length) return;

  let currentIndex = 0;

  const updateLightboxContent = (index) => {
    if (index < 0) index = galleryItems.length - 1;
    if (index >= galleryItems.length) index = 0;
    currentIndex = index;

    const currentTrigger = galleryItems[currentIndex];
    const imgSrc = currentTrigger.getAttribute("data-img") || currentTrigger.querySelector("img")?.getAttribute("src");
    const title = currentTrigger.getAttribute("data-title") || "School Activity";
    const category = currentTrigger.getAttribute("data-category") || "Campus Life";

    if (modalImg) {
      modalImg.src = imgSrc;
      modalImg.alt = title;
    }
    if (modalTitle) modalTitle.textContent = title;
    if (modalCat) modalCat.textContent = category;
  };

  galleryItems.forEach((trigger, index) => {
    trigger.addEventListener("click", (e) => {
      e.preventDefault();
      updateLightboxContent(index);
    });
  });

  if (prevBtn) {
    prevBtn.addEventListener("click", () => {
      updateLightboxContent(currentIndex - 1);
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener("click", () => {
      updateLightboxContent(currentIndex + 1);
    });
  }

  // Keyboard navigation
  document.addEventListener("keydown", (e) => {
    if (!modalEl.classList.contains("show")) return;
    if (e.key === "ArrowLeft") {
      updateLightboxContent(currentIndex - 1);
    } else if (e.key === "ArrowRight") {
      updateLightboxContent(currentIndex + 1);
    }
  });
}
