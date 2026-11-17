/**
 * Notice Search, Category Filtering & Results Filter
 * CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR
 */

(function () {
  "use strict";

  // ==========================================
  // 1. NOTICE CENTER SEARCH & FILTER ENGINE
  // ==========================================
  function initNoticeCenter() {
    const noticeListContainer = document.getElementById("noticeListContainer");
    const noticeSearchInput = document.getElementById("noticeSearchInput");
    const noticeFilterPills = document.querySelectorAll(".notice-filter-pill");

    if (!noticeListContainer || !window.SCHOOL_DATA || !window.SCHOOL_DATA.notices) {
      return;
    }

    let currentCategory = "all";
    let currentSearchTerm = "";

    function filterAndRenderNotices() {
      let filtered = window.SCHOOL_DATA.notices.filter(function (notice) {
        const matchesCategory = currentCategory === "all" || notice.category.toLowerCase() === currentCategory.toLowerCase();
        const matchesSearch = notice.title.toLowerCase().includes(currentSearchTerm.toLowerCase()) ||
                              notice.desc.toLowerCase().includes(currentSearchTerm.toLowerCase()) ||
                              notice.category.toLowerCase().includes(currentSearchTerm.toLowerCase());
        return matchesCategory && matchesSearch;
      });

      renderNotices(filtered);
    }

    function renderNotices(notices) {
      if (notices.length === 0) {
        noticeListContainer.innerHTML = `
          <div class="col-12 py-4 text-center">
            <div class="p-4 bg-light rounded-4 border">
              <i class="bi bi-search text-muted fs-2 mb-2 d-block"></i>
              <h5 class="fw-bold text-deep-green">No announcements match your search</h5>
              <p class="text-secondary-green small mb-0">Try clearing your search keyword or switching category tabs.</p>
            </div>
          </div>
        `;
        return;
      }

      let html = "";
      notices.forEach(function (n) {
        html += `
          <div class="col-12 mb-3">
            <div class="organic-notice-card p-3 p-md-4 rounded-4 bg-white border border-soft shadow-sm transition-hover">
              <div class="d-flex flex-wrap align-items-center justify-content-between gap-2 mb-2">
                <div class="d-flex align-items-center gap-2">
                  <span class="badge bg-mint text-primary-green px-3 py-1 rounded-pill fw-semibold">${n.category}</span>
                  ${n.isSample ? '<span class="badge bg-light text-muted border px-2 py-1 rounded-pill small">Sample Placeholder</span>' : ''}
                </div>
                <div class="text-secondary-green small">
                  <i class="bi bi-calendar3 me-1"></i>${n.displayDate}
                </div>
              </div>
              <h3 class="h6 fw-bold text-deep-green mb-2">${n.title}</h3>
              <p class="text-secondary-green small mb-3">${n.desc}</p>
              <div class="d-flex justify-content-between align-items-center">
                <button type="button" class="btn btn-sm btn-outline-green view-notice-btn rounded-pill px-3" data-notice-id="${n.id}">
                  View Details <i class="bi bi-arrow-right ms-1"></i>
                </button>
                <span class="text-muted small">Ref: ${n.id}</span>
              </div>
            </div>
          </div>
        `;
      });

      noticeListContainer.innerHTML = html;

      // Attach view notice event
      const viewButtons = noticeListContainer.querySelectorAll(".view-notice-btn");
      viewButtons.forEach(function (btn) {
        btn.addEventListener("click", function () {
          const id = this.getAttribute("data-notice-id");
          const targetNotice = window.SCHOOL_DATA.notices.find(item => item.id === id);
          if (targetNotice) {
            openNoticeModal(targetNotice);
          }
        });
      });
    }

    if (noticeSearchInput) {
      noticeSearchInput.addEventListener("input", function () {
        currentSearchTerm = this.value.trim();
        filterAndRenderNotices();
      });
    }

    noticeFilterPills.forEach(function (pill) {
      pill.addEventListener("click", function () {
        noticeFilterPills.forEach(p => p.classList.remove("active"));
        this.classList.add("active");
        currentCategory = this.getAttribute("data-category") || "all";
        filterAndRenderNotices();
      });
    });

    // Initial render
    filterAndRenderNotices();
  }

  function openNoticeModal(notice) {
    const modalEl = document.getElementById("noticeDetailModal");
    if (!modalEl || typeof bootstrap === "undefined") return;

    const titleEl = document.getElementById("noticeModalTitle");
    const metaEl = document.getElementById("noticeModalMeta");
    const bodyEl = document.getElementById("noticeModalBody");

    if (titleEl) titleEl.textContent = notice.title;
    if (metaEl) {
      metaEl.innerHTML = `
        <span class="badge bg-mint text-primary-green me-2">${notice.category}</span>
        <span class="text-muted"><i class="bi bi-calendar-event me-1"></i>${notice.displayDate}</span>
      `;
    }
    if (bodyEl) {
      bodyEl.innerHTML = `
        <p class="mb-3">${notice.desc}</p>
        <div class="alert alert-light border small">
          <i class="bi bi-info-circle text-primary me-2"></i>
          <strong>Transparency Notice:</strong> This is a sample educational announcement provided as an illustrative template for CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR. Actual official school notifications are approved by the Principal's office and pinned to the physical campus notice desk.
        </div>
      `;
    }

    const modal = bootstrap.Modal.getOrCreateInstance(modalEl);
    modal.show();
  }

  // ==========================================
  // 2. EXAMINATION RESULTS FILTER ENGINE
  // ==========================================
  function initResultsFilter() {
    const sessionFilter = document.getElementById("resultSessionSelect");
    const examFilter = document.getElementById("resultExamSelect");
    const classFilter = document.getElementById("resultClassSelect");
    const resultTableBody = document.getElementById("resultTableBody");

    if (!resultTableBody || !window.SCHOOL_DATA || !window.SCHOOL_DATA.resultsData) {
      return;
    }

    function renderResults() {
      const selectedSession = sessionFilter ? sessionFilter.value : "all";
      const selectedExam = examFilter ? examFilter.value : "all";
      const selectedClass = classFilter ? classFilter.value : "all";

      const filtered = window.SCHOOL_DATA.resultsData.filter(function (row) {
        const matchesSession = selectedSession === "all" || row.session === selectedSession;
        const matchesExam = selectedExam === "all" || row.exam.toLowerCase().includes(selectedExam.toLowerCase());
        const matchesClass = selectedClass === "all" || row.cls.toLowerCase().includes(selectedClass.toLowerCase());
        return matchesSession && matchesExam && matchesClass;
      });

      if (filtered.length === 0) {
        resultTableBody.innerHTML = `
          <tr>
            <td colspan="5" class="text-center py-4 text-muted">
              <i class="bi bi-file-earmark-x fs-2 d-block mb-2"></i>
              No records found matching the chosen examination filter criteria.
            </td>
          </tr>
        `;
        return;
      }

      const isInPagesDir = window.location.pathname.includes("/pages/");
      const assetPrefix = isInPagesDir ? "../" : "";

      let html = "";
      filtered.forEach(function (r, i) {
        html += `
          <tr>
            <td class="fw-semibold text-center">${i + 1}</td>
            <td class="fw-bold text-deep-green">${r.session}</td>
            <td>${r.exam}</td>
            <td><span class="badge bg-mint text-primary-green">${r.cls}</span></td>
            <td>
              <div class="d-flex align-items-center gap-2">
                <span class="badge bg-light text-secondary border px-2 py-1"><i class="bi bi-clock-history me-1"></i>${r.status}</span>
                <a href="${assetPrefix}${r.docLink}" target="_blank" class="btn btn-sm btn-outline-green rounded-pill py-0 px-2" title="Download Official Verification Statement">
                  <i class="bi bi-download"></i> Notice
                </a>
              </div>
            </td>
          </tr>
        `;
      });

      resultTableBody.innerHTML = html;
    }

    if (sessionFilter) sessionFilter.addEventListener("change", renderResults);
    if (examFilter) examFilter.addEventListener("change", renderResults);
    if (classFilter) classFilter.addEventListener("change", renderResults);

    // Initial render
    renderResults();
  }

  // Self-initialize on DOM ready
  document.addEventListener("DOMContentLoaded", function () {
    initNoticeCenter();
    initResultsFilter();
  });
})();
