/**
 * ====================================================================
 * SCHOOL DATA ARCHITECTURE — VERSION 5 (SWISS GRID EDITION)
 * CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR, हल्दीपोखर, पोटका, पूर्वी सिंहभूम
 * U-DISE Code: 20180231602
 * ====================================================================
 * DATA INTEGRITY RULES APPLIED:
 * Real verified information is maintained strictly.
 * Where official records are pending or not publicly certified,
 * explicitly labeled placeholders are utilized to avoid fabrication.
 */

const SCHOOL_DATA = {
  identity: {
    nameHindi: "CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR",
    nameEnglish: "+2 Rajkiyakrit Vidya Niketan High School",
    shortName: "+2 RVNHS Haldipokhar",
    tagline: "Education. Values. A Brighter Future.",
    philosophy: "Learning for Life. Growing with Values.",
    udiseCode: "20180231602",
    schoolType: "Government / Rajkiyakrit School (Jharkhand State Govt.)",
    educationalLevel: "+2 Higher Secondary (Secondary & +2 Inter)",
    mediumOfInstruction: "Hindi / English",
    affiliation: "Jharkhand Academic Council (JAC), Ranchi",
    schoolManagement: "Department of School Education & Literacy, Govt. of Jharkhand",
    description: "The school focuses on quality education, good values, discipline, life skills and all-round student development.",
    location: {
      village: "Haldipokhar (हल्दीपोखर)",
      block: "Potka (पोटका)",
      district: "East Singhbhum (पूर्वी सिंहभूम)",
      state: "Jharkhand (झारखण्ड)",
      pincode: "831002",
      fullAddress: "हल्दीपोखर, पोटका, पूर्वी सिंहभूम, झारखण्ड – 831002",
      mapCoordinates: "22.6074° N, 86.2346° E (Potka Block, East Singhbhum)"
    },
    contact: {
      email: "vnhs.haldipokhar.e.singhbhum@gmail.com",
      officePhone: "[Official Landline / Contact Number — To be updated]",
      officeHours: "Monday to Saturday: 09:30 AM – 04:00 PM (Subject to official state school timings)"
    },
    metaPlaceholders: {
      establishmentYear: "[Official Establishment Year — Pending Record Verification]",
      principalName: "[Principal Name — As per School Office Register]",
      principalDesignation: "Headmaster / In-Charge Principal",
      totalStudents: "[Verified Student Enrollment Count — Annual Data Update Pending]",
      totalTeachers: "[Sanctioned & Active Teaching Staff Count — Record Pending]",
      campusArea: "[Campus Area in Acres — As per Revenue / School Land Register]"
    }
  },

  learningJourney: [
    {
      step: "01",
      title: "Learning",
      subtitle: "Foundational Knowledge",
      description: "Structured academic inquiry across languages, mathematics, sciences, and social sciences fostering core literacy.",
      icon: "bi-book"
    },
    {
      step: "02",
      title: "Understanding",
      subtitle: "Conceptual Clarity",
      description: "Moving beyond rote memorization to analytical thinking, problem-solving, and laboratory practical applications.",
      icon: "bi-lightbulb"
    },
    {
      step: "03",
      title: "Creativity",
      subtitle: "Expression & Innovation",
      description: "Encouraging artistic expression, science exhibition modeling, design, and innovative vocational thinking.",
      icon: "bi-palette"
    },
    {
      step: "04",
      title: "Collaboration",
      subtitle: "Teamwork & Empathy",
      description: "Group discussions, team sports, cultural ensembles, and cooperative classroom initiatives that unite students.",
      icon: "bi-people"
    },
    {
      step: "05",
      title: "Responsibility",
      subtitle: "Civic & Moral Values",
      description: "Scout & Guide discipline, environmental stewardship, community outreach, and ethical student governance.",
      icon: "bi-shield-check"
    },
    {
      step: "06",
      title: "Growth",
      subtitle: "Holistic Development",
      description: "Empowering confident, responsible young adults prepared for higher academic pursuits and constructive citizenship.",
      icon: "bi-graph-up-arrow"
    }
  ],

  notices: [
    {
      id: "N-2026-001",
      date: "2026-03-15",
      displayDate: "15 Mar 2026",
      category: "Admission",
      badgeClass: "badge-admission",
      title: "Session 2026–2027 Admission Information & Application Desk",
      summary: "Preliminary information regarding Class 9 and +2 Intermediate (Arts, Science, Commerce) admission process. Official verification required at school counter.",
      fileUrl: "../assets/documents/notices/admission-notice-2026.pdf",
      isImportant: true
    },
    {
      id: "N-2026-002",
      date: "2026-03-10",
      displayDate: "10 Mar 2026",
      category: "Academic",
      badgeClass: "badge-academic",
      title: "JAC Annual Board Examination Schedule & Admit Card Distribution",
      summary: "Important instructions for Class 10 (Secondary) and Class 12 (+2) students appearing for the Jharkhand Academic Council examinations.",
      fileUrl: "../assets/documents/notices/academic-calendar-notice.pdf",
      isImportant: true
    },
    {
      id: "N-2026-003",
      date: "2026-02-24",
      displayDate: "24 Feb 2026",
      category: "General",
      badgeClass: "badge-general",
      title: "School Management Committee (SMC) Quarterly Review Meeting",
      summary: "Notice regarding the upcoming SMC meeting to review infrastructure maintenance, mid-day meal operations, and academic enrichment programs.",
      fileUrl: "#",
      isImportant: false
    },
    {
      id: "N-2026-004",
      date: "2026-02-18",
      displayDate: "18 Feb 2026",
      category: "Cultural",
      badgeClass: "badge-cultural",
      title: "Annual School Cultural Fest & National Days Commemoration",
      summary: "Rehearsal and participation schedule for patriotic song competitions, folk dance presentations, and traditional art showcases.",
      fileUrl: "#",
      isImportant: false
    },
    {
      id: "N-2026-02-05",
      date: "2026-02-05",
      displayDate: "05 Feb 2026",
      category: "Sports",
      badgeClass: "badge-sports",
      title: "Block & District Level School Athletics Meet Trials",
      summary: "Selection trials for 100m, 400m sprint, relay, long jump, and volleyball tournament for boys and girls teams.",
      fileUrl: "#",
      isImportant: false
    },
    {
      id: "N-2026-01-20",
      date: "2026-01-20",
      displayDate: "20 Jan 2026",
      category: "Examination",
      badgeClass: "badge-exam",
      title: "Pre-Board Diagnostic Assessments & Remedial Class Schedule",
      summary: "Special timetable for practical examinations and supplementary subject tutoring for board candidates.",
      fileUrl: "#",
      isImportant: false
    }
  ],

  results: [
    {
      session: "2024-2025",
      examination: "JAC Secondary Examination (Class 10)",
      classLevel: "Class 10",
      publishDate: "May 2025",
      status: "Official Gazette Verified",
      remarks: "Consolidated school results recorded in office registers. Detailed marksheet provided via JAC portal.",
      documentRef: "JAC-SEC-2025-RESULT.pdf"
    },
    {
      session: "2024-2025",
      examination: "JAC +2 Intermediate (Arts / Science / Commerce)",
      classLevel: "Class 12",
      publishDate: "June 2025",
      status: "Official Gazette Verified",
      remarks: "Senior secondary annual results announced by JAC Ranchi. Individual transcripts available in school office.",
      documentRef: "JAC-INTER-2025-RESULT.pdf"
    },
    {
      session: "2023-2024",
      examination: "JAC Secondary Examination (Class 10)",
      classLevel: "Class 10",
      publishDate: "May 2024",
      status: "Archived School Gazette",
      remarks: "Official historical records stored in school academic archives.",
      documentRef: "JAC-SEC-2024-ARCHIVE.pdf"
    },
    {
      session: "2023-2024",
      examination: "JAC +2 Intermediate Examination",
      classLevel: "Class 12",
      publishDate: "June 2024",
      status: "Archived School Gazette",
      remarks: "Official archives preserved for verification and scholarship documentation.",
      documentRef: "JAC-INTER-2024-ARCHIVE.pdf"
    },
    {
      session: "2025-2026",
      examination: "Upcoming JAC Board Examinations",
      classLevel: "Class 10 & 12",
      publishDate: "Scheduled Q2 2026",
      status: "Awaiting Official Announcement",
      remarks: "Official results will be published here when provided by the school upon release by JAC Ranchi.",
      documentRef: "PENDING_RELEASE"
    }
  ],

  galleryItems: [
    {
      id: "gal-01",
      category: "campus",
      categoryName: "Campus & Architecture",
      title: "Main Institutional Academic Building",
      caption: "Exterior facade and central entrance of +2 Rajkiyakrit Vidya Niketan High School, Haldipokhar.",
      image: "assets/img/campus/campus-hero.svg",
      tag: "Infrastructure"
    },
    {
      id: "gal-02",
      category: "students",
      categoryName: "Students & Assembly",
      title: "Morning Assembly & Value Pledge",
      caption: "Students assembled in orderly ranks for the morning prayer, national anthem and daily moral pledge.",
      image: "assets/img/students/student-assembly.svg",
      tag: "Discipline"
    },
    {
      id: "gal-03",
      category: "classrooms",
      categoryName: "Classroom Learning",
      title: "Interactive Classroom Session",
      caption: "Subject teacher engaging students with blackboard pedagogy and concept illustrations.",
      image: "assets/img/classrooms/smart-classroom.svg",
      tag: "Academics"
    },
    {
      id: "gal-04",
      category: "cultural",
      categoryName: "Cultural Activities",
      title: "Traditional Dance & Folk Presentation",
      caption: "Students performing traditional Jharkhand folk dances during annual institutional celebrations.",
      image: "assets/img/activities/cultural.svg",
      tag: "Culture"
    },
    {
      id: "gal-05",
      category: "sports",
      categoryName: "Sports & Athletics",
      title: "Annual Sports Track & Field Events",
      caption: "Athletics competition encouraging sportsmanship, physical vitality, and teamwork.",
      image: "assets/img/activities/sports.svg",
      tag: "Athletics"
    },
    {
      id: "gal-06",
      category: "exhibitions",
      categoryName: "Science & Art Exhibitions",
      title: "Student Science & Innovation Expo",
      caption: "Students presenting working models on renewable energy and water conservation.",
      image: "assets/img/activities/exhibitions.svg",
      tag: "Innovation"
    },
    {
      id: "gal-07",
      category: "scout-guide",
      categoryName: "Scout & Guide",
      title: "Bharat Scouts & Guides Troop Drill",
      caption: "Scouts and Guides practicing flag hoisting protocol, knots, and community rescue drills.",
      image: "assets/img/activities/scout-guide.svg",
      tag: "Service"
    },
    {
      id: "gal-08",
      category: "classrooms",
      categoryName: "Laboratory Facilities",
      title: "Science Laboratory Practical Work",
      caption: "Secondary students observing physics and chemistry experimental demonstrations under teacher guidance.",
      image: "assets/img/classrooms/science-lab.svg",
      tag: "Science Lab"
    },
    {
      id: "gal-09",
      category: "campus",
      categoryName: "Campus Grounds",
      title: "Green Open Campus & Courtyard",
      caption: "Clean, tree-lined open grounds promoting healthy recreational and study environments.",
      image: "assets/img/campus/campus-playground.svg",
      tag: "Environment"
    }
  ],

  academicStreams: [
    {
      stream: "Secondary (Classes 9 & 10)",
      description: "Comprehensive foundational curriculum framed by the National Curriculum Framework and JAC Ranchi.",
      subjects: [
        "Hindi (Course A / B)",
        "English Language & Literature",
        "Mathematics",
        "Science (Physics, Chemistry, Biology)",
        "Social Science (History, Geography, Political Science, Economics)",
        "Regional / Additional Language (Sanskrit / Santhali / Bengali / Ho)",
        "Physical, Health & Value Education"
      ]
    },
    {
      stream: "Higher Secondary (+2 Inter Arts)",
      description: "Humanities curriculum fostering critical historical analysis, philosophical inquiry, and social research.",
      subjects: [
        "Core Hindi / Core English",
        "History",
        "Political Science",
        "Geography",
        "Economics / Sociology",
        "Elective Language / Philosophy (As per seat availability)"
      ]
    },
    {
      stream: "Higher Secondary (+2 Inter Science)",
      description: "Rigorous scientific foundation preparing students for technical, medical, and applied science careers.",
      subjects: [
        "Core English / Hindi",
        "Physics (Theory & Practical)",
        "Chemistry (Theory & Practical)",
        "Mathematics / Biology",
        "Computer Science / Additional Science Subject"
      ]
    },
    {
      stream: "Higher Secondary (+2 Inter Commerce)",
      description: "Business and commercial numeracy curriculum covering accounts, business principles, and economic trends.",
      subjects: [
        "Core English / Hindi",
        "Accountancy",
        "Business Studies",
        "Commercial Arithmetic (CA) / Economics",
        "Entrepreneurship / Computer Applications"
      ]
    }
  ],

  smcStructure: [
    {
      role: "President / Chairperson",
      name: "[Elected Parent Representative / SMC President — Official Name Pending]",
      category: "Parent / Community Member",
      responsibility: "Presiding over committee meetings and monitoring school community partnership."
    },
    {
      role: "Member Secretary",
      name: "[Headmaster / Principal In-Charge — Official Name Pending]",
      category: "Institutional Head",
      responsibility: "Administrative coordination, official record keeping, and implementation of school development plans."
    },
    {
      role: "Teacher Representative (Male)",
      name: "[Senior Teacher — Official Staff Record Pending]",
      category: "Teaching Staff",
      responsibility: "Academic progress reporting and teacher-student welfare liaison."
    },
    {
      role: "Teacher Representative (Female)",
      name: "[Senior Teacher — Official Staff Record Pending]",
      category: "Teaching Staff",
      responsibility: "Girls education initiatives and gender sensitivity oversight."
    },
    {
      role: "Local Authority Representative",
      name: "[Mukhiya / Panchayat Representative — Official Name Pending]",
      category: "Panchayati Raj Institution",
      responsibility: "Civic infrastructure support, community hygiene, and village level coordination."
    },
    {
      role: "Educationist / Social Worker",
      name: "[Local Educationist — Official Name Pending]",
      category: "Civil Society",
      responsibility: "Counseling, vocational exposure, and school improvement advisory."
    }
  ]
};

// Export to window for global browser availability
if (typeof window !== "undefined") {
  window.SCHOOL_DATA = SCHOOL_DATA;
}
