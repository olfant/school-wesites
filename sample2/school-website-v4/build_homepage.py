import os

output_path = r"c:\Users\ACER\OneDrive\Desktop\school\school-website-v4\index.html"

index_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>+2 राजकीयकृत विद्या निकेतन उच्च विद्यालय | Haldipokhar, East Singhbhum | Jharkhand</title>
  <meta name="description" content="Official website of +2 Rajkiyakrit Vidya Niketan Higher Secondary School, Haldipokhar, Potka, East Singhbhum, Jharkhand. Discover our cinematic campus, academic excellence, values and holistic student development.">
  <link rel="icon" type="image/svg+xml" href="assets/img/logo/school-logo.svg">

  <!-- Bootstrap 5 CSS & Icons CDN -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" rel="stylesheet">

  <!-- Custom Cinematic Green Theme Stylesheets -->
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="stylesheet" href="assets/css/responsive.css">
</head>
<body>

  <!-- ====================================================================
       GLOBAL HEADER: TOP INFORMATION STRIP
       ==================================================================== -->
  <header class="site-header">
    <div class="top-info-strip">
      <div class="container d-flex flex-wrap justify-content-between align-items-center">
        <div class="d-flex flex-wrap align-items-center">
          <span class="top-info-item">
            <i class="bi bi-geo-alt-fill"></i> हल्दीपोखर, पोटका, पूर्वी सिंहभूम (झारखण्ड)
          </span>
          <span class="top-info-item">
            <i class="bi bi-envelope-fill"></i>
            <a href="mailto:vnhs.haldipokhar.e.singhbhum@gmail.com">vnhs.haldipokhar.e.singhbhum@gmail.com</a>
          </span>
          <span class="top-info-item">
            <i class="bi bi-upc-scan"></i> U-DISE: <strong>20180231602</strong>
          </span>
        </div>
        <div class="d-flex align-items-center font-controls-box mt-1 mt-md-0">
          <span class="me-2 text-white-50" style="font-size:0.75rem;">Text Size:</span>
          <button class="font-resizer-btn" data-size="sm" title="Smaller Font">A-</button>
          <button class="font-resizer-btn active" data-size="md" title="Default Font">A</button>
          <button class="font-resizer-btn" data-size="lg" title="Larger Font">A+</button>
        </div>
      </div>
    </div>

    <!-- ====================================================================
         BRANDING HEADER AREA
         ==================================================================== -->
    <div class="branding-header">
      <div class="container d-flex flex-wrap justify-content-between align-items-center">
        <div class="branding-logo-box">
          <img src="assets/img/logo/school-logo.svg" alt="School Emblem" class="school-header-logo">
          <div>
            <div class="school-name-hindi">+2 राजकीयकृत विद्या निकेतन उच्च विद्यालय</div>
            <div class="school-name-english">+2 Rajkiyakrit Vidya Niketan Higher Secondary School</div>
            <div class="school-address-subtitle">
              <i class="bi bi-pin-map-fill text-success"></i> हल्दीपोखर, पोटका, पूर्वी सिंहभूम, झारखण्ड – 831002
            </div>
          </div>
        </div>
        <div class="branding-actions-col d-none d-lg-flex align-items-center gap-3">
          <div class="text-end me-2">
            <div style="font-size:0.75rem; color:#6B7280; text-transform:uppercase; font-weight:700;">Affiliation &amp; Code</div>
            <div style="font-weight:700; color:var(--deep-forest-green); font-size:0.9rem;">JAC, Ranchi • +2 Level</div>
          </div>
          <a href="pages/admission.html" class="branding-action-btn">
            <i class="bi bi-file-earmark-text-fill"></i> Admission Information
          </a>
        </div>
        <!-- Mobile Drawer Hamburger Toggle Button -->
        <button class="mobile-drawer-toggle d-lg-none" type="button" aria-label="Toggle Navigation Menu">
          <i class="bi bi-list text-dark"></i>
        </button>
      </div>
    </div>

    <!-- ====================================================================
         DEEP GREEN MAIN NAVIGATION BAR (STICKY)
         ==================================================================== -->
    <nav class="main-nav-bar navbar navbar-expand-lg" aria-label="Main Navigation">
      <div class="container">
        <div class="collapse navbar-collapse" id="desktopNavbarNav">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link active" href="index.html"><i class="bi bi-house-door-fill me-1"></i> Home</a>
            </li>

            <!-- About Us Dropdown -->
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                About Us
              </a>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="pages/about-school.html"><i class="bi bi-building me-2"></i> About School</a></li>
                <li><a class="dropdown-item" href="pages/principal.html"><i class="bi bi-person-badge me-2"></i> Principal's Desk</a></li>
                <li><a class="dropdown-item" href="pages/mission-vision.html"><i class="bi bi-compass me-2"></i> Mission &amp; Vision</a></li>
                <li><a class="dropdown-item" href="pages/smc-members.html"><i class="bi bi-people me-2"></i> SMC Members</a></li>
              </ul>
            </li>

            <!-- Academic Dropdown -->
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Academic
              </a>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="pages/academic-overview.html"><i class="bi bi-journal-bookmark me-2"></i> Academic Overview</a></li>
                <li><a class="dropdown-item" href="pages/classes-subjects.html"><i class="bi bi-collection me-2"></i> Classes &amp; Subjects</a></li>
                <li><a class="dropdown-item" href="pages/academic-calendar.html"><i class="bi bi-calendar-event me-2"></i> Academic Calendar</a></li>
                <li><a class="dropdown-item" href="pages/teaching-learning.html"><i class="bi bi-easel me-2"></i> Teaching &amp; Learning</a></li>
              </ul>
            </li>

            <!-- Examination Dropdown -->
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Examination
              </a>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="pages/results.html"><i class="bi bi-award me-2"></i> Examination Results</a></li>
              </ul>
            </li>

            <!-- Achievements Dropdown -->
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Achievements
              </a>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="pages/achievements.html"><i class="bi bi-trophy me-2"></i> Overview Achievements</a></li>
                <li><a class="dropdown-item" href="pages/cultural-activities.html"><i class="bi bi-palette me-2"></i> Cultural Activities</a></li>
                <li><a class="dropdown-item" href="pages/sports-activities.html"><i class="bi bi-dribbble me-2"></i> Sports Activities</a></li>
                <li><a class="dropdown-item" href="pages/exhibitions.html"><i class="bi bi-lightbulb me-2"></i> Science &amp; Exhibitions</a></li>
                <li><a class="dropdown-item" href="pages/skills-competition.html"><i class="bi bi-stars me-2"></i> Skills Competition</a></li>
                <li><a class="dropdown-item" href="pages/vocational-activities.html"><i class="bi bi-tools me-2"></i> Vocational Activities</a></li>
              </ul>
            </li>

            <li class="nav-item">
              <a class="nav-link" href="pages/admission.html">Admission</a>
            </li>

            <li class="nav-item">
              <a class="nav-link" href="pages/scout-guide.html">Scout &amp; Guide</a>
            </li>

            <li class="nav-item">
              <a class="nav-link" href="pages/gallery.html">Gallery</a>
            </li>

            <li class="nav-item">
              <a class="nav-link" href="pages/contact.html">Contact Us</a>
            </li>
          </ul>

          <div class="d-flex align-items-center">
            <a href="pages/contact.html" class="btn btn-sm btn-outline-light rounded-pill px-3 py-1" style="font-size:0.8rem; font-weight:600;">
              <i class="bi bi-telephone-fill me-1"></i> Helpline
            </a>
          </div>
        </div>
      </div>
    </nav>

    <!-- Mobile Slide-In Navigation Drawer -->
    <div class="mobile-drawer-backdrop"></div>
    <div class="mobile-drawer">
      <div class="d-flex justify-content-between align-items-center pb-3 border-bottom border-light border-opacity-25 mb-3">
        <div class="d-flex align-items-center gap-2">
          <img src="assets/img/logo/school-logo.svg" alt="Emblem" style="width:36px; height:36px;">
          <span style="font-weight:700; font-size:0.9rem; color:var(--gold-light);">VNHS Haldipokhar</span>
        </div>
        <button class="mobile-drawer-close" aria-label="Close Navigation Drawer">&times;</button>
      </div>

      <div class="mobile-nav-links">
        <a class="nav-link active" href="index.html">Home</a>

        <div>
          <div class="nav-link text-white-50" style="cursor:default; font-size:0.8rem; text-transform:uppercase; letter-spacing:0.05em; margin-top:0.5rem;">About Us</div>
          <div class="mobile-sub-menu">
            <a href="pages/about-school.html"><i class="bi bi-chevron-right me-1"></i> About School</a>
            <a href="pages/principal.html"><i class="bi bi-chevron-right me-1"></i> Principal's Desk</a>
            <a href="pages/mission-vision.html"><i class="bi bi-chevron-right me-1"></i> Mission &amp; Vision</a>
            <a href="pages/smc-members.html"><i class="bi bi-chevron-right me-1"></i> SMC Members</a>
          </div>
        </div>

        <div>
          <div class="nav-link text-white-50" style="cursor:default; font-size:0.8rem; text-transform:uppercase; letter-spacing:0.05em; margin-top:0.5rem;">Academic</div>
          <div class="mobile-sub-menu">
            <a href="pages/academic-overview.html"><i class="bi bi-chevron-right me-1"></i> Academic Overview</a>
            <a href="pages/classes-subjects.html"><i class="bi bi-chevron-right me-1"></i> Classes &amp; Subjects</a>
            <a href="pages/academic-calendar.html"><i class="bi bi-chevron-right me-1"></i> Academic Calendar</a>
            <a href="pages/teaching-learning.html"><i class="bi bi-chevron-right me-1"></i> Teaching &amp; Learning</a>
          </div>
        </div>

        <div>
          <div class="nav-link text-white-50" style="cursor:default; font-size:0.8rem; text-transform:uppercase; letter-spacing:0.05em; margin-top:0.5rem;">Achievements</div>
          <div class="mobile-sub-menu">
            <a href="pages/achievements.html"><i class="bi bi-chevron-right me-1"></i> Achievements Overview</a>
            <a href="pages/cultural-activities.html"><i class="bi bi-chevron-right me-1"></i> Cultural Activities</a>
            <a href="pages/sports-activities.html"><i class="bi bi-chevron-right me-1"></i> Sports Activities</a>
            <a href="pages/exhibitions.html"><i class="bi bi-chevron-right me-1"></i> Science &amp; Exhibitions</a>
            <a href="pages/skills-competition.html"><i class="bi bi-chevron-right me-1"></i> Skills Competition</a>
            <a href="pages/vocational-activities.html"><i class="bi bi-chevron-right me-1"></i> Vocational Activities</a>
          </div>
        </div>

        <a class="nav-link" href="pages/results.html">Examination Results</a>
        <a class="nav-link" href="pages/admission.html">Admission</a>
        <a class="nav-link" href="pages/scout-guide.html">Scout &amp; Guide</a>
        <a class="nav-link" href="pages/gallery.html">Campus Gallery</a>
        <a class="nav-link" href="pages/contact.html">Contact Us</a>
      </div>

      <div class="mt-4 pt-3 border-top border-light border-opacity-10 text-white-50" style="font-size:0.8rem;">
        <div>U-DISE: 20180231602</div>
        <div>Haldipokhar, Potka, East Singhbhum</div>
      </div>
    </div>
  </header>


  <!-- ====================================================================
       SECTION 01 — FULLSCREEN CINEMATIC HERO (~85vh)
       ==================================================================== -->
  <section class="cinematic-hero-section">
    <img src="assets/img/hero/hero-campus-cinematic.svg" alt="Cinematic Campus Background" class="hero-bg-media">
    <div class="hero-overlay-gradient"></div>

    <div class="hero-content-wrapper text-center reveal-on-scroll">
      <div class="hero-badge-pill">
        <i class="bi bi-patch-check-fill text-warning"></i> +2 Higher Secondary Institution • Government Affiliated
      </div>
      <h1 class="hero-main-headline">
        Empowering Minds.<br>Building Futures.
      </h1>
      <div class="hero-subheading">
        Welcome to +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय
      </div>
      <p class="hero-description mx-auto">
        A learning environment focused on quality education, discipline, values and all-round student development situated in the serene rural landscape of Haldipokhar, East Singhbhum.
      </p>
      <div class="hero-cta-group justify-content-center">
        <a href="#school-identity" class="btn-cinematic-primary">
          <i class="bi bi-compass-fill"></i> Discover Our School
        </a>
        <a href="pages/academic-overview.html" class="btn-cinematic-outline">
          <i class="bi bi-book-half"></i> Explore Academics
        </a>
      </div>
    </div>

    <a href="#school-identity" class="hero-scroll-cue" aria-label="Scroll to School Identity Section">
      <span>Scroll Down</span>
      <i class="bi bi-chevron-down"></i>
    </a>
  </section>


  <!-- ====================================================================
       SECTION 02 — SCHOOL IDENTITY (EDITORIAL OVERSIZED)
       ==================================================================== -->
  <section class="school-identity-section" id="school-identity">
    <div class="container">
      <div class="row align-items-center g-5">
        <div class="col-lg-6 reveal-on-scroll">
          <div class="editorial-image-frame">
            <img src="assets/img/students/students-discussion.svg" alt="Students engaged in collaborative learning">
            <div class="editorial-badge-float">
              <div style="font-size:0.75rem; color:var(--gold-light); font-weight:700; text-transform:uppercase; letter-spacing:0.1em;">Institutional Ethos</div>
              <div style="font-size:1.1rem; font-weight:800; color:#FFFFFF;">विद्या ददाति विनयं</div>
              <p style="font-size:0.8rem; color:#E2E8F0; margin-bottom:0;">True knowledge bestows humility, character, and wisdom upon every seeker.</p>
            </div>
          </div>
        </div>

        <div class="col-lg-6 reveal-on-scroll">
          <span class="editorial-number-tag">02 — School Identity</span>
          <h2 class="editorial-headline">
            More Than Education.<br>A Journey of Growth.
          </h2>
          <p class="editorial-lead-text">
            At +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय, Haldipokhar, education transcends conventional textbooks. We foster a supportive, inclusive and intellectually vibrant atmosphere where secondary and higher secondary students cultivate critical curiosity, moral resilience and lifelong competencies.
          </p>

          <div class="editorial-principles-list">
            <div class="principle-item">
              <div class="principle-num">01</div>
              <div>
                <div class="principle-title">Quality Education</div>
                <p class="principle-desc">Structured state board curriculum delivery with focus on conceptual mastery, interactive classroom discussions and analytical thinking.</p>
              </div>
            </div>

            <div class="principle-item">
              <div class="principle-num">02</div>
              <div>
                <div class="principle-title">Good Values</div>
                <p class="principle-desc">Inculcating civic responsibility, ethical conduct, mutual respect, and cultural pride through guided assemblies and mentorship.</p>
              </div>
            </div>

            <div class="principle-item">
              <div class="principle-num">03</div>
              <div>
                <div class="principle-title">Holistic Development</div>
                <p class="principle-desc">Equally balancing athletic training, science exhibitions, scout &amp; guide discipline, vocational skills and creative performing arts.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>


  <!-- ====================================================================
       SECTION 03 — CAMPUS STORY (65% IMAGE COMPOSITION)
       ==================================================================== -->
  <section class="campus-story-section">
    <div class="container">
      <div class="campus-story-grid">
        <div class="campus-large-media reveal-on-scroll">
          <img src="assets/img/campus/campus-main-facade.svg" alt="Campus Academic Complex Facade">
        </div>

        <div class="campus-story-content reveal-on-scroll">
          <span class="section-label-green">OUR SCHOOL</span>
          <h2 class="campus-story-title">An Environment Where Students Learn and Grow.</h2>
          <p style="color:var(--body-text); line-height:1.7;">
            Set amidst the scenic and peaceful rural landscape of Potka block in East Singhbhum, our campus provides a spacious sanctuary for focused study, natural reflection and vibrant peer collaboration.
          </p>

          <div class="campus-quick-meta">
            <div class="meta-row">
              <i class="bi bi-geo-alt-fill"></i>
              <strong>Location:</strong>
              <span>हल्दीपोखर, पोटका, पूर्वी सिंहभूम, झारखण्ड – 831002</span>
            </div>
            <div class="meta-row">
              <i class="bi bi-mortarboard-fill"></i>
              <strong>Education Level:</strong>
              <span>+2 Higher Secondary (Secondary &amp; +2 Wings)</span>
            </div>
            <div class="meta-row">
              <i class="bi bi-shield-check"></i>
              <strong>U-DISE Code:</strong>
              <span>20180231602 (Government Managed)</span>
            </div>
          </div>

          <a href="pages/about-school.html" class="btn btn-outline-success rounded-pill px-4 py-2" style="font-weight:700;">
            Read Complete Campus Story <i class="bi bi-arrow-right ms-1"></i>
          </a>
        </div>
      </div>
    </div>
  </section>


  <!-- ====================================================================
       SECTION 04 — SCHOOL INFORMATION BAR
       ==================================================================== -->
  <section class="school-info-band">
    <div class="container">
      <div class="info-band-grid">
        <div class="info-band-item">
          <div class="info-band-icon"><i class="bi bi-building"></i></div>
          <div>
            <div class="info-band-label">School Name</div>
            <div class="info-band-value">+2 राजकीयकृत विद्या निकेतन</div>
          </div>
        </div>

        <div class="info-band-item">
          <div class="info-band-icon"><i class="bi bi-mortarboard"></i></div>
          <div>
            <div class="info-band-label">Educational Level</div>
            <div class="info-band-value">+2 Higher Secondary</div>
          </div>
        </div>

        <div class="info-band-item">
          <div class="info-band-icon"><i class="bi bi-geo-alt"></i></div>
          <div>
            <div class="info-band-label">Campus Location</div>
            <div class="info-band-value">Haldipokhar, Potka (831002)</div>
          </div>
        </div>

        <div class="info-band-item">
          <div class="info-band-icon"><i class="bi bi-upc"></i></div>
          <div>
            <div class="info-band-label">U-DISE Code</div>
            <div class="info-band-value">20180231602</div>
          </div>
        </div>

        <div class="info-band-item">
          <div class="info-band-icon"><i class="bi bi-envelope"></i></div>
          <div>
            <div class="info-band-label">Official Email</div>
            <div class="info-band-value" style="font-size:0.8rem;">vnhs.haldipokhar.e.singhbhum@gmail.com</div>
          </div>
        </div>
      </div>
    </div>
  </section>


  <!-- ====================================================================
       SECTION 05 — PRINCIPAL'S MESSAGE (FULL-WIDTH GREEN STORYTELLING)
       ==================================================================== -->
  <section class="principal-cinematic-section">
    <div class="container position-relative" style="z-index:2;">
      <div class="row align-items-center g-5">
        <div class="col-lg-5 reveal-on-scroll">
          <div class="principal-portrait-container">
            <img src="assets/img/principal/principal-desk-portrait.svg" alt="Office of the Head of Institution">
          </div>
        </div>

        <div class="col-lg-7 reveal-on-scroll">
          <div class="principal-quote-box">
            <div class="quote-icon-large"><i class="bi bi-quote"></i></div>
            <h2 class="font-serif text-white mb-3" style="font-size:2.2rem; font-weight:700;">
              Guiding Youth Towards Knowledge &amp; Purpose
            </h2>
            <p class="principal-speech-lead">
              "Every young learner walking through our gates carries boundless capability. Our institutional mission is to cultivate not only academic brilliance, but the humility, integrity, and social conscience needed to lead meaningful lives."
            </p>
            <p style="color:#D1E7DD; line-height:1.75; font-size:1rem;">
              At +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय, we believe in democratic and student-centric pedagogy. Through continuous parental cooperation, dedicated faculty guidance and state curriculum enrichment, our students are prepared for higher education and responsible global citizenship.
            </p>

            <div class="principal-signature-block">
              <div>
                <div class="principal-name-tag">[Principal Name - Official Record Pending Verification]</div>
                <div class="principal-title-tag">Principal / In-Charge Headmaster • +2 राजकीयकृत विद्या निकेतन</div>
              </div>
              <a href="pages/principal.html" class="btn btn-sm btn-outline-light rounded-pill px-3 py-2">
                Read Full Message <i class="bi bi-arrow-right ms-1"></i>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>


  <!-- ====================================================================
       SECTION 06 — ACADEMIC EXCELLENCE (ASYMMETRIC EDITORIAL)
       ==================================================================== -->
  <section class="academic-excellence-section">
    <div class="container">
      <div class="text-center max-w-700 mx-auto mb-5 reveal-on-scroll">
        <span class="section-label-green">ACADEMIC FOUNDATION</span>
        <h2 class="editorial-headline">Learning That Creates Opportunities.</h2>
        <p class="text-muted">
          Our curriculum is structured to support sequential conceptual growth from secondary education through higher secondary specialized streams.
        </p>
      </div>

      <div class="asymmetric-academic-grid">
        <div class="academic-panel-featured reveal-on-scroll">
          <div>
            <div class="d-flex align-items-center gap-2 mb-3">
              <span class="stream-pill-badge">+2 Higher Secondary Wing</span>
              <span class="stream-pill-badge">Classes 11 &amp; 12</span>
            </div>
            <h3 style="font-size:1.85rem; font-weight:800; color:var(--deep-forest-green); margin-bottom:1rem;">
              Higher Secondary Stream Specializations
            </h3>
            <p style="color:var(--body-text); line-height:1.75;">
              Under the affiliation of Jharkhand Academic Council (JAC), Ranchi, our +2 division offers dedicated streams in Science, Arts, and Commerce with well-structured elective subject options.
            </p>
            <div class="row g-3 my-2">
              <div class="col-md-4">
                <div class="p-3 bg-white rounded border">
                  <div style="font-weight:700; color:var(--primary-green);"><i class="bi bi-radioactive me-1"></i> Science Stream</div>
                  <div style="font-size:0.8rem; color:#6B7280;">Physics, Chemistry, Math, Biology</div>
                </div>
              </div>
              <div class="col-md-4">
                <div class="p-3 bg-white rounded border">
                  <div style="font-weight:700; color:var(--primary-green);"><i class="bi bi-bank me-1"></i> Arts Stream</div>
                  <div style="font-size:0.8rem; color:#6B7280;">History, Pol Science, Geography, Economics</div>
                </div>
              </div>
              <div class="col-md-4">
                <div class="p-3 bg-white rounded border">
                  <div style="font-weight:700; color:var(--primary-green);"><i class="bi bi-graph-up-arrow me-1"></i> Commerce Stream</div>
                  <div style="font-size:0.8rem; color:#6B7280;">Accountancy, Business Studies, Economics</div>
                </div>
              </div>
            </div>
          </div>
          <div class="pt-4 border-top mt-4 d-flex justify-content-between align-items-center">
            <span style="font-size:0.85rem; color:#6B7280;">Curriculum: JAC Ranchi Board Guidelines</span>
            <a href="pages/classes-subjects.html" class="btn btn-sm btn-success rounded-pill px-3">
              View Detailed Stream Table <i class="bi bi-arrow-right ms-1"></i>
            </a>
          </div>
        </div>

        <div class="academic-panel-sidebar reveal-on-scroll">
          <div class="academic-sub-card">
            <div class="d-flex align-items-center gap-3 mb-2">
              <div class="info-band-icon" style="background:var(--light-mint); color:var(--primary-green);"><i class="bi bi-laptop"></i></div>
              <h4 style="font-size:1.15rem; margin-bottom:0; font-weight:700;">Teaching &amp; Learning Pedagogy</h4>
            </div>
            <p style="font-size:0.875rem; color:var(--body-text); margin-bottom:0.75rem;">
              ICT-aided classrooms, regular formative periodic tests, and experimental discovery across science laboratories.
            </p>
            <a href="pages/teaching-learning.html" style="font-size:0.85rem; font-weight:700;">Learn Methodology &rarr;</a>
          </div>

          <div class="academic-sub-card">
            <div class="d-flex align-items-center gap-3 mb-2">
              <div class="info-band-icon" style="background:var(--light-mint); color:var(--primary-green);"><i class="bi bi-calendar3"></i></div>
              <h4 style="font-size:1.15rem; margin-bottom:0; font-weight:700;">Academic Calendar</h4>
            </div>
            <p style="font-size:0.875rem; color:var(--body-text); margin-bottom:0.75rem;">
              Sequential annual roadmap tracking term assessments, government holidays, institutional milestones, and national days.
            </p>
            <a href="pages/academic-calendar.html" style="font-size:0.85rem; font-weight:700;">Review Calendar &rarr;</a>
          </div>

          <div class="academic-sub-card">
            <div class="d-flex align-items-center gap-3 mb-2">
              <div class="info-band-icon" style="background:var(--light-mint); color:var(--primary-green);"><i class="bi bi-card-checklist"></i></div>
              <h4 style="font-size:1.15rem; margin-bottom:0; font-weight:700;">Secondary Wing (Classes 9 &amp; 10)</h4>
            </div>
            <p style="font-size:0.875rem; color:var(--body-text); margin-bottom:0.75rem;">
              Strong foundational secondary schooling laying comprehensive groundwork in languages, math, sciences, and social sciences.
            </p>
            <a href="pages/classes-subjects.html" style="font-size:0.85rem; font-weight:700;">Explore Class Details &rarr;</a>
          </div>
        </div>
      </div>
    </div>
  </section>


  <!-- ====================================================================
       SECTION 07 — THE CAMPUS EXPERIENCE (IMAGE STORYTELLING)
       ==================================================================== -->
  <section class="campus-experience-section">
    <div class="container">
      <div class="d-flex flex-wrap justify-content-between align-items-end mb-4 reveal-on-scroll">
        <div>
          <span class="section-label-green">CAMPUS LIFE &amp; ACTIVITIES</span>
          <h2 class="editorial-headline text-white mb-0">The Campus Experience</h2>
        </div>
        <div class="text-white-50 mt-2 mt-md-0" style="max-width:400px; font-size:0.925rem;">
          Engaging beyond textbook boundaries with structured co-curricular opportunities that develop teamwork and creative leadership.
        </div>
      </div>

      <div class="experience-grid">
        <!-- 1. Cultural -->
        <div class="experience-card span-6 reveal-on-scroll" onclick="window.location.href='pages/cultural-activities.html'">
          <img src="assets/img/cultural/cultural-annual-day.svg" alt="Cultural Activities" class="experience-card-img">
          <div class="experience-card-overlay">
            <div class="experience-card-tag">Performing Arts</div>
            <h3 class="experience-card-title">Cultural Activities &amp; Heritage</h3>
            <p class="experience-card-desc">Annual cultural festivals, regional folk dance celebrations, patriotic presentations and theatrical arts.</p>
            <span class="experience-card-btn">Explore Cultural Programs <i class="bi bi-arrow-right"></i></span>
          </div>
        </div>

        <!-- 2. Sports -->
        <div class="experience-card span-6 reveal-on-scroll" onclick="window.location.href='pages/sports-activities.html'">
          <img src="assets/img/sports/sports-track-field.svg" alt="Sports Activities" class="experience-card-img">
          <div class="experience-card-overlay">
            <div class="experience-card-tag">Athletic Vitality</div>
            <h3 class="experience-card-title">Sports &amp; Physical Education</h3>
            <p class="experience-card-desc">Annual track and field meets, football, volleyball, yoga practice, and inter-house athletic tournaments.</p>
            <span class="experience-card-btn">Explore Sports Arena <i class="bi bi-arrow-right"></i></span>
          </div>
        </div>

        <!-- 3. Exhibitions -->
        <div class="experience-card span-4 reveal-on-scroll" onclick="window.location.href='pages/exhibitions.html'">
          <img src="assets/img/exhibitions/science-exhibition-models.svg" alt="Science Exhibitions" class="experience-card-img">
          <div class="experience-card-overlay">
            <div class="experience-card-tag">Science &amp; Innovation</div>
            <h3 class="experience-card-title">Science Exhibitions</h3>
            <p class="experience-card-desc">Demonstrating solar energy, environmental science and working models.</p>
            <span class="experience-card-btn">Explore Exhibitions <i class="bi bi-arrow-right"></i></span>
          </div>
        </div>

        <!-- 4. Scout & Guide -->
        <div class="experience-card span-4 reveal-on-scroll" onclick="window.location.href='pages/scout-guide.html'">
          <img src="assets/img/gallery/gallery-scout-1.svg" alt="Scout and Guide" class="experience-card-img">
          <div class="experience-card-overlay">
            <div class="experience-card-tag">Character &amp; Service</div>
            <h3 class="experience-card-title">Scout &amp; Guide Wing</h3>
            <p class="experience-card-desc">Camping discipline, outdoor survival, flag protocol, and civic service.</p>
            <span class="experience-card-btn">Explore Scout Wing <i class="bi bi-arrow-right"></i></span>
          </div>
        </div>

        <!-- 5. Vocational -->
        <div class="experience-card span-4 reveal-on-scroll" onclick="window.location.href='pages/vocational-activities.html'">
          <img src="assets/img/exhibitions/skills-workshop.svg" alt="Vocational Activities" class="experience-card-img">
          <div class="experience-card-overlay">
            <div class="experience-card-tag">Practical Training</div>
            <h3 class="experience-card-title">Vocational Learning</h3>
            <p class="experience-card-desc">Hands-on technical competencies and applied craft skills for life readiness.</p>
            <span class="experience-card-btn">Explore Vocational <i class="bi bi-arrow-right"></i></span>
          </div>
        </div>
      </div>
    </div>
  </section>


  <!-- ====================================================================
       SECTION 08 — OUR EDUCATIONAL VALUES (VERTICAL NUMBERED TIMELINE)
       ==================================================================== -->
  <section class="educational-values-section">
    <div class="container">
      <div class="text-center max-w-700 mx-auto mb-4 reveal-on-scroll">
        <span class="section-label-green">INSTITUTIONAL PILLARS</span>
        <h2 class="editorial-headline">Values That Shape Tomorrow.</h2>
        <p class="text-muted">
          Our core educational values form a continuous continuum that guides every student from classroom enrollment to responsible adulthood.
        </p>
      </div>

      <div class="values-timeline-container">
        <!-- 1. Quality Education -->
        <div class="timeline-row reveal-on-scroll">
          <div class="timeline-marker">1</div>
          <div class="timeline-content-card">
            <h3 class="timeline-title">Quality Education</h3>
            <p class="timeline-desc">Rigorous conceptual clarity, structured curriculum adherence, interactive classroom dialogues, and continuous formative assessment.</p>
          </div>
        </div>

        <!-- 2. Discipline -->
        <div class="timeline-row inverted reveal-on-scroll">
          <div class="timeline-marker">2</div>
          <div class="timeline-content-card">
            <h3 class="timeline-title">Discipline</h3>
            <p class="timeline-desc">Punctuality, respectful interpersonal conduct, neat uniform adherence, and unwavering commitment to institutional decorum.</p>
          </div>
        </div>

        <!-- 3. Creativity -->
        <div class="timeline-row reveal-on-scroll">
          <div class="timeline-marker">3</div>
          <div class="timeline-content-card">
            <h3 class="timeline-title">Creativity</h3>
            <p class="timeline-desc">Encouraging divergent thinking, creative literature writing, theatrical expressions, and innovative scientific problem-solving.</p>
          </div>
        </div>

        <!-- 4. Responsibility -->
        <div class="timeline-row inverted reveal-on-scroll">
          <div class="timeline-marker">4</div>
          <div class="timeline-content-card">
            <h3 class="timeline-title">Responsibility</h3>
            <p class="timeline-desc">Civic consciousness, environmental stewardship, tree plantation drives, and empathy towards the community and society.</p>
          </div>
        </div>

        <!-- 5. Practical Skills -->
        <div class="timeline-row reveal-on-scroll">
          <div class="timeline-marker">5</div>
          <div class="timeline-content-card">
            <h3 class="timeline-title">Practical Skills</h3>
            <p class="timeline-desc">Laboratory experiments, digital literacy, practical arts, vocational workshops, and application of knowledge to real-world tasks.</p>
          </div>
        </div>

        <!-- 6. Student Development -->
        <div class="timeline-row inverted reveal-on-scroll">
          <div class="timeline-marker">6</div>
          <div class="timeline-content-card">
            <h3 class="timeline-title">Student Development</h3>
            <p class="timeline-desc">Cultivating emotional resilience, physical endurance, leadership confidence, and holistic readiness for future aspirations.</p>
          </div>
        </div>
      </div>
    </div>
  </section>


  <!-- ====================================================================
       SECTION 09 — SCHOOL ACHIEVEMENTS (ALTERNATING IMAGE COMPOSITIONS)
       ==================================================================== -->
  <section class="achievements-section">
    <div class="container">
      <div class="text-center max-w-700 mx-auto mb-5 reveal-on-scroll">
        <span class="section-label-green">RECOGNITION &amp; PROGRESS</span>
        <h2 class="editorial-headline">School Achievements &amp; Highlights</h2>
        <p class="text-muted">
          Celebrating student participation, creative endeavors, athletic perseverance, and institutional milestones.
        </p>
      </div>

      <!-- Item 1: Cultural & Folk -->
      <div class="achievement-feature-item reveal-on-scroll">
        <div class="achievement-img-wrap">
          <img src="assets/img/cultural/cultural-folk-dance.svg" alt="Cultural Fest Achievement">
        </div>
        <div>
          <span class="badge bg-success-subtle text-success mb-2 px-3 py-2 rounded-pill font-monospace">Cultural Excellence</span>
          <h3 style="font-size:1.85rem; font-weight:800; color:var(--deep-forest-green); margin-bottom:1rem;">
            Preserving Regional Heritage Through Performing Arts
          </h3>
          <p style="color:var(--body-text); line-height:1.75;">
            Our students take active pride in representing the school in regional youth festivals and patriotic events, presenting tribal dance forms, drama, and classical vocal performances.
          </p>
          <div class="official-placeholder-badge mb-3">
            <i class="bi bi-info-circle-fill"></i> [Achievement Record to be Verified by School Head]
          </div>
          <div>
            <a href="pages/cultural-activities.html" class="btn btn-outline-success rounded-pill px-4">View Cultural Highlights</a>
          </div>
        </div>
      </div>

      <!-- Item 2: Sports & Athletic (Reverse) -->
      <div class="achievement-feature-item reverse reveal-on-scroll">
        <div class="achievement-img-wrap">
          <img src="assets/img/sports/sports-football-ground.svg" alt="Sports Ground Achievement">
        </div>
        <div>
          <span class="badge bg-success-subtle text-success mb-2 px-3 py-2 rounded-pill font-monospace">Athletic Spirit</span>
          <h3 style="font-size:1.85rem; font-weight:800; color:var(--deep-forest-green); margin-bottom:1rem;">
            Inter-House Tournaments &amp; Athletic Conditioning
          </h3>
          <p style="color:var(--body-text); line-height:1.75;">
            From track sprint meets to football and volleyball matches on our school grounds, student athletes cultivate stamina, discipline, and healthy sportsmanship.
          </p>
          <div class="official-placeholder-badge mb-3">
            <i class="bi bi-info-circle-fill"></i> [Sports Roster Subject to Verification by Physical Instructor]
          </div>
          <div>
            <a href="pages/sports-activities.html" class="btn btn-outline-success rounded-pill px-4">View Sports Highlights</a>
          </div>
        </div>
      </div>

      <!-- Item 3: Science & Innovation -->
      <div class="achievement-feature-item reveal-on-scroll">
        <div class="achievement-img-wrap">
          <img src="assets/img/exhibitions/science-exhibition-models.svg" alt="Science Exhibition Showcase">
        </div>
        <div>
          <span class="badge bg-success-subtle text-success mb-2 px-3 py-2 rounded-pill font-monospace">Scientific Innovation</span>
          <h3 style="font-size:1.85rem; font-weight:800; color:var(--deep-forest-green); margin-bottom:1rem;">
            Annual Science Fair &amp; Renewable Energy Prototypes
          </h3>
          <p style="color:var(--body-text); line-height:1.75;">
            Encouraging scientific temperament through working prototypes in solar pumping, rainwater harvesting, hydraulic physics, and sustainable ecological solutions.
          </p>
          <div class="official-placeholder-badge mb-3">
            <i class="bi bi-info-circle-fill"></i> [Exhibition Portfolio Pending Verification]
          </div>
          <div>
            <a href="pages/exhibitions.html" class="btn btn-outline-success rounded-pill px-4">View Exhibitions Showcase</a>
          </div>
        </div>
      </div>
    </div>
  </section>


  <!-- ====================================================================
       SECTION 10 — LATEST NOTICES (ANNOUNCEMENT CENTER)
       ==================================================================== -->
  <section class="notices-section" id="notices">
    <div class="container">
      <div class="notices-header-box reveal-on-scroll">
        <div class="row align-items-center justify-content-between g-3">
          <div class="col-lg-6">
            <span class="badge bg-warning text-dark px-3 py-1 rounded-pill mb-2 fw-bold">Official Bulletin</span>
            <h2 class="text-white mb-1" style="font-size:2rem; font-weight:800;">Notice &amp; Announcement Center</h2>
            <p class="text-white-50 mb-0" style="font-size:0.9rem;">
              Stay updated with the latest circulars, examination advisories, and administrative releases.
            </p>
          </div>
          <div class="col-lg-4 text-lg-end">
            <input type="text" class="notice-search-input" placeholder="Search announcements..." aria-label="Search notices">
          </div>
        </div>

        <div class="notices-filter-bar">
          <button class="notice-filter-btn active" data-category="all">All Notices</button>
          <button class="notice-filter-btn" data-category="academic">Academic</button>
          <button class="notice-filter-btn" data-category="examination">Examination</button>
          <button class="notice-filter-btn" data-category="admission">Admission</button>
          <button class="notice-filter-btn" data-category="cultural">Cultural</button>
          <button class="notice-filter-btn" data-category="sports">Sports</button>
          <button class="notice-filter-btn" data-category="general">General</button>
        </div>
      </div>

      <div class="notice-panels-body reveal-on-scroll">
        <!-- Notice 1 -->
        <div class="notice-row-card" data-category="academic">
          <div class="d-flex align-items-center gap-3">
            <div class="text-center px-3 py-2 bg-light rounded border">
              <div style="font-size:0.75rem; text-transform:uppercase; color:#6B7280; font-weight:700;">Nov</div>
              <div style="font-size:1.35rem; font-weight:800; color:var(--deep-forest-green); line-height:1;">12</div>
            </div>
            <div>
              <span class="notice-badge badge-academic">Academic</span>
              <h4 style="font-size:1.05rem; font-weight:700; color:var(--heading); margin:0.35rem 0 0.2rem;">
                Commencement of Secondary &amp; Higher Secondary Periodic Assessments
              </h4>
              <p style="font-size:0.85rem; color:var(--body-text); margin-bottom:0;">
                Students of Classes 9 to 12 are notified regarding the upcoming periodic unit assessments.
              </p>
            </div>
          </div>
          <span class="badge bg-success-subtle text-success px-3 py-2 rounded-pill font-monospace">Active Notice</span>
        </div>

        <!-- Notice 2 -->
        <div class="notice-row-card" data-category="examination">
          <div class="d-flex align-items-center gap-3">
            <div class="text-center px-3 py-2 bg-light rounded border">
              <div style="font-size:0.75rem; text-transform:uppercase; color:#6B7280; font-weight:700;">Nov</div>
              <div style="font-size:1.35rem; font-weight:800; color:var(--deep-forest-green); line-height:1;">08</div>
            </div>
            <div>
              <span class="notice-badge badge-examination">Examination</span>
              <h4 style="font-size:1.05rem; font-weight:700; color:var(--heading); margin:0.35rem 0 0.2rem;">
                JAC Board Examination Form Filling &amp; Verification Schedule [Sample Notice]
              </h4>
              <p style="font-size:0.85rem; color:var(--body-text); margin-bottom:0;">
                Instructional advisory for Class 10 and 12 candidate registration validation. Official dates subject to JAC notification.
              </p>
            </div>
          </div>
          <span class="official-placeholder-badge">Official Record Pending</span>
        </div>

        <!-- Notice 3 -->
        <div class="notice-row-card" data-category="cultural">
          <div class="d-flex align-items-center gap-3">
            <div class="text-center px-3 py-2 bg-light rounded border">
              <div style="font-size:0.75rem; text-transform:uppercase; color:#6B7280; font-weight:700;">Nov</div>
              <div style="font-size:1.35rem; font-weight:800; color:var(--deep-forest-green); line-height:1;">04</div>
            </div>
            <div>
              <span class="notice-badge badge-cultural">Cultural</span>
              <h4 style="font-size:1.05rem; font-weight:700; color:var(--heading); margin:0.35rem 0 0.2rem;">
                Auditions for Annual Cultural Meet &amp; Folk Arts Showcase
              </h4>
              <p style="font-size:0.85rem; color:var(--body-text); margin-bottom:0;">
                Interested students from all houses may register with their respective mentors for folk dance and music auditions.
              </p>
            </div>
          </div>
          <span class="badge bg-primary-subtle text-primary px-3 py-2 rounded-pill font-monospace">Registration</span>
        </div>

        <!-- Notice 4 -->
        <div class="notice-row-card" data-category="sports">
          <div class="d-flex align-items-center gap-3">
            <div class="text-center px-3 py-2 bg-light rounded border">
              <div style="font-size:0.75rem; text-transform:uppercase; color:#6B7280; font-weight:700;">Oct</div>
              <div style="font-size:1.35rem; font-weight:800; color:var(--deep-forest-green); line-height:1;">28</div>
            </div>
            <div>
              <span class="notice-badge badge-sports">Sports</span>
              <h4 style="font-size:1.05rem; font-weight:700; color:var(--heading); margin:0.35rem 0 0.2rem;">
                Annual Athletic Trials for Track and Field Events
              </h4>
              <p style="font-size:0.85rem; color:var(--body-text); margin-bottom:0;">
                Selection trials for 100m, 200m sprint, long jump, and volleyball will be held on the school playground.
              </p>
            </div>
          </div>
          <span class="badge bg-secondary-subtle text-secondary px-3 py-2 rounded-pill font-monospace">Completed</span>
        </div>
      </div>
    </div>
  </section>


  <!-- ====================================================================
       SECTION 11 — EXAMINATION RESULTS (INSTITUTIONAL ARCHIVE PREVIEW)
       ==================================================================== -->
  <section class="results-section">
    <div class="container">
      <div class="text-center max-w-700 mx-auto mb-4 reveal-on-scroll">
        <span class="section-label-green">ACADEMIC PERFORMANCE</span>
        <h2 class="editorial-headline">Official Examination Results</h2>
        <p class="text-muted">
          Official board examination results are published by Jharkhand Academic Council (JAC), Ranchi. Access archived institutional gazette information.
        </p>
      </div>

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
            <input type="text" class="form-control form-control-sm" id="resultSearchInput" placeholder="Search result records...">
          </div>
        </div>

        <table class="results-table">
          <thead>
            <tr>
              <th>Examination Title</th>
              <th>Academic Session</th>
              <th>Class / Stream</th>
              <th>Status / Gazette</th>
              <th>Administrative Action</th>
            </tr>
          </thead>
          <tbody>
            <tr class="result-data-row" data-session="2024 - 2025" data-class="Class 10">
              <td><strong>JAC Secondary (Class X) Annual Examination</strong></td>
              <td>2024 - 2025</td>
              <td>Class 10 (Secondary)</td>
              <td><span class="badge bg-success-subtle text-success">Gazette Archived</span></td>
              <td>
                <a href="pages/results.html" class="btn btn-sm btn-outline-success">
                  <i class="bi bi-file-earmark-pdf"></i> View Gazette Details
                </a>
              </td>
            </tr>

            <tr class="result-data-row" data-session="2024 - 2025" data-class="Science">
              <td><strong>JAC Higher Secondary (+2) Science Annual Board</strong></td>
              <td>2024 - 2025</td>
              <td>Class 12 (Science Stream)</td>
              <td><span class="badge bg-success-subtle text-success">Gazette Archived</span></td>
              <td>
                <a href="pages/results.html" class="btn btn-sm btn-outline-success">
                  <i class="bi bi-file-earmark-pdf"></i> View Gazette Details
                </a>
              </td>
            </tr>

            <tr class="result-data-row" data-session="2024 - 2025" data-class="Arts">
              <td><strong>JAC Higher Secondary (+2) Arts Annual Board</strong></td>
              <td>2024 - 2025</td>
              <td>Class 12 (Arts Stream)</td>
              <td><span class="badge bg-success-subtle text-success">Gazette Archived</span></td>
              <td>
                <a href="pages/results.html" class="btn btn-sm btn-outline-success">
                  <i class="bi bi-file-earmark-pdf"></i> View Gazette Details
                </a>
              </td>
            </tr>

            <tr class="result-data-row" data-session="2024 - 2025" data-class="Commerce">
              <td><strong>JAC Higher Secondary (+2) Commerce Annual Board</strong></td>
              <td>2024 - 2025</td>
              <td>Class 12 (Commerce Stream)</td>
              <td><span class="badge bg-success-subtle text-success">Gazette Archived</span></td>
              <td>
                <a href="pages/results.html" class="btn btn-sm btn-outline-success">
                  <i class="bi bi-file-earmark-pdf"></i> View Gazette Details
                </a>
              </td>
            </tr>
          </tbody>
        </table>

        <div class="p-3 bg-light border-top text-center">
          <small class="text-muted">
            <i class="bi bi-info-circle me-1"></i> Note: Official marks-sheets and original passing certificates are released via the school administrative desk following formal clearance by the Jharkhand Academic Council, Ranchi.
          </small>
        </div>
      </div>
    </div>
  </section>


  <!-- ====================================================================
       SECTION 12 — CAMPUS PHOTO STORY (CINEMATIC PHOTO GALLERY PREVIEW)
       ==================================================================== -->
  <section class="photo-story-section">
    <div class="container">
      <div class="d-flex flex-wrap justify-content-between align-items-end mb-4 reveal-on-scroll">
        <div>
          <span class="section-label-green">VISUAL CHRONICLES</span>
          <h2 class="editorial-headline text-white mb-0">Campus Photo Story</h2>
        </div>
        <div>
          <a href="pages/gallery.html" class="btn btn-outline-light rounded-pill px-4">
            View Complete Gallery <i class="bi bi-arrow-right ms-1"></i>
          </a>
        </div>
      </div>

      <!-- Hero large photo -->
      <div class="photo-story-hero-wrapper reveal-on-scroll">
        <img src="assets/img/campus/campus-aerial-view.svg" alt="Panoramic Campus View">
      </div>

      <!-- Overlapping 3 photo cards -->
      <div class="photo-overlapping-grid reveal-on-scroll">
        <div class="photo-thumb-card lightbox-trigger" data-src="assets/img/classrooms/science-laboratory.svg" data-title="Composite Science Laboratory" data-caption="Students conducting hands-on chemistry and physics experiments in our equipped laboratory.">
          <img src="assets/img/classrooms/science-laboratory.svg" alt="Science Laboratory">
          <div class="photo-thumb-caption">Science Laboratory</div>
        </div>

        <div class="photo-thumb-card lightbox-trigger" data-src="assets/img/cultural/cultural-annual-day.svg" data-title="Annual Cultural Celebrations" data-caption="Student performances celebrating Indian classical dance, vocal music, and Jharkhand folk heritage.">
          <img src="assets/img/cultural/cultural-annual-day.svg" alt="Cultural Celebrations">
          <div class="photo-thumb-caption">Cultural Celebrations</div>
        </div>

        <div class="photo-thumb-card lightbox-trigger" data-src="assets/img/sports/sports-track-field.svg" data-title="Annual Athletic Meet" data-caption="Student sprinters and athletes competing in 100m sprint and field events.">
          <img src="assets/img/sports/sports-track-field.svg" alt="Athletic Track Meet">
          <div class="photo-thumb-caption">Athletic Track Meet</div>
        </div>
      </div>
    </div>
  </section>


  <!-- ====================================================================
       SECTION 13 — ADMISSION CALL TO ACTION (CINEMATIC BANNER)
       ==================================================================== -->
  <section class="admission-cta-section">
    <img src="assets/img/campus/campus-garden-courtyard.svg" alt="Campus Courtyard Background" class="admission-cta-bg">
    <div class="container admission-cta-content reveal-on-scroll">
      <span class="badge bg-warning text-dark px-3 py-1 rounded-pill mb-3 fw-bold">ADMISSIONS &amp; ENROLLMENT</span>
      <h2 class="font-serif text-white mb-3" style="font-size:clamp(2rem, 3.5vw, 3rem); font-weight:800;">
        Start Your Educational Journey With Us.
      </h2>
      <p style="font-size:1.15rem; color:#E2F0D9; line-height:1.75; margin-bottom:2rem;">
        Explore school admission information, eligibility criteria, required documents and contact the school for official guidance regarding Secondary and +2 Higher Secondary admissions.
      </p>
      <div class="d-flex flex-wrap justify-content-center gap-3">
        <a href="pages/admission.html" class="btn-cinematic-primary">
          <i class="bi bi-file-earmark-person-fill"></i> Explore Admission Information
        </a>
        <a href="pages/contact.html" class="btn-cinematic-outline">
          <i class="bi bi-telephone-inbound-fill"></i> Contact Admission Desk
        </a>
      </div>
      <div class="mt-4">
        <small class="text-white-50">
          <i class="bi bi-shield-exclamation me-1"></i> Admissions adhere to Jharkhand State Education Department guidelines and seat intake allocations.
        </small>
      </div>
    </div>
  </section>


  <!-- ====================================================================
       SECTION 14 — CONTACT SECTION (3 LARGE INFORMATION BLOCKS)
       ==================================================================== -->
  <section class="contact-section-home">
    <div class="container">
      <div class="text-center max-w-700 mx-auto mb-5 reveal-on-scroll">
        <span class="section-label-green">CONNECT WITH US</span>
        <h2 class="editorial-headline">Institutional Contact Details</h2>
        <p class="text-muted">
          Our administrative office is open during standard school hours to assist parents, students, and community members.
        </p>
      </div>

      <div class="row g-4 justify-content-center">
        <!-- 1. Location -->
        <div class="col-lg-4 col-md-6 reveal-on-scroll">
          <div class="contact-info-block">
            <div class="contact-icon-bubble"><i class="bi bi-geo-alt-fill"></i></div>
            <h3 style="font-size:1.25rem; font-weight:700; color:var(--deep-forest-green); margin-bottom:0.75rem;">School Location</h3>
            <p style="font-size:0.95rem; color:var(--body-text); margin-bottom:1.5rem;">
              हल्दीपोखर, पोटका, पूर्वी सिंहभूम<br>झारखण्ड – 831002, भारत
            </p>
            <a href="https://maps.google.com" target="_blank" rel="noopener noreferrer" class="btn btn-sm btn-outline-success rounded-pill px-4">
              <i class="bi bi-map-fill me-1"></i> Open Google Map
            </a>
          </div>
        </div>

        <!-- 2. Email -->
        <div class="col-lg-4 col-md-6 reveal-on-scroll">
          <div class="contact-info-block">
            <div class="contact-icon-bubble"><i class="bi bi-envelope-open-fill"></i></div>
            <h3 style="font-size:1.25rem; font-weight:700; color:var(--deep-forest-green); margin-bottom:0.75rem;">Official Email</h3>
            <p style="font-size:0.95rem; color:var(--body-text); margin-bottom:1.5rem; word-break:break-all;">
              vnhs.haldipokhar.e.singhbhum<br>@gmail.com
            </p>
            <a href="mailto:vnhs.haldipokhar.e.singhbhum@gmail.com" class="btn btn-sm btn-outline-success rounded-pill px-4">
              <i class="bi bi-send-fill me-1"></i> Send Official Email
            </a>
          </div>
        </div>

        <!-- 3. U-DISE & Code -->
        <div class="col-lg-4 col-md-6 reveal-on-scroll">
          <div class="contact-info-block">
            <div class="contact-icon-bubble"><i class="bi bi-shield-check"></i></div>
            <h3 style="font-size:1.25rem; font-weight:700; color:var(--deep-forest-green); margin-bottom:0.75rem;">Official Registry</h3>
            <p style="font-size:0.95rem; color:var(--body-text); margin-bottom:1.5rem;">
              U-DISE Code: <strong>20180231602</strong><br>
              Affiliation: <strong>JAC, Ranchi (+2 Level)</strong>
            </p>
            <a href="pages/contact.html" class="btn btn-sm btn-outline-success rounded-pill px-4">
              <i class="bi bi-chat-text-fill me-1"></i> Contact Desk Form
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>


  <!-- ====================================================================
       SECTION 15 — PREMIUM FOOTER (4 COLUMNS + BACK TO TOP)
       ==================================================================== -->
  <footer class="premium-footer">
    <div class="container">
      <div class="row g-4">
        <!-- Col 1: About School -->
        <div class="col-lg-4 col-md-6">
          <div class="d-flex align-items-center gap-3 mb-3">
            <img src="assets/img/logo/school-logo.svg" alt="School Logo" style="width:54px; height:54px;">
            <div>
              <div style="font-family:var(--font-hindi); font-weight:700; color:var(--white); font-size:1.1rem; line-height:1.2;">
                +2 राजकीयकृत विद्या निकेतन
              </div>
              <div style="font-size:0.75rem; color:var(--gold-light); text-transform:uppercase; letter-spacing:0.05em;">
                Higher Secondary School
              </div>
            </div>
          </div>
          <p style="font-size:0.875rem; color:#CBD5E1; line-height:1.65; margin-bottom:1.25rem;">
            A premier rural educational institution committed to imparting holistic education, value formation, disciplined lifestyle and academic excellence in Haldipokhar, East Singhbhum.
          </p>
          <div style="font-size:0.8rem; color:#A7F3D0;">
            <i class="bi bi-patch-check-fill me-1"></i> U-DISE Code: 20180231602 • JAC Affiliated
          </div>
        </div>

        <!-- Col 2: Quick Links -->
        <div class="col-lg-2 col-md-6">
          <div class="footer-col-title">Quick Links</div>
          <ul class="footer-links-list">
            <li><a href="index.html"><i class="bi bi-chevron-right"></i> Home</a></li>
            <li><a href="pages/about-school.html"><i class="bi bi-chevron-right"></i> About School</a></li>
            <li><a href="pages/principal.html"><i class="bi bi-chevron-right"></i> Principal's Desk</a></li>
            <li><a href="pages/mission-vision.html"><i class="bi bi-chevron-right"></i> Mission &amp; Vision</a></li>
            <li><a href="pages/smc-members.html"><i class="bi bi-chevron-right"></i> SMC Members</a></li>
            <li><a href="pages/admission.html"><i class="bi bi-chevron-right"></i> Admission Info</a></li>
          </ul>
        </div>

        <!-- Col 3: Academics & Activities -->
        <div class="col-lg-3 col-md-6">
          <div class="footer-col-title">Academics &amp; Activities</div>
          <ul class="footer-links-list">
            <li><a href="pages/academic-overview.html"><i class="bi bi-chevron-right"></i> Academic Overview</a></li>
            <li><a href="pages/classes-subjects.html"><i class="bi bi-chevron-right"></i> Classes &amp; Subjects</a></li>
            <li><a href="pages/cultural-activities.html"><i class="bi bi-chevron-right"></i> Cultural Activities</a></li>
            <li><a href="pages/sports-activities.html"><i class="bi bi-chevron-right"></i> Sports Activities</a></li>
            <li><a href="pages/exhibitions.html"><i class="bi bi-chevron-right"></i> Science Exhibitions</a></li>
            <li><a href="pages/scout-guide.html"><i class="bi bi-chevron-right"></i> Scout &amp; Guide Wing</a></li>
          </ul>
        </div>

        <!-- Col 4: Contact Information -->
        <div class="col-lg-3 col-md-6">
          <div class="footer-col-title">Contact Information</div>
          <div class="footer-contact-item">
            <i class="bi bi-geo-alt-fill"></i>
            <div>हल्दीपोखर, पोटका, पूर्वी सिंहभूम, झारखण्ड – 831002</div>
          </div>
          <div class="footer-contact-item">
            <i class="bi bi-envelope-fill"></i>
            <div>vnhs.haldipokhar.e.singhbhum<br>@gmail.com</div>
          </div>
          <div class="footer-contact-item">
            <i class="bi bi-clock-fill"></i>
            <div>Mon – Sat: 09:30 AM – 04:00 PM<br>(Standard School Working Hours)</div>
          </div>
        </div>
      </div>

      <div class="footer-bottom-bar">
        <div>
          &copy; <span class="auto-year"></span> +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय, हल्दीपोखर. All Rights Reserved.
        </div>
        <div>
          Designed for Excellence • Premium Green Storytelling Edition
        </div>
      </div>
    </div>
  </footer>

  <!-- Floating Back To Top Button -->
  <button class="back-to-top-btn" aria-label="Back to Top of Page">
    <i class="bi bi-arrow-up"></i>
  </button>

  <!-- Interactive Lightbox Modal -->
  <div class="cinematic-lightbox-modal" role="dialog" aria-modal="true" aria-label="Campus Image Lightbox">
    <div class="lightbox-content-box">
      <button class="lightbox-close-btn" aria-label="Close Lightbox">&times;</button>
      <button class="lightbox-nav-btn lightbox-prev" aria-label="Previous Image"><i class="bi bi-chevron-left"></i></button>
      <button class="lightbox-nav-btn lightbox-next" aria-label="Next Image"><i class="bi bi-chevron-right"></i></button>
      <img src="" alt="Expanded View" class="lightbox-img-render">
      <div class="lightbox-meta-box">
        <div class="lightbox-counter badge bg-success-subtle text-success px-2 py-1 mb-1"></div>
        <div class="lightbox-title"></div>
        <div class="lightbox-caption"></div>
      </div>
    </div>
  </div>

  <!-- Scripts: Bootstrap 5 Bundle, Site Data, Main JS, Gallery JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  <script src="assets/js/site-data.js"></script>
  <script src="assets/js/main.js"></script>
  <script src="assets/js/gallery.js"></script>
</body>
</html>
"""

with open(output_path, "w", encoding="utf-8") as f:
    f.write(index_html.strip())

print("Homepage index.html generated successfully with all 15 sections!")
