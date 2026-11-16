import os
from generate_pages_batch1 import get_page_template, save_page

# ==============================================================================
# 6. CLASSES & SUBJECTS (pages/classes-subjects.html)
# ==============================================================================
classes_subjects_content = """
<section class="py-5 bg-white">
  <div class="container">
    <div class="text-center max-w-700 mx-auto mb-5 reveal-on-scroll">
      <span class="section-label-green">CLASS STRUCTURE &amp; STREAMS</span>
      <h2 class="editorial-headline">Classes, Subject Streams &amp; Curriculum</h2>
      <p class="text-muted">
        Detailed breakdown of classes offered, compulsory core subjects, elective stream choices, and examination guidelines affiliated with Jharkhand Academic Council (JAC), Ranchi.
      </p>
    </div>

    <!-- Higher Secondary +2 Streams -->
    <div class="mb-5 reveal-on-scroll">
      <h3 style="font-size:1.85rem; font-weight:800; color:var(--deep-forest-green); margin-bottom:1.5rem;">
        +2 Higher Secondary Streams (Classes 11 &amp; 12)
      </h3>

      <div class="row g-4">
        <!-- Science -->
        <div class="col-lg-4">
          <div class="p-4 bg-light rounded-4 border h-100">
            <div class="d-flex align-items-center gap-2 mb-3">
              <span class="badge bg-primary px-3 py-2 rounded-pill font-monospace">Science Stream</span>
            </div>
            <h4 style="font-size:1.3rem; font-weight:700; color:var(--heading);">Pure &amp; Applied Sciences</h4>
            <p style="font-size:0.875rem; color:var(--body-text);">Comprehensive scientific education preparing candidates for engineering, medical sciences, research, and technical professions.</p>
            
            <div class="mt-3 pt-3 border-top">
              <div style="font-size:0.8rem; font-weight:700; color:var(--deep-forest-green); text-transform:uppercase;">Compulsory Core:</div>
              <ul class="list-unstyled mb-2" style="font-size:0.85rem; color:var(--body-text);">
                <li><i class="bi bi-dot text-primary"></i> Core Language (Hindi / English)</li>
                <li><i class="bi bi-dot text-primary"></i> Physics (Theory + Practical)</li>
                <li><i class="bi bi-dot text-primary"></i> Chemistry (Theory + Practical)</li>
              </ul>

              <div style="font-size:0.8rem; font-weight:700; color:var(--deep-forest-green); text-transform:uppercase;">Elective Options:</div>
              <ul class="list-unstyled mb-0" style="font-size:0.85rem; color:var(--body-text);">
                <li><i class="bi bi-dot text-primary"></i> Mathematics / Biology</li>
                <li><i class="bi bi-dot text-primary"></i> Computer Science / Economics</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- Arts -->
        <div class="col-lg-4">
          <div class="p-4 bg-light rounded-4 border h-100">
            <div class="d-flex align-items-center gap-2 mb-3">
              <span class="badge bg-success px-3 py-2 rounded-pill font-monospace">Arts Stream</span>
            </div>
            <h4 style="font-size:1.3rem; font-weight:700; color:var(--heading);">Humanities &amp; Social Sciences</h4>
            <p style="font-size:0.875rem; color:var(--body-text);">Deep investigation of historical trajectories, democratic governance, economic theory, geographic geography, and languages.</p>
            
            <div class="mt-3 pt-3 border-top">
              <div style="font-size:0.8rem; font-weight:700; color:var(--deep-forest-green); text-transform:uppercase;">Compulsory Core:</div>
              <ul class="list-unstyled mb-2" style="font-size:0.85rem; color:var(--body-text);">
                <li><i class="bi bi-dot text-success"></i> Core Language (Hindi / English)</li>
                <li><i class="bi bi-dot text-success"></i> History</li>
                <li><i class="bi bi-dot text-success"></i> Political Science</li>
              </ul>

              <div style="font-size:0.8rem; font-weight:700; color:var(--deep-forest-green); text-transform:uppercase;">Elective Options:</div>
              <ul class="list-unstyled mb-0" style="font-size:0.85rem; color:var(--body-text);">
                <li><i class="bi bi-dot text-success"></i> Geography (Theory + Practical)</li>
                <li><i class="bi bi-dot text-success"></i> Economics / Sociology</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- Commerce -->
        <div class="col-lg-4">
          <div class="p-4 bg-light rounded-4 border h-100">
            <div class="d-flex align-items-center gap-2 mb-3">
              <span class="badge bg-warning text-dark px-3 py-2 rounded-pill font-monospace">Commerce Stream</span>
            </div>
            <h4 style="font-size:1.3rem; font-weight:700; color:var(--heading);">Commerce &amp; Financial Studies</h4>
            <p style="font-size:0.875rem; color:var(--body-text);">Focus on financial accounting, corporate principles, trade dynamics, banking institutions, and economic development.</p>
            
            <div class="mt-3 pt-3 border-top">
              <div style="font-size:0.8rem; font-weight:700; color:var(--deep-forest-green); text-transform:uppercase;">Compulsory Core:</div>
              <ul class="list-unstyled mb-2" style="font-size:0.85rem; color:var(--body-text);">
                <li><i class="bi bi-dot text-warning"></i> Core Language (Hindi / English)</li>
                <li><i class="bi bi-dot text-warning"></i> Accountancy</li>
                <li><i class="bi bi-dot text-warning"></i> Business Studies</li>
              </ul>

              <div style="font-size:0.8rem; font-weight:700; color:var(--deep-forest-green); text-transform:uppercase;">Elective Options:</div>
              <ul class="list-unstyled mb-0" style="font-size:0.85rem; color:var(--body-text);">
                <li><i class="bi bi-dot text-warning"></i> Economics</li>
                <li><i class="bi bi-dot text-warning"></i> Commercial Mathematics / Entrepreneurship</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Secondary Wing Table -->
    <div class="reveal-on-scroll">
      <h3 style="font-size:1.85rem; font-weight:800; color:var(--deep-forest-green); margin-bottom:1.5rem;">
        Secondary Wing Curriculum (Classes 9 &amp; 10)
      </h3>

      <div class="table-responsive bg-white rounded-4 border shadow-sm overflow-hidden mb-4">
        <table class="table table-hover align-middle mb-0">
          <thead style="background-color:var(--deep-forest-green); color:var(--white);">
            <tr>
              <th class="py-3 px-4">Subject Category</th>
              <th class="py-3 px-4">Subjects Prescribed</th>
              <th class="py-3 px-4">Assessment Structure</th>
              <th class="py-3 px-4">Board Examination</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="px-4 fw-bold">First Language</td>
              <td class="px-4">Hindi (Course A / Course B)</td>
              <td class="px-4">80 Marks Board + 20 Marks Internal</td>
              <td class="px-4">JAC Matriculation</td>
            </tr>
            <tr>
              <td class="px-4 fw-bold">Second Language</td>
              <td class="px-4">English / Regional Language</td>
              <td class="px-4">80 Marks Board + 20 Marks Internal</td>
              <td class="px-4">JAC Matriculation</td>
            </tr>
            <tr>
              <td class="px-4 fw-bold">Third Language</td>
              <td class="px-4">Sanskrit / Regional Elective</td>
              <td class="px-4">80 Marks Board + 20 Marks Internal</td>
              <td class="px-4">JAC Matriculation</td>
            </tr>
            <tr>
              <td class="px-4 fw-bold">Mathematics</td>
              <td class="px-4">Standard &amp; Basic Mathematics</td>
              <td class="px-4">80 Marks Board + 20 Marks Internal Practical</td>
              <td class="px-4">JAC Matriculation</td>
            </tr>
            <tr>
              <td class="px-4 fw-bold">Science &amp; Technology</td>
              <td class="px-4">Physics, Chemistry, Biology</td>
              <td class="px-4">80 Marks Board + 20 Marks Lab Practical</td>
              <td class="px-4">JAC Matriculation</td>
            </tr>
            <tr>
              <td class="px-4 fw-bold">Social Science</td>
              <td class="px-4">History, Civics, Geography, Economics</td>
              <td class="px-4">80 Marks Board + 20 Marks Project Assessment</td>
              <td class="px-4">JAC Matriculation</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="official-placeholder-badge">
        <i class="bi bi-info-circle"></i> Note: Specific subject elective quotas and fee details are governed by annual Jharkhand State Department notifications.
      </div>
    </div>
  </div>
</section>
"""

