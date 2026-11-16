import os
from generate_pages_batch1 import get_page_template, save_page

# ==============================================================================
# 16. ADMISSION (pages/admission.html)
# ==============================================================================
admission_content = """
<section class="py-5 bg-white">
  <div class="container">
    <div class="text-center max-w-700 mx-auto mb-5 reveal-on-scroll">
      <span class="section-label-green">ENROLLMENT &amp; GUIDANCE</span>
      <h2 class="editorial-headline">Admission Process &amp; Guidelines</h2>
      <p class="text-muted">
        Information on admissions for Secondary (Classes 9 &amp; 10) and Higher Secondary (+2 Science, Arts, and Commerce) streams at +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय.
      </p>
    </div>

    <!-- Official Policy Note -->
    <div class="official-notice-box mb-5 reveal-on-scroll">
      <i class="bi bi-info-circle-fill me-2"></i>
      <strong>State Government Admission Guidelines:</strong> Admissions are conducted in accordance with the annual notifications and reservation policies mandated by the Department of School Education and Literacy, Government of Jharkhand.
    </div>

    <!-- Step by Step Process -->
    <div class="row g-4 mb-5 reveal-on-scroll">
      <div class="col-md-3">
        <div class="p-4 bg-light rounded-4 border h-100 text-center">
          <div class="contact-icon-bubble mx-auto mb-3" style="width:50px; height:50px; font-size:1.25rem;">
            1
          </div>
          <h4 style="font-size:1.15rem; font-weight:700; color:var(--heading);">Notification Release</h4>
          <p style="font-size:0.85rem; color:var(--body-text); margin-bottom:0;">
            Annual notification published on school notice board following declaration of JAC Board results.
          </p>
        </div>
      </div>

      <div class="col-md-3">
        <div class="p-4 bg-light rounded-4 border h-100 text-center">
          <div class="contact-icon-bubble mx-auto mb-3" style="width:50px; height:50px; font-size:1.25rem;">
            2
          </div>
          <h4 style="font-size:1.15rem; font-weight:700; color:var(--heading);">Form Submission</h4>
          <p style="font-size:0.85rem; color:var(--body-text); margin-bottom:0;">
            Collection and submission of completed application forms along with required academic credentials.
          </p>
        </div>
      </div>

      <div class="col-md-3">
        <div class="p-4 bg-light rounded-4 border h-100 text-center">
          <div class="contact-icon-bubble mx-auto mb-3" style="width:50px; height:50px; font-size:1.25rem;">
            3
          </div>
          <h4 style="font-size:1.15rem; font-weight:700; color:var(--heading);">Document Verification</h4>
          <p style="font-size:0.85rem; color:var(--body-text); margin-bottom:0;">
            Scrutiny of original transfer certificates (SLC/CLC), marks-sheets, and category certificates by the committee.
          </p>
        </div>
      </div>

      <div class="col-md-3">
        <div class="p-4 bg-light rounded-4 border h-100 text-center">
          <div class="contact-icon-bubble mx-auto mb-3" style="width:50px; height:50px; font-size:1.25rem;">
            4
          </div>
          <h4 style="font-size:1.15rem; font-weight:700; color:var(--heading);">Enrollment &amp; Roll Allotment</h4>
          <p style="font-size:0.85rem; color:var(--body-text); margin-bottom:0;">
            Final admission approval, section allocation, issue of student ID, and orientation program.
          </p>
        </div>
      </div>
    </div>

    <!-- Required Documents Checklist -->
    <div class="p-4 p-lg-5 bg-light rounded-4 border mb-5 reveal-on-scroll">
      <div class="row g-4 align-items-center">
        <div class="col-lg-6">
          <span class="badge bg-success-subtle text-success px-3 py-1 rounded-pill mb-2 font-monospace">CHECKLIST</span>
          <h3 style="font-size:1.85rem; font-weight:800; color:var(--deep-forest-green); margin-bottom:1rem;">
            Mandatory Documents Required
          </h3>
          <p style="color:var(--body-text); line-height:1.7;">
            Applicants seeking admission to Class 9 or +2 (Class 11) must submit self-attested photocopies along with original documents for in-person verification:
          </p>
          <ul class="list-unstyled d-flex flex-column gap-2 mb-0" style="font-size:0.9rem; color:var(--body-text);">
            <li><i class="bi bi-check-circle-fill text-success me-2"></i> Original School Leaving Certificate (SLC) / College Leaving Certificate (CLC).</li>
            <li><i class="bi bi-check-circle-fill text-success me-2"></i> Mark-sheet of Previous Qualifying Examination (Class 8 / Class 10 Board).</li>
            <li><i class="bi bi-check-circle-fill text-success me-2"></i> Character Certificate from the Head of the previous institution.</li>
            <li><i class="bi bi-check-circle-fill text-success me-2"></i> Copy of Aadhaar Card of student and parent.</li>
            <li><i class="bi bi-check-circle-fill text-success me-2"></i> Caste &amp; Residential Certificate (if applicable for reservation benefits).</li>
            <li><i class="bi bi-check-circle-fill text-success me-2"></i> Recent passport-sized color photographs (4 copies).</li>
          </ul>
        </div>
        <div class="col-lg-6">
          <div class="p-4 bg-white rounded-4 shadow-sm border">
            <h4 style="font-size:1.2rem; font-weight:700; color:var(--deep-forest-green); margin-bottom:0.75rem;">
              Fee Structure Policy
            </h4>
            <p style="font-size:0.875rem; color:var(--body-text); line-height:1.65;">
              As a government-managed institution, tuition and development fees are highly subsidized in strict accordance with the fee regulations of the Department of School Education and Literacy, Government of Jharkhand.
            </p>
            <div class="official-placeholder-badge">
              <i class="bi bi-wallet2"></i> [Fee Structure Subject to Official State Government Notification]
            </div>
            <div class="mt-3 pt-3 border-top">
              <small class="text-muted">Exemptions and government scholarship benefits apply to eligible reserved categories, SC/ST, and girl students under state welfare schemes.</small>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Admission FAQs Accordion -->
    <div class="reveal-on-scroll">
      <div class="text-center max-w-700 mx-auto mb-4">
        <span class="section-label-green">FREQUENTLY ASKED QUESTIONS</span>
        <h3 style="font-size:1.75rem; font-weight:800; color:var(--heading);">Admission Inquiries</h3>
      </div>

      <div class="accordion custom-faq-accordion" id="admissionFaq">
        <div class="card border mb-3 rounded-3 overflow-hidden">
          <button class="faq-trigger-btn w-100 text-start p-3 bg-white border-0 d-flex justify-content-between align-items-center" data-target="faq1">
            <span class="fw-bold text-dark">When do admissions for Class 11 (+2) begin each year?</span>
            <i class="bi bi-chevron-down text-success"></i>
          </button>
          <div id="faq1" class="faq-collapse-body collapse show p-3 bg-light border-top">
            <p class="mb-0 text-muted" style="font-size:0.9rem;">
              Admissions for +2 Science, Arts, and Commerce streams typically open immediately following the announcement of JAC Matriculation (Class 10) results, usually between May and June.
            </p>
          </div>
        </div>

        <div class="card border mb-3 rounded-3 overflow-hidden">
          <button class="faq-trigger-btn w-100 text-start p-3 bg-white border-0 d-flex justify-content-between align-items-center" data-target="faq2">
            <span class="fw-bold text-dark">Can students from other boards (CBSE / ICSE) take admission in +2?</span>
            <i class="bi bi-chevron-down text-success"></i>
          </button>
          <div id="faq2" class="faq-collapse-body collapse p-3 bg-light border-top">
            <p class="mb-0 text-muted" style="font-size:0.9rem;">
              Yes, students passing from recognized central and state boards (such as CBSE or CISCE) are eligible for admission in +2 Higher Secondary upon submitting their migration certificate and qualifying marks-sheet.
            </p>
          </div>
        </div>

        <div class="card border mb-3 rounded-3 overflow-hidden">
          <button class="faq-trigger-btn w-100 text-start p-3 bg-white border-0 d-flex justify-content-between align-items-center" data-target="faq3">
            <span class="fw-bold text-dark">Are hostel facilities available on campus?</span>
            <i class="bi bi-chevron-down text-success"></i>
          </button>
          <div id="faq3" class="faq-collapse-body collapse p-3 bg-light border-top">
            <p class="mb-0 text-muted" style="font-size:0.9rem;">
              Currently, +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय operates as a day school. Students commute from Haldipokhar and surrounding villages of Potka block.
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
"""

