/**
 * CM SOE UPG GOVT +2 SCHOOL VNIKETAN HALDIPOKHAR
 * Main Application Orchestrator
 */

document.addEventListener('DOMContentLoaded', () => {
  initBackToTop();
  injectCurrentYear();
  initDownloadHandlers();
  initBootstrapComponents();
});

/**
 * Back to Top Floating Button
 */
function initBackToTop() {
  const backToTopBtn = document.querySelector('.back-to-top');
  if (!backToTopBtn) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
      backToTopBtn.classList.add('active');
    } else {
      backToTopBtn.classList.remove('active');
    }
  }, { passive: true });

  backToTopBtn.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
}

/**
 * Automatically updates current year in footer
 */
function injectCurrentYear() {
  const yearSpans = document.querySelectorAll('.current-year');
  const currentYear = new Date().getFullYear();
  yearSpans.forEach(span => {
    span.textContent = currentYear;
  });
}

/**
 * Friendly notification for Download buttons
 */
function initDownloadHandlers() {
  const downloadButtons = document.querySelectorAll('[data-download-name]');
  downloadButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      const docName = btn.getAttribute('data-download-name') || 'Document';
      console.log(`Institutional Document Download requested: ${docName}`);
    });
  });
}

/**
 * Initialize Bootstrap Tooltips / Popovers if library is present
 */
function initBootstrapComponents() {
  if (window.bootstrap && bootstrap.Tooltip) {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));
  }
}
