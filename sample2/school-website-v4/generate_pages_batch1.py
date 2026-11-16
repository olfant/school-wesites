import os

pages_dir = r"c:\Users\ACER\OneDrive\Desktop\school\school-website-v4\pages"

def get_page_template(title, badge, desc, active_nav, breadcrumbs, page_content):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय</title>
  <meta name="description" content="{desc}">
  <link rel="icon" type="image/svg+xml" href="../assets/img/logo/school-logo.svg">

  <!-- Bootstrap 5 CSS & Icons CDN -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" rel="stylesheet">

  <!-- Custom Cinematic Green Theme Stylesheets -->
  <link rel="stylesheet" href="../assets/css/style.css">
  <link rel="stylesheet" href="../assets/css/responsive.css">
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

    <!-- BRANDING HEADER AREA -->
    <div class="branding-header">
      <div class="container d-flex flex-wrap justify-content-between align-items-center">
        <div class="branding-logo-box">
          <a href="../index.html" class="d-flex align-items-center gap-3 text-decoration-none">
            <img src="../assets/img/logo/school-logo.svg" alt="School Emblem" class="school-header-logo">
            <div>
              <div class="school-name-hindi">+2 राजकीयकृत विद्या निकेतन उच्च विद्यालय</div>
              <div class="school-name-english">+2 Rajkiyakrit Vidya Niketan Higher Secondary School</div>
              <div class="school-address-subtitle">
                <i class="bi bi-pin-map-fill text-success"></i> हल्दीपोखर, पोटका, पूर्वी सिंहभूम, झारखण्ड – 831002
              </div>
            </div>
          </a>
        </div>
        <div class="branding-actions-col d-none d-lg-flex align-items-center gap-3">
          <div class="text-end me-2">
            <div style="font-size:0.75rem; color:#6B7280; text-transform:uppercase; font-weight:700;">Affiliation &amp; Code</div>
            <div style="font-weight:700; color:var(--deep-forest-green); font-size:0.9rem;">JAC, Ranchi • +2 Level</div>
          </div>
          <a href="admission.html" class="branding-action-btn">
            <i class="bi bi-file-earmark-text-fill"></i> Admission Information
          </a>
        </div>
        <!-- Mobile Drawer Hamburger Toggle Button -->
        <button class="mobile-drawer-toggle d-lg-none" type="button" aria-label="Toggle Navigation Menu">
          <i class="bi bi-list text-dark"></i>
        </button>
      </div>
    </div>

    <!-- MAIN NAVIGATION BAR (STICKY) -->
    <nav class="main-nav-bar navbar navbar-expand-lg" aria-label="Main Navigation">
      <div class="container">
        <div class="collapse navbar-collapse" id="desktopNavbarNav">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link" href="../index.html"><i class="bi bi-house-door-fill me-1"></i> Home</a>
            </li>

            <!-- About Us Dropdown -->
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle {'active' if active_nav == 'about' else ''}" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                About Us
              </a>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="about-school.html"><i class="bi bi-building me-2"></i> About School</a></li>
                <li><a class="dropdown-item" href="principal.html"><i class="bi bi-person-badge me-2"></i> Principal's Desk</a></li>
                <li><a class="dropdown-item" href="mission-vision.html"><i class="bi bi-compass me-2"></i> Mission &amp; Vision</a></li>
                <li><a class="dropdown-item" href="smc-members.html"><i class="bi bi-people me-2"></i> SMC Members</a></li>
              </ul>
            </li>

            <!-- Academic Dropdown -->
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle {'active' if active_nav == 'academic' else ''}" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Academic
              </a>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="academic-overview.html"><i class="bi bi-journal-bookmark me-2"></i> Academic Overview</a></li>
                <li><a class="dropdown-item" href="classes-subjects.html"><i class="bi bi-collection me-2"></i> Classes &amp; Subjects</a></li>
                <li><a class="dropdown-item" href="academic-calendar.html"><i class="bi bi-calendar-event me-2"></i> Academic Calendar</a></li>
                <li><a class="dropdown-item" href="teaching-learning.html"><i class="bi bi-easel me-2"></i> Teaching &amp; Learning</a></li>
              </ul>
            </li>

            <!-- Examination Dropdown -->
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle {'active' if active_nav == 'examination' else ''}" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Examination
              </a>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="results.html"><i class="bi bi-award me-2"></i> Examination Results</a></li>
              </ul>
            </li>

            <!-- Achievements Dropdown -->
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle {'active' if active_nav == 'achievements' else ''}" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Achievements
              </a>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="achievements.html"><i class="bi bi-trophy me-2"></i> Overview Achievements</a></li>
                <li><a class="dropdown-item" href="cultural-activities.html"><i class="bi bi-palette me-2"></i> Cultural Activities</a></li>
                <li><a class="dropdown-item" href="sports-activities.html"><i class="bi bi-dribbble me-2"></i> Sports Activities</a></li>
                <li><a class="dropdown-item" href="exhibitions.html"><i class="bi bi-lightbulb me-2"></i> Science &amp; Exhibitions</a></li>
                <li><a class="dropdown-item" href="skills-competition.html"><i class="bi bi-stars me-2"></i> Skills Competition</a></li>
                <li><a class="dropdown-item" href="vocational-activities.html"><i class="bi bi-tools me-2"></i> Vocational Activities</a></li>
              </ul>
            </li>

            <li class="nav-item">
              <a class="nav-link {'active' if active_nav == 'admission' else ''}" href="admission.html">Admission</a>
            </li>

            <li class="nav-item">
              <a class="nav-link {'active' if active_nav == 'scout' else ''}" href="scout-guide.html">Scout &amp; Guide</a>
            </li>

            <li class="nav-item">
              <a class="nav-link {'active' if active_nav == 'gallery' else ''}" href="gallery.html">Gallery</a>
            </li>

            <li class="nav-item">
              <a class="nav-link {'active' if active_nav == 'contact' else ''}" href="contact.html">Contact Us</a>
            </li>
          </ul>

          <div class="d-flex align-items-center">
            <a href="contact.html" class="btn btn-sm btn-outline-light rounded-pill px-3 py-1" style="font-size:0.8rem; font-weight:600;">
              <i class="bi bi-telephone-fill me-1"></i> Helpline
            </a>
          </div>
        </div>
      </div>
    </nav>

    <!-- Mobile Drawer -->
    <div class="mobile-drawer-backdrop"></div>
    <div class="mobile-drawer">
      <div class="d-flex justify-content-between align-items-center pb-3 border-bottom border-light border-opacity-25 mb-3">
        <div class="d-flex align-items-center gap-2">
          <img src="../assets/img/logo/school-logo.svg" alt="Emblem" style="width:36px; height:36px;">
          <span style="font-weight:700; font-size:0.9rem; color:var(--gold-light);">VNHS Haldipokhar</span>
        </div>
        <button class="mobile-drawer-close" aria-label="Close Navigation Drawer">&times;</button>
      </div>

      <div class="mobile-nav-links">
        <a class="nav-link" href="../index.html">Home</a>
        <div class="text-white-50 mt-2" style="font-size:0.8rem; text-transform:uppercase;">About Us</div>
        <div class="mobile-sub-menu">
          <a href="about-school.html"><i class="bi bi-chevron-right me-1"></i> About School</a>
          <a href="principal.html"><i class="bi bi-chevron-right me-1"></i> Principal's Desk</a>
          <a href="mission-vision.html"><i class="bi bi-chevron-right me-1"></i> Mission &amp; Vision</a>
          <a href="smc-members.html"><i class="bi bi-chevron-right me-1"></i> SMC Members</a>
        </div>

        <div class="text-white-50 mt-2" style="font-size:0.8rem; text-transform:uppercase;">Academic</div>
        <div class="mobile-sub-menu">
          <a href="academic-overview.html"><i class="bi bi-chevron-right me-1"></i> Academic Overview</a>
          <a href="classes-subjects.html"><i class="bi bi-chevron-right me-1"></i> Classes &amp; Subjects</a>
          <a href="academic-calendar.html"><i class="bi bi-chevron-right me-1"></i> Academic Calendar</a>
          <a href="teaching-learning.html"><i class="bi bi-chevron-right me-1"></i> Teaching &amp; Learning</a>
        </div>

        <div class="text-white-50 mt-2" style="font-size:0.8rem; text-transform:uppercase;">Achievements</div>
        <div class="mobile-sub-menu">
          <a href="achievements.html"><i class="bi bi-chevron-right me-1"></i> Achievements Overview</a>
          <a href="cultural-activities.html"><i class="bi bi-chevron-right me-1"></i> Cultural Activities</a>
          <a href="sports-activities.html"><i class="bi bi-chevron-right me-1"></i> Sports Activities</a>
          <a href="exhibitions.html"><i class="bi bi-chevron-right me-1"></i> Science &amp; Exhibitions</a>
          <a href="skills-competition.html"><i class="bi bi-chevron-right me-1"></i> Skills Competition</a>
          <a href="vocational-activities.html"><i class="bi bi-chevron-right me-1"></i> Vocational Activities</a>
        </div>

        <a class="nav-link" href="results.html">Examination Results</a>
        <a class="nav-link" href="admission.html">Admission</a>
        <a class="nav-link" href="scout-guide.html">Scout &amp; Guide</a>
        <a class="nav-link" href="gallery.html">Campus Gallery</a>
        <a class="nav-link" href="contact.html">Contact Us</a>
      </div>
    </div>
  </header>

  <!-- ====================================================================
       INNER PAGE HERO BANNER WITH BREADCRUMBS
       ==================================================================== -->
  <section class="inner-hero-banner">
    <div class="container position-relative" style="z-index:2;">
      <span class="inner-hero-badge"><i class="bi bi-compass-fill"></i> {badge}</span>
      <h1 class="inner-hero-title">{title}</h1>
      <p class="inner-hero-desc">{desc}</p>

      <nav aria-label="breadcrumb">
        <ol class="inner-breadcrumbs list-unstyled mb-0">
          <li><a href="../index.html"><i class="bi bi-house-door-fill"></i> Home</a></li>
          {breadcrumbs}
          <li class="text-white fw-bold">/ {title}</li>
        </ol>
      </nav>
    </div>
  </section>

  <!-- ====================================================================
       PAGE MAIN CONTENT
       ==================================================================== -->
  <main>
    {page_content}
  </main>

  <!-- ====================================================================
       GLOBAL FOOTER
       ==================================================================== -->
  <footer class="premium-footer">
    <div class="container">
      <div class="row g-4">
        <!-- Col 1: About School -->
        <div class="col-lg-4 col-md-6">
          <div class="d-flex align-items-center gap-3 mb-3">
            <img src="../assets/img/logo/school-logo.svg" alt="School Logo" style="width:54px; height:54px;">
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
            <li><a href="../index.html"><i class="bi bi-chevron-right"></i> Home</a></li>
            <li><a href="about-school.html"><i class="bi bi-chevron-right"></i> About School</a></li>
            <li><a href="principal.html"><i class="bi bi-chevron-right"></i> Principal's Desk</a></li>
            <li><a href="mission-vision.html"><i class="bi bi-chevron-right"></i> Mission &amp; Vision</a></li>
            <li><a href="smc-members.html"><i class="bi bi-chevron-right"></i> SMC Members</a></li>
            <li><a href="admission.html"><i class="bi bi-chevron-right"></i> Admission Info</a></li>
          </ul>
        </div>

        <!-- Col 3: Academics & Activities -->
        <div class="col-lg-3 col-md-6">
          <div class="footer-col-title">Academics &amp; Activities</div>
          <ul class="footer-links-list">
            <li><a href="academic-overview.html"><i class="bi bi-chevron-right"></i> Academic Overview</a></li>
            <li><a href="classes-subjects.html"><i class="bi bi-chevron-right"></i> Classes &amp; Subjects</a></li>
            <li><a href="cultural-activities.html"><i class="bi bi-chevron-right"></i> Cultural Activities</a></li>
            <li><a href="sports-activities.html"><i class="bi bi-chevron-right"></i> Sports Activities</a></li>
            <li><a href="exhibitions.html"><i class="bi bi-chevron-right"></i> Science Exhibitions</a></li>
            <li><a href="scout-guide.html"><i class="bi bi-chevron-right"></i> Scout &amp; Guide Wing</a></li>
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

  <!-- Scripts -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  <script src="../assets/js/site-data.js"></script>
  <script src="../assets/js/main.js"></script>
  <script src="../assets/js/gallery.js"></script>
