/**
 * ====================================================================
 * FILTERS JAVASCRIPT — NOTICES & EXAMINATION RESULTS
 * CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR, हल्दीपोखर
 * ====================================================================
 */

document.addEventListener('DOMContentLoaded', () => {
  initNoticeFiltering();
  initResultFiltering();
});

/**
 * Notice Board Search and Category Filter
 */
function initNoticeFiltering() {
  const categoryPills = document.querySelectorAll('.notice-cat-pill');
  const searchInput = document.getElementById('noticeSearchInput');
  const noticeRows = document.querySelectorAll('.notice-row-item');
  const noNoticesMsg = document.getElementById('noNoticesMessage');

  if (!noticeRows.length) return;

  let activeCategory = 'all';
  let searchTerm = '';

  const applyFilters = () => {
    let visibleCount = 0;

    noticeRows.forEach(row => {
      const rowCategory = (row.getAttribute('data-category') || '').toLowerCase();
      const rowTitle = (row.querySelector('.notice-title-col') ? row.querySelector('.notice-title-col').textContent : '').toLowerCase();
      const rowDate = (row.querySelector('.notice-date') ? row.querySelector('.notice-date').textContent : '').toLowerCase();

      const matchesCategory = activeCategory === 'all' || rowCategory === activeCategory;
      const matchesSearch = searchTerm === '' || rowTitle.includes(searchTerm) || rowDate.includes(searchTerm);

      if (matchesCategory && matchesSearch) {
        row.style.display = 'grid';
        visibleCount++;
      } else {
        row.style.display = 'none';
      }
    });

    if (noNoticesMsg) {
      noNoticesMsg.style.display = visibleCount === 0 ? 'block' : 'none';
    }
  };

  categoryPills.forEach(pill => {
    pill.addEventListener('click', () => {
      categoryPills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      activeCategory = (pill.getAttribute('data-category') || 'all').toLowerCase();
      applyFilters();
    });
  });

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchTerm = e.target.value.trim().toLowerCase();
      applyFilters();
    });
  }
}

/**
 * Examination Results Filters (Session, Exam, Class)
 */
function initResultFiltering() {
  const sessionSelect = document.getElementById('resultSessionFilter');
  const examSelect = document.getElementById('resultExamFilter');
  const classSelect = document.getElementById('resultClassFilter');
  const resultRows = document.querySelectorAll('.result-table-row');
  const emptyResultsMsg = document.getElementById('noResultsMessage');

  if (!resultRows.length) return;

  const filterResults = () => {
    const selSession = sessionSelect ? sessionSelect.value.toLowerCase() : 'all';
    const selExam = examSelect ? examSelect.value.toLowerCase() : 'all';
    const selClass = classSelect ? classSelect.value.toLowerCase() : 'all';

    let visibleCount = 0;

    resultRows.forEach(row => {
      const rowSession = (row.getAttribute('data-session') || '').toLowerCase();
      const rowExam = (row.getAttribute('data-exam') || '').toLowerCase();
      const rowClass = (row.getAttribute('data-class') || '').toLowerCase();

      const matchesSession = selSession === 'all' || rowSession.includes(selSession);
      const matchesExam = selExam === 'all' || rowExam.includes(selExam);
      const matchesClass = selClass === 'all' || rowClass.includes(selClass);

      if (matchesSession && matchesExam && matchesClass) {
        row.style.display = '';
        visibleCount++;
      } else {
        row.style.display = 'none';
      }
    });

    if (emptyResultsMsg) {
      emptyResultsMsg.style.display = visibleCount === 0 ? 'block' : 'none';
    }
  };

  if (sessionSelect) sessionSelect.addEventListener('change', filterResults);
  if (examSelect) examSelect.addEventListener('change', filterResults);
  if (classSelect) classSelect.addEventListener('change', filterResults);
}
