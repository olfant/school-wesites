/* ==========================================================================
   CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR
   GALLERY & LIGHTBOX VIEWER
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  initGalleryFilterAndLightbox();
});

function initGalleryFilterAndLightbox() {
  const filterButtons = document.querySelectorAll('.gallery-filter-pill');
  const galleryItems = document.querySelectorAll('.gallery-card-item');
  const lightboxModalEl = document.getElementById('galleryLightboxModal');

  if (!galleryItems.length) return;

  // Category Filtering
  filterButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      filterButtons.forEach(b => {
        b.classList.remove('active');
        b.setAttribute('aria-pressed', 'false');
      });
      btn.classList.add('active');
      btn.setAttribute('aria-pressed', 'true');

      const filterCategory = btn.getAttribute('data-filter');

      galleryItems.forEach(item => {
        const itemCat = item.getAttribute('data-category');
        if (filterCategory === 'all' || itemCat === filterCategory) {
          item.style.display = 'block';
          item.classList.add('reveal-fade-up', 'is-revealed');
        } else {
          item.style.display = 'none';
        }
      });
    });
  });

  // Lightbox Logic
  if (!lightboxModalEl) return;
  const lbModal = new bootstrap.Modal(lightboxModalEl);
  const lbImg = document.getElementById('lightboxImg');
  const lbTitle = document.getElementById('lightboxTitle');
  const lbCaption = document.getElementById('lightboxCaption');
  const lbCounter = document.getElementById('lightboxCounter');
  const lbPrev = document.getElementById('lightboxPrevBtn');
  const lbNext = document.getElementById('lightboxNextBtn');

  let activeList = [];
  let currentIndex = 0;

  function updateLightbox(index) {
    currentIndex = (index + activeList.length) % activeList.length;
    const currentItem = activeList[currentIndex];
    const src = currentItem.getAttribute('data-src');
    const title = currentItem.getAttribute('data-title') || 'Gallery Photo';
    const caption = currentItem.getAttribute('data-caption') || '';

    if (lbImg) {
      lbImg.src = src;
      lbImg.alt = title;
    }
    if (lbTitle) lbTitle.textContent = title;
    if (lbCaption) lbCaption.textContent = caption;
    if (lbCounter) lbCounter.textContent = `${currentIndex + 1} of ${activeList.length}`;

    if (lbPrev && lbNext) {
      lbPrev.disabled = activeList.length <= 1;
      lbNext.disabled = activeList.length <= 1;
    }
  }

  galleryItems.forEach(item => {
    item.addEventListener('click', (e) => {
      e.preventDefault();
      // Get all currently visible items
      activeList = Array.from(document.querySelectorAll('.gallery-card-item')).filter(
        el => window.getComputedStyle(el).display !== 'none'
      );
      currentIndex = activeList.indexOf(item);
      if (currentIndex === -1) currentIndex = 0;

      updateLightbox(currentIndex);
      lbModal.show();
    });
  });

  if (lbPrev) {
    lbPrev.addEventListener('click', () => updateLightbox(currentIndex - 1));
  }
  if (lbNext) {
    lbNext.addEventListener('click', () => updateLightbox(currentIndex + 1));
  }

  // Keyboard Navigation
  lightboxModalEl.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft') updateLightbox(currentIndex - 1);
    if (e.key === 'ArrowRight') updateLightbox(currentIndex + 1);
  });
}
