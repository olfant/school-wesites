import os
from generate_pages_batch1 import get_page_template, save_page

# ==============================================================================
# 11. SPORTS ACTIVITIES (pages/sports-activities.html)
# ==============================================================================
sports_content = """
<section class="py-5 bg-white">
  <div class="container">
    <div class="row align-items-center g-5 mb-5 reveal-on-scroll">
      <div class="col-lg-6">
        <span class="section-label-green">ATHLETIC EXCELLENCE &amp; HEALTH</span>
        <h2 class="editorial-headline">Building Endurance, Team Spirit &amp; Sportsmanship</h2>
        <p class="editorial-lead-text">
          Physical fitness and sports form an integral dimension of student life at +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय. With our expansive green campus grounds and dedicated sports coaching, students build stamina, strategic agility, and mutual comradeship.
        </p>
        <p style="color:var(--body-text); line-height:1.75;">
          Our physical education program balances track &amp; field athletics with outdoor team sports like football and volleyball, as well as mental fitness through yoga, meditation, chess, and carrom. All students are grouped into four institutional houses to promote healthy sporting rivalry during the Annual Athletic Meet.
        </p>
      </div>
      <div class="col-lg-6">
        <div class="editorial-image-frame">
          <img src="../assets/img/sports/sports-track-field.svg" alt="Athletic Track and Field Meet">
        </div>
      </div>
    </div>

    <!-- Sports Facilities & Disciplines -->
    <div class="row g-4 mb-5 reveal-on-scroll">
      <div class="col-md-4">
        <div class="p-4 bg-light rounded-4 border h-100">
          <div class="info-band-icon mb-3" style="background:var(--light-mint); color:var(--primary-green);"><i class="bi bi-stopwatch-fill"></i></div>
          <h4 style="font-size:1.25rem; font-weight:700; color:var(--heading);">Track &amp; Field Athletics</h4>
          <p style="font-size:0.9rem; color:var(--body-text); margin-bottom:0;">
            100m, 200m, and 400m sprint tracks, 4x100m relay races, long jump pit, high jump bar, and shot put conditioning under coach supervision.
          </p>
        </div>
      </div>

      <div class="col-md-4">
        <div class="p-4 bg-light rounded-4 border h-100">
          <div class="info-band-icon mb-3" style="background:var(--light-mint); color:var(--primary-green);"><i class="bi bi-dribbble"></i></div>
          <h4 style="font-size:1.25rem; font-weight:700; color:var(--heading);">Outdoor Team Sports</h4>
          <p style="font-size:0.9rem; color:var(--body-text); margin-bottom:0;">
            Full-size football ground, regulated volleyball court, badminton courts, and cricket practice nets for inter-house leagues.
          </p>
        </div>
      </div>

      <div class="col-md-4">
        <div class="p-4 bg-light rounded-4 border h-100">
          <div class="info-band-icon mb-3" style="background:var(--light-mint); color:var(--primary-green);"><i class="bi bi-heart-pulse-fill"></i></div>
          <h4 style="font-size:1.25rem; font-weight:700; color:var(--heading);">Yoga &amp; Mind-Body Wellness</h4>
          <p style="font-size:0.9rem; color:var(--body-text); margin-bottom:0;">
            Morning assembly pranayama breathing exercises, Surya Namaskar series, and indoor mind games including chess and carrom tournaments.
          </p>
        </div>
      </div>
    </div>

    <!-- Inter-House Championship -->
    <div class="p-4 p-lg-5 rounded-4 text-white reveal-on-scroll" style="background:var(--deep-forest-green);">
      <div class="row g-4 align-items-center">
        <div class="col-lg-8">
          <span class="badge bg-warning text-dark px-3 py-1 rounded-pill mb-2 fw-bold">ANNUAL ATHLETIC MEET</span>
          <h3 style="font-size:2rem; font-weight:800; margin-bottom:1rem;">The Inter-House Trophy</h3>
          <p style="color:#D1E7DD; line-height:1.75; margin-bottom:0;">
            Every winter, our school playground hosts the two-day Annual Sports Championship featuring ceremonial march-pasts, torch lighting, student track heats, teacher-parent novelty races, and championship trophy awards.
          </p>
        </div>
        <div class="col-lg-4 text-center">
          <div class="official-placeholder-badge">
            <i class="bi bi-info-circle"></i> [Sports Roster Subject to Verification by Physical Instructor]
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
"""