save_page("classes-subjects.html", get_page_template(
    "Classes & Subjects", 
    "Academic Streams", 
    "Comprehensive guide to classes offered, secondary subject structure, and +2 Science, Arts, and Commerce streams at +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय.",
    "academic",
    "<li><a href='academic-overview.html'>Academic</a></li>",
    classes_subjects_content
))

# ==============================================================================
# 7. ACADEMIC CALENDAR (pages/academic-calendar.html)
# ==============================================================================
calendar_content = """
<section class="py-5 bg-white">
  <div class="container">
    <div class="text-center max-w-700 mx-auto mb-5 reveal-on-scroll">
      <span class="section-label-green">ANNUAL ROADMAP</span>
      <h2 class="editorial-headline">Academic Calendar &amp; Important Dates</h2>
      <p class="text-muted">
        Chronological schedule of terms, internal evaluations, JAC board examination milestones, national celebrations, and seasonal recesses.
      </p>
    </div>

    <div class="official-notice-box mb-4 reveal-on-scroll">
      <i class="bi bi-calendar-check-fill me-2"></i>
      <strong>Institutional Notice:</strong> Official calendar timelines adhere to notifications published by the Department of School Education and Literacy, Government of Jharkhand, and Jharkhand Academic Council, Ranchi.
    </div>

    <!-- Timeline of Academic Milestones -->
    <div class="row g-4 mb-5 reveal-on-scroll">
      <!-- April - June -->
      <div class="col-lg-6">
        <div class="p-4 bg-light rounded-4 border h-100">
          <div class="d-flex justify-content-between align-items-center mb-3">
            <h4 style="font-size:1.3rem; font-weight:800; color:var(--deep-forest-green); margin-bottom:0;">Term I: April – June</h4>
            <span class="badge bg-success-subtle text-success">New Session</span>
          </div>
          <ul class="list-unstyled d-flex flex-column gap-3 mb-0" style="font-size:0.9rem; color:var(--body-text);">
            <li class="d-flex gap-3">
              <span class="badge bg-secondary rounded-pill" style="height:fit-content;">Apr</span>
              <div>
                <strong>Commencement of New Academic Session:</strong> Classroom allotment, distribution of state textbooks, and parent orientation for Class 9 and +2 entrants.
              </div>
            </li>
            <li class="d-flex gap-3">
              <span class="badge bg-secondary rounded-pill" style="height:fit-content;">May</span>
              <div>
                <strong>Summer Co-Curricular Week &amp; Pre-Vacation Work:</strong> Project assignments, tree plantation drives on campus, and holiday homework distribution.
              </div>
            </li>
            <li class="d-flex gap-3">
              <span class="badge bg-secondary rounded-pill" style="height:fit-content;">Jun</span>
              <div>
                <strong>Re-opening Post Summer Recess &amp; Diagnostic Tests:</strong> Review of student vacation projects and commencement of first periodic assessment.
              </div>
            </li>
          </ul>
        </div>
      </div>

      <!-- July - September -->
      <div class="col-lg-6">
        <div class="p-4 bg-light rounded-4 border h-100">
          <div class="d-flex justify-content-between align-items-center mb-3">
            <h4 style="font-size:1.3rem; font-weight:800; color:var(--deep-forest-green); margin-bottom:0;">Term II: July – September</h4>
            <span class="badge bg-primary-subtle text-primary">Formative Stage</span>
          </div>
          <ul class="list-unstyled d-flex flex-column gap-3 mb-0" style="font-size:0.9rem; color:var(--body-text);">
            <li class="d-flex gap-3">
              <span class="badge bg-secondary rounded-pill" style="height:fit-content;">Jul</span>
              <div>
                <strong>First Periodic Assessments &amp; Science Club Formation:</strong> Conduct of unit examinations across secondary and higher secondary batches.
              </div>
            </li>
            <li class="d-flex gap-3">
              <span class="badge bg-secondary rounded-pill" style="height:fit-content;">Aug</span>
              <div>
                <strong>Independence Day Celebrations (15th August):</strong> Ceremonial flag hoisting, patriotic song presentations, speech contest, and Scout &amp; Guide parade.
              </div>
            </li>
            <li class="d-flex gap-3">
              <span class="badge bg-secondary rounded-pill" style="height:fit-content;">Sep</span>
              <div>
                <strong>Teachers' Day (5th Sept) &amp; Mid-Term Evaluations:</strong> Student-led felicitation of faculty and conduct of Mid-Term Terminal Examinations.
              </div>
            </li>
          </ul>
        </div>
      </div>

      <!-- October - December -->
      <div class="col-lg-6">
        <div class="p-4 bg-light rounded-4 border h-100">
          <div class="d-flex justify-content-between align-items-center mb-3">
            <h4 style="font-size:1.3rem; font-weight:800; color:var(--deep-forest-green); margin-bottom:0;">Term III: October – December</h4>
            <span class="badge bg-warning-subtle text-dark">Festive &amp; Exhibitions</span>
          </div>
          <ul class="list-unstyled d-flex flex-column gap-3 mb-0" style="font-size:0.9rem; color:var(--body-text);">
            <li class="d-flex gap-3">
              <span class="badge bg-secondary rounded-pill" style="height:fit-content;">Oct</span>
              <div>
                <strong>Mahatma Gandhi Jayanti &amp; Autumn Recess:</strong> Cleanliness drive (Swachhata Pakhwada) and autumn festival holidays.
              </div>
            </li>
            <li class="d-flex gap-3">
              <span class="badge bg-secondary rounded-pill" style="height:fit-content;">Nov</span>
              <div>
                <strong>Annual Science Exhibition &amp; Jharkhand Statehood Day:</strong> Student model displays, tribal cultural showcase, and regional heritage celebration.
              </div>
            </li>
            <li class="d-flex gap-3">
              <span class="badge bg-secondary rounded-pill" style="height:fit-content;">Dec</span>
              <div>
                <strong>Annual Athletic Sports Meet &amp; Winter Preparation:</strong> Track races, inter-house volleyball, and revision classes for Classes 10 &amp; 12.
              </div>
            </li>
          </ul>
        </div>
      </div>

      <!-- January - March -->
      <div class="col-lg-6">
        <div class="p-4 bg-light rounded-4 border h-100">
          <div class="d-flex justify-content-between align-items-center mb-3">
            <h4 style="font-size:1.3rem; font-weight:800; color:var(--deep-forest-green); margin-bottom:0;">Term IV: January – March</h4>
            <span class="badge bg-danger-subtle text-danger">Board Examinations</span>
          </div>
          <ul class="list-unstyled d-flex flex-column gap-3 mb-0" style="font-size:0.9rem; color:var(--body-text);">
            <li class="d-flex gap-3">
              <span class="badge bg-secondary rounded-pill" style="height:fit-content;">Jan</span>
              <div>
                <strong>Pre-Board Examinations &amp; Republic Day (26th Jan):</strong> Pre-matric and pre-intermediate examinations; ceremonial parade and patriotic arts.
              </div>
            </li>
            <li class="d-flex gap-3">
              <span class="badge bg-secondary rounded-pill" style="height:fit-content;">Feb</span>
              <div>
                <strong>JAC Annual Board Examinations:</strong> Formal conduct of Class 10 (Secondary) and Class 12 (Higher Secondary) State Board Examinations.
              </div>
            </li>
            <li class="d-flex gap-3">
              <span class="badge bg-secondary rounded-pill" style="height:fit-content;">Mar</span>
              <div>
                <strong>Annual Results Declaration &amp; Session Wrap:</strong> Evaluation of home examinations for Classes 9 &amp; 11 and commencement of new admissions.
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>
"""

