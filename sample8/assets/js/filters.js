/**
 * CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR
 * Prompt 08 - Premium Glassmorphism & Digital Campus Portal
 * Search & Filters: filters.js
 */

document.addEventListener("DOMContentLoaded", () => {
  initNoticeFiltering();
  initResultFiltering();
});

/* 1. Notice Board Filtering & Search */
function initNoticeFiltering() {
  const filterBtns = document.querySelectorAll(".notice-filter-btn");
  const searchInput = document.getElementById("noticeSearchInput");
  const noticeItems = document.querySelectorAll(".notice-item-card");
  const emptyState = document.getElementById("noticesEmptyState");

  if (!noticeItems.length) return;

  let currentCategory = "all";
  let currentSearch = "";

  const applyFilters = () => {
    let visibleCount = 0;

    noticeItems.forEach(item => {
      const category = item.getAttribute("data-category") || "";
      const text = item.textContent.toLowerCase();

      const matchesCategory = currentCategory === "all" || category.toLowerCase() === currentCategory.toLowerCase();
      const matchesSearch = !currentSearch || text.includes(currentSearch.toLowerCase());

      if (matchesCategory && matchesSearch) {
        item.style.display = "";
        visibleCount++;
      } else {
        item.style.display = "none";
      }
    });

    if (emptyState) {
      emptyState.style.display = visibleCount === 0 ? "block" : "none";
    }
  };

  filterBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      filterBtns.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      currentCategory = btn.getAttribute("data-filter") || "all";
      applyFilters();
    });
  });

  if (searchInput) {
    searchInput.addEventListener("input", (e) => {
      currentSearch = e.target.value.trim();
      applyFilters();
    });
  }
}

/* 2. Examination Result Filtering */
function initResultFiltering() {
  const sessionSelect = document.getElementById("resultSessionSelect");
  const classSelect = document.getElementById("resultClassSelect");
  const searchInput = document.getElementById("resultSearchInput");
  const resultRows = document.querySelectorAll(".result-data-row");
  const emptyState = document.getElementById("resultEmptyState");

  if (!resultRows.length) return;

  const filterResults = () => {
    const selectedSession = sessionSelect ? sessionSelect.value.trim() : "all";
    const selectedClass = classSelect ? classSelect.value.trim() : "all";
    const searchTerm = searchInput ? searchInput.value.toLowerCase().trim() : "";

    let matchCount = 0;

    resultRows.forEach(row => {
      const rowSession = row.getAttribute("data-session") || "";
      const rowClass = row.getAttribute("data-class") || "";
      const rowText = row.textContent.toLowerCase();

      const matchSession = selectedSession === "all" || rowSession === selectedSession;
      const matchClass = selectedClass === "all" || rowClass === selectedClass;
      const matchSearch = !searchTerm || rowText.includes(searchTerm);

      if (matchSession && matchClass && matchSearch) {
        row.style.display = "";
        matchCount++;
      } else {
        row.style.display = "none";
      }
    });

    if (emptyState) {
      emptyState.style.display = matchCount === 0 ? "block" : "none";
    }
  };

  if (sessionSelect) sessionSelect.addEventListener("change", filterResults);
  if (classSelect) classSelect.addEventListener("change", filterResults);
  if (searchInput) searchInput.addEventListener("input", filterResults);
}