save_page("sports-activities.html", get_page_template(
    "Sports Activities", 
    "Athletics & Games", 
    "Sports programs, athletic track events, football ground, volleyball tournaments, and yoga wellness at +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय.",
    "achievements",
    "<li><a href='achievements.html'>Achievements</a></li>",
    sports_content
))

# ==============================================================================
# 12. EXHIBITIONS (pages/exhibitions.html)
# ==============================================================================
exhibitions_content = """
<section class="py-5 bg-white">
  <div class="container">
    <div class="row align-items-center g-5 mb-5 reveal-on-scroll">
      <div class="col-lg-6">
        <span class="section-label-green">SCIENTIFIC INQUIRY &amp; INNOVATION</span>
        <h2 class="editorial-headline">Science, Technology &amp; Educational Exhibitions</h2>
        <p class="editorial-lead-text">
          Science exhibitions at +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय ignite student curiosity and apply textbook physics, chemistry, biology, and environmental science principles to real-world rural challenges.
        </p>
        <p style="color:var(--body-text); line-height:1.75;">
          Under the guidance of faculty mentors, secondary and higher secondary students design working prototypes, hydraulic mechanisms, renewable energy systems, and interactive math models. Our exhibition serves as a regional learning hub where parents and community visitors engage directly with young innovators.
        </p>
      </div>
      <div class="col-lg-6">
        <div class="editorial-image-frame">
          <img src="../assets/img/exhibitions/science-exhibition-models.svg" alt="Science Exhibition Models">
        </div>
      </div>
    </div>

    <!-- 3 Exhibition Key Focus Areas -->
    <div class="row g-4 mb-5 reveal-on-scroll">
      <div class="col-md-4">
        <div class="p-4 bg-light rounded-4 border h-100">
          <span class="badge bg-success-subtle text-success px-3 py-1 rounded-pill mb-2 font-monospace">ECOLOGY</span>
          <h4 style="font-size:1.25rem; font-weight:700; color:var(--heading);">Renewable Energy &amp; Solar</h4>
          <p style="font-size:0.9rem; color:var(--body-text); margin-bottom:0;">
            Demonstrations in solar panel power systems, mini wind turbine models, eco-friendly cooking stoves, and biomass energy concepts.
          </p>
        </div>
      </div>

      <div class="col-md-4">
        <div class="p-4 bg-light rounded-4 border h-100">
          <span class="badge bg-primary-subtle text-primary px-3 py-1 rounded-pill mb-2 font-monospace">PHYSICS &amp; ROBOTICS</span>
          <h4 style="font-size:1.25rem; font-weight:700; color:var(--heading);">Hydraulics &amp; Mechanical Physics</h4>
          <p style="font-size:0.9rem; color:var(--body-text); margin-bottom:0;">
            Pascal's law hydraulic lift models, automated railway crossing gates, rainwater harvesting architectures, and water purification units.
          </p>
        </div>
      </div>

      <div class="col-md-4">
        <div class="p-4 bg-light rounded-4 border h-100">
          <span class="badge bg-warning-subtle text-dark px-3 py-1 rounded-pill mb-2 font-monospace">MATHEMATICS &amp; ART</span>
          <h4 style="font-size:1.25rem; font-weight:700; color:var(--heading);">Math Models &amp; Craft Exhibits</h4>
          <p style="font-size:0.9rem; color:var(--body-text); margin-bottom:0;">
            Geometric solids, Pythagoras theorem visual proofs, trigonometric clinometers, regional handicraft exhibits, and eco-art installations.
          </p>
        </div>
      </div>
    </div>

    <!-- Official Notice Note -->
    <div class="official-notice-box reveal-on-scroll">
      <i class="bi bi-lightbulb-fill me-2"></i>
      <strong>District Participation:</strong> Selected models from our annual intra-school exhibition are nominated for block, district, and state-level science fairs organized by the Department of School Education and Literacy, Jharkhand.
    </div>
  </div>
</section>
"""