save_page("academic-calendar.html", get_page_template(
    "Academic Calendar", 
    "Annual Schedule", 
    "Annual academic roadmap, term assessment schedules, holidays, and board exam timeline for +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय.",
    "academic",
    "<li><a href='academic-overview.html'>Academic</a></li>",
    calendar_content
))

# ==============================================================================
# 8. TEACHING & LEARNING (pages/teaching-learning.html)
# ==============================================================================
teaching_content = """
<section class="py-5 bg-white">
  <div class="container">
    <div class="row align-items-center g-5 mb-5 reveal-on-scroll">
      <div class="col-lg-6">
        <span class="section-label-green">PEDAGOGICAL INNOVATION</span>
        <h2 class="editorial-headline">Cultivating Curiosity Through Active Learning</h2>
        <p class="editorial-lead-text">
          At +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय, we believe teaching is an active dialogue between teacher and student. We combine classic foundational instruction with experimental demonstrations, group dialogues, and ICT-assisted multimedia pedagogy.
        </p>
        <p style="color:var(--body-text); line-height:1.75;">
          Our certified teaching staff is regularly trained in child-centered pedagogy, continuous comprehensive evaluation (CCE), and empathetic classroom management. Every learner is encouraged to question concepts, perform lab apparatus setups, and express their individual insights.
        </p>
      </div>
      <div class="col-lg-6">
        <div class="editorial-image-frame">
          <img src="../assets/img/classrooms/smart-classroom.svg" alt="Smart Classroom Pedagogy">
        </div>
      </div>
    </div>

    <!-- 4 Key Learning Modalities -->
    <div class="row g-4 mb-5 reveal-on-scroll">
      <div class="col-md-3">
        <div class="p-4 bg-light rounded-4 border h-100 text-center">
          <div class="contact-icon-bubble mx-auto mb-3" style="width:55px; height:55px; font-size:1.4rem;">
            <i class="bi bi-easel-fill"></i>
          </div>
          <h4 style="font-size:1.15rem; font-weight:700; color:var(--heading);">Classroom Instruction</h4>
          <p style="font-size:0.85rem; color:var(--body-text); margin-bottom:0;">
            Structured concept delivery, rigorous blackboard derivation, clear bilingual exposition, and daily homework review.
          </p>
        </div>
      </div>

      <div class="col-md-3">
        <div class="p-4 bg-light rounded-4 border h-100 text-center">
          <div class="contact-icon-bubble mx-auto mb-3" style="width:55px; height:55px; font-size:1.4rem;">
            <i class="bi bi-people-fill"></i>
          </div>
          <h4 style="font-size:1.15rem; font-weight:700; color:var(--heading);">Collaborative Peer Circles</h4>
          <p style="font-size:0.85rem; color:var(--body-text); margin-bottom:0;">
            Group study circles where students solve complex mathematical problems and scientific numericals together.
          </p>
        </div>
      </div>

      <div class="col-md-3">
        <div class="p-4 bg-light rounded-4 border h-100 text-center">
          <div class="contact-icon-bubble mx-auto mb-3" style="width:55px; height:55px; font-size:1.4rem;">
            <i class="bi bi-flask-fill"></i>
          </div>
          <h4 style="font-size:1.15rem; font-weight:700; color:var(--heading);">Practical Laboratories</h4>
          <p style="font-size:0.85rem; color:var(--body-text); margin-bottom:0;">
            Hands-on physics experiments, chemical reaction analysis, microscope biology slides, and computer software labs.
          </p>
        </div>
      </div>

      <div class="col-md-3">
        <div class="p-4 bg-light rounded-4 border h-100 text-center">
          <div class="contact-icon-bubble mx-auto mb-3" style="width:55px; height:55px; font-size:1.4rem;">
            <i class="bi bi-check2-circle"></i>
          </div>
          <h4 style="font-size:1.15rem; font-weight:700; color:var(--heading);">Formative Assessments</h4>
          <p style="font-size:0.85rem; color:var(--body-text); margin-bottom:0;">
            Frequent low-stakes quizzes, periodic unit tests, and remedial support sessions to reinforce conceptual clarity.
          </p>
        </div>
      </div>
    </div>

    <!-- Remedial & Enrichment Support -->
    <div class="p-4 p-lg-5 bg-light rounded-4 border reveal-on-scroll">
      <div class="row g-4 align-items-center">
        <div class="col-lg-8">
          <span class="badge bg-success-subtle text-success px-3 py-1 rounded-pill mb-2 font-monospace">STUDENT SUCCESS</span>
          <h3 style="font-size:1.85rem; font-weight:800; color:var(--deep-forest-green); margin-bottom:1rem;">
            Remedial Mentoring &amp; Exam Preparation
          </h3>
          <p style="color:var(--body-text); line-height:1.75; margin-bottom:0;">
            Before board examinations, special morning and afternoon tutorial sessions are conducted for students requiring additional conceptual reinforcement. Previous years' JAC board question papers are solved under the direct supervision of subject teachers.
          </p>
        </div>
        <div class="col-lg-4 text-center">
          <a href="contact.html" class="btn btn-success rounded-pill px-4 py-3 fw-bold">
            <i class="bi bi-chat-dots-fill me-1"></i> Speak with Academic Mentors
          </a>
        </div>
      </div>
    </div>
  </div>
</section>
"""

