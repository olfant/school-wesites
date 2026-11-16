# CM SOE UPG GOVT +2 SCHOOL VNIKETAN HALDIPOKHAR
## Premium Modern Multi-Page Government School Website

---

### Official Institution Details
- **Official Display Name:** CM SOE UPG GOVT +2 SCHOOL VNIKETAN HALDIPOKHAR
- **Short Branding:** CM SOE VNIKETAN HALDIPOKHAR
- **Institution Category:** Upgraded Government +2 School (Higher Secondary)
- **Affiliation / Status:** Government School of Excellence (SOE), Dept. of School Education and Literacy, Govt. of Jharkhand
- **Location:** Vniketan Haldipokhar, Potka Block, East Singhbhum District, Jharkhand, India - PIN: [Official Verification Pending / 831002 Placeholder]
- **Website Tagline:** *"Learn Today, Lead Tomorrow."*
- **Supporting Tagline:** *"Building Knowledge, Character and a Brighter Future."*

---

## 1. Project Overview & Architecture
This project is a complete, multi-page, responsive, and accessible educational institution website built strictly with standard web technologies (**HTML5, CSS3, ES6+ JavaScript, Bootstrap 5.3.3, and Bootstrap Icons**). It contains no proprietary framework dependencies (no React, Vue, Angular, or Next.js), ensuring exceptional performance, universal device support, and seamless offline deployment.

### Emerald Green Color System
| Token Name | Hex Code | Primary Role |
| :--- | :--- | :--- |
| **Primary Green** | `#087F50` | Primary brand color, key buttons, and accents |
| **Dark Green** | `#075B3B` | Section banners, headers, and secondary UI |
| **Forest Green** | `#064E36` | Navigation bar, page headers, and footer |
| **Light Green** | `#E8F5EC` | Background cards, pills, and highlighted sections |
| **Lime Accent** | `#A3D977` | Accent badges, borders, icons, and status flags |
| **White** | `#FFFFFF` | Card surfaces, container backgrounds, text contrast |
| **Page Background**| `#F7FAF7` | Base body background |
| **Main Text** | `#17251D` | High-contrast readable typography |
| **Muted Text** | `#68776D` | Subtitles and meta details |
| **Border Color** | `#E1EAE3` | Subtle card outlines and dividers |

---

## 2. Complete 13 HTML Pages Directory

| Page File | Title | Primary Content & Components |
| :--- | :--- | :--- |
| `index.html` | Homepage | Top info bar, sticky header, hero section with stats counters, notice board, about excerpt, mission/vision/values, academic highlights, facility previews, Principal's message, events, photo gallery preview, downloads, and contact helpdesk. |
| `about-school.html` | About Our School | Comprehensive history, School of Excellence framework, educational objectives, campus environment, and institutional parameters. |
| `principal.html` | Principal's Desk | Formal address, educational philosophy, triad of student growth (Knowledge, Character, Leadership), and appointment contact desk. |
| `awards.html` | Awards & Achievements | State government School of Excellence accreditation, academic board distinctions, district science fair laurels, and milestones timeline. |
| `infrastructure.html` | School Infrastructure | All 12 confirmed facilities (School building, Classrooms, Smart classrooms, Computer lab, Physics lab, Chemistry lab, Biology lab, Library, Playground, RO Drinking water, Sanitation blocks, Sports kit) with interactive detail modals. |
| `academics.html` | Academics (+2) | Tiered curriculum (Secondary 9-10 and +2 Higher Secondary Science, Arts, Commerce), subject breakdown, CCE assessment protocols, and zero-fee welfare policy. |
| `curriculum.html` | Curriculum & Documents | NCERT/JCERT textbook framework, academic calendar, Transfer Certificate (TC) application format, self-affidavit, and Mandatory Public Disclosure (Appendix IX). |
| `faculty.html` | Faculty & Teachers | Academic leadership, Science faculty, Humanities & Commerce educators, Language teachers, Sports instructors, and non-teaching laboratory cadre. |
| `gallery.html` | Photo & Video Gallery | 12-item filterable responsive image grid (Campus, Classrooms, Science Labs, Sports, Cultural), interactive Lightbox with Next/Previous arrows, and video showcases. |
| `contact.html` | Contact Us & Directions | Physical address, official email, phone placeholders, interactive contact form with client-side validation, transit guidelines, and Google Maps embed. |
| `smc.html` | School Management (SMC)| Section 21 RTE Act mandate, 75% parent quota, 50% women representation, executive member directory, and community monitoring guidelines. |
| `events.html` | School Events | Upcoming and past events with interactive category filtering (Sports, Science exhibitions, Jharkhand Statehood Gala, National celebrations). |
| `notices.html` | Notice Board | Real-time bulletin board with keyword search input, category buttons, date flags, interactive notice reader modals, and PDF download buttons. |

---

## 3. Folder & File Structure