</body>
</html>
"""

def save_page(filename, content):
    path = os.path.join(pages_dir, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Generated: pages/{filename}")

# ==============================================================================
# 1. ABOUT SCHOOL (pages/about-school.html)
# ==============================================================================
about_content = """
<section class="py-5 bg-white">
  <div class="container">
    <div class="row align-items-center g-5 mb-5">
      <div class="col-lg-6 reveal-on-scroll">
        <span class="section-label-green">INSTITUTIONAL PROFILE</span>
        <h2 class="editorial-headline">Nurturing Knowledge in the Heart of Haldipokhar</h2>
        <p class="editorial-lead-text">
          +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय stands as a premier educational beacon in Potka block of East Singhbhum, Jharkhand. Established to empower the rural and semi-urban youth, our institution delivers holistic secondary and higher secondary education rooted in moral integrity, academic discipline, and modern pedagogical excellence.
        </p>
        <p style="color:var(--body-text); line-height:1.75;">
          Our school focuses on quality education, good values, discipline, life skills and the all-round development of students. Under the aegis of the Department of School Education and Literacy, Government of Jharkhand, and affiliated with the Jharkhand Academic Council (JAC), Ranchi, we bridge traditional human values with 21st-century vocational and academic competencies.
        </p>
      </div>
      <div class="col-lg-6 reveal-on-scroll">
        <div class="editorial-image-frame">
          <img src="../assets/img/campus/campus-main-facade.svg" alt="School Academic Facade">
        </div>
      </div>
    </div>

    <!-- History & Background -->
    <div class="p-4 p-lg-5 bg-light rounded-4 border mb-5 reveal-on-scroll">
      <div class="row g-4 align-items-center">
        <div class="col-lg-8">
          <span class="badge bg-success-subtle text-success px-3 py-1 rounded-pill mb-2 font-monospace">HISTORICAL ROOTS</span>
          <h3 style="font-size:1.85rem; font-weight:800; color:var(--deep-forest-green); margin-bottom:1rem;">
            History &amp; Evolutionary Background
          </h3>
          <p style="color:var(--body-text); line-height:1.75;">
            Founded with the collective philanthropic aspiration of local community elders, educationists, and social leaders of Haldipokhar, the school was instituted to dismantle geographic and economic barriers to high-quality secondary learning. Over consecutive decades, the institution evolved from a modest local high school into a recognized government higher secondary (+2) institution nurturing students across diverse communities.
          </p>
          <div class="official-placeholder-badge">
            <i class="bi bi-clock-history"></i> Establishment Milestone: [Year Pending Official Record Verification]
          </div>
        </div>
        <div class="col-lg-4 text-center">
          <div class="p-4 bg-white rounded-3 shadow-sm border">
            <div style="font-size:0.8rem; font-weight:700; color:#6B7280; text-transform:uppercase;">National Unified Registry</div>
            <div style="font-size:1.6rem; font-weight:800; color:var(--deep-forest-green); margin:0.5rem 0;">U-DISE Code</div>
            <div class="badge bg-success fs-6 px-3 py-2">20180231602</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Campus Facilities Showcase -->
    <div class="mb-5 reveal-on-scroll">
      <div class="text-center max-w-700 mx-auto mb-4">
        <span class="section-label-green">CAMPUS INFRASTRUCTURE</span>
        <h2 class="editorial-headline">Facilities Designed for Comprehensive Learning</h2>
        <p class="text-muted">A look inside our learning environments, laboratories, and green open areas.</p>
      </div>

      <div class="row g-4">
        <div class="col-md-4">
          <div class="card h-100 border-0 shadow-sm rounded-4 overflow-hidden">
            <img src="../assets/img/classrooms/smart-classroom.svg" class="card-img-top" style="height:220px; object-fit:cover;" alt="Smart ICT Classrooms">
            <div class="card-body p-4">
              <h4 style="font-size:1.2rem; font-weight:700; color:var(--heading);">Smart Classrooms &amp; ICT</h4>
              <p style="font-size:0.9rem; color:var(--body-text); margin-bottom:0;">Equipped with audio-visual learning tools, interactive educational software, and modern projection for engaging concept delivery.</p>
            </div>
          </div>
        </div>

        <div class="col-md-4">
          <div class="card h-100 border-0 shadow-sm rounded-4 overflow-hidden">
            <img src="../assets/img/classrooms/science-laboratory.svg" class="card-img-top" style="height:220px; object-fit:cover;" alt="Science Laboratory">
            <div class="card-body p-4">
              <h4 style="font-size:1.2rem; font-weight:700; color:var(--heading);">Composite Science Laboratories</h4>
              <p style="font-size:0.9rem; color:var(--body-text); margin-bottom:0;">Dedicated practical workstations for physics, chemistry, and biological experiments fostering genuine scientific curiosity.</p>
            </div>
          </div>
        </div>

        <div class="col-md-4">
          <div class="card h-100 border-0 shadow-sm rounded-4 overflow-hidden">
            <img src="../assets/img/classrooms/library-reading.svg" class="card-img-top" style="height:220px; object-fit:cover;" alt="School Library">
            <div class="card-body p-4">
              <h4 style="font-size:1.2rem; font-weight:700; color:var(--heading);">Library &amp; Knowledge Resource</h4>
              <p style="font-size:0.9rem; color:var(--body-text); margin-bottom:0;">Curated catalog of reference textbooks, literary works, regional history volumes, competitive guides and national periodicals.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