save_page("teaching-learning.html", get_page_template(
    "Teaching & Learning", 
    "Pedagogy & Methodology", 
    "Child-centric teaching pedagogies, experiential laboratory learning, peer study circles, and assessment systems at +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय.",
    "academic",
    "<li><a href='academic-overview.html'>Academic</a></li>",
    teaching_content
))

# ==============================================================================
# 9. ACHIEVEMENTS (pages/achievements.html)
# ==============================================================================
achievements_content = """
<section class="py-5 bg-white">
  <div class="container">
    <div class="text-center max-w-700 mx-auto mb-5 reveal-on-scroll">
      <span class="section-label-green">RECOGNITION &amp; DISTINCTIONS</span>
      <h2 class="editorial-headline">Celebrating Student Endeavors &amp; Milestones</h2>
      <p class="text-muted">
        Documenting student dedication, inter-school participation, sportsmanship, and institutional recognitions across Potka block and East Singhbhum district.
      </p>
    </div>

    <div class="official-notice-box mb-5 reveal-on-scroll">
      <i class="bi bi-shield-check me-2"></i>
      <strong>Data Accuracy Protocol:</strong> In accordance with our official editorial policy, specific historical examination percentages and individual awards are subject to ongoing administrative verification from school records.
    </div>

    <!-- Achievement Pillars -->
    <div class="row g-4 mb-5 reveal-on-scroll">
      <div class="col-lg-4">
        <div class="card h-100 border-0 shadow-sm rounded-4 overflow-hidden">
          <img src="../assets/img/cultural/cultural-folk-dance.svg" class="card-img-top" style="height:220px; object-fit:cover;" alt="Cultural Heritage">
          <div class="card-body p-4">
            <span class="badge bg-warning-subtle text-dark px-3 py-1 rounded-pill mb-2 font-monospace">Cultural Honors</span>
            <h4 style="font-size:1.25rem; font-weight:700; color:var(--heading);">Block &amp; District Cultural Festivals</h4>
            <p style="font-size:0.9rem; color:var(--body-text);">Regular representation of indigenous Jharkhand folk dances, patriotic choruses, and theatrical performances celebrating regional culture.</p>
            <div class="official-placeholder-badge mt-2">
              <i class="bi bi-info-circle"></i> [Achievement Record to be Verified by School Head]
            </div>
          </div>
        </div>
      </div>

      <div class="col-lg-4">
        <div class="card h-100 border-0 shadow-sm rounded-4 overflow-hidden">
          <img src="../assets/img/sports/sports-track-field.svg" class="card-img-top" style="height:220px; object-fit:cover;" alt="Athletic Honors">
          <div class="card-body p-4">
            <span class="badge bg-success-subtle text-success px-3 py-1 rounded-pill mb-2 font-monospace">Athletic Distinctions</span>
            <h4 style="font-size:1.25rem; font-weight:700; color:var(--heading);">Inter-School Track &amp; Field Tournaments</h4>
            <p style="font-size:0.9rem; color:var(--body-text);">Outstanding performances in 100m, 400m sprint events, long jump, volleyball and football tournaments within East Singhbhum.</p>
            <div class="official-placeholder-badge mt-2">
              <i class="bi bi-info-circle"></i> [Sports Roster Subject to Verification by Physical Instructor]
            </div>
          </div>
        </div>
      </div>

      <div class="col-lg-4">
        <div class="card h-100 border-0 shadow-sm rounded-4 overflow-hidden">
          <img src="../assets/img/exhibitions/science-exhibition-models.svg" class="card-img-top" style="height:220px; object-fit:cover;" alt="Science Honors">
          <div class="card-body p-4">
            <span class="badge bg-primary-subtle text-primary px-3 py-1 rounded-pill mb-2 font-monospace">Innovation &amp; Science</span>
            <h4 style="font-size:1.25rem; font-weight:700; color:var(--heading);">District Science Exhibition Prototypes</h4>
            <p style="font-size:0.9rem; color:var(--body-text);">Student-crafted working models demonstrating sustainable rural irrigation, solar pumping, and organic waste management.</p>
            <div class="official-placeholder-badge mt-2">
              <i class="bi bi-info-circle"></i> [Exhibition Portfolio Pending Verification]
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Activity Gateway Buttons -->
    <div class="p-4 bg-light rounded-4 border text-center reveal-on-scroll">
      <h3 style="font-size:1.5rem; font-weight:800; color:var(--deep-forest-green); margin-bottom:1rem;">
        Explore Individual Activity Domains
      </h3>
      <div class="d-flex flex-wrap justify-content-center gap-2">
        <a href="cultural-activities.html" class="btn btn-outline-success rounded-pill px-3 py-2">Cultural Activities</a>
        <a href="sports-activities.html" class="btn btn-outline-success rounded-pill px-3 py-2">Sports Activities</a>
        <a href="exhibitions.html" class="btn btn-outline-success rounded-pill px-3 py-2">Science Exhibitions</a>
        <a href="skills-competition.html" class="btn btn-outline-success rounded-pill px-3 py-2">Skills Competition</a>
        <a href="vocational-activities.html" class="btn btn-outline-success rounded-pill px-3 py-2">Vocational Activities</a>
      </div>
    </div>
  </div>
</section>
"""

