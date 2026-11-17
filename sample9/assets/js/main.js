/**
 * CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR
 * Architectural Geometry + Isometric Campus Interactions
 * Core System Engine (main.js)
 */

document.addEventListener("DOMContentLoaded", () => {
  initStickyNavbar();
  initMobileDrawer();
  initActiveNavLink();
  initAccessibilityControls();
  initScrollAnimations();
  initBackToTop();
  initCopyrightYear();
  initDevelopmentDiagram();
  initContactForm();
});

/* ==========================================================================
   1. Sticky Navbar
   ========================================================================== */
function initStickyNavbar() {
  const navbar = document.getElementById("mainNavbar");
  if (!navbar) return;

  const handleScroll = () => {
    if (window.scrollY > 80) {
      navbar.classList.add("navbar-sticky", "shadow-sm");
    } else {
      navbar.classList.remove("navbar-sticky", "shadow-sm");
    }
  };

  window.addEventListener("scroll", handleScroll, { passive: true });
  handleScroll();
}

/* ==========================================================================
   2. Mobile Drawer Navigation
   ========================================================================== */
function initMobileDrawer() {
  const toggleBtn = document.getElementById("mobileNavToggle");
  const closeBtn = document.getElementById("mobileDrawerClose");
  const drawer = document.getElementById("mobileNavDrawer");
  const backdrop = document.getElementById("mobileNavBackdrop");

  if (!toggleBtn || !drawer) return;

  const openDrawer = () => {
    drawer.classList.add("show");
    if (backdrop) backdrop.classList.add("show");
    document.body.classList.add("drawer-open");
    toggleBtn.setAttribute("aria-expanded", "true");
  };

  const closeDrawer = () => {
    drawer.classList.remove("show");
    if (backdrop) backdrop.classList.remove("show");
    document.body.classList.remove("drawer-open");
    toggleBtn.setAttribute("aria-expanded", "false");
  };

  toggleBtn.addEventListener("click", openDrawer);
  if (closeBtn) closeBtn.addEventListener("click", closeDrawer);
  if (backdrop) backdrop.addEventListener("click", closeDrawer);

  // Close drawer when clicking internal link
  const navLinks = drawer.querySelectorAll("a:not(.dropdown-toggle)");
  navLinks.forEach(link => {
    link.addEventListener("click", closeDrawer);
  });

  // Escape key close
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && drawer.classList.contains("show")) {
      closeDrawer();
    }
  });
}

/* ==========================================================================
   3. Active Navigation Item Highlighting
   ========================================================================== */
function initActiveNavLink() {
  const currentPath = window.location.pathname.split("/").pop() || "index.html";
  const navLinks = document.querySelectorAll(".nav-link, .dropdown-item, .mobile-nav-link");

  navLinks.forEach(link => {
    const href = link.getAttribute("href");
    if (!href) return;
    const linkPath = href.split("/").pop();

    if (linkPath === currentPath) {
      link.classList.add("active");
      const parentDropdown = link.closest(".dropdown");
      if (parentDropdown) {
        const toggle = parentDropdown.querySelector(".dropdown-toggle");
        if (toggle) toggle.classList.add("active");
      }
    }
  });
}

/* ==========================================================================
   4. Accessibility Font Size Controls
   ========================================================================== */
function initAccessibilityControls() {
  const decreaseBtn = document.getElementById("fontDecreaseBtn");
  const resetBtn = document.getElementById("fontResetBtn");
  const increaseBtn = document.getElementById("fontIncreaseBtn");
  const root = document.documentElement;

  const fontSizes = ["font-size-sm", "font-size-md", "font-size-lg"];
  let currentIndex = 1; // default font-size-md

  const applyFontSize = (idx) => {
    fontSizes.forEach(cls => root.classList.remove(cls));
    root.classList.add(fontSizes[idx]);
    currentIndex = idx;
    localStorage.setItem("cmsoe_font_size", idx);
  };

  // Check saved state
  const saved = localStorage.getItem("cmsoe_font_size");
  if (saved !== null) {
    const idx = parseInt(saved, 10);
    if (!isNaN(idx) && idx >= 0 && idx <= 2) {
      applyFontSize(idx);
    }
  }

  if (decreaseBtn) {
    decreaseBtn.addEventListener("click", (e) => {
      e.preventDefault();
      if (currentIndex > 0) applyFontSize(currentIndex - 1);
    });
  }

  if (resetBtn) {
    resetBtn.addEventListener("click", (e) => {
      e.preventDefault();
      applyFontSize(1);
    });
  }

  if (increaseBtn) {
    increaseBtn.addEventListener("click", (e) => {
      e.preventDefault();
      if (currentIndex < 2) applyFontSize(currentIndex + 1);
    });
  }
}

/* ==========================================================================
   5. Scroll Reveal Animations (IntersectionObserver)
   ========================================================================== */
function initScrollAnimations() {
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    document.querySelectorAll(".reveal-fade, .reveal-up, .reveal-scale").forEach(el => {
      el.classList.add("revealed");
    });
    return;
  }

  const revealElements = document.querySelectorAll(".reveal-fade, .reveal-up, .reveal-scale, .arch-section-number, .arch-card, .foundation-card");

  if (!("IntersectionObserver" in window)) {
    revealElements.forEach(el => el.classList.add("revealed"));
    return;
  }

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("revealed");
        obs.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: "0px 0px -40px 0px"
  });

  revealElements.forEach(el => observer.observe(el));
}

/* ==========================================================================
   6. Student Development Framework Interactive Diagram
   ========================================================================== */
