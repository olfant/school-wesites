/* ==========================================================================
   CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR
   3D INTERACTIONS & CARD TILT ENGINE
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  initCard3DTilt();
  initContactFormValidation();
});

/* 3D Tilt Effect on Elements with [data-tilt] */
function initCard3DTilt() {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  if (window.innerWidth < 992) return; // Desktop only

  const tiltCards = document.querySelectorAll('[data-tilt]');
  if (!tiltCards.length) return;

  tiltCards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;

      const rotateX = ((y - centerY) / centerY) * -10; // max 10 deg tilt
      const rotateY = ((x - centerX) / centerX) * 10;

      card.style.transform = `perspective(1000px) rotateX(${rotateX.toFixed(2)}deg) rotateY(${rotateY.toFixed(2)}deg) scale3d(1.02, 1.02, 1.02)`;
    });

    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
    });
  });
}

/* Contact Form Validation with Mailto Fallback */
function initContactFormValidation() {
  const form = document.getElementById('schoolContactForm');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    form.classList.add('was-validated');

    if (!form.checkValidity()) {
      const firstInvalid = form.querySelector(':invalid');
      if (firstInvalid) firstInvalid.focus();
      return;
    }

    const name = (document.getElementById('contactName')?.value || '').trim();
    const email = (document.getElementById('contactEmail')?.value || '').trim();
    const subject = (document.getElementById('contactSubject')?.value || 'School Inquiry').trim();
    const message = (document.getElementById('contactMessage')?.value || '').trim();

    const recipient = 'vnhs.haldipokhar.e.singhbhum@gmail.com';
    const bodyContent = `Name: ${name}\nEmail: ${email}\n\nMessage:\n${message}\n\n--\nSubmitted via Website: CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR`;

    const mailtoUrl = `mailto:${recipient}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(bodyContent)}`;

    // Show feedback alert
    const alertBox = document.getElementById('contactAlertSuccess');
    if (alertBox) {
      alertBox.classList.remove('d-none');
    }

    setTimeout(() => {
      window.location.href = mailtoUrl;
    }, 600);
  });
}