"""

save_page("about-school.html", get_page_template(
    "About School", 
    "Institutional Overview", 
    "Discover the history, educational ethos, and campus facilities of +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय, Haldipokhar.",
    "about",
    "<li><a href='about-school.html'>About Us</a></li>",
    about_content
))

# ==============================================================================
# 2. PRINCIPAL'S DESK (pages/principal.html)
# ==============================================================================
principal_content = """
<section class="py-5 bg-white">
  <div class="container">
    <div class="row g-5 align-items-center mb-5">
      <div class="col-lg-5 reveal-on-scroll">
        <div class="principal-portrait-container">
          <img src="../assets/img/principal/principal-desk-portrait.svg" alt="Principal Desk Setting">
        </div>
        <div class="p-3 bg-light rounded-3 border mt-3 text-center">
          <div class="official-placeholder-badge mb-1">
            <i class="bi bi-person-fill-check"></i> Administrative Leadership
          </div>
          <div style="font-size:1.15rem; font-weight:800; color:var(--deep-forest-green);">
            [Principal Name - Official Record Pending Verification]
          </div>
          <div style="font-size:0.85rem; color:#6B7280;">Principal / In-Charge Headmaster • +2 राजकीयकृत विद्या निकेतन</div>
        </div>
      </div>

      <div class="col-lg-7 reveal-on-scroll">
        <span class="section-label-green">LEADERSHIP ADDRESS</span>
        <h2 class="editorial-headline">From the Principal's Desk</h2>
        <div class="quote-icon-large text-success mb-2"><i class="bi bi-quote"></i></div>
        <p class="editorial-lead-text">
          "Education is the greatest equalizer and the most transformative catalyst in society. Our foremost responsibility is to cultivate resilient, enlightened, and compassionate citizens who carry both academic competence and moral conviction."
        </p>

        <p style="color:var(--body-text); line-height:1.75;">
          Dear Students, Respected Parents, and Community Well-Wishers,
        </p>
        <p style="color:var(--body-text); line-height:1.75;">
          It is an honor to welcome you to the official portal of +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय, हल्दीपोखर. Situated in the culturally rich region of Potka, our institution has consistently dedicated itself to delivering quality secondary and higher secondary education that meets state benchmarks while remaining accessible to every deserving student.
        </p>
        <p style="color:var(--body-text); line-height:1.75;">
          Our academic approach is founded on three unwavering pillars: rigorous curriculum delivery, uncompromised student discipline, and diverse co-curricular avenues. Whether on the sports field, in science exhibitions, through the Bharat Scouts &amp; Guides, or in vocational workshops, we urge each student to explore their unique talents and strive for personal excellence.
        </p>
      </div>
    </div>

    <!-- Educational Philosophy & Pillars -->
    <div class="row g-4 mb-5 reveal-on-scroll">
      <div class="col-md-4">
        <div class="p-4 bg-light rounded-4 border h-100">
          <div class="info-band-icon mb-3" style="background:var(--light-mint); color:var(--primary-green);"><i class="bi bi-mortarboard-fill"></i></div>
          <h4 style="font-size:1.2rem; font-weight:700; color:var(--heading);">Inclusive Academic Rigor</h4>
          <p style="font-size:0.9rem; color:var(--body-text); margin-bottom:0;">
            Ensuring every child, regardless of socio-economic background, receives dedicated instructional guidance and conceptual support.
          </p>
        </div>
      </div>

      <div class="col-md-4">
        <div class="p-4 bg-light rounded-4 border h-100">
          <div class="info-band-icon mb-3" style="background:var(--light-mint); color:var(--primary-green);"><i class="bi bi-shield-heart-fill"></i></div>
          <h4 style="font-size:1.2rem; font-weight:700; color:var(--heading);">Ethical Character Formation</h4>
          <p style="font-size:0.9rem; color:var(--body-text); margin-bottom:0;">
            Inculcating civic duties, environmental consciousness, mutual empathy, and adherence to democratic Indian constitutional values.
          </p>
        </div>
      </div>

      <div class="col-md-4">
        <div class="p-4 bg-light rounded-4 border h-100">
          <div class="info-band-icon mb-3" style="background:var(--light-mint); color:var(--primary-green);"><i class="bi bi-lightbulb-fill"></i></div>
          <h4 style="font-size:1.2rem; font-weight:700; color:var(--heading);">Future Life Readiness</h4>
          <p style="font-size:0.9rem; color:var(--body-text); margin-bottom:0;">
            Preparing learners with practical vocational skills, analytical problem-solving acumen, and confidence for higher education.
          </p>
        </div>
      </div>
    </div>
  </div>
