/**
 * CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR
 * Architectural Gallery & Interactive Lightbox Engine
 */

document.addEventListener("DOMContentLoaded", () => {
  initGallery();
});

let currentGalleryList = [];
let currentImageIndex = 0;

function initGallery() {
  const galleryContainer = document.getElementById("galleryGrid");
  const filterBtns = document.querySelectorAll(".gallery-filter-btn");

  // If container exists and has GALLERY_DATA
  if (galleryContainer && window.GALLERY_DATA) {
    currentGalleryList = [...window.GALLERY_DATA];
    renderGalleryItems(currentGalleryList, galleryContainer);

    filterBtns.forEach(btn => {
      btn.addEventListener("click", () => {
        filterBtns.forEach(b => b.classList.remove("active"));
        btn.classList.add("active");

        const filter = btn.getAttribute("data-filter");
        if (filter === "all") {
          currentGalleryList = [...window.GALLERY_DATA];
        } else {
          currentGalleryList = window.GALLERY_DATA.filter(item => item.category === filter);
        }
        renderGalleryItems(currentGalleryList, galleryContainer);
      });
    });
  }

  // Setup Lightbox
  setupLightbox();
}

function renderGalleryItems(items, container) {
  container.innerHTML = "";
  if (items.length === 0) {
    container.innerHTML = `
      <div class="col-12 py-5 text-center">
        <div class="p-4 bg-light border border-success-subtle rounded-0">
          <i class="bi bi-images fs-1 text-secondary mb-3 d-block"></i>
          <h5 class="fw-bold">No gallery records found</h5>
          <p class="text-muted mb-0">Records for this category will be updated as official school photography is archived.</p>
        </div>
      </div>
    `;
    return;
  }

  items.forEach((item, index) => {
    const col = document.createElement("div");
    col.className = "col-lg-4 col-md-6 gallery-item-col mb-4";
    col.setAttribute("data-category", item.category);

    col.innerHTML = `
      <div class="arch-gallery-card position-relative overflow-hidden" data-index="${index}">
        <div class="arch-frame-bracket top-left"></div>
        <div class="arch-frame-bracket bottom-right"></div>
        <div class="gallery-image-wrap position-relative">
          <img src="${item.image}" alt="${item.title}" class="img-fluid w-100 gallery-thumb" loading="lazy" />
          <div class="gallery-overlay d-flex flex-column justify-content-end p-4">
            <span class="gallery-badge text-uppercase mb-2">${item.category}</span>
            <h5 class="gallery-title text-white fw-bold mb-1">${item.title}</h5>
            <p class="gallery-caption text-light small mb-3">${item.caption}</p>
            <div class="d-flex align-items-center justify-content-between pt-2 border-top border-white-50">
              <span class="gallery-num text-white-50 font-monospace">REF #${String(item.id).padStart(3, '0')}</span>
              <button type="button" class="btn btn-sm btn-outline-light rounded-0 px-3 py-1 view-btn" aria-label="Expand image ${item.title}">
                <i class="bi bi-arrows-fullscreen me-1"></i> Expand
              </button>
            </div>
          </div>
        </div>
      </div>
    `;

    // Click handler to open lightbox
    col.querySelector(".arch-gallery-card").addEventListener("click", () => {
      openLightbox(index);
    });

    container.appendChild(col);
  });
}

function setupLightbox() {
  // Check if lightbox modal element exists, if not create it
  let lightbox = document.getElementById("archLightbox");
  if (!lightbox) {
    lightbox = document.createElement("div");
    lightbox.id = "archLightbox";
    lightbox.className = "arch-lightbox-overlay d-none";
    lightbox.innerHTML = `
      <div class="lightbox-dialog position-relative">
        <button type="button" class="lightbox-close" id="lightboxCloseBtn" aria-label="Close Lightbox">
          <i class="bi bi-x-lg"></i>
        </button>
        <button type="button" class="lightbox-nav prev" id="lightboxPrevBtn" aria-label="Previous Image">
          <i class="bi bi-chevron-left"></i>
        </button>
        <button type="button" class="lightbox-nav next" id="lightboxNextBtn" aria-label="Next Image">
          <i class="bi bi-chevron-right"></i>
        </button>
        <div class="lightbox-content text-center">
          <div class="lightbox-media-container position-relative">
            <img src="" id="lightboxImg" alt="" class="img-fluid" />
            <div class="lightbox-corner tl"></div>
            <div class="lightbox-corner tr"></div>
            <div class="lightbox-corner bl"></div>
            <div class="lightbox-corner br"></div>
          </div>
          <div class="lightbox-info mt-3 p-3 text-start bg-dark text-white border-top border-success">
            <div class="d-flex justify-content-between align-items-center mb-1">
              <h5 id="lightboxTitle" class="fw-bold mb-0 text-success-light"></h5>
              <span id="lightboxCounter" class="badge bg-forest font-monospace"></span>
            </div>
            <p id="lightboxCaption" class="text-white-50 small mb-0"></p>
          </div>
        </div>
      </div>
    `;
    document.body.appendChild(lightbox);
  }

  // Attach controls
  const closeBtn = document.getElementById("lightboxCloseBtn");
  const prevBtn = document.getElementById("lightboxPrevBtn");
  const nextBtn = document.getElementById("lightboxNextBtn");

  if (closeBtn) closeBtn.addEventListener("click", closeLightbox);
  if (prevBtn) prevBtn.addEventListener("click", () => navigateLightbox(-1));
  if (nextBtn) nextBtn.addEventListener("click", () => navigateLightbox(1));

  // Overlay click to close
  lightbox.addEventListener("click", (e) => {
    if (e.target === lightbox) {
      closeLightbox();
    }
  });

  // Keyboard navigation
  document.addEventListener("keydown", (e) => {
    if (lightbox.classList.contains("d-none")) return;
    if (e.key === "Escape") closeLightbox();
    if (e.key === "ArrowLeft") navigateLightbox(-1);
    if (e.key === "ArrowRight") navigateLightbox(1);
  });
}

function openLightbox(index) {
  if (!currentGalleryList || currentGalleryList.length === 0) return;
  currentImageIndex = index;
  updateLightboxContent();

  const lightbox = document.getElementById("archLightbox");
  if (lightbox) {
    lightbox.classList.remove("d-none");
    document.body.classList.add("modal-open");
  }
}

function closeLightbox() {
  const lightbox = document.getElementById("archLightbox");
  if (lightbox) {
    lightbox.classList.add("d-none");
    document.body.classList.remove("modal-open");
  }
}

function navigateLightbox(direction) {
  if (!currentGalleryList || currentGalleryList.length === 0) return;
  currentImageIndex = (currentImageIndex + direction + currentGalleryList.length) % currentGalleryList.length;
  updateLightboxContent();
}

function updateLightboxContent() {
  const item = currentGalleryList[currentImageIndex];
  if (!item) return;

  const img = document.getElementById("lightboxImg");
  const title = document.getElementById("lightboxTitle");
  const caption = document.getElementById("lightboxCaption");
  const counter = document.getElementById("lightboxCounter");

  if (img) {
    img.src = item.image;
    img.alt = item.title;
  }
  if (title) title.textContent = item.title;
  if (caption) caption.textContent = item.caption;
  if (counter) counter.textContent = `${currentImageIndex + 1} / ${currentGalleryList.length}`;
}

// Export functions for global use
window.openLightbox = openLightbox;
window.closeLightbox = closeLightbox;