save_page("exhibitions.html", get_page_template(
    "Science Exhibitions", 
    "Innovation & Science", 
    "Annual science and educational exhibitions, working prototypes, solar energy displays, and innovative student models at +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय.",
    "achievements",
    "<li><a href='achievements.html'>Achievements</a></li>",
    exhibitions_content
))

# ==============================================================================
# 13. SKILLS COMPETITION (pages/skills-competition.html)
# ==============================================================================
skills_content = """
<section class="py-5 bg-white">
  <div class="container">
    <div class="row align-items-center g-5 mb-5 reveal-on-scroll">
      <div class="col-lg-6">
        <span class="section-label-green">TALENT &amp; INTELLECTUAL CHALLENGE</span>
        <h2 class="editorial-headline">Skills Competition &amp; Talent Development</h2>
        <p class="editorial-lead-text">
          Encouraging healthy intellectual contest, rapid analytical thinking, and expressive creativity through intra-school and inter-school academic competitions at +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय.
        </p>
        <p style="color:var(--body-text); line-height:1.75;">
          Our annual skills calendar incorporates debate competitions in Hindi and English, general knowledge and current affairs quizzes, essay writing contests, handwriting excellence, fine arts, and mathematical problem-solving challenges.
        </p>
      </div>
      <div class="col-lg-6">
        <div class="editorial-image-frame">
          <img src="../assets/img/students/students-discussion.svg" alt="Students in Skills Discussion">
        </div>
      </div>
    </div>

    <!-- Competition Categories -->
    <div class="row g-4 mb-5 reveal-on-scroll">
      <div class="col-md-6">
        <div class="p-4 bg-light rounded-4 border h-100">
          <div class="d-flex align-items-center gap-3 mb-2">
            <div class="info-band-icon" style="background:var(--light-mint); color:var(--primary-green);"><i class="bi bi-mic-fill"></i></div>
            <h4 style="font-size:1.25rem; font-weight:700; color:var(--heading); margin-bottom:0;">Debate &amp; Elocution</h4>
          </div>
          <p style="font-size:0.9rem; color:var(--body-text); margin-bottom:0;">
            Bilingual debating leagues on contemporary issues including environmental conservation, technology in education, and youth civic responsibilities.
          </p>
        </div>
      </div>

      <div class="col-md-6">
        <div class="p-4 bg-light rounded-4 border h-100">
          <div class="d-flex align-items-center gap-3 mb-2">
            <div class="info-band-icon" style="background:var(--light-mint); color:var(--primary-green);"><i class="bi bi-patch-question-fill"></i></div>
            <h4 style="font-size:1.25rem; font-weight:700; color:var(--heading); margin-bottom:0;">General Knowledge &amp; Science Quiz</h4>
          </div>
          <p style="font-size:0.9rem; color:var(--body-text); margin-bottom:0;">
            Fast-paced multi-round buzzer quizzes assessing awareness of Indian heritage, world geography, scientific inventions, and current events.
          </p>
        </div>
      </div>

      <div class="col-md-6">
        <div class="p-4 bg-light rounded-4 border h-100">
          <div class="d-flex align-items-center gap-3 mb-2">
            <div class="info-band-icon" style="background:var(--light-mint); color:var(--primary-green);"><i class="bi bi-pen-fill"></i></div>
            <h4 style="font-size:1.25rem; font-weight:700; color:var(--heading); margin-bottom:0;">Creative Writing &amp; Essay Contest</h4>
          </div>
          <p style="font-size:0.9rem; color:var(--body-text); margin-bottom:0;">
            Stimulating literary prose, poetry creation, and essay composition in Hindi, English, and regional languages.
          </p>
        </div>
      </div>

      <div class="col-md-6">
        <div class="p-4 bg-light rounded-4 border h-100">
          <div class="d-flex align-items-center gap-3 mb-2">
            <div class="info-band-icon" style="background:var(--light-mint); color:var(--primary-green);"><i class="bi bi-palette-fill"></i></div>
            <h4 style="font-size:1.25rem; font-weight:700; color:var(--heading); margin-bottom:0;">Painting &amp; Poster Making</h4>
          </div>
          <p style="font-size:0.9rem; color:var(--body-text); margin-bottom:0;">
            Expressive fine art contests on themes of national harmony, forest conservation, and local rural culture.
          </p>
        </div>
      </div>
    </div>
  </div>
</section>
"""