```
CM-SOE-VNIKETAN-WEBSITE/
│
├── index.html                   # Page 01: Homepage
├── about-school.html            # Page 02: About Our School
├── principal.html               # Page 03: Principal's Desk
├── awards.html                  # Page 04: Awards and Achievements
├── infrastructure.html          # Page 05: School Infrastructure
├── academics.html               # Page 06: Academics & Streams
├── curriculum.html              # Page 07: Curriculum and Learning
├── faculty.html                 # Page 08: Teachers & Faculty
├── gallery.html                 # Page 09: Photo and Video Gallery
├── contact.html                 # Page 10: Contact Us
├── smc.html                     # Page 11: School Management Committee
├── events.html                  # Page 12: School Events
├── notices.html                 # Page 13: Notice Board & Circulars
│
├── .media/                      # Original media archive
│   ├── school-logo.svg
│   ├── school-building.svg
│   ├── school-campus.svg
│   ├── school-entrance.svg
│   ├── principal.svg
│   ├── classroom.svg
│   ├── computer-lab.svg
│   ├── science-lab.svg
│   ├── library.svg
│   └── playground.svg
│
├── assets/
│   ├── css/
│   │   ├── style.css            # Core design tokens, components & layout
│   │   ├── responsive.css       # Mobile-first breakpoints (1400, 1200, 992, 768, 576, 375px)
│   │   └── animations.css       # Keyframes, hover lifts, and IntersectionObserver reveals
│   │
│   ├── js/
│   │   ├── main.js              # Back-to-top, copyright year, tooltips, downloads
│   │   ├── navigation.js        # Mobile offcanvas drawer, active link highlighter, sticky header
│   │   ├── gallery.js           # Category filter & Lightbox modal with keyboard controls
│   │   ├── animations.js        # Scroll-reveal transitions & numeric counters
│   │   └── forms.js             # Form validation, live notice search & event filter
│   │
│   ├── img/
│   │   ├── logo/
│   │   │   └── school-logo.svg  # Official school vector crest
│   │   ├── hero/
│   │   │   └── school-campus.svg# Hero banner illustration
│   │   ├── facilities/          # High-resolution SVGs for all 12 facilities
│   │   ├── faculty/             # Faculty silhouettes & profile badges
│   │   ├── events/              # Event visual illustrations
│   │   └── gallery/             # 12 distinct campus & student activity illustrations
│   │
│   └── docs/                    # Real sample downloadable PDF documents
│       ├── academic-calendar-2026-27.pdf
│       ├── admission-guidelines.pdf
│       ├── holiday-list-2026.pdf
│       ├── fee-structure-declaration.pdf
│       ├── mandatory-public-disclosure.pdf
│       ├── transfer-certificate-format.pdf
│       ├── self-affidavit-document.pdf
│       └── annual-school-report.pdf
│
└── README.md                    # Technical documentation
```

---

## 4. Key Interactive Features
1. **Responsive Mobile Navigation:**
   - Slide-in offcanvas drawer on devices under `992px`.
   - Backdrop overlay, escape-key accessibility, and focus trapping.
   - Dynamic active link highlighter based on current page URL.

2. **Live Notice Board Search & Category Filtering:**
   - Real-time client-side search filtering notices by title or content.
   - Category filter pills (*Admissions, Examinations, Academic, Holidays*).
   - Interactive modal popups to read full circular text.

3. **Interactive Image Lightbox:**
   - Category filtering across 12 gallery cards.
   - Modal popup supporting Next / Previous image navigation.
   - Keyboard arrow keys (`Left`, `Right`) and `Escape` key controls.

4. **Client-Side Form Validation:**
   - Validates name length, email regex, 10-digit Indian phone number, subject selection, and message body.
   - Displays clear contextual error messages.
   - Triggers an institutional acknowledgement dialog upon valid submission.

5. **Direct Sample Document Downloads:**
   - All download buttons link directly to valid sample PDF files inside `assets/docs/`.
   - Prevents dead links or 404 errors during inspections.

6. **Accessibility & Performance:**
   - Semantic HTML5 tags (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`).
   - High color contrast ratio meeting WCAG 2.1 AA standards.
   - Respects user accessibility preferences (`@media (prefers-reduced-motion: reduce)`).

---

## 5. How to Run Locally

### Option A: Direct Browser Preview
Double-click `index.html` or open any `.html` file directly in Google Chrome, Microsoft Edge, Mozilla Firefox, or Safari.

### Option B: Local HTTP Server (Python)
```bash
cd D:\CM-SOE-VNIKETAN-WEBSITE
python -m http.server 8000
```
Open your browser at `http://localhost:8000`.

### Option C: Node.js / VS Code Live Server
Right-click `index.html` in VS Code and select **"Open with Live Server"**.

---

## 6. Official Data Verification Guidelines
- **UDISE Code, School Code & Affiliation:** Marked with clear editable placeholders (`[Official Verification Pending]`). When officially certified details are released, update them directly in `index.html`, `about-school.html`, and `curriculum.html`.
- **Faculty Names & Contact Details:** Standardized designations and placeholders are preserved to comply with official privacy mandates.
- **Replacing Imagery:** Original school photographs can be dropped into `assets/img/facilities/`, `assets/img/faculty/`, and `assets/img/gallery/` with matching file names, or updated directly in the HTML `src` attributes.
