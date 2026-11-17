/**
 * CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR
 * Dynamic Search & Filter Handlers for Notices and Examination Records
 */

document.addEventListener("DOMContentLoaded", () => {
  initNoticeFilters();
  initResultFilters();
});

/* ==========================================================================
   Notice Search & Category Filtering
   ========================================================================== */
function initNoticeFilters() {
  const noticesContainer = document.getElementById("noticesContainer");
  const searchInput = document.getElementById("noticeSearchInput");
  const categoryFilters = document.querySelectorAll(".notice-cat-filter");
  const countBadge = document.getElementById("noticeCountBadge");

  if (!noticesContainer || !window.NOTICES_DATA) return;

  let currentCategory = "all";
  let searchQuery = "";

  function filterNotices() {
    const filtered = window.NOTICES_DATA.filter(notice => {
      const matchesCat = currentCategory === "all" || notice.category.toLowerCase() === currentCategory.toLowerCase();
      const matchesQuery = searchQuery === "" || 
        notice.title.toLowerCase().includes(searchQuery.toLowerCase()) || 
        notice.description.toLowerCase().includes(searchQuery.toLowerCase()) ||
        notice.id.toLowerCase().includes(searchQuery.toLowerCase());
      return matchesCat && matchesQuery;
    });

    renderNotices(filtered);
    if (countBadge) {
      countBadge.textContent = `${filtered.length} Notice${filtered.length === 1 ? '' : 's'}`;
    }
  }

  function renderNotices(list) {
    noticesContainer.innerHTML = "";
    if (list.length === 0) {
      noticesContainer.innerHTML = `
        <div class="col-12 py-5 text-center">
          <div class="p-4 bg-white border border-success-subtle shadow-sm">
            <i class="bi bi-search text-secondary fs-1 mb-3 d-block"></i>
            <h5 class="fw-bold">No Matching Notices Found</h5>
            <p class="text-muted mb-0">Try clearing your search query or choosing another category filter.</p>
          </div>
        </div>
      `;
      return;
    }

    list.forEach((item, index) => {
      const col = document.createElement("div");
      col.className = "col-lg-6 mb-4 notice-card-wrapper";
      col.innerHTML = `
        <div class="arch-notice-card bg-white p-4 h-100 position-relative border border-start-0 border-end-0 border-top-0 border-3 border-bottom border-success shadow-sm">
          <div class="d-flex justify-content-between align-items-center mb-3">
            <span class="badge bg-pale text-forest font-monospace px-3 py-2 border border-success-subtle">
              <i class="bi bi-tag-fill me-1 text-primary-green"></i> ${item.category}
            </span>
            <span class="small text-muted font-monospace"><i class="bi bi-calendar3 me-1"></i> ${item.date}</span>
          </div>
          <h5 class="fw-bold mb-2 text-dark notice-title">
            <a href="javascript:void(0)" class="text-decoration-none text-dark hover-green" onclick="showNoticeModal('${item.id}')">${item.title}</a>
          </h5>
          <p class="text-secondary small mb-3 flex-grow-1">${item.description}</p>
          
          <div class="d-flex justify-content-between align-items-center pt-3 border-top border-light-subtle">
            <span class="small font-monospace text-muted">ID: ${item.id}</span>
            <button type="button" class="btn btn-sm btn-outline-forest rounded-0 px-3" onclick="showNoticeModal('${item.id}')">
              View Details <i class="bi bi-arrow-right ms-1"></i>
            </button>
          </div>
        </div>
      `;
      noticesContainer.appendChild(col);
    });
  }

  // Category filter click
  categoryFilters.forEach(btn => {
    btn.addEventListener("click", () => {
      categoryFilters.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      currentCategory = btn.getAttribute("data-category") || "all";
      filterNotices();
    });
  });

  // Search input
  if (searchInput) {
    searchInput.addEventListener("input", (e) => {
      searchQuery = e.target.value.trim();
      filterNotices();
    });
  }

  // Initial render
  filterNotices();
}

/* ==========================================================================
   Notice Modal Handler
   ========================================================================== */