save_page("admission.html", get_page_template(
    "Admission Information", 
    "Enrollment Desk", 
    "Step-by-step admission process, required documents checklist, stream eligibility, and FAQs for +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय.",
    "admission",
    "<li><a href='admission.html'>Admission</a></li>",
    admission_content
))

# ==============================================================================
# 17. SCOUT & GUIDE (pages/scout-guide.html)
# ==============================================================================
scout_content = """
<section class="py-5 bg-white">
  <div class="container">
    <div class="row align-items-center g-5 mb-5 reveal-on-scroll">
      <div class="col-lg-6">
        <span class="section-label-green">BHARAT SCOUTS &amp; GUIDES</span>
        <h2 class="editorial-headline">Character Building, Discipline &amp; Community Service</h2>
        <p class="editorial-lead-text">
          The Bharat Scouts &amp; Guides wing at +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय instills lifelong values of leadership, selfless community service, outdoor resilience, and moral discipline among our youth.
        </p>
        <p style="color:var(--body-text); line-height:1.75;">
          Under trained Scout Masters and Guide Captains, our troop actively participates in annual camping exercises, pioneering knots, first-aid drills, emergency disaster mitigation, and ceremonial guard-of-honor during National Days. Scouting shapes responsible, patriotic, and self-reliant youth who live by the motto: "Be Prepared".
        </p>
      </div>
      <div class="col-lg-6">
        <div class="editorial-image-frame">
          <img src="../assets/img/gallery/gallery-scout-1.svg" alt="Bharat Scouts and Guides Training">
        </div>
      </div>
    </div>

    <!-- Core Scouting Tenets -->
    <div class="row g-4 mb-5 reveal-on-scroll">
      <div class="col-md-3">
        <div class="p-4 bg-light rounded-4 border h-100 text-center">
          <div class="contact-icon-bubble mx-auto mb-3" style="width:55px; height:55px; font-size:1.4rem;">
            <i class="bi bi-compass-fill"></i>
          </div>
          <h4 style="font-size:1.15rem; font-weight:700; color:var(--heading);">Pioneering &amp; Survival</h4>
          <p style="font-size:0.85rem; color:var(--body-text); margin-bottom:0;">
            Mastery of traditional rope knots, lashing techniques, tent pitching, compass navigation, and wilderness tracking.
          </p>
        </div>
      </div>

      <div class="col-md-3">
        <div class="p-4 bg-light rounded-4 border h-100 text-center">
          <div class="contact-icon-bubble mx-auto mb-3" style="width:55px; height:55px; font-size:1.4rem;">
            <i class="bi bi-bandaid-fill"></i>
          </div>
          <h4 style="font-size:1.15rem; font-weight:700; color:var(--heading);">First Aid &amp; Safety</h4>
          <p style="font-size:0.85rem; color:var(--body-text); margin-bottom:0;">
            Essential emergency bandaging, stretcher improvisation, rescue procedures, and community disaster response.
          </p>
        </div>
      </div>

      <div class="col-md-3">
        <div class="p-4 bg-light rounded-4 border h-100 text-center">
          <div class="contact-icon-bubble mx-auto mb-3" style="width:55px; height:55px; font-size:1.4rem;">
            <i class="bi bi-people-fill"></i>
          </div>
          <h4 style="font-size:1.15rem; font-weight:700; color:var(--heading);">Civic &amp; Social Service</h4>
          <p style="font-size:0.85rem; color:var(--body-text); margin-bottom:0;">
            Traffic order management during campus celebrations, tree planting, clean water awareness, and blood donation camps.
          </p>
        </div>
      </div>

      <div class="col-md-3">
        <div class="p-4 bg-light rounded-4 border h-100 text-center">
          <div class="contact-icon-bubble mx-auto mb-3" style="width:55px; height:55px; font-size:1.4rem;">
            <i class="bi bi-award-fill"></i>
          </div>
          <h4 style="font-size:1.15rem; font-weight:700; color:var(--heading);">Badge Progression</h4>
          <p style="font-size:0.85rem; color:var(--body-text); margin-bottom:0;">
            Structured advancement from Pravesh and Pratham Sopan through Dwitiya, Tritiya, and Rajya Puraskar levels.
          </p>
        </div>
      </div>
    </div>
  </div>
</section>
"""

