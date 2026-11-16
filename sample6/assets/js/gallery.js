/**
 * CM SOE UPG GOVT +2 SCHOOL VNIKETAN HALDIPOKHAR
 * Gallery & Lightbox Controller
 */

document.addEventListener('DOMContentLoaded', () => {
  initGalleryFiltering();
  initLightbox();
});

let currentGalleryItems = [];
let currentLightboxIndex = 0;

/**
 * Filter Gallery by Category Tabs
 */
function initGalleryFiltering() {
  const filterButtons = document.querySelectorAll('.gallery-filter-btn');
  const galleryItems = document.querySelectorAll('.gallery-grid-item');

  if (!filterButtons.length || !galleryItems.length) return;

  filterButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      // Update active state
      filterButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filterValue = btn.getAttribute('data-filter');

      galleryItems.forEach(item => {
        const category = item.getAttribute('data-category');
        if (filterValue === 'all' || category === filterValue) {
          item.style.display = 'block';
          setTimeout(() => {
            item.style.opacity = '1';
            item.style.transform = 'scale(1)';
          }, 50);
        } else {
          item.style.opacity = '0';
          item.style.transform = 'scale(0.95)';
          setTimeout(() => {
            item.style.display = 'none';
          }, 250);
        }
      });
    });
  });
}

/**
 * Lightbox Modal with Next / Prev and Touch/Keyboard Support
 */
function initLightbox() {
  // Ensure Lightbox DOM exists
  let modal = document.getElementById('schoolLightbox');
  if (!modal) {
    modal = document.createElement('div');
    modal.id = 'schoolLightbox';
    modal.className = 'lightbox-modal';
    modal.setAttribute('role', 'dialog');
    modal.setAttribute('aria-modal', 'true');
    modal.setAttribute('aria-label', 'Image Lightbox');
    modal.innerHTML = `
      <button class="lightbox-close-btn" aria-label="Close Lightbox"><i class="bi bi-x-lg"></i></button>
      <button class="lightbox-nav-btn lightbox-prev-btn" aria-label="Previous Image"><i class="bi bi-chevron-left"></i></button>
      <button class="lightbox-nav-btn lightbox-next-btn" aria-label="Next Image"><i class="bi bi-chevron-right"></i></button>
      <div class="lightbox-content">
        <img src="" alt="" class="lightbox-image" id="lightboxImg">
        <div class="lightbox-caption" id="lightboxCaption"></div>
      </div>
    `;
    document.body.appendChild(modal);
  }

  const lightboxImg = document.getElementById('lightboxImg');
  const lightboxCaption = document.getElementById('lightboxCaption');
  const closeBtn = modal.querySelector('.lightbox-close-btn');
  const prevBtn = modal.querySelector('.lightbox-prev-btn');
  const nextBtn = modal.querySelector('.lightbox-next-btn');

  // Collect all clickable gallery triggers
  function updateGalleryTriggers() {
    const clickableItems = Array.from(document.querySelectorAll('.gallery-item, [data-lightbox]')).filter(el => {
      return window.getComputedStyle(el.closest('.gallery-grid-item') || el).display !== 'none';
    });
    return clickableItems;
  }

  function showImage(index) {
    currentGalleryItems = updateGalleryTriggers();
    if (index < 0) index = currentGalleryItems.length - 1;
    if (index >= currentGalleryItems.length) index = 0;
    currentLightboxIndex = index;

    const item = currentGalleryItems[index];
    const imgEl = item.querySelector('img') || item;
    const fullSrc = item.getAttribute('data-full') || imgEl.getAttribute('src');
    const caption = item.getAttribute('data-caption') || imgEl.getAttribute('alt') || 'School Gallery Preview';

    lightboxImg.src = fullSrc;
    lightboxImg.alt = caption;
    lightboxCaption.textContent = caption;
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    modal.classList.remove('active');
    document.body.style.overflow = '';
    lightboxImg.src = '';
  }

  // Delegated click on gallery items
  document.addEventListener('click', (e) => {
    const trigger = e.target.closest('.gallery-item, [data-lightbox]');
    if (trigger) {
      e.preventDefault();
      currentGalleryItems = updateGalleryTriggers();
      const index = currentGalleryItems.indexOf(trigger);
      showImage(index >= 0 ? index : 0);
    }
  });

  closeBtn.addEventListener('click', closeLightbox);
  prevBtn.addEventListener('click', () => showImage(currentLightboxIndex - 1));
  nextBtn.addEventListener('click', () => showImage(currentLightboxIndex + 1));

  // Close on clicking outside content
  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      closeLightbox();
    }
  });

  // Keyboard navigation
  document.addEventListener('keydown', (e) => {
    if (!modal.classList.contains('active')) return;
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowLeft') showImage(currentLightboxIndex - 1);
    if (e.key === 'ArrowRight') showImage(currentLightboxIndex + 1);
  });
}