save_page("skills-competition.html", get_page_template(
    "Skills Competition", 
    "Student Talent", 
    "Debates, quizzes, creative writing, and skills competitions cultivating talent and leadership at +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय.",
    "achievements",
    "<li><a href='achievements.html'>Achievements</a></li>",
    skills_content
))

# ==============================================================================
# 14. VOCATIONAL ACTIVITIES (pages/vocational-activities.html)
# ==============================================================================
vocational_content = """
<section class="py-5 bg-white">
  <div class="container">
    <div class="row align-items-center g-5 mb-5 reveal-on-scroll">
      <div class="col-lg-6">
        <span class="section-label-green">APPLIED EDUCATION &amp; VOCATIONAL READINESS</span>
        <h2 class="editorial-headline">Empowering Youth with Practical Life Skills</h2>
        <p class="editorial-lead-text">
          Aligned with the National Education Policy (NEP) goals and Jharkhand State educational guidelines, vocational learning at +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय bridges academic theory with practical craftsmanship and livelihood readiness.
        </p>
        <p style="color:var(--body-text); line-height:1.75;">
          Our vocational and work-experience modules expose students to hands-on technical skills, basic electrical wiring safety, digital spreadsheet literacy, handicraft creation, organic agriculture techniques, and basic bookkeeping. This fosters dignity of labor, financial prudence, and entrepreneurial self-reliance.
        </p>
      </div>
      <div class="col-lg-6">
        <div class="editorial-image-frame">
          <img src="../assets/img/exhibitions/skills-workshop.svg" alt="Vocational Skills Workshop">
        </div>
      </div>
    </div>

    <!-- Practical Modules -->
    <div class="row g-4 mb-5 reveal-on-scroll">
      <div class="col-md-4">
        <div class="p-4 bg-light rounded-4 border h-100">
          <div class="info-band-icon mb-3" style="background:var(--light-mint); color:var(--primary-green);"><i class="bi bi-cpu-fill"></i></div>
          <h4 style="font-size:1.25rem; font-weight:700; color:var(--heading);">Digital &amp; ICT Literacy</h4>
          <p style="font-size:0.9rem; color:var(--body-text); margin-bottom:0;">
            Word processing, spreadsheet accounting, internet research skills, cyber safety essentials, and introductory programming principles.
          </p>
        </div>
      </div>

      <div class="col-md-4">
        <div class="p-4 bg-light rounded-4 border h-100">
          <div class="info-band-icon mb-3" style="background:var(--light-mint); color:var(--primary-green);"><i class="bi bi-tools"></i></div>
          <h4 style="font-size:1.25rem; font-weight:700; color:var(--heading);">Applied Technical Crafts</h4>
          <p style="font-size:0.9rem; color:var(--body-text); margin-bottom:0;">
            Basic domestic circuit assembly, safe appliance troubleshooting, measurement instruments, and woodworking craft.
          </p>
        </div>
      </div>

      <div class="col-md-4">
        <div class="p-4 bg-light rounded-4 border h-100">
          <div class="info-band-icon mb-3" style="background:var(--light-mint); color:var(--primary-green);"><i class="bi bi-flower1"></i></div>
          <h4 style="font-size:1.25rem; font-weight:700; color:var(--heading);">Agro &amp; Botanical Skills</h4>
          <p style="font-size:0.9rem; color:var(--body-text); margin-bottom:0;">
            Campus botanical gardening, organic composting techniques, nursery management, and understanding local soil health.
          </p>
        </div>
      </div>
    </div>
  </div>
</section>
"""

