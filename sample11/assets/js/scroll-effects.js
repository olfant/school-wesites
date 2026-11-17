/* ==========================================================================
   CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR
   SCROLL EFFECTS & PARALLAX ENGINE
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  initScrollProgressBar();
  initIntersectionObserverReveals();
  initParallaxEffects();
  initTimelineScrollSync();
  initHorizontalScrollDrag();
});

/* Top Reading Progress Bar */
function initScrollProgressBar() {
  const bar = document.getElementById('scrollProgress');
  if (!bar) return;

  const updateBar = () => {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const scrollPercent = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    bar.style.width = `${scrollPercent}%`;
  };

  window.addEventListener('scroll', updateBar, { passive: true });
  updateBar();
}

/* Scroll-Triggered Section & Element Reveals */
function initIntersectionObserverReveals() {
  const revealElements = document.querySelectorAll('.reveal-fade-up, .reveal-fade-in, .reveal-scale-in');
  if (!revealElements.length) return;

  // If user prefers reduced motion, reveal immediately
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    revealElements.forEach(el => el.classList.add('is-revealed'));
    return;
  }

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-revealed');
        obs.unobserve(entry.target);
      }
    });
  }, {
    root: null,
    threshold: 0.12,
    rootMargin: '0px 0px -40px 0px'
  });

  revealElements.forEach(el => observer.observe(el));
}

/* Subtle Hero & Background Parallax Motion */
function initParallaxEffects() {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  if (window.innerWidth < 992) return; // Disable intensive parallax on mobile/tablet

  const heroScene = document.querySelector('.hero-scene-3d');
  const heroGrid = document.querySelector('.hero-3d-grid-bg');

  if (!heroScene && !heroGrid) return;

  let ticking = false;

  window.addEventListener('scroll', () => {
    if (!ticking) {
      window.requestAnimationFrame(() => {
        const scrolled = window.scrollY;
        if (scrolled < window.innerHeight) {
          if (heroScene) {
            heroScene.style.transform = `translateY(${scrolled * 0.14}px) rotateX(${scrolled * 0.02}deg)`;
          }
          if (heroGrid) {
            heroGrid.style.transform = `translateY(${scrolled * 0.25}px)`;
          }
        }
        ticking = false;
      });
      ticking = true;
    }
  }, { passive: true });
}

/* Interactive Timeline Node Highlight on Scroll */
function initTimelineScrollSync() {
  const timelineNodes = document.querySelectorAll('.timeline-node-item');
  if (!timelineNodes.length) return;

  const timelineBar = document.querySelector('.timeline-progress-bar-fill');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active-node');
        const nodeIndex = Array.from(timelineNodes).indexOf(entry.target);
        if (timelineBar) {
          const fillPercent = ((nodeIndex + 1) / timelineNodes.length) * 100;
          timelineBar.style.width = `${fillPercent}%`;
        }
      }
    });
  }, { threshold: 0.5 });

  timelineNodes.forEach(node => observer.observe(node));
}

/* Horizontal Scroll Showcase Helper */
function initHorizontalScrollDrag() {
  const track = document.querySelector('.horizontal-scroll-container');
  if (!track) return;

  const prevBtn = document.getElementById('horizPrevBtn');
  const nextBtn = document.getElementById('horizNextBtn');

  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      track.scrollBy({ left: -360, behavior: 'smooth' });
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      track.scrollBy({ left: 360, behavior: 'smooth' });
    });
  }
}