save_page("scout-guide.html", get_page_template(
    "Scout & Guide Wing", 
    "Youth Leadership", 
    "Bharat Scouts & Guides troop, leadership training, campcraft, first aid, and community service at +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय.",
    "scout",
    "<li><a href='scout-guide.html'>Scout &amp; Guide</a></li>",
    scout_content
))

# ==============================================================================
# 18. GALLERY (pages/gallery.html)
# ==============================================================================
gallery_content = """
<section class="py-5 bg-white">
  <div class="container">
    <div class="text-center max-w-700 mx-auto mb-5 reveal-on-scroll">
      <span class="section-label-green">PHOTOGRAPHIC CHRONICLES</span>
      <h2 class="editorial-headline">Campus Visual Gallery</h2>
      <p class="text-muted">
        Explore a curated photographic showcase of academic spaces, celebrations, sports meets, science fairs, and campus life at +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय.
      </p>

      <!-- Category Filter Pills -->
      <div class="d-flex flex-wrap justify-content-center gap-2 mt-4">
        <button class="btn btn-sm btn-outline-success rounded-pill px-3 py-2 gallery-filter-btn active" data-filter="all">All Photographs</button>
        <button class="btn btn-sm btn-outline-success rounded-pill px-3 py-2 gallery-filter-btn" data-filter="campus">Campus</button>
        <button class="btn btn-sm btn-outline-success rounded-pill px-3 py-2 gallery-filter-btn" data-filter="classrooms">Classrooms &amp; Labs</button>
        <button class="btn btn-sm btn-outline-success rounded-pill px-3 py-2 gallery-filter-btn" data-filter="students">Students</button>
        <button class="btn btn-sm btn-outline-success rounded-pill px-3 py-2 gallery-filter-btn" data-filter="cultural">Cultural</button>
        <button class="btn btn-sm btn-outline-success rounded-pill px-3 py-2 gallery-filter-btn" data-filter="sports">Sports</button>
        <button class="btn btn-sm btn-outline-success rounded-pill px-3 py-2 gallery-filter-btn" data-filter="exhibitions">Exhibitions</button>
        <button class="btn btn-sm btn-outline-success rounded-pill px-3 py-2 gallery-filter-btn" data-filter="scout">Scout &amp; Guide</button>
      </div>
    </div>

    <!-- Gallery Grid with Lightbox Triggers -->
    <div class="row g-4 reveal-on-scroll">
      <!-- 1 -->
      <div class="col-lg-4 col-md-6 gallery-grid-item" data-category="campus">
        <div class="photo-thumb-card lightbox-trigger" data-src="../assets/img/campus/campus-main-facade.svg" data-title="Main Academic Complex" data-caption="Architectural front entrance of +2 Rajkiyakrit Vidya Niketan Higher Secondary School.">
          <img src="../assets/img/campus/campus-main-facade.svg" alt="Main Academic Complex">
          <div class="photo-thumb-caption">Main Academic Complex</div>
        </div>
      </div>

      <!-- 2 -->
      <div class="col-lg-4 col-md-6 gallery-grid-item" data-category="campus">
        <div class="photo-thumb-card lightbox-trigger" data-src="../assets/img/campus/campus-aerial-view.svg" data-title="Panoramic Campus Landscape" data-caption="Aerial view showing expansive campus grounds and surrounding scenic green hills of Haldipokhar.">
          <img src="../assets/img/campus/campus-aerial-view.svg" alt="Panoramic Campus Landscape">
          <div class="photo-thumb-caption">Panoramic Campus Landscape</div>
        </div>
      </div>

      <!-- 3 -->
      <div class="col-lg-4 col-md-6 gallery-grid-item" data-category="campus">
        <div class="photo-thumb-card lightbox-trigger" data-src="../assets/img/campus/campus-garden-courtyard.svg" data-title="Botanical Courtyard &amp; Eco Park" data-caption="Serene garden courtyards providing students a peaceful environment for study and contemplation.">
          <img src="../assets/img/campus/campus-garden-courtyard.svg" alt="Botanical Courtyard">
          <div class="photo-thumb-caption">Botanical Courtyard &amp; Eco Park</div>
        </div>
      </div>

      <!-- 4 -->
      <div class="col-lg-4 col-md-6 gallery-grid-item" data-category="classrooms">
        <div class="photo-thumb-card lightbox-trigger" data-src="../assets/img/classrooms/smart-classroom.svg" data-title="Smart ICT Digital Classroom" data-caption="Audio-visual interactive screen technology facilitating engaging concept delivery.">
          <img src="../assets/img/classrooms/smart-classroom.svg" alt="Smart Classroom">
          <div class="photo-thumb-caption">Smart ICT Digital Classroom</div>
        </div>
      </div>

      <!-- 5 -->
      <div class="col-lg-4 col-md-6 gallery-grid-item" data-category="classrooms">
        <div class="photo-thumb-card lightbox-trigger" data-src="../assets/img/classrooms/science-laboratory.svg" data-title="Composite Science Laboratory" data-caption="Equipped experimental workstations for physics, chemistry, and biology investigations.">
          <img src="../assets/img/classrooms/science-laboratory.svg" alt="Science Laboratory">
          <div class="photo-thumb-caption">Composite Science Laboratory</div>
        </div>
      </div>

      <!-- 6 -->
      <div class="col-lg-4 col-md-6 gallery-grid-item" data-category="classrooms">
        <div class="photo-thumb-card lightbox-trigger" data-src="../assets/img/classrooms/library-reading.svg" data-title="Institutional Library &amp; Reading Room" data-caption="Vast collection of reference textbooks, literary volumes, and competitive journals.">
          <img src="../assets/img/classrooms/library-reading.svg" alt="Institutional Library">
          <div class="photo-thumb-caption">Institutional Library</div>
        </div>
      </div>

      <!-- 7 -->
      <div class="col-lg-4 col-md-6 gallery-grid-item" data-category="students">
        <div class="photo-thumb-card lightbox-trigger" data-src="../assets/img/students/students-discussion.svg" data-title="Collaborative Study Circles" data-caption="Secondary and higher secondary students solving mathematical problems together.">
          <img src="../assets/img/students/students-discussion.svg" alt="Collaborative Study">
          <div class="photo-thumb-caption">Collaborative Study Circles</div>
        </div>
      </div>

      <!-- 8 -->
      <div class="col-lg-4 col-md-6 gallery-grid-item" data-category="students">
        <div class="photo-thumb-card lightbox-trigger" data-src="../assets/img/students/students-assembly.svg" data-title="Morning Assembly &amp; National Pride" data-caption="Daily prayer, pledge of integrity, and value discourse instilling discipline.">
          <img src="../assets/img/students/students-assembly.svg" alt="Morning Assembly">
          <div class="photo-thumb-caption">Morning Assembly &amp; Discipline</div>
        </div>
      </div>

      <!-- 9 -->
      <div class="col-lg-4 col-md-6 gallery-grid-item" data-category="cultural">
        <div class="photo-thumb-card lightbox-trigger" data-src="../assets/img/cultural/cultural-annual-day.svg" data-title="Annual Cultural Celebrations" data-caption="Music, classical dance, and dramatic performances on the school annual day stage.">
          <img src="../assets/img/cultural/cultural-annual-day.svg" alt="Cultural Celebrations">
          <div class="photo-thumb-caption">Annual Cultural Celebrations</div>
        </div>
      </div>

      <!-- 10 -->
      <div class="col-lg-4 col-md-6 gallery-grid-item" data-category="cultural">
        <div class="photo-thumb-card lightbox-trigger" data-src="../assets/img/cultural/cultural-folk-dance.svg" data-title="Jharkhand Folk Dance Heritage" data-caption="Students celebrating indigenous tribal art, music, and traditions of Jharkhand.">
          <img src="../assets/img/cultural/cultural-folk-dance.svg" alt="Folk Dance Heritage">
          <div class="photo-thumb-caption">Jharkhand Folk Dance</div>
        </div>
      </div>

      <!-- 11 -->
      <div class="col-lg-4 col-md-6 gallery-grid-item" data-category="sports">
        <div class="photo-thumb-card lightbox-trigger" data-src="../assets/img/sports/sports-track-field.svg" data-title="Annual Athletics Meet 100m Sprint" data-caption="Student sprinters competing on the running track during the Annual Sports Meet.">
          <img src="../assets/img/sports/sports-track-field.svg" alt="Athletic Track Race">
          <div class="photo-thumb-caption">Annual Athletics Sprint</div>
        </div>
      </div>

      <!-- 12 -->
      <div class="col-lg-4 col-md-6 gallery-grid-item" data-category="sports">
        <div class="photo-thumb-card lightbox-trigger" data-src="../assets/img/sports/sports-football-ground.svg" data-title="School Football &amp; Team Sports Arena" data-caption="Regular outdoor training on the school sports field promoting physical fitness.">
          <img src="../assets/img/sports/sports-football-ground.svg" alt="Football Sports Ground">
          <div class="photo-thumb-caption">Football &amp; Sports Arena</div>
        </div>
      </div>

      <!-- 13 -->
      <div class="col-lg-4 col-md-6 gallery-grid-item" data-category="exhibitions">
        <div class="photo-thumb-card lightbox-trigger" data-src="../assets/img/exhibitions/science-exhibition-models.svg" data-title="Annual Science &amp; Innovation Fair" data-caption="Working student models in renewable energy, solar pumps, and hydraulics.">
          <img src="../assets/img/exhibitions/science-exhibition-models.svg" alt="Science Innovation Fair">
          <div class="photo-thumb-caption">Science &amp; Innovation Fair</div>
        </div>
      </div>

      <!-- 14 -->
      <div class="col-lg-4 col-md-6 gallery-grid-item" data-category="exhibitions">
        <div class="photo-thumb-card lightbox-trigger" data-src="../assets/img/exhibitions/skills-workshop.svg" data-title="Vocational Skills &amp; Applied Crafts" data-caption="Hands-on technical craft workshops developing applied life competencies.">
          <img src="../assets/img/exhibitions/skills-workshop.svg" alt="Vocational Crafts">
          <div class="photo-thumb-caption">Vocational Skills Workshop</div>
        </div>
      </div>

      <!-- 15 -->
      <div class="col-lg-4 col-md-6 gallery-grid-item" data-category="scout">
        <div class="photo-thumb-card lightbox-trigger" data-src="../assets/img/gallery/gallery-scout-1.svg" data-title="Bharat Scouts &amp; Guides Camp Training" data-caption="Outdoor campcraft, pioneering knots, tent pitching, and survival drills.">
          <img src="../assets/img/gallery/gallery-scout-1.svg" alt="Scout Campcraft">
          <div class="photo-thumb-caption">Bharat Scouts &amp; Guides Camp</div>
        </div>
      </div>
    </div>
  </div>
</section>
"""

