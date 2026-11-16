/**
 * CM SOE UPG GOVT +2 SCHOOL VNIKETAN HALDIPOKHAR
 * Forms, Live Notice Search & Event Filter Controller
 */

document.addEventListener('DOMContentLoaded', () => {
  initContactFormValidation();
  initNoticeBoardFilters();
  initEventFilters();
});

/**
 * Contact Form Client-side Validation & Feedback
 */
function initContactFormValidation() {
  const contactForm = document.getElementById('schoolContactForm');
  if (!contactForm) return;

  contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    e.stopPropagation();

    let isValid = true;
    const nameInput = document.getElementById('contactName');
    const emailInput = document.getElementById('contactEmail');
    const phoneInput = document.getElementById('contactPhone');
    const subjectInput = document.getElementById('contactSubject');
    const messageInput = document.getElementById('contactMessage');

    // Validation rules
    if (!nameInput.value.trim() || nameInput.value.trim().length < 3) {
      setFieldValidity(nameInput, false, 'Please enter your full name (minimum 3 characters).');
      isValid = false;
    } else {
      setFieldValidity(nameInput, true);
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailInput.value.trim() || !emailRegex.test(emailInput.value.trim())) {
      setFieldValidity(emailInput, false, 'Please provide a valid email address.');
      isValid = false;
    } else {
      setFieldValidity(emailInput, true);
    }

    const phoneRegex = /^[6-9]\d{9}$/;
    if (!phoneInput.value.trim() || !phoneRegex.test(phoneInput.value.trim().replace(/\D/g, ''))) {
      setFieldValidity(phoneInput, false, 'Please enter a valid 10-digit Indian mobile number.');
      isValid = false;
    } else {
      setFieldValidity(phoneInput, true);
    }

    if (!subjectInput.value.trim()) {
      setFieldValidity(subjectInput, false, 'Please select or enter the subject of your inquiry.');
      isValid = false;
    } else {
      setFieldValidity(subjectInput, true);
    }

    if (!messageInput.value.trim() || messageInput.value.trim().length < 10) {
      setFieldValidity(messageInput, false, 'Please enter your message (at least 10 characters).');
      isValid = false;
    } else {
      setFieldValidity(messageInput, true);
    }

    if (isValid) {
      showSubmissionConfirmation({
        name: nameInput.value.trim(),
        subject: subjectInput.value.trim()
      });
      contactForm.reset();
      // Reset validation states
      [nameInput, emailInput, phoneInput, subjectInput, messageInput].forEach(el => {
        el.classList.remove('is-valid');
      });
    }
  });

  function setFieldValidity(element, valid, errorMsg = '') {
    const feedback = element.parentElement.querySelector('.invalid-feedback');
    if (valid) {
      element.classList.remove('is-invalid');
      element.classList.add('is-valid');
    } else {
      element.classList.remove('is-valid');
      element.classList.add('is-invalid');
      if (feedback && errorMsg) {
        feedback.textContent = errorMsg;
      }
    }
  }

  function showSubmissionConfirmation(data) {
    // Show confirmation modal or alert box
    let confirmModal = document.getElementById('contactFeedbackModal');
    if (!confirmModal) {
      confirmModal = document.createElement('div');
      confirmModal.id = 'contactFeedbackModal';
      confirmModal.className = 'modal fade';
      confirmModal.tabIndex = -1;
      confirmModal.innerHTML = `
        <div class="modal-dialog modal-dialog-centered">
          <div class="modal-content border-0 shadow-lg" style="border-radius: var(--radius-lg);">
            <div class="modal-body text-center p-4">
              <div class="mb-3">
                <i class="bi bi-check-circle-fill text-success" style="font-size: 3.5rem;"></i>
              </div>
              <h4 class="font-heading fw-bold text-forest mb-2">Message Acknowledged!</h4>
              <p class="text-muted small mb-3">
                Thank you, <strong>${data.name}</strong>. Your inquiry regarding <em>"${data.subject}"</em> has been recorded in the institutional preview portal.
              </p>
              <div class="alert alert-light border small text-start mb-3">
                <i class="bi bi-info-circle text-primary me-2"></i>
                <strong>Notice:</strong> As this is the frontend presentation system for <em>CM SOE UPG GOVT +2 SCHOOL VNIKETAN HALDIPOKHAR</em>, official queries may also be submitted directly at the school administrative desk.
              </div>
              <button type="button" class="btn btn-emerald px-4" data-bs-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      `;
      document.body.appendChild(confirmModal);
    }

    if (window.bootstrap && bootstrap.Modal) {
      const bsModal = new bootstrap.Modal(confirmModal);
      bsModal.show();
    } else {
      alert(`Thank you, ${data.name}! Your message regarding "${data.subject}" has been submitted.`);
    }
  }
}

/**
 * Notice Board Live Search & Category Filtering
 */
function initNoticeBoardFilters() {
  const searchInput = document.getElementById('noticeSearchInput');
  const categoryFilters = document.querySelectorAll('.notice-filter-btn');
  const noticeRows = document.querySelectorAll('.notice-item-row');

  if (!noticeRows.length) return;

  function filterNotices() {
    const query = searchInput ? searchInput.value.toLowerCase().trim() : '';
    const activeCategoryBtn = document.querySelector('.notice-filter-btn.active');
    const selectedCategory = activeCategoryBtn ? activeCategoryBtn.getAttribute('data-category') : 'all';

    let matchCount = 0;

    noticeRows.forEach(row => {
      const title = (row.getAttribute('data-title') || '').toLowerCase();
      const category = row.getAttribute('data-category') || '';
      const text = row.textContent.toLowerCase();

      const matchesSearch = !query || title.includes(query) || text.includes(query);
      const matchesCategory = selectedCategory === 'all' || category === selectedCategory;

      if (matchesSearch && matchesCategory) {
        row.style.display = '';
        matchCount++;
      } else {
        row.style.display = 'none';
      }
    });

    const noResultsEl = document.getElementById('noNoticesFound');
    if (noResultsEl) {
      noResultsEl.style.display = matchCount === 0 ? 'block' : 'none';
    }
  }

  if (searchInput) {
    searchInput.addEventListener('input', filterNotices);
  }

  if (categoryFilters.length) {
    categoryFilters.forEach(btn => {
      btn.addEventListener('click', () => {
        categoryFilters.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        filterNotices();
      });
    });
  }
}

/**
 * Events Page Category Filter
 */
function initEventFilters() {
  const eventFilterBtns = document.querySelectorAll('.event-filter-btn');
  const eventCards = document.querySelectorAll('.event-card-item');

  if (!eventFilterBtns.length || !eventCards.length) return;

  eventFilterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      eventFilterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filter = btn.getAttribute('data-filter');

      eventCards.forEach(card => {
        const category = card.getAttribute('data-category');
        if (filter === 'all' || category === filter) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}
