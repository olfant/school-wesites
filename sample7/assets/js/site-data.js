/**
 * Official School Website Data Source
 * CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR
 * U-DISE Code: 20180231602
 * Location: हल्दीपोखर, पोटका, पूर्वी सिंहभूम, झारखण्ड – 831002
 */

const SCHOOL_DATA = {
  name: "CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR",
  hindiLocation: "हल्दीपोखर, पोटका, पूर्वी सिंहभूम, झारखण्ड – 831002",
  udiseCode: "20180231602",
  email: "vnhs.haldipokhar.e.singhbhum@gmail.com",
  level: "+2 Higher Secondary",
  focus: [
    "Quality Education",
    "Good Values",
    "Discipline",
    "Life Skills",
    "All-round Student Development"
  ],
  activities: [
    "Academic Programs",
    "Cultural Activities",
    "Sports Activities",
    "Scout & Guide",
    "Exhibitions",
    "Skills Competition",
    "Vocational Activities"
  ],

  // Core Values
  values: [
    {
      title: "Knowledge",
      icon: "bi-book-half",
      desc: "Comprehensive academic learning fostering analytical inquiry, problem-solving, and a lifelong thirst for understanding.",
      badge: "Academic Base"
    },
    {
      title: "Discipline",
      icon: "bi-shield-check",
      desc: "Cultivating punctuality, self-restraint, respect for rules, and personal integrity in every classroom and playing field.",
      badge: "Moral Pillar"
    },
    {
      title: "Creativity",
      icon: "bi-palette2",
      desc: "Encouraging original thinking, fine arts, scientific invention, and innovative expression across school events.",
      badge: "Innovation"
    },
    {
      title: "Responsibility",
      icon: "bi-people-fill",
      desc: "Instilling environmental awareness, community stewardship, empathy, and citizenship towards society and nation.",
      badge: "Social Care"
    }
  ],

  // Student Journey Stages
  journeyStages: [
    {
      step: "01",
      title: "Discover",
      desc: "Igniting curiosity through guided exploration, diagnostic assessments, and an introduction to core scientific and cultural concepts.",
      icon: "bi-compass"
    },
    {
      step: "02",
      title: "Learn",
      desc: "Active participation in foundational curricula, structured textbook lessons, and daily interactive teacher guidance.",
      icon: "bi-mortarboard"
    },
    {
      step: "03",
      title: "Understand",
      desc: "Deep conceptual comprehension developed through science experiments, group exercises, and practical problem discussions.",
      icon: "bi-lightbulb"
    },
    {
      step: "04",
      title: "Create",
      desc: "Applying classroom learning into original projects, scientific models, art crafts, essays, and regional innovation fairs.",
      icon: "bi-gear-wide-connected"
    },
    {
      step: "05",
      title: "Collaborate",
      desc: "Developing teamwork, leadership, empathy, and camaraderie via sports, Scout & Guide rallies, and cultural dramas.",
      icon: "bi-diagram-3"
    },
    {
      step: "06",
      title: "Grow",
      desc: "Maturing into resilient, morally upright, academically prepared youth ready for higher college education and nation-building.",
      icon: "bi-trophy"
    }
  ],

  // Notices Data
  notices: [
    {
      id: "NTC-01",
      date: "2026-11-15",
      displayDate: "15 Nov 2026",
      category: "Academic",
      title: "Sample Notice: Preparation Guidelines for Upcoming Term Assessments",
      desc: "Students of Classes 9 through 12 are advised to review updated subject syllabi and sample question patterns available in the academic wing.",
      tag: "Latest",
      isSample: true
    },
    {
      id: "NTC-02",
      date: "2026-11-10",
      displayDate: "10 Nov 2026",
      category: "General",
      title: "Sample Notice: Annual Parent-Teacher Interaction & Review Session",
      desc: "Scheduled consultative meeting with parents and guardians to discuss individual student learning progress, attendance, and moral development.",
      tag: "Important",
      isSample: true
    },
    {
      id: "NTC-03",
      date: "2026-11-04",
      displayDate: "04 Nov 2026",
      category: "Sports",
      title: "Sample Notice: Annual Inter-House Athletics & Football Trials",
      desc: "House trials for track events, relay sprints, volleyball, and football. Interested students must submit medical fitness confirmations.",
      tag: "Events",
      isSample: true
    },
    {
      id: "NTC-04",
      date: "2026-10-28",
      displayDate: "28 Oct 2026",
      category: "Cultural",
      title: "Sample Notice: Auditions for Republic & State Foundation Day Cultural Tableau",
      desc: "Auditions for traditional folk dance, tribal music instruments (Mandhar, Nagada), and historical skit presentations are commencing shortly.",
      tag: "Culture",
      isSample: true
    },
    {
      id: "NTC-05",
      date: "2026-10-20",
      displayDate: "20 Oct 2026",
      category: "Examination",
      title: "Sample Notice: JAC Board Registration Verification for +2 Higher Secondary",
      desc: "Senior secondary candidates (+2 Arts, Science, Commerce) are directed to cross-verify registered personal details on JAC verification drafts.",
      tag: "Academic",
      isSample: true
    },
    {
      id: "NTC-06",
      date: "2026-10-12",
      displayDate: "12 Oct 2026",
      category: "Admission",
      title: "Sample Notice: Illustrative Information Regarding Intermediate (+2) Admission Cycle",
      desc: "Descriptive procedural notice detailing documentation requirements and counseling steps for incoming secondary pass-outs.",
      tag: "Notice",
      isSample: true
    }
  ],

  // Examination Results Placeholders
  resultsData: [
    {
      session: "2024-2025",
      exam: "JAC +2 Annual Board Examination",
      cls: "Class 12 (Arts/Science/Commerce)",
      status: "Official Record Pending Verification",
      docLink: "assets/documents/results/official_results_placeholder.txt",
      verified: false
    },
    {
      session: "2024-2025",
      exam: "Secondary Annual Examination (Class 10)",
      cls: "Class 10 (Secondary)",
      status: "Official Record Pending Verification",
      docLink: "assets/documents/results/official_results_placeholder.txt",
      verified: false
    },
    {
      session: "2023-2024",
      exam: "JAC +2 Annual Board Examination",
      cls: "Class 12 (Arts/Science/Commerce)",
      status: "Archived Gazette in Administrative Office",
      docLink: "assets/documents/results/official_results_placeholder.txt",
      verified: false
    },
    {
      session: "2023-2024",
      exam: "Secondary Annual Examination (Class 10)",
      cls: "Class 10 (Secondary)",
      status: "Archived Gazette in Administrative Office",
      docLink: "assets/documents/results/official_results_placeholder.txt",
      verified: false
    }
  ],

  // Gallery Photos
  gallery: [
    {
      id: 1,
      title: "Campus Green Quadrangle",
      category: "campus",
      src: "assets/img/gallery/gallery-1.svg",
      caption: "Spacious and green school campus quadrangle at Haldipokhar, Potka."
    },
    {
      id: 2,
      title: "High School Science Laboratory",
      category: "classrooms",
      src: "assets/img/gallery/gallery-2.svg",
      caption: "Science lab supporting practical biology, chemistry, and physics experiments."
    },
    {
      id: 3,
      title: "Smart Interactive Classroom",
      category: "classrooms",
      src: "assets/img/gallery/gallery-3.svg",
      caption: "Digital instructional aids and interactive learning displays for higher secondary students."
    },
    {
      id: 4,
      title: "Annual Sports Track & Field",
      category: "sports",
      src: "assets/img/gallery/gallery-4.svg",
      caption: "Outdoor sports track and athletic field activities encouraging physical fitness."
    },
    {
      id: 5,
      title: "State Cultural Festival Folk Dance",
      category: "cultural",
      src: "assets/img/gallery/gallery-5.svg",
      caption: "Students performing traditional Jharkhandi folk dance and festive cultural programs."
    },
    {
      id: 6,
      title: "Bharat Scouts & Guides Camporee",
      category: "scout",
      src: "assets/img/gallery/gallery-6.svg",
      caption: "Discipline, leadership camps, tent pitching, and community service drills."
    },
    {
      id: 7,
      title: "Science & Eco Innovation Fair",
      category: "exhibitions",
      src: "assets/img/gallery/gallery-7.svg",
      caption: "Student-crafted working models on renewable energy and environmental conservation."
    },
    {
      id: 8,
      title: "School Central Library & Reading Room",
      category: "campus",
      src: "assets/img/gallery/gallery-8.svg",
      caption: "Dedicated reading space with reference books, literature, and educational journals."
    },
    {
      id: 9,
      title: "Plantation & Nature Conservation Drive",
      category: "campus",
      src: "assets/img/gallery/gallery-9.svg",
      caption: "Green plantation initiative on school grounds nurturing eco-friendly awareness."
    },
    {
      id: 10,
      title: "Computer & Digital Literacy Lab",
      category: "classrooms",
      src: "assets/img/gallery/gallery-10.svg",
      caption: "Hands-on computer training, digital skills, and cyber-safety education."
    },
    {
      id: 11,
      title: "Art, Craft & Skills Exhibition",
      category: "exhibitions",
      src: "assets/img/gallery/gallery-11.svg",
      caption: "Creative arts, handicraft models, painting, and regional craftsmanship display."
    },
    {
      id: 12,
      title: "Morning Assembly & Moral Education",
      category: "cultural",
      src: "assets/img/gallery/gallery-12.svg",
      caption: "Daily school assembly fostering collective harmony, national anthem, and moral reflection."
    }
  ],

  // SMC Committee Members (Strictly labelled placeholders)
  smcMembers: [
    { sn: 1, name: "[Principal / Headmaster Name]", designation: "Ex-Officio President / Member Secretary", category: "School Administration", contact: "Official School Office" },
    { sn: 2, name: "[Parent Representative Name 01]", designation: "Vice President", category: "Parent Community", contact: "—" },
    { sn: 3, name: "[Parent Representative Name 02]", designation: "Member", category: "Parent Community (Female)", contact: "—" },
    { sn: 4, name: "[Parent Representative Name 03]", designation: "Member", category: "Parent Community", contact: "—" },
    { sn: 5, name: "[Senior Teacher Representative]", designation: "Teacher Representative", category: "Teaching Faculty", contact: "—" },
    { sn: 6, name: "[Gram Panchayat / Local Body Nominee]", designation: "Member", category: "Local Self-Government", contact: "—" },
    { sn: 7, name: "[Educationist / Social Worker Nominee]", designation: "Member", category: "Eminent Educationist", contact: "—" },
    { sn: 8, name: "[SC / ST / OBC Community Nominee]", designation: "Member", category: "Community Representative", contact: "—" }
  ]
};

// Export to window
if (typeof window !== "undefined") {
  window.SCHOOL_DATA = SCHOOL_DATA;
}
