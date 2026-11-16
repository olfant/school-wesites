/**
 * ====================================================================
 * GALLERY JAVASCRIPT — FILTERING & SWISS LIGHTBOX MODAL
 * CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR, हल्दीपोखर
 * ====================================================================
 */

document.addEventListener('DOMContentLoaded', () => {
  initGalleryFiltering();
  initGalleryLightbox();
});

function initGalleryFiltering() {
  const filterBtns = document.querySelectorAll('.gallery-filter-btn');
  const galleryItems = document.querySelectorAll('.gallery-item-card');

  if (!filterBtns.length || !galleryItems.length) return;

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filterVal = btn.getAttribute('data-filter');

      galleryItems.forEach(item => {
        const itemCat = item.getAttribute('data-category');
        if (filterVal === 'all' || itemCat === filterVal) {
          item.style.display = 'block';
          item.style.opacity = '0';
          setTimeout(() => {
            item.style.opacity = '1';
            item.style.transition = 'opacity 0.3s ease';
          }, 20);
        } else {
          item.style.display = 'none';
        }
      });
    });
  });
}

function initGalleryLightbox() {
  const galleryCards = document.querySelectorAll('.gallery-item-card');
  const lightbox = document.getElementById('swissLightboxModal');
  if (!lightbox) return;

  const lightboxImg = lightbox.querySelector('.lightbox-current-img');
  const lightboxCaption = lightbox.querySelector('.lightbox-caption-text');
  const lightboxCounter = lightbox.querySelector('.lightbox-counter');
  const closeBtn = lightbox.querySelector('.lightbox-close-btn');
  const prevBtn = lightbox.querySelector('.lightbox-prev-btn');
  const nextBtn = lightbox.querySelector('.lightbox-next-btn');

  let activeIndex = 0;
  let currentList = [];

  const updateCurrentList = () => {
    currentList = Array.from(document.querySelectorAll('.gallery-item-card')).filter(item => {
      return window.getComputedStyle(item).display !== 'none';
    });
  };

  const showImage = (index) => {
    if (!currentList.length) return;
    if (index < 0) index = currentList.length - 1;
    if (index >= currentList.length) index = 0;

    activeIndex = index;
    const card = currentList[activeIndex];
    const imgEl = card.querySelector('img');
    const title = card.getAttribute('data-title') || imgEl.getAttribute('alt') || 'School Gallery';
    const caption = card.getAttribute('data-caption') || '';

    if (lightboxImg && imgEl) {
      lightboxImg.src = imgEl.src;
      lightboxImg.alt = title;
    }

    if (lightboxCaption) {
      lightboxCaption.innerHTML = `<strong>${title}</strong> — <span>${caption}</span>`;
    }

    if (lightboxCounter) {
      lightboxCounter.textContent = `${activeIndex + 1} / ${currentList.length}`;
    }
  };

  const openLightbox = (card) => {
    updateCurrentList();
    const index = currentList.indexOf(card);
    showImage(index >= 0 ? index : 0);

    lightbox.classList.add('is-active');
    document.body.style.overflow = 'hidden';
  };

  const closeLightbox = () => {
    lightbox.classList.remove('is-active');
    document.body.style.overflow = '';
  };

  galleryCards.forEach(card => {
    card.addEventListener('click', () => openLightbox(card));
  });

  if (closeBtn) closeBtn.addEventListener('click', closeLightbox);
  if (prevBtn) prevBtn.addEventListener('click', () => showImage(activeIndex - 1));
  if (nextBtn) nextBtn.addEventListener('click', () => showImage(activeIndex + 1));

  // Close when clicking backdrop outside stage
  lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) closeLightbox();
  });

  // Keyboard navigation
  document.addEventListener('keydown', (e) => {
    if (!lightbox.classList.contains('is-active')) return;
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowLeft') showImage(activeIndex - 1);
    if (e.key === 'ArrowRight') showImage(activeIndex + 1);
  });
}
