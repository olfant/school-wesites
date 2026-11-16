/**
 * ====================================================================
 * +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय, हल्दीपोखर
 * INTERACTIVE CINEMATIC GALLERY & LIGHTBOX ENGINE
 * Version 4 — Cinematic Campus Storytelling Edition
 * ====================================================================
 */

document.addEventListener('DOMContentLoaded', () => {
  initGalleryFiltering();
  initCinematicLightbox();
});

/* ====================================================================
   1. GALLERY CATEGORY FILTERING
   ==================================================================== */
function initGalleryFiltering() {
  const filterBtns = document.querySelectorAll('.gallery-filter-btn');
  const galleryItems = document.querySelectorAll('.gallery-grid-item');

  if (!filterBtns.length || !galleryItems.length) return;

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const selectedCategory = btn.getAttribute('data-filter') || 'all';

      galleryItems.forEach(item => {
        const itemCategory = item.getAttribute('data-category') || '';

        if (selectedCategory === 'all' || itemCategory === selectedCategory) {
          item.style.display = 'block';
          item.classList.add('fadeIn');
        } else {
          item.style.display = 'none';
          item.classList.remove('fadeIn');
        }
      });
    });
  });
}

/* ====================================================================
   2. CINEMATIC LIGHTBOX MODAL WITH FULL CONTROLS
   ==================================================================== */
function initCinematicLightbox() {
  const lightboxModal = document.querySelector('.cinematic-lightbox-modal');
  const galleryCards = document.querySelectorAll('.lightbox-trigger');

  if (!lightboxModal || !galleryCards.length) return;

  const renderImg = lightboxModal.querySelector('.lightbox-img-render');
  const titleEl = lightboxModal.querySelector('.lightbox-title');
  const captionEl = lightboxModal.querySelector('.lightbox-caption');
  const counterEl = lightboxModal.querySelector('.lightbox-counter');
  const closeBtn = lightboxModal.querySelector('.lightbox-close-btn');
  const prevBtn = lightboxModal.querySelector('.lightbox-prev');
  const nextBtn = lightboxModal.querySelector('.lightbox-next');

  let activeIndex = 0;
  let visibleCards = [];

  const updateVisibleList = () => {
    visibleCards = Array.from(galleryCards).filter(card => {
      const parent = card.closest('.gallery-grid-item');
      return !parent || parent.style.display !== 'none';
    });
  };

  const showImage = (index) => {
    updateVisibleList();
    if (!visibleCards.length) return;

    if (index < 0) index = visibleCards.length - 1;
    if (index >= visibleCards.length) index = 0;

    activeIndex = index;
    const card = visibleCards[activeIndex];

    const imgSrc = card.getAttribute('data-src') || card.querySelector('img')?.getAttribute('src');
    const title = card.getAttribute('data-title') || 'Campus Photograph';
    const caption = card.getAttribute('data-caption') || '+2 राजकीयकृत विद्या निकेतन उच्च विद्यालय, हल्दीपोखर';

    if (renderImg) renderImg.src = imgSrc;
    if (titleEl) titleEl.textContent = title;
    if (captionEl) captionEl.textContent = caption;
    if (counterEl) counterEl.textContent = `${activeIndex + 1} / ${visibleCards.length}`;

    lightboxModal.classList.add('active');
    document.body.style.overflow = 'hidden';
  };

  const closeLightbox = () => {
    lightboxModal.classList.remove('active');
    document.body.style.overflow = '';
  };

  galleryCards.forEach(card => {
    card.addEventListener('click', (e) => {
      e.preventDefault();
      updateVisibleList();
      const cardIndex = visibleCards.indexOf(card);
      showImage(cardIndex !== -1 ? cardIndex : 0);
    });
  });

  if (closeBtn) closeBtn.addEventListener('click', closeLightbox);
  if (prevBtn) prevBtn.addEventListener('click', () => showImage(activeIndex - 1));
  if (nextBtn) nextBtn.addEventListener('click', () => showImage(activeIndex + 1));

  lightboxModal.addEventListener('click', (e) => {
    if (e.target === lightboxModal) {
      closeLightbox();
    }
  });

  document.addEventListener('keydown', (e) => {
    if (!lightboxModal.classList.contains('active')) return;

    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowLeft') showImage(activeIndex - 1);
    if (e.key === 'ArrowRight') showImage(activeIndex + 1);
  });
}
