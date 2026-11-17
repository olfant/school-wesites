/**
 * CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR
 * Prompt 08 - Premium Glassmorphism & Digital Campus Portal
 * Core Interactions: main.js
 */

document.addEventListener("DOMContentLoaded", () => {
  initStickyNavbar();
  initActiveNavLink();
  initFontSizeControls();
  initBackToTop();
  initCopyrightYear();
  initScrollReveal();
  initDigitalClock();
  initContactFormValidation();
});

/* 1. Sticky Glass Navbar */
function initStickyNavbar() {
  const navbar = document.querySelector(".main-navbar");
  if (!navbar) return;

  const handleScroll = () => {
    if (window.scrollY > 40) {
      navbar.classList.add("scrolled");
    } else {
      navbar.classList.remove("scrolled");
    }
  };

  window.addEventListener("scroll", handleScroll, { passive: true });
  handleScroll();
}

/* 2. Active Navigation Link Highlighting */
function initActiveNavLink() {
  const currentPath = window.location.pathname.split("/").pop() || "index.html";
  const navLinks = document.querySelectorAll(".navbar-nav .nav-link, .dropdown-item");

  navLinks.forEach(link => {
    const href = link.getAttribute("href");
    if (!href) return;
    const linkPath = href.split("/").pop();

    if (linkPath === currentPath) {
      link.classList.add("active");
      link.setAttribute("aria-current", "page");

      // Also highlight parent dropdown toggle
      const parentDropdown = link.closest(".dropdown");
      if (parentDropdown) {
        const toggle = parentDropdown.querySelector(".dropdown-toggle");
        if (toggle) toggle.classList.add("active");
      }
    }
  });
}

/* 3. Font Size Accessibility Controls (A-, A, A+) */
function initFontSizeControls() {
  const fsButtons = document.querySelectorAll(".fs-btn");
  if (!fsButtons.length) return;

  const root = document.documentElement;
  const sizes = {
    "-1": "14px",
    "0": "16px",
    "1": "18px"
  };

  fsButtons.forEach(btn => {
    btn.addEventListener("click", () => {
      fsButtons.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      const val = btn.getAttribute("data-fs");
      if (sizes[val]) {
        root.style.fontSize = sizes[val];
      }
    });
  });
}

/* 4. Back-to-Top Floating Button */
function initBackToTop() {
  const topBtn = document.getElementById("toTop");
  if (!topBtn) return;

  const toggleTopBtn = () => {
    if (window.scrollY > 300) {
      topBtn.classList.add("visible");
    } else {
      topBtn.classList.remove("visible");
    }
  };

  window.addEventListener("scroll", toggleTopBtn, { passive: true });
  topBtn.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
}

/* 5. Automatic Dynamic Copyright Year */
function initCopyrightYear() {
  const yearEls = document.querySelectorAll(".current-year");
  const year = new Date().getFullYear();
  yearEls.forEach(el => {
    el.textContent = year;
  });
}

/* 6. IntersectionObserver Lightweight Scroll Reveal */
function initScrollReveal() {
  if (!("IntersectionObserver" in window)) return;

  const revealElements = document.querySelectorAll(".reveal-on-scroll");
  if (!revealElements.length) return;

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        obs.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.12,
    rootMargin: "0px 0px -40px 0px"
  });

  revealElements.forEach(el => observer.observe(el));
}

/* 7. Live Digital Campus Clock (Local Indian Standard Time display) */
function initDigitalClock() {
  const clockEl = document.getElementById("digitalCampusClock");
  if (!clockEl) return;

  const updateClock = () => {
    const now = new Date();
    const options = {
      weekday: "short",
      day: "2-digit",
      month: "short",
      hour: "2-digit",
      minute: "2-digit",
      hour12: true
    };
    clockEl.textContent = now.toLocaleDateString("en-IN", options);
  };

  updateClock();
  setInterval(updateClock, 30000);
}

/* 8. Contact Form Client-Side Validation */
function initContactFormValidation() {
  const form = document.getElementById("schoolContactForm");
  if (!form) return;

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const name = form.querySelector("#contactName");
    const email = form.querySelector("#contactEmail");
    const subject = form.querySelector("#contactSubject");
    const message = form.querySelector("#contactMessage");
    const alertBox = document.getElementById("contactFormAlert");

    if (!name.value.trim() || !email.value.trim() || !subject.value.trim() || !message.value.trim()) {
      showAlert(alertBox, "Please fill out all required fields before submitting.", "warning");
      return;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email.value.trim())) {
      showAlert(alertBox, "Please enter a valid email address.", "danger");
      return;
    }

    // Static site notice & fallback option
    const mailtoLink = `mailto:vnhs.haldipokhar.e.singhbhum@gmail.com?subject=${encodeURIComponent(subject.value)}&body=${encodeURIComponent("From: " + name.value + " (" + email.value + ")\n\n" + message.value)}`;
    
    showAlert(alertBox, `Note: This static website has no backend server. You can click below to dispatch your message via your email client directly to the official school inbox: <br><a href="${mailtoLink}" class="btn-glass-primary mt-2 d-inline-block">Open Mail Client</a>`, "success");
    form.reset();
  });

  function showAlert(target, html, type) {
    if (!target) return;
    target.innerHTML = `<div class="alert alert-${type} mt-3 mb-0" role="alert">${html}</div>`;
  }
}