function initDevelopmentDiagram() {
  const markers = document.querySelectorAll(".diagram-marker-item");
  const stageDisplayTitle = document.getElementById("stageDisplayTitle");
  const stageDisplayDesc = document.getElementById("stageDisplayDesc");

  if (!markers.length || !stageDisplayTitle || !stageDisplayDesc) return;

  const stageDescriptions = {
    knowledge: {
      title: "01. Knowledge",
      desc: "Scholastic rigor, factual comprehension, scientific curiosity and conceptual mastery across academic disciplines."
    },
    understanding: {
      title: "02. Understanding",
      desc: "Deep cognitive grasp, critical reasoning, contextual analysis, and synthesis of principles in real-life problems."
    },
    creativity: {
      title: "03. Creativity",
      desc: "Original expression, scientific experimentation, artistic endeavors, and innovative vocational design thinking."
    },
    communication: {
      title: "04. Communication",
      desc: "Articulate linguistic clarity, active listening, respectful discourse, and confident presentation abilities."
    },
    leadership: {
      title: "05. Leadership",
      desc: "Ethical initiative, teamwork coordination, Bharat Scouts and Guides discipline, and peer motivation."
    },
    responsibility: {
      title: "06. Responsibility",
      desc: "Civic consciousness, environmental care, moral integrity, community duty, and commitment to institutional values."
    }
  };

  markers.forEach(marker => {
    marker.addEventListener("mouseenter", () => {
      markers.forEach(m => m.classList.remove("active"));
      marker.classList.add("active");
      const key = marker.getAttribute("data-stage");
      if (stageDescriptions[key]) {
        stageDisplayTitle.textContent = stageDescriptions[key].title;
        stageDisplayDesc.textContent = stageDescriptions[key].desc;
      }
    });

    marker.addEventListener("click", () => {
      markers.forEach(m => m.classList.remove("active"));
      marker.classList.add("active");
      const key = marker.getAttribute("data-stage");
      if (stageDescriptions[key]) {
        stageDisplayTitle.textContent = stageDescriptions[key].title;
        stageDisplayDesc.textContent = stageDescriptions[key].desc;
      }
    });
  });
}

/* ==========================================================================
   7. Contact Form Client-side Validation & Mailto Fallback
   ========================================================================== */
function initContactForm() {
  const form = document.getElementById("schoolContactForm");
  const alertBox = document.getElementById("contactFormAlert");

  if (!form) return;

  form.addEventListener("submit", (e) => {
    e.preventDefault();

    const name = form.querySelector("#contactName")?.value.trim() || "";
    const email = form.querySelector("#contactEmail")?.value.trim() || "";
    const subject = form.querySelector("#contactSubject")?.value.trim() || "";
    const message = form.querySelector("#contactMessage")?.value.trim() || "";

    if (!name || !email || !subject || !message) {
      if (alertBox) {
        alertBox.className = "alert alert-warning border border-warning-subtle rounded-0 small mb-4";
        alertBox.innerHTML = `<i class="bi bi-exclamation-triangle-fill me-1"></i> Please complete all required fields before generating communication.`;
        alertBox.classList.remove("d-none");
      }
      return;
    }

    // Basic email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      if (alertBox) {
        alertBox.className = "alert alert-danger border border-danger-subtle rounded-0 small mb-4";
        alertBox.innerHTML = `<i class="bi bi-x-circle-fill me-1"></i> Please provide a valid email address.`;
        alertBox.classList.remove("d-none");
      }
      return;
    }

    // Show mailto action fallback
    const schoolEmail = "vnhs.haldipokhar.e.singhbhum@gmail.com";
    const mailtoUrl = `mailto:${schoolEmail}?subject=${encodeURIComponent(subject + ' - ' + name)}&body=${encodeURIComponent('From: ' + name + ' (' + email + ')\n\nMessage:\n' + message)}`;

    if (alertBox) {
      alertBox.className = "alert alert-success border border-success-subtle rounded-0 small mb-4";
      alertBox.innerHTML = `
        <div class="d-flex flex-column gap-2">
          <div><i class="bi bi-check-circle-fill text-success me-1"></i> <strong>Validation Successful!</strong> As this is a static frontend deployment without an internal server database, click the official dispatch button below to send your query directly via your email client.</div>
          <div class="mt-2">
            <a href="${mailtoUrl}" class="btn btn-sm btn-forest rounded-0 text-white px-3 py-2">
              <i class="bi bi-envelope-arrow-up-fill me-1"></i> Open in Email App to Send (${schoolEmail})
            </a>
          </div>
        </div>
      `;
      alertBox.classList.remove("d-none");
    }

    form.reset();
  });
}

/* ==========================================================================
   8. Back to Top Button
   ========================================================================== */
function initBackToTop() {
  const backToTopBtn = document.getElementById("backToTopBtn");
  if (!backToTopBtn) return;

  window.addEventListener("scroll", () => {
    if (window.scrollY > 400) {
      backToTopBtn.classList.add("visible");
    } else {
      backToTopBtn.classList.remove("visible");
    }
  }, { passive: true });

  backToTopBtn.addEventListener("click", () => {
    window.scrollTo({
      top: 0,
      behavior: "smooth"
    });
  });
}

/* ==========================================================================
   9. Copyright Year Auto Update
   ========================================================================== */
function initCopyrightYear() {
  const yrSpans = document.querySelectorAll(".current-year");
  const year = new Date().getFullYear();
  yrSpans.forEach(span => {
    span.textContent = year;
  });
}