</section>
"""

save_page("principal.html", get_page_template(
    "Principal's Desk", 
    "Leadership Message", 
    "Official message, leadership vision, and educational philosophy from the Principal's Desk of +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय.",
    "about",
    "<li><a href='about-school.html'>About Us</a></li>",
    principal_content
))

# ==============================================================================
# 3. MISSION & VISION (pages/mission-vision.html)
# ==============================================================================
mission_vision_content = """
<section class="py-5 bg-white">
  <div class="container">
    <div class="row g-4 mb-5">
      <!-- Mission Card -->
      <div class="col-lg-6 reveal-on-scroll">
        <div class="p-5 rounded-4 h-100 border text-white" style="background:linear-gradient(135deg, var(--deep-forest-green), var(--primary-green));">
          <div class="d-inline-flex align-items-center gap-2 px-3 py-1 bg-white bg-opacity-15 rounded-pill mb-3">
            <i class="bi bi-bullseye text-warning"></i>
            <span style="font-size:0.8rem; font-weight:700; letter-spacing:0.1em; text-transform:uppercase;">Institutional Purpose</span>
          </div>
          <h2 style="font-size:2.2rem; font-weight:800; margin-bottom:1.25rem;">Our Mission</h2>
          <p style="font-size:1.1rem; line-height:1.75; color:#E2F0D9;">
            To deliver accessible, high-quality secondary and higher secondary education that empowers rural and semi-urban learners with strong foundational concepts, moral integrity, physical fitness, creative expression, and vocational readiness.
          </p>
          <ul class="list-unstyled mt-4 d-flex flex-column gap-2" style="font-size:0.95rem; color:#D1E7DD;">
            <li><i class="bi bi-check-circle-fill text-warning me-2"></i> Ensure equitable academic access and individualized student mentoring.</li>
            <li><i class="bi bi-check-circle-fill text-warning me-2"></i> Build disciplined character through continuous value education and assemblies.</li>
            <li><i class="bi bi-check-circle-fill text-warning me-2"></i> Promote experiential learning across science laboratories and workshops.</li>
          </ul>
        </div>
      </div>

      <!-- Vision Card -->
      <div class="col-lg-6 reveal-on-scroll">
        <div class="p-5 rounded-4 h-100 border bg-light">
          <div class="d-inline-flex align-items-center gap-2 px-3 py-1 bg-success-subtle text-success rounded-pill mb-3">
            <i class="bi bi-eye-fill"></i>
            <span style="font-size:0.8rem; font-weight:700; letter-spacing:0.1em; text-transform:uppercase;">Future Aspiration</span>
          </div>
          <h2 style="font-size:2.2rem; font-weight:800; color:var(--deep-forest-green); margin-bottom:1.25rem;">Our Vision</h2>
          <p style="font-size:1.1rem; line-height:1.75; color:var(--body-text);">
            To become an exemplary model higher secondary school in Jharkhand, celebrated for academic excellence, holistic character cultivation, cultural preservation, and producing responsible citizens capable of driving positive societal change.
          </p>
          <ul class="list-unstyled mt-4 d-flex flex-column gap-2" style="font-size:0.95rem; color:var(--body-text);">
            <li><i class="bi bi-star-fill text-success me-2"></i> Achieve outstanding benchmarks in JAC Secondary and +2 Board examinations.</li>
            <li><i class="bi bi-star-fill text-success me-2"></i> Lead district and state competitions in sports, sciences, and cultural arts.</li>
            <li><i class="bi bi-star-fill text-success me-2"></i> Establish our campus as an environmentally conscious green eco-sanctuary.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Core Values Matrix -->
    <div class="reveal-on-scroll mt-5">
      <div class="text-center max-w-700 mx-auto mb-5">
        <span class="section-label-green">GUIDING PRINCIPLES</span>
        <h2 class="editorial-headline">The Values That Define Us</h2>
        <p class="text-muted">Six foundational tenets that guide everyday interactions, pedagogy, and student growth.</p>
      </div>

      <div class="row g-4">
        <div class="col-md-4">
          <div class="p-4 bg-light rounded-4 border h-100">
            <div style="font-size:2rem; font-weight:800; color:var(--primary-green); font-family:var(--font-serif);">01</div>
            <h4 style="font-size:1.25rem; font-weight:700; color:var(--heading);">Integrity &amp; Truth</h4>
            <p style="font-size:0.9rem; color:var(--body-text); margin-bottom:0;">Upholding honesty, ethical responsibility, and moral courage in all academic and social conduct.</p>
          </div>
        </div>
        <div class="col-md-4">
          <div class="p-4 bg-light rounded-4 border h-100">
            <div style="font-size:2rem; font-weight:800; color:var(--primary-green); font-family:var(--font-serif);">02</div>
            <h4 style="font-size:1.25rem; font-weight:700; color:var(--heading);">Discipline &amp; Respect</h4>
            <p style="font-size:0.9rem; color:var(--body-text); margin-bottom:0;">Punctuality, polite speech, respect for elders, teachers, peers, and institutional guidelines.</p>
          </div>
        </div>
        <div class="col-md-4">
          <div class="p-4 bg-light rounded-4 border h-100">
            <div style="font-size:2rem; font-weight:800; color:var(--primary-green); font-family:var(--font-serif);">03</div>
            <h4 style="font-size:1.25rem; font-weight:700; color:var(--heading);">Academic Diligence</h4>
            <p style="font-size:0.9rem; color:var(--body-text); margin-bottom:0;">Commitment to daily study, curiosity to inquire, scientific temper, and intellectual perseverance.</p>
          </div>
        </div>
        <div class="col-md-4">
          <div class="p-4 bg-light rounded-4 border h-100">
            <div style="font-size:2rem; font-weight:800; color:var(--primary-green); font-family:var(--font-serif);">04</div>
            <h4 style="font-size:1.25rem; font-weight:700; color:var(--heading);">Civic &amp; Social Duty</h4>
            <p style="font-size:0.9rem; color:var(--body-text); margin-bottom:0;">Active service toward the underprivileged, gender equality, and national harmony.</p>
          </div>
        </div>
        <div class="col-md-4">
          <div class="p-4 bg-light rounded-4 border h-100">
            <div style="font-size:2rem; font-weight:800; color:var(--primary-green); font-family:var(--font-serif);">05</div>
            <h4 style="font-size:1.25rem; font-weight:700; color:var(--heading);">Ecological Harmony</h4>
            <p style="font-size:0.9rem; color:var(--body-text); margin-bottom:0;">Planting green canopies, conserving water and electricity, and minimizing single-use waste.</p>
          </div>
        </div>
        <div class="col-md-4">
          <div class="p-4 bg-light rounded-4 border h-100">
            <div style="font-size:2rem; font-weight:800; color:var(--primary-green); font-family:var(--font-serif);">06</div>
            <h4 style="font-size:1.25rem; font-weight:700; color:var(--heading);">Inclusive Growth</h4>
            <p style="font-size:0.9rem; color:var(--body-text); margin-bottom:0;">Welcoming students of all communities with equal care, warmth, and developmental opportunity.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