save_page("gallery.html", get_page_template(
    "Campus Gallery", 
    "Visual Chronicles", 
    "High-resolution photographic gallery of campus buildings, classrooms, laboratory setups, sports tournaments, and cultural events at +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय.",
    "gallery",
    "<li><a href='gallery.html'>Gallery</a></li>",
    gallery_content
))

# ==============================================================================
# 19. CONTACT US (pages/contact.html)
# ==============================================================================
contact_content = """
<section class="py-5 bg-white">
  <div class="container">
    <div class="text-center max-w-700 mx-auto mb-5 reveal-on-scroll">
      <span class="section-label-green">GET IN TOUCH</span>
      <h2 class="editorial-headline">Contact School Administration</h2>
      <p class="text-muted">
        Reach out to +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय for admissions guidance, academic inquiries, or administrative assistance.
      </p>
    </div>

    <div class="row g-5">
      <!-- Left Column: Official Contact Details & Map Visual -->
      <div class="col-lg-5 reveal-on-scroll">
        <div class="p-4 p-lg-5 bg-light rounded-4 border h-100">
          <h3 style="font-size:1.6rem; font-weight:800; color:var(--deep-forest-green); margin-bottom:1.5rem;">
            Institutional Headquarters
          </h3>

          <div class="d-flex gap-3 mb-4">
            <div class="info-band-icon" style="background:var(--light-mint); color:var(--primary-green); flex-shrink:0;">
              <i class="bi bi-geo-alt-fill"></i>
            </div>
            <div>
              <div style="font-size:0.8rem; font-weight:700; color:#6B7280; text-transform:uppercase;">Postal Address:</div>
              <div style="font-size:0.95rem; font-weight:600; color:var(--heading);">
                +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय<br>
                हल्दीपोखर, पोटका, पूर्वी सिंहभूम<br>
                झारखण्ड – 831002, भारत
              </div>
            </div>
          </div>

          <div class="d-flex gap-3 mb-4">
            <div class="info-band-icon" style="background:var(--light-mint); color:var(--primary-green); flex-shrink:0;">
              <i class="bi bi-envelope-open-fill"></i>
            </div>
            <div>
              <div style="font-size:0.8rem; font-weight:700; color:#6B7280; text-transform:uppercase;">Official Email:</div>
              <div style="font-size:0.95rem; font-weight:600; color:var(--heading); word-break:break-all;">
                <a href="mailto:vnhs.haldipokhar.e.singhbhum@gmail.com">vnhs.haldipokhar.e.singhbhum@gmail.com</a>
              </div>
            </div>
          </div>

          <div class="d-flex gap-3 mb-4">
            <div class="info-band-icon" style="background:var(--light-mint); color:var(--primary-green); flex-shrink:0;">
              <i class="bi bi-shield-check"></i>
            </div>
            <div>
              <div style="font-size:0.8rem; font-weight:700; color:#6B7280; text-transform:uppercase;">National Institutional ID:</div>
              <div style="font-size:0.95rem; font-weight:600; color:var(--heading);">
                U-DISE Code: <strong>20180231602</strong>
              </div>
            </div>
          </div>

          <div class="d-flex gap-3 mb-4">
            <div class="info-band-icon" style="background:var(--light-mint); color:var(--primary-green); flex-shrink:0;">
              <i class="bi bi-clock-fill"></i>
            </div>
            <div>
              <div style="font-size:0.8rem; font-weight:700; color:#6B7280; text-transform:uppercase;">Administrative Hours:</div>
              <div style="font-size:0.95rem; font-weight:600; color:var(--heading);">
                Monday to Saturday: 09:30 AM – 04:00 PM<br>
                <small class="text-muted">(Closed on Sundays and State Gazetted Holidays)</small>
              </div>
            </div>
          </div>

          <!-- Map Location Visual Placeholder -->
          <div class="mt-4 p-3 bg-white rounded-3 border text-center">
            <div style="font-size:0.85rem; font-weight:700; color:var(--deep-forest-green); margin-bottom:0.35rem;">
              <i class="bi bi-pin-map-fill text-danger me-1"></i> Haldipokhar Campus Coordinates
            </div>
            <p style="font-size:0.8rem; color:#6B7280; margin-bottom:0.75rem;">Potka Block • East Singhbhum • Jharkhand 831002</p>
            <a href="https://maps.google.com" target="_blank" rel="noopener noreferrer" class="btn btn-sm btn-outline-success rounded-pill px-4">
              <i class="bi bi-box-arrow-up-right me-1"></i> Open Google Maps Direction
            </a>
          </div>
        </div>
      </div>

      <!-- Right Column: Validated Interactive Contact Form -->
      <div class="col-lg-7 reveal-on-scroll">
        <div class="p-4 p-lg-5 bg-white rounded-4 border shadow-sm">
          <span class="badge bg-success-subtle text-success px-3 py-1 rounded-pill mb-2 font-monospace">ONLINE INQUIRY</span>
          <h3 style="font-size:1.85rem; font-weight:800; color:var(--deep-forest-green); margin-bottom:1.5rem;">
            Send an Official Message
          </h3>

          <div id="formStatusAlert" class="alert d-none" role="alert"></div>

          <form id="schoolContactForm" novalidate>
            <div class="row g-3">
              <div class="col-md-6">
                <label for="contactName" class="form-label fw-bold" style="font-size:0.9rem;">Full Name <span class="text-danger">*</span></label>
                <input type="text" class="form-control" id="contactName" placeholder="Enter your full name" required>
                <div class="invalid-feedback">Please enter your full name.</div>
              </div>

              <div class="col-md-6">
                <label for="contactEmail" class="form-label fw-bold" style="font-size:0.9rem;">Email Address <span class="text-danger">*</span></label>
                <input type="email" class="form-control" id="contactEmail" placeholder="name@example.com" required>
                <div class="invalid-feedback">Please provide a valid email address.</div>
              </div>

              <div class="col-md-6">
                <label for="contactPhone" class="form-label fw-bold" style="font-size:0.9rem;">Phone / Mobile Number <span class="text-danger">*</span></label>
                <input type="tel" class="form-control" id="contactPhone" placeholder="10-digit mobile number" required>
                <div class="invalid-feedback">Please enter your contact number.</div>
              </div>

              <div class="col-md-6">
                <label for="contactSubject" class="form-label fw-bold" style="font-size:0.9rem;">Inquiry Subject <span class="text-danger">*</span></label>
                <select class="form-select" id="contactSubject" required>
                  <option value="">Select subject category...</option>
                  <option value="Admission Inquiry">Admission Inquiry (+2 / Secondary)</option>
                  <option value="Academic Verification">Academic &amp; Results Verification</option>
                  <option value="Transfer Certificate">Transfer Certificate (SLC / CLC)</option>
                  <option value="SMC / Community Matters">SMC &amp; Community Matters</option>
                  <option value="General Information">General Institutional Information</option>
                </select>
                <div class="invalid-feedback">Please select an inquiry category.</div>
              </div>

              <div class="col-12">
                <label for="contactMessage" class="form-label fw-bold" style="font-size:0.9rem;">Your Detailed Message <span class="text-danger">*</span></label>
                <textarea class="form-control" id="contactMessage" rows="5" placeholder="Please write your query clearly here..." required></textarea>
                <div class="invalid-feedback">Please write your message.</div>
              </div>

              <div class="col-12 mt-4">
                <button type="submit" class="btn-cinematic-primary w-100 justify-content-center">
                  <i class="bi bi-send-fill"></i> Submit Official Inquiry
                </button>
              </div>
            </div>
          </form>

          <div class="mt-4 pt-3 border-top text-center text-muted" style="font-size:0.8rem;">
            <i class="bi bi-shield-lock-fill me-1"></i> Your details are confidential and used solely for academic correspondence by school authorities.
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
"""

save_page("contact.html", get_page_template(
    "Contact Us", 
    "Inquiries & Location", 
    "Official contact information, location map, office hours, and inquiry form for +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय, Haldipokhar.",
    "contact",
    "<li><a href='contact.html'>Contact Us</a></li>",
    contact_content
))

print("Batch 4 generated successfully!")