save_page("achievements.html", get_page_template(
    "Achievements", 
    "School Honors", 
    "Comprehensive record of school achievements, cultural participation, athletic distinctions, and academic recognition of +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय.",
    "achievements",
    "<li><a href='achievements.html'>Achievements</a></li>",
    achievements_content
))

# ==============================================================================
# 10. CULTURAL ACTIVITIES (pages/cultural-activities.html)
# ==============================================================================
cultural_content = """
<section class="py-5 bg-white">
  <div class="container">
    <div class="row align-items-center g-5 mb-5 reveal-on-scroll">
      <div class="col-lg-6">
        <span class="section-label-green">HERITAGE &amp; PERFORMING ARTS</span>
        <h2 class="editorial-headline">Expressing Culture, Harmony &amp; Creative Energy</h2>
        <p class="editorial-lead-text">
          Cultural activities are woven into the vibrant life of +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय. Our campus celebrates the rich cultural diversity of Jharkhand, fostering appreciation for indigenous tribal arts, classical Indian traditions, literature, and patriotic expression.
        </p>
        <p style="color:var(--body-text); line-height:1.75;">
          Throughout the academic year, students take stage during National Days, the Annual Cultural Day, Saraswati Puja, and youth festivals. Under the guidance of our cultural committee, learners cultivate vocal music, theatre, drama, and regional folk dances.
        </p>
      </div>
      <div class="col-lg-6">
        <div class="editorial-image-frame">
          <img src="../assets/img/cultural/cultural-annual-day.svg" alt="Cultural Annual Day Presentation">
        </div>
      </div>
    </div>

    <!-- Annual Cultural Events Roster -->
    <div class="row g-4 mb-5 reveal-on-scroll">
      <div class="col-md-6">
        <div class="p-4 p-lg-5 bg-light rounded-4 border h-100">
          <span class="badge bg-warning text-dark px-3 py-1 rounded-pill mb-2 fw-bold">PATRIOTIC CELEBRATIONS</span>
          <h3 style="font-size:1.5rem; font-weight:800; color:var(--deep-forest-green); margin-bottom:1rem;">
            Independence Day &amp; Republic Day Parades
          </h3>
          <p style="color:var(--body-text); line-height:1.7;">
            The entire school community gathers for ceremonial flag hoisting, guard of honor by the Scout &amp; Guide troop, patriotic poetry recitation, and patriotic songs fostering national pride.
          </p>
        </div>
      </div>

      <div class="col-md-6">
        <div class="p-4 p-lg-5 bg-light rounded-4 border h-100">
          <span class="badge bg-success-subtle text-success px-3 py-1 rounded-pill mb-2 font-monospace">REGIONAL TRADITION</span>
          <h3 style="font-size:1.5rem; font-weight:800; color:var(--deep-forest-green); margin-bottom:1rem;">
            Jharkhand Folk Dance &amp; Heritage Showcase
          </h3>
          <p style="color:var(--body-text); line-height:1.7;">
            Students perform traditional regional dances accompanied by Mandar and Dhol drums, celebrating indigenous harvest fests, Karma, Sarhul, and regional unity.
          </p>
        </div>
      </div>

      <div class="col-md-6">
        <div class="p-4 p-lg-5 bg-light rounded-4 border h-100">
          <span class="badge bg-primary-subtle text-primary px-3 py-1 rounded-pill mb-2 font-monospace">DIVINE KNOWLEDGE</span>
          <h3 style="font-size:1.5rem; font-weight:800; color:var(--deep-forest-green); margin-bottom:1rem;">
            Saraswati Puja &amp; Vasant Panchami
          </h3>
          <p style="color:var(--body-text); line-height:1.7;">
            Annual prayer to Goddess Saraswati, symbol of wisdom and fine arts. Students create artistic rangoli, perform devotional stutis, and distribute prasad in harmony.
          </p>
        </div>
      </div>

      <div class="col-md-6">
        <div class="p-4 p-lg-5 bg-light rounded-4 border h-100">
          <span class="badge bg-info-subtle text-dark px-3 py-1 rounded-pill mb-2 font-monospace">DRAMA &amp; SPEECH</span>
          <h3 style="font-size:1.5rem; font-weight:800; color:var(--deep-forest-green); margin-bottom:1rem;">
            Annual Theatrical &amp; Elocution Festival
          </h3>
          <p style="color:var(--body-text); line-height:1.7;">
            One-act plays addressing social themes such as child rights, environmental conservation, literacy, and gender equality, promoting public speaking poise.
          </p>
        </div>
      </div>
    </div>
  </div>
</section>
"""

save_page("cultural-activities.html", get_page_template(
    "Cultural Activities", 
    "Performing Arts", 
    "Vibrant cultural festivals, folk dances of Jharkhand, annual days, and theatrical arts at +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय.",
    "achievements",
    "<li><a href='achievements.html'>Achievements</a></li>",
    cultural_content
))

print("Batch 2 generated successfully!")