"""

save_page("mission-vision.html", get_page_template(
    "Mission & Vision", 
    "Core Philosophy", 
    "Institutional mission, long-term vision, core values, and student development goals of +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय.",
    "about",
    "<li><a href='about-school.html'>About Us</a></li>",
    mission_vision_content
))

# ==============================================================================
# 4. SMC MEMBERS (pages/smc-members.html)
# ==============================================================================
smc_content = """
<section class="py-5 bg-white">
  <div class="container">
    <div class="row align-items-center g-5 mb-5 reveal-on-scroll">
      <div class="col-lg-7">
        <span class="section-label-green">COMMUNITY GOVERNANCE</span>
        <h2 class="editorial-headline">School Management Committee (SMC)</h2>
        <p class="editorial-lead-text">
          In alignment with the Right to Education (RTE) Act and Jharkhand State School Education Department directives, the School Management Committee ensures transparent administration, student welfare oversight, and community collaboration.
        </p>
        <p style="color:var(--body-text); line-height:1.75;">
          The SMC brings together institutional administrators, experienced faculty, elected local panchayat representatives, and parent nominees to supervise campus infrastructural maintenance, midday meal nutrition, academic attendance, and school development plans (SDP).
        </p>
      </div>
      <div class="col-lg-5">
        <div class="p-4 bg-light rounded-4 border">
          <h4 style="font-size:1.2rem; font-weight:700; color:var(--deep-forest-green); margin-bottom:1rem;">Key Responsibilities</h4>
          <ul class="list-unstyled d-flex flex-column gap-2 mb-0" style="font-size:0.9rem; color:var(--body-text);">
            <li><i class="bi bi-check-circle-fill text-success me-2"></i> Monitor student enrollment and prevent dropouts.</li>
            <li><i class="bi bi-check-circle-fill text-success me-2"></i> Review midday meal preparation and drinking water quality.</li>
            <li><i class="bi bi-check-circle-fill text-success me-2"></i> Formulate the Three-Year School Development Plan (SDP).</li>
            <li><i class="bi bi-check-circle-fill text-success me-2"></i> Foster parent-teacher collaboration and community trust.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- SMC Members Table -->
    <div class="reveal-on-scroll">
      <div class="d-flex justify-content-between align-items-center mb-3">
        <h3 style="font-size:1.5rem; font-weight:800; color:var(--heading); margin-bottom:0;">Committee Composition</h3>
        <span class="official-placeholder-badge"><i class="bi bi-info-circle"></i> Committee Register Pending Official Updates</span>
      </div>

      <div class="table-responsive bg-white rounded-4 border shadow-sm overflow-hidden">
        <table class="table table-hover align-middle mb-0">
          <thead style="background-color:var(--deep-forest-green); color:var(--white);">
            <tr>
              <th class="py-3 px-4">Designation / Role</th>
              <th class="py-3 px-4">Member Name</th>
              <th class="py-3 px-4">Category</th>
              <th class="py-3 px-4">Tenure / Status</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="px-4 fw-bold">President (SMC)</td>
              <td class="px-4">[Elected Parent / Community Member - Official Record Pending]</td>
              <td class="px-4"><span class="badge bg-primary-subtle text-primary">Parent Category</span></td>
              <td class="px-4">Active Term</td>
            </tr>
            <tr>
              <td class="px-4 fw-bold">Member Secretary</td>
              <td class="px-4">[Principal / In-Charge Headmaster - Ex-Officio]</td>
              <td class="px-4"><span class="badge bg-success-subtle text-success">Institutional Head</span></td>
              <td class="px-4">Ex-Officio</td>
            </tr>
            <tr>
              <td class="px-4 fw-bold">Teacher Representative (Secondary)</td>
              <td class="px-4">[Nominated Senior Assistant Teacher]</td>
              <td class="px-4"><span class="badge bg-secondary-subtle text-secondary">Teaching Faculty</span></td>
              <td class="px-4">Active Term</td>
            </tr>
            <tr>
              <td class="px-4 fw-bold">Teacher Representative (+2 Wing)</td>
              <td class="px-4">[Nominated Faculty Member / PGT]</td>
              <td class="px-4"><span class="badge bg-secondary-subtle text-secondary">Teaching Faculty</span></td>
              <td class="px-4">Active Term</td>
            </tr>
            <tr>
              <td class="px-4 fw-bold">Parent Representative (Mother)</td>
              <td class="px-4">[Nominated Female Parent Member]</td>
              <td class="px-4"><span class="badge bg-primary-subtle text-primary">Parent Category (Female)</span></td>
              <td class="px-4">Active Term</td>
            </tr>
            <tr>
              <td class="px-4 fw-bold">Parent Representative (Father)</td>
              <td class="px-4">[Nominated Male Parent Member]</td>
              <td class="px-4"><span class="badge bg-primary-subtle text-primary">Parent Category (Male)</span></td>
              <td class="px-4">Active Term</td>
            </tr>
            <tr>
              <td class="px-4 fw-bold">Local Panchayat Representative</td>
              <td class="px-4">[Elected Ward Member / Mukhiya Nominee - Haldipokhar]</td>
              <td class="px-4"><span class="badge bg-warning-subtle text-dark">Local Self-Government</span></td>
              <td class="px-4">Active Term</td>
            </tr>
            <tr>
              <td class="px-4 fw-bold">Educationist / Social Worker</td>
              <td class="px-4">[Local Educationist - Committee Nominee]</td>
              <td class="px-4"><span class="badge bg-info-subtle text-dark">Civil Society</span></td>
              <td class="px-4">Active Term</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="official-notice-box mt-4">
        <i class="bi bi-exclamation-triangle-fill me-2"></i>
        <strong>Official Compliance Notice:</strong> In compliance with official school governance standards, the above roster reflects statutory positions under the RTE framework. Specific member names and tenure details are updated following official administrative notifications from the District Education Office, East Singhbhum.
      </div>
    </div>
  </div>
