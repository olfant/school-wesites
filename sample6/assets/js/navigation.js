/**
 * CM SOE UPG GOVT +2 SCHOOL VNIKETAN HALDIPOKHAR
 * Navigation Controller - Sticky Navbar, Offcanvas Mobile Menu & Dropdowns
 */

document.addEventListener('DOMContentLoaded', () => {
  initMobileNavigation();
  highlightActiveNavLink();
  initStickyHeader();
});

/**
 * Mobile Drawer / Offcanvas Navigation
 */
function initMobileNavigation() {
  const toggler = document.querySelector('.navbar-toggler');
  const collapse = document.querySelector('.navbar-collapse');
  
  if (!toggler || !collapse) return;

  // Create backdrop if not already existing
  let backdrop = document.querySelector('.mobile-nav-backdrop');
  if (!backdrop) {
    backdrop = document.createElement('div');
    backdrop.className = 'mobile-nav-backdrop';
    document.body.appendChild(backdrop);
  }

  // Insert close button inside mobile navbar if not present
  if (!collapse.querySelector('.mobile-menu-close-btn')) {
    const mobileHeader = document.createElement('div');
    mobileHeader.className = 'mobile-menu-header d-lg-none';
    mobileHeader.innerHTML = `
      <div class="d-flex align-items-center gap-2">
        <img src="assets/img/logo/school-logo.svg" alt="School Logo" width="36" height="36">
        <span class="fw-bold text-success font-heading" style="font-size:0.85rem;">CM SOE VNIKETAN</span>
      </div>
      <button type="button" class="mobile-menu-close-btn" aria-label="Close Navigation">
        <i class="bi bi-x-lg"></i>
      </button>
    `;
    collapse.insertBefore(mobileHeader, collapse.firstChild);

    const closeBtn = mobileHeader.querySelector('.mobile-menu-close-btn');
    closeBtn.addEventListener('click', closeMobileNav);
  }

  function openMobileNav() {
    collapse.classList.add('show');
    backdrop.classList.add('show');
    document.body.style.overflow = 'hidden';
  }

  function closeMobileNav() {
    collapse.classList.remove('show');
    backdrop.classList.remove('show');
    document.body.style.overflow = '';
  }

  toggler.addEventListener('click', (e) => {
    e.preventDefault();
    if (collapse.classList.contains('show')) {
      closeMobileNav();
    } else {
      openMobileNav();
    }
  });

  backdrop.addEventListener('click', closeMobileNav);

  // Close on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && collapse.classList.contains('show')) {
      closeMobileNav();
    }
  });

  // Close when clicking nav-links on mobile (except dropdown toggles)
  const navLinks = collapse.querySelectorAll('.nav-link:not(.dropdown-toggle), .dropdown-item');
  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      if (window.innerWidth < 992) {
        closeMobileNav();
      }
    });
  });
}

/**
 * Highlights current page link in navigation
 */
function highlightActiveNavLink() {
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.navbar-nav .nav-link, .dropdown-item');

  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath || (currentPath === '' && href === 'index.html')) {
      link.classList.add('active');
      const parentDropdown = link.closest('.dropdown');
      if (parentDropdown) {
        const toggleBtn = parentDropdown.querySelector('.dropdown-toggle');
        if (toggleBtn) toggleBtn.classList.add('active');
      }
    }
  });
}

/**
 * Sticky Header Scroll Observer
 */
function initStickyHeader() {
  const header = document.querySelector('.site-header');
  if (!header) return;

  const handleScroll = () => {
    if (window.scrollY > 40) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  };

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();
}