save_page("vocational-activities.html", get_page_template(
    "Vocational Activities", 
    "Applied Skills", 
    "Vocational training, applied life skills, ICT education, and practical workshops at +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय.",
    "achievements",
    "<li><a href='achievements.html'>Achievements</a></li>",
    vocational_content
))

# ==============================================================================
# 15. RESULTS (pages/results.html)
# ==============================================================================
results_content = """
<section class="py-5 bg-white">
  <div class="container">
    <div class="text-center max-w-700 mx-auto mb-5 reveal-on-scroll">
      <span class="section-label-green">BOARD GAZETTE &amp; ARCHIVE</span>
      <h2 class="editorial-headline">Official Examination Results Portal</h2>
      <p class="text-muted">
        Access official board examination gazette archives and session results affiliated with the Jharkhand Academic Council (JAC), Ranchi.
      </p>
    </div>

    <!-- Official Protocol Notice -->
    <div class="official-notice-box mb-4 reveal-on-scroll">
      <i class="bi bi-file-earmark-check-fill me-2"></i>
      <strong>Official Result Protocol:</strong> Official examination results and mark-sheets for Class 10 (Secondary) and Class 12 (+2 Higher Secondary) are issued by the Jharkhand Academic Council, Ranchi. Verified original passing certificates are distributed to candidates directly through the administrative desk.
    </div>

    <!-- Interactive Results Table with Filters -->
    <div class="results-table-container reveal-on-scroll">
      <div class="results-filter-controls">
        <div class="d-flex flex-wrap gap-2 align-items-center">
          <label class="fw-bold text-dark" style="font-size:0.85rem;">Filter by Session:</label>
          <select class="form-select form-select-sm" id="resultSessionFilter" style="width:160px;">
            <option value="all">All Sessions</option>
            <option value="2024 - 2025">2024 - 2025</option>
            <option value="2023 - 2024">2023 - 2024</option>
          </select>
        </div>

        <div class="d-flex flex-wrap gap-2 align-items-center">
          <label class="fw-bold text-dark" style="font-size:0.85rem;">Filter by Class:</label>
          <select class="form-select form-select-sm" id="resultClassFilter" style="width:180px;">
            <option value="all">All Classes &amp; Streams</option>
            <option value="Class 10">Class 10 (Secondary)</option>
            <option value="Science">Class 12 (Science)</option>
            <option value="Arts">Class 12 (Arts)</option>
            <option value="Commerce">Class 12 (Commerce)</option>
          </select>
        </div>

        <div>
          <input type="text" class="form-control form-control-sm" id="resultSearchInput" placeholder="Search gazette archives...">
        </div>
      </div>

      <table class="results-table">
        <thead>
          <tr>
            <th>Examination Name</th>
            <th>Academic Session</th>
            <th>Class / Stream</th>
            <th>Gazette Status</th>
            <th>Verification Action</th>
          </tr>
        </thead>
        <tbody>
          <tr class="result-data-row" data-session="2024 - 2025" data-class="Class 10">
            <td>
              <strong>JAC Secondary (Class X) Annual Board Examination</strong>
              <div style="font-size:0.75rem; color:#6B7280;">Conducted by Jharkhand Academic Council, Ranchi</div>
            </td>
            <td>2024 - 2025</td>
            <td>Class 10 (Secondary)</td>
            <td><span class="badge bg-success-subtle text-success">Official Gazette On Record</span></td>
            <td>
              <a href="../assets/documents/results/official-results-notice.txt" target="_blank" class="btn btn-sm btn-outline-success">
                <i class="bi bi-file-earmark-text"></i> View Gazette Notice
              </a>
            </td>
          </tr>

          <tr class="result-data-row" data-session="2024 - 2025" data-class="Science">
            <td>
              <strong>JAC Higher Secondary (Class XII) Science Stream Board</strong>
              <div style="font-size:0.75rem; color:#6B7280;">Physics, Chemistry, Math &amp; Biology Batches</div>
            </td>
            <td>2024 - 2025</td>
            <td>Class 12 (Science)</td>
            <td><span class="badge bg-success-subtle text-success">Official Gazette On Record</span></td>
            <td>
              <a href="../assets/documents/results/official-results-notice.txt" target="_blank" class="btn btn-sm btn-outline-success">
                <i class="bi bi-file-earmark-text"></i> View Gazette Notice
              </a>
            </td>
          </tr>

          <tr class="result-data-row" data-session="2024 - 2025" data-class="Arts">
            <td>
              <strong>JAC Higher Secondary (Class XII) Arts Stream Board</strong>
              <div style="font-size:0.75rem; color:#6B7280;">History, Political Science &amp; Economics Batches</div>
            </td>
            <td>2024 - 2025</td>
            <td>Class 12 (Arts)</td>
            <td><span class="badge bg-success-subtle text-success">Official Gazette On Record</span></td>
            <td>
              <a href="../assets/documents/results/official-results-notice.txt" target="_blank" class="btn btn-sm btn-outline-success">
                <i class="bi bi-file-earmark-text"></i> View Gazette Notice
              </a>
            </td>
          </tr>

          <tr class="result-data-row" data-session="2024 - 2025" data-class="Commerce">
            <td>
              <strong>JAC Higher Secondary (Class XII) Commerce Stream Board</strong>
              <div style="font-size:0.75rem; color:#6B7280;">Accountancy &amp; Business Studies Batches</div>
            </td>
            <td>2024 - 2025</td>
            <td>Class 12 (Commerce)</td>
            <td><span class="badge bg-success-subtle text-success">Official Gazette On Record</span></td>
            <td>
              <a href="../assets/documents/results/official-results-notice.txt" target="_blank" class="btn btn-sm btn-outline-success">
                <i class="bi bi-file-earmark-text"></i> View Gazette Notice
              </a>
            </td>
          </tr>

          <tr class="result-data-row" data-session="2023 - 2024" data-class="Class 10">
            <td>
              <strong>JAC Secondary (Class X) Annual Board Examination</strong>
              <div style="font-size:0.75rem; color:#6B7280;">Matriculation Batch Archive</div>
            </td>
            <td>2023 - 2024</td>
            <td>Class 10 (Secondary)</td>
            <td><span class="badge bg-secondary-subtle text-secondary">Archived Record</span></td>
            <td>
              <a href="../assets/documents/results/official-results-notice.txt" target="_blank" class="btn btn-sm btn-outline-secondary">
                <i class="bi bi-archive"></i> Archive Record
              </a>
            </td>
          </tr>
        </tbody>
      </table>

      <div class="p-3 bg-light border-top text-center">
        <small class="text-muted">
          For candidate-specific mark-sheet corrections or migration certificates, contact the administrative desk during official working hours.
        </small>
      </div>
    </div>
  </div>
</section>
"""

save_page("results.html", get_page_template(
    "Examination Results", 
    "Academic Gazette", 
    "Official JAC examination results, archived result gazettes, and academic verification guidance for +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय.",
    "examination",
    "<li><a href='results.html'>Examination</a></li>",
    results_content
))

print("Batch 3 generated successfully!")