function showNoticeModal(id) {
  if (!window.NOTICES_DATA) return;
  const notice = window.NOTICES_DATA.find(n => n.id === id);
  if (!notice) return;

  let modalEl = document.getElementById("noticeDetailModal");
  if (!modalEl) {
    modalEl = document.createElement("div");
    modalEl.id = "noticeDetailModal";
    modalEl.className = "modal fade";
    modalEl.tabIndex = -1;
    modalEl.innerHTML = `
      <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content border-0 rounded-0 shadow-lg">
          <div class="modal-header bg-forest text-white rounded-0 py-3">
            <div class="d-flex align-items-center">
              <span class="badge bg-bright-green text-dark font-monospace me-2" id="modalNoticeCat"></span>
              <h5 class="modal-title fw-bold font-monospace" id="modalNoticeId"></h5>
            </div>
            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body p-4 p-md-5">
            <div class="d-flex align-items-center text-muted small font-monospace mb-3">
              <i class="bi bi-calendar-event me-2 text-primary-green"></i> Published: <span id="modalNoticeDate" class="ms-1 fw-bold text-dark"></span>
              <span class="mx-2">•</span>
              <i class="bi bi-building me-1 text-primary-green"></i> CM SOE VNIKETAN HALDIPOKHAR
            </div>
            <h4 class="fw-bold text-dark mb-4" id="modalNoticeTitle"></h4>
            <div class="p-3 bg-pale border-start border-4 border-success mb-4" id="modalNoticeContent"></div>
            
            <div class="alert alert-light border border-success-subtle rounded-0 small text-secondary">
              <i class="bi bi-info-circle-fill text-primary-green me-1"></i>
              <strong>Official Notice Policy:</strong> Demonstration circulars illustrate information architecture. Signed and stamped physical circulars are archived in the principal's administrative wing under U-DISE 20180231602.
            </div>
          </div>
          <div class="modal-footer bg-light rounded-0 py-2">
            <button type="button" class="btn btn-secondary rounded-0 px-4" data-bs-dismiss="modal">Close</button>
            <a href="contact.html" class="btn btn-forest rounded-0 px-4">Contact Office</a>
          </div>
        </div>
      </div>
    `;
    document.body.appendChild(modalEl);
  }

  document.getElementById("modalNoticeCat").textContent = notice.category;
  document.getElementById("modalNoticeId").textContent = notice.id;
  document.getElementById("modalNoticeDate").textContent = notice.date;
  document.getElementById("modalNoticeTitle").textContent = notice.title;
  document.getElementById("modalNoticeContent").textContent = notice.description;

  const bsModal = new bootstrap.Modal(modalEl);
  bsModal.show();
}
window.showNoticeModal = showNoticeModal;

/* ==========================================================================
   Academic Results Directory Filtering
   ========================================================================== */
function initResultFilters() {
  const resultsTableBody = document.getElementById("resultsTableBody");
  const sessionSelect = document.getElementById("sessionFilter");
  const examTypeSelect = document.getElementById("examTypeFilter");
  const streamSelect = document.getElementById("streamFilter");
  const resultsCount = document.getElementById("resultsCountBadge");

  if (!resultsTableBody || !window.RESULTS_DATA) return;

  function filterResults() {
    const sessionVal = sessionSelect ? sessionSelect.value : "all";
    const examVal = examTypeSelect ? examTypeSelect.value : "all";
    const streamVal = streamSelect ? streamSelect.value : "all";

    const filtered = window.RESULTS_DATA.filter(item => {
      const matchSession = sessionVal === "all" || item.session === sessionVal;
      const matchExam = examVal === "all" || item.examType.toLowerCase().includes(examVal.toLowerCase());
      const matchStream = streamVal === "all" || item.streamClass.toLowerCase().includes(streamVal.toLowerCase());
      return matchSession && matchExam && matchStream;
    });

    renderResultsTable(filtered);
    if (resultsCount) {
      resultsCount.textContent = `${filtered.length} Record${filtered.length === 1 ? '' : 's'}`;
    }
  }

  function renderResultsTable(list) {
    resultsTableBody.innerHTML = "";
    if (list.length === 0) {
      resultsTableBody.innerHTML = `
        <tr>
          <td colspan="6" class="text-center py-4 text-muted">
            <i class="bi bi-folder-x fs-2 d-block mb-2 text-secondary"></i>
            No official examination records match the selected filter criteria.
          </td>
        </tr>
      `;
      return;
    }

    list.forEach((item, index) => {
      const tr = document.createElement("tr");
      tr.innerHTML = `
        <td class="font-monospace fw-bold text-forest">${String(index + 1).padStart(2, '0')}</td>
        <td><span class="badge bg-pale text-forest border border-success-subtle font-monospace">${item.session}</span></td>
        <td class="fw-semibold text-dark">${item.examType}</td>
        <td><span class="badge bg-light text-dark border font-monospace">${item.streamClass}</span></td>
        <td class="small text-muted font-monospace">${item.date}</td>
        <td class="text-end">
          <a href="${item.docLink}" target="_blank" class="btn btn-sm btn-outline-forest rounded-0 px-2 py-1">
            <i class="bi bi-file-earmark-text me-1"></i> Official Document
          </a>
        </td>
      `;
      resultsTableBody.appendChild(tr);
    });
  }

  if (sessionSelect) sessionSelect.addEventListener("change", filterResults);
  if (examTypeSelect) examTypeSelect.addEventListener("change", filterResults);
  if (streamSelect) streamSelect.addEventListener("change", filterResults);

  filterResults();
}
