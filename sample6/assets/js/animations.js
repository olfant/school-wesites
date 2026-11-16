/**
 * CM SOE UPG GOVT +2 SCHOOL VNIKETAN HALDIPOKHAR
 * Animations & Scroll Reveal Controller
 */

document.addEventListener('DOMContentLoaded', () => {
  initScrollReveal();
  initCounterAnimations();
});

/**
 * Scroll Reveal using IntersectionObserver
 */
function initScrollReveal() {
  const revealElements = document.querySelectorAll('.reveal, .reveal-up, .reveal-left, .reveal-right, .reveal-scale');

  if (!('IntersectionObserver' in window)) {
    // Fallback if IntersectionObserver is not supported
    revealElements.forEach(el => el.classList.add('is-revealed'));
    return;
  }

  const observerOptions = {
    threshold: 0.12,
    rootMargin: '0px 0px -40px 0px'
  };

  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-revealed');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  revealElements.forEach(el => revealObserver.observe(el));
}

/**
 * Animated Statistic Counters
 */
function initCounterAnimations() {
  const counterElements = document.querySelectorAll('[data-counter]');

  if (!counterElements.length) return;

  const counterObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const target = entry.target;
        const targetValue = parseInt(target.getAttribute('data-counter'), 10);
        const suffix = target.getAttribute('data-suffix') || '';
        const duration = 1800; // ms
        const startTime = performance.now();

        function updateCounter(currentTime) {
          const elapsed = currentTime - startTime;
          const progress = Math.min(elapsed / duration, 1);
          // Ease out cubic
          const easedProgress = 1 - Math.pow(1 - progress, 3);
          const currentValue = Math.floor(easedProgress * targetValue);

          target.textContent = currentValue + suffix;

          if (progress < 1) {
            requestAnimationFrame(updateCounter);
          } else {
            target.textContent = targetValue + suffix;
          }
        }

        requestAnimationFrame(updateCounter);
        observer.unobserve(target);
      }
    });
  }, { threshold: 0.25 });

  counterElements.forEach(el => counterObserver.observe(el));
}
