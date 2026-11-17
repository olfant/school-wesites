/**
 * Main Frontend Interactions & Accessibility Engine
 * CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR
 */

document.addEventListener("DOMContentLoaded", function () {
  "use strict";

  // 1. Dynamic Copyright Year
  const yearEls = document.querySelectorAll("#yr, .current-year");
  const curYear = new Date().getFullYear();
  yearEls.forEach(function (el) {
    el.textContent = curYear;
  });

  // 2. Font Size Accessibility Controls (A-, A, A+)
  const fsButtons = document.querySelectorAll("[data-fs]");
  const htmlEl = document.documentElement;
  const savedFs = localStorage.getItem("school_font_scale") || "0";
  applyFontSize(savedFs);

  fsButtons.forEach(function (btn) {
    if (btn.getAttribute("data-fs") === savedFs) {
      btn.classList.add("active");
    }
    btn.addEventListener("click", function () {
      const scale = this.getAttribute("data-fs");
      applyFontSize(scale);
      localStorage.setItem("school_font_scale", scale);
      fsButtons.forEach(b => b.classList.remove("active"));
      this.classList.add("active");
    });
  });

  function applyFontSize(scale) {
    if (scale === "-1") {
      htmlEl.style.fontSize = "14.5px";
    } else if (scale === "1") {
      htmlEl.style.fontSize = "17.5px";
    } else {
      htmlEl.style.fontSize = "16px";
    }
  }

  // 3. Sticky Navbar with Soft Shadow & Blur
  const mainNavbar = document.querySelector(".main-nav");
  if (mainNavbar) {
    window.addEventListener("scroll", function () {
      if (window.scrollY > 45) {
        mainNavbar.classList.add("nav-scrolled");
      } else {
        mainNavbar.classList.remove("nav-scrolled");
      }
    });
  }

  // 4. Back to Top Button
  const toTopBtn = document.getElementById("toTop");
  if (toTopBtn) {
    window.addEventListener("scroll", function () {
      if (window.scrollY > 350) {
        toTopBtn.classList.add("visible");
      } else {
        toTopBtn.classList.remove("visible");
      }
    });

    toTopBtn.addEventListener("click", function (e) {
      e.preventDefault();
      window.scrollTo({
        top: 0,
        behavior: "smooth"
      });
    });
  }

  // 5. Scroll-Triggered Reveal Animations using IntersectionObserver
  const revealElements = document.querySelectorAll(".reveal, .reveal-up, .reveal-left, .reveal-right");
  if ("IntersectionObserver" in window && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    const revealObserver = new IntersectionObserver(
      function (entries, observer) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("active");
            observer.unobserve(entry.target);
          }
        });
      },
      {
        threshold: 0.12,
        rootMargin: "0px 0px -40px 0px"
      }
    );

    revealElements.forEach(function (el) {
      revealObserver.observe(el);
    });
  } else {
    // Fallback for reduced motion or older browsers
    revealElements.forEach(function (el) {
      el.classList.add("active");
    });
  }

  // 6. Interactive Student Journey Timeline (Section 08)
  const journeyStages = document.querySelectorAll(".journey-step-item");
  const journeyDetailsBox = document.getElementById("journeyDetailsBox");

  if (journeyStages.length > 0 && journeyDetailsBox && window.SCHOOL_DATA) {
    journeyStages.forEach(function (item, index) {
      item.addEventListener("click", function () {
        journeyStages.forEach(s => s.classList.remove("active"));
        this.classList.add("active");

        const data = window.SCHOOL_DATA.journeyStages[index];
        if (data) {
          journeyDetailsBox.innerHTML = `
            <div class="journey-bubble p-4 text-center">
              <div class="d-inline-flex align-items-center justify-content-center bg-mint text-primary-green rounded-circle mb-3" style="width: 54px; height: 54px; font-size: 1.5rem;">
                <i class="bi ${data.icon}"></i>
              </div>
              <h4 class="h5 fw-bold text-deep-green mb-2">Stage ${data.step} — ${data.title}</h4>
              <p class="text-secondary-green mb-0 mx-auto" style="max-width: 620px;">${data.desc}</p>
            </div>
          `;
        }
      });
    });
  }

  // 7. Contact Form Client-Side Validation & Mailto Fallback
  const contactForm = document.getElementById("schoolContactForm");
  const formFeedback = document.getElementById("formFeedback");

  if (contactForm) {
    contactForm.addEventListener("submit", function (e) {
      e.preventDefault();

      const nameInput = document.getElementById("contactName");
      const emailInput = document.getElementById("contactEmail");
      const subjectInput = document.getElementById("contactSubject");
      const messageInput = document.getElementById("contactMessage");

      let isValid = true;
      let errorMsg = "";

      // Validate Name
      if (!nameInput.value.trim() || nameInput.value.trim().length < 2) {
        isValid = false;
        nameInput.classList.add("is-invalid");
        errorMsg += "Please enter a valid full name (minimum 2 characters).<br>";
      } else {
        nameInput.classList.remove("is-invalid");
        nameInput.classList.add("is-valid");
      }

      // Validate Email
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailPattern.test(emailInput.value.trim())) {
        isValid = false;
        emailInput.classList.add("is-invalid");
        errorMsg += "Please enter a valid email address.<br>";
      } else {
        emailInput.classList.remove("is-invalid");
        emailInput.classList.add("is-valid");
      }

      // Validate Subject
      if (!subjectInput.value.trim() || subjectInput.value.trim().length < 3) {
        isValid = false;
        subjectInput.classList.add("is-invalid");
        errorMsg += "Please enter a message subject.<br>";
      } else {
        subjectInput.classList.remove("is-invalid");
        subjectInput.classList.add("is-valid");
      }

      // Validate Message
      if (!messageInput.value.trim() || messageInput.value.trim().length < 10) {
        isValid = false;
        messageInput.classList.add("is-invalid");
        errorMsg += "Please write a message with at least 10 characters.<br>";
      } else {
        messageInput.classList.remove("is-invalid");
        messageInput.classList.add("is-valid");
      }

      if (!isValid) {
        if (formFeedback) {
          formFeedback.className = "alert alert-danger mt-3";
          formFeedback.innerHTML = errorMsg;
          formFeedback.classList.remove("d-none");
        }
        return;
      }

      // If valid, show friendly confirmation modal / message with mailto fallback
      const schoolEmail = "vnhs.haldipokhar.e.singhbhum@gmail.com";
      const mailtoUrl = `mailto:${schoolEmail}?subject=${encodeURIComponent(subjectInput.value.trim())}&body=${encodeURIComponent("Sender Name: " + nameInput.value.trim() + "\nSender Email: " + emailInput.value.trim() + "\n\nMessage:\n" + messageInput.value.trim())}`;

      if (formFeedback) {
        formFeedback.className = "alert alert-success mt-3";
        formFeedback.innerHTML = `
          <strong><i class="bi bi-check-circle-fill me-2"></i>Validation Successful!</strong><br>
          <span class="small">Note: As this is a static institutional frontend, no backend server or database is linked. Your default mail client is opening to send this inquiry directly to <strong>${schoolEmail}</strong>.</span>
          <div class="mt-2">
            <a href="${mailtoUrl}" class="btn btn-sm btn-green">Open Email Client <i class="bi bi-box-arrow-up-right ms-1"></i></a>
          </div>
        `;
        formFeedback.classList.remove("d-none");
      }

      // Attempt open mailto
      setTimeout(function () {
        window.location.href = mailtoUrl;
      }, 700);
    });
  }

  // 8. Mobile Offcanvas / Dropdown click enhancement
  const mobileNavLinks = document.querySelectorAll(".navbar-nav .nav-link:not(.dropdown-toggle)");
  const navCollapse = document.getElementById("mainMenu");
  if (navCollapse && typeof bootstrap !== "undefined") {
    mobileNavLinks.forEach(function (link) {
      link.addEventListener("click", function () {
        const bsCollapse = bootstrap.Collapse.getInstance(navCollapse);
        if (bsCollapse && window.innerWidth < 992) {
          bsCollapse.hide();
        }
      });
    });
  }
});