</section>
"""

save_page("smc-members.html", get_page_template(
    "SMC Members", 
    "Governance & Committee", 
    "School Management Committee (SMC) details, membership structure, and community governance framework of +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय.",
    "about",
    "<li><a href='about-school.html'>About Us</a></li>",
    smc_content
))

# ==============================================================================
# 5. ACADEMIC OVERVIEW (pages/academic-overview.html)
# ==============================================================================
academic_content = """
<section class="py-5 bg-white">
  <div class="container">
    <div class="row align-items-center g-5 mb-5 reveal-on-scroll">
      <div class="col-lg-6">
        <span class="section-label-green">EDUCATIONAL PATHWAY</span>
        <h2 class="editorial-headline">Curriculum Excellence Affiliated with JAC, Ranchi</h2>
        <p class="editorial-lead-text">
          +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय offers structured academic programs spanning Secondary Education (Classes 9 &amp; 10) through Higher Secondary (+2 Classes 11 &amp; 12) across Science, Arts, and Commerce disciplines.
        </p>
        <p style="color:var(--body-text); line-height:1.75;">
          Our academic framework follows the prescribed curriculum of the Jharkhand Academic Council (JAC), Ranchi, combined with NCERT standards. We place special focus on conceptual foundations, bilingual instruction (Hindi &amp; English), continuous formative evaluations, and comprehensive laboratory practicals.
        </p>
      </div>
      <div class="col-lg-6">
        <div class="editorial-image-frame">
          <img src="../assets/img/students/students-excellence.svg" alt="Students Academic Excellence">
        </div>
      </div>
    </div>

    <!-- Programs Grid -->
    <div class="row g-4 mb-5 reveal-on-scroll">
      <div class="col-md-6">
        <div class="p-4 p-lg-5 bg-light rounded-4 border h-100">
          <span class="badge bg-success-subtle text-success px-3 py-1 rounded-pill mb-2 font-monospace">STAGE I</span>
          <h3 style="font-size:1.6rem; font-weight:800; color:var(--deep-forest-green); margin-bottom:1rem;">Secondary Wing (Classes IX &amp; X)</h3>
          <p style="color:var(--body-text); line-height:1.7;">
            Designed to build solid fundamental competencies in languages, mathematics, composite sciences, and social sciences, culminating in the JAC Secondary Board Examination (Matriculation).
          </p>
          <ul class="list-unstyled d-flex flex-column gap-2 mt-3" style="font-size:0.9rem; color:var(--body-text);">
            <li><i class="bi bi-check2 text-success me-2"></i> Robust foundations in algebra, geometry, physics, chemistry &amp; biology.</li>
            <li><i class="bi bi-check2 text-success me-2"></i> Dual language proficiency: Hindi, English, and Sanskrit.</li>
            <li><i class="bi bi-check2 text-success me-2"></i> Social sciences covering Indian history, geography, civics, and economics.</li>
          </ul>
        </div>
      </div>

      <div class="col-md-6">
        <div class="p-4 p-lg-5 bg-light rounded-4 border h-100">
          <span class="badge bg-success-subtle text-success px-3 py-1 rounded-pill mb-2 font-monospace">STAGE II</span>
          <h3 style="font-size:1.6rem; font-weight:800; color:var(--deep-forest-green); margin-bottom:1rem;">Higher Secondary (+2 Classes XI &amp; XII)</h3>
          <p style="color:var(--body-text); line-height:1.7;">
            Streamlined specialization tailored for higher educational entrance exams, university admissions, and vocational excellence in Science, Arts, and Commerce streams.
          </p>
          <ul class="list-unstyled d-flex flex-column gap-2 mt-3" style="font-size:0.9rem; color:var(--body-text);">
            <li><i class="bi bi-check2 text-success me-2"></i> <strong>Science:</strong> Physics, Chemistry, Mathematics, Biology, Computer Science.</li>
            <li><i class="bi bi-check2 text-success me-2"></i> <strong>Arts:</strong> History, Political Science, Geography, Economics, Literature.</li>
            <li><i class="bi bi-check2 text-success me-2"></i> <strong>Commerce:</strong> Accountancy, Business Studies, Commercial Math, Economics.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Pedagogy & Methodology -->
    <div class="p-4 p-lg-5 rounded-4 text-white reveal-on-scroll" style="background:var(--deep-forest-green);">
      <div class="row g-4 align-items-center">
        <div class="col-lg-8">
          <span class="badge bg-warning text-dark px-3 py-1 rounded-pill mb-2 fw-bold">TEACHING METHODOLOGY</span>
          <h3 style="font-size:2rem; font-weight:800; margin-bottom:1rem;">Interactive &amp; Experiential Pedagogy</h3>
          <p style="color:#D1E7DD; line-height:1.75; margin-bottom:0;">
            Our teachers combine traditional blackboard derivation with digital interactive screens, hands-on science lab sessions, group discussions, and peer mentoring. Weekly doubt-clearing sessions ensure no learner is left behind before term examinations.
          </p>
        </div>
        <div class="col-lg-4 text-center">
          <a href="classes-subjects.html" class="btn btn-warning rounded-pill px-4 py-3 fw-bold">
            <i class="bi bi-collection-fill me-1"></i> View Subject Combinations
          </a>
        </div>
      </div>
    </div>
  </div>
</section>
"""

save_page("academic-overview.html", get_page_template(
    "Academic Overview", 
    "Programs & Curriculum", 
    "Comprehensive academic overview, curriculum standards, and teaching methodologies of +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय.",
    "academic",
    "<li><a href='academic-overview.html'>Academic</a></li>",
    academic_content
))

print("Batch 1 generated successfully!")
