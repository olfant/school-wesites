/* ==========================================================================
   CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR
   NOTICES & EXAMINATION RESULTS FILTER CONTROLLER
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  initNoticesFilter();
  initResultsFilter();
});

/* Notices Search & Category Filtering */
function initNoticesFilter() {
  const noticeContainer = document.getElementById('noticeListContainer');
  const searchInput = document.getElementById('noticeSearchInput');
  const filterBtns = document.querySelectorAll('.notice-filter-btn');

  if (!noticeContainer) return;

  let currentCategory = 'all';
  let searchQuery = '';

  function renderNotices() {
    if (typeof SITE_NOTICES === 'undefined') return;

    const filtered = SITE_NOTICES.filter(item => {
      const matchesCategory = currentCategory === 'all' || item.category.toLowerCase() === currentCategory.toLowerCase();
      const textToSearch = `${item.title} ${item.description} ${item.category}`.toLowerCase();
      const matchesSearch = textToSearch.includes(searchQuery.toLowerCase());
      return matchesCategory && matchesSearch;
    });

    if (filtered.length === 0) {
      noticeContainer.innerHTML = `
        <div class="text-center p-4 bg-white rounded-4 border border-light-subtle shadow-sm">
          <i class="bi bi-info-circle text-success fs-2 mb-2 d-block"></i>
          <h5 class="fw-bold mb-1">No Announcements Found</h5>
          <p class="text-muted small mb-0">Try adjusting your search keyword or selected category filter.</p>
        </div>
      `;
      return;
    }

    noticeContainer.innerHTML = filtered.map(item => `
      <div class="notice-item-card reveal-fade-up is-revealed">
        <div class="notice-item-left">
          <div class="notice-date-box">
            <i class="bi bi-calendar3 me-1"></i>${item.date}
          </div>
          <div>
            <span class="notice-tag-badge">${item.category}</span>
            <h4 class="notice-title">${item.title}</h4>
            <p class="text-muted small mb-0 mt-1">${item.description}</p>
          </div>
        </div>
        <div class="notice-item-right text-nowrap mt-2 mt-md-0">
          <a href="${item.file}" class="btn btn-sm btn-outline-success rounded-pill px-3 fw-bold" target="_blank" rel="noopener">
            <i class="bi bi-file-earmark-text me-1"></i>View Details
          </a>
        </div>
      </div>
    `).join('');
  }

  // Event Listeners for category buttons
  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentCategory = btn.getAttribute('data-cat') || 'all';
      renderNotices();
    });
  });

  // Event Listener for Search
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value.trim();
      renderNotices();
    });
  }

  // Initial Render
  renderNotices();
}

/* Examination Results Multi-Filter */
function initResultsFilter() {
  const resultTableBody = document.getElementById('resultsTableBody');
  const sessionSelect = document.getElementById('filterSession');
  const classSelect = document.getElementById('filterClass');
  const examSelect = document.getElementById('filterExam');
  const searchInput = document.getElementById('filterRollSearch');
  const emptyStateAlert = document.getElementById('resultsEmptyAlert');

  if (!resultTableBody) return;

  function populateDropdownOptions() {
    if (typeof SITE_RESULTS === 'undefined') return;

    const sessions = [...new Set(SITE_RESULTS.map(r => r.session))];
    const classes = [...new Set(SITE_RESULTS.map(r => r.cls))];
    const exams = [...new Set(SITE_RESULTS.map(r => r.exam))];

    if (sessionSelect) {
      sessions.forEach(s => {
        const opt = document.createElement('option');
        opt.value = s;
        opt.textContent = s;
        sessionSelect.appendChild(opt);
      });
    }

    if (classSelect) {
      classes.forEach(c => {
        const opt = document.createElement('option');
        opt.value = c;
        opt.textContent = c;
        classSelect.appendChild(opt);
      });
    }

    if (examSelect) {
      exams.forEach(e => {
        const opt = document.createElement('option');
        opt.value = e;
        opt.textContent = e;
        examSelect.appendChild(opt);
      });
    }
  }

  function renderResults() {
    if (typeof SITE_RESULTS === 'undefined') return;

    const selSession = sessionSelect ? sessionSelect.value : '';
    const selClass = classSelect ? classSelect.value : '';
    const selExam = examSelect ? examSelect.value : '';
    const query = searchInput ? searchInput.value.trim().toLowerCase() : '';

    const filtered = SITE_RESULTS.filter(r => {
      if (selSession && r.session !== selSession) return false;
      if (selClass && r.cls !== selClass) return false;
      if (selExam && r.exam !== selExam) return false;
      if (query && !(`${r.roll} ${r.exam} ${r.name || ''}`).toLowerCase().includes(query)) return false;
      return true;
    });

    if (filtered.length === 0) {
      resultTableBody.innerHTML = '';
      if (emptyStateAlert) {
        emptyStateAlert.classList.remove('d-none');
        emptyStateAlert.innerHTML = `
          <i class="bi bi-info-circle-fill me-2 fs-5"></i>
          <div>
            <strong>No Matching Official Results Found.</strong>
            <div class="small mt-1">Official examination results for CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR are published sequentially as certified by the examination board.</div>
          </div>
        `;
      }
      return;
    }

    if (emptyStateAlert) {
      emptyStateAlert.classList.add('d-none');
    }

    resultTableBody.innerHTML = filtered.map(r => `
      <tr>
        <td data-label="Roll Number"><strong>${r.roll}</strong></td>
        <td data-label="Student Reference">${r.name || '—'}</td>
        <td data-label="Class / Stream"><span class="badge bg-light text-dark border">${r.cls}</span></td>
        <td data-label="Examination">${r.exam}</td>
        <td data-label="Session">${r.session}</td>
        <td data-label="Status"><span class="badge bg-success-subtle text-success fw-bold">${r.status}</span></td>
        <td data-label="Document">
          ${r.pdf ? `
            <a href="${r.pdf}" class="btn btn-sm btn-outline-success rounded-pill fw-bold" target="_blank" rel="noopener">
              <i class="bi bi-file-earmark-pdf me-1"></i>Official PDF
            </a>
          ` : '—'}
        </td>
      </tr>
    `).join('');
  }

  populateDropdownOptions();
  renderResults();

  if (sessionSelect) sessionSelect.addEventListener('change', renderResults);
  if (classSelect) classSelect.addEventListener('change', renderResults);
  if (examSelect) examSelect.addEventListener('change', renderResults);
  if (searchInput) searchInput.addEventListener('input', renderResults);
}
