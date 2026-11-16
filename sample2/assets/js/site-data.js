/**
 * +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय, हल्दीपोखर
 * Centralized Site Data & Verified Information Repository
 * Version 4 — Cinematic Campus Storytelling Edition
 */

const SITE_DATA = {
  school: {
    nameHindi: "+2 राजकीयकृत विद्या निकेतन उच्च विद्यालय",
    nameEnglish: "+2 Rajkiyakrit Vidya Niketan Higher Secondary School",
    shortName: "Vidya Niketan Haldipokhar",
    location: "हल्दीपोखर, पोटका, पूर्वी सिंहभूम, झारखण्ड – 831002",
    locationShort: "Haldipokhar, Potka, East Singhbhum, Jharkhand",
    pincode: "831002",
    udise: "20180231602",
    email: "vnhs.haldipokhar.e.singhbhum@gmail.com",
    educationalLevel: "+2 Higher Secondary",
    affiliation: "Jharkhand Academic Council (JAC), Ranchi",
    managementType: "Government / Rajkiyakrit (+2)",
    establishmentYear: "[Year Pending Official Record]",
    principalName: "[Principal Name - Official Record Pending Verification]",
    principalDesignation: "Principal / In-Charge Headmaster",
    intro: "The school focuses on quality education, good values, discipline, life skills and the all-round development of students.",
    tagline: "Empowering Minds. Building Futures.",
    motto: "विद्या ददाति विनयं (Knowledge Imparts Humility & Wisdom)"
  },

  principles: [
    {
      number: "01",
      title: "Quality Education",
      desc: "Structured curriculum delivery aligned with state educational standards, interactive teaching pedagogies and concept clarity."
    },
    {
      number: "02",
      title: "Good Values & Discipline",
      desc: "Character development, moral integrity, mutual respect and civic responsibility fostered through daily morning assemblies and guidance."
    },
    {
      number: "03",
      title: "Holistic Development",
      desc: "Balanced emphasis on co-curricular pursuits, physical fitness, creative arts, scientific inquiry, scout & guide and vocational skills."
    }
  ],

  valuesTimeline: [
    { number: "01", title: "Quality Education", desc: "Rigorous classroom pedagogy, comprehensive curriculum coverage, and continuous formative assessment." },
    { number: "02", title: "Discipline", desc: "Punctuality, respectful conduct, structured campus routine, and adherence to institutional ethics." },
    { number: "03", title: "Creativity", desc: "Encouraging artistic expression, debate, literature, scientific curiosity, and innovative problem-solving." },
    { number: "04", title: "Responsibility", desc: "Civic consciousness, environmental care, community service, and accountability towards society." },
    { number: "05", title: "Practical Skills", desc: "Hands-on laboratory investigations, computer literacy, vocational competencies, and applied learning." },
    { number: "06", title: "Student Development", desc: "Nurturing emotional resilience, physical endurance, leadership qualities, and future readiness." }
  ],

  campusExperience: [
    {
      id: "cultural",
      title: "Cultural Activities",
      category: "Creative Arts",
      summary: "Annual celebrations, traditional folk dances of Jharkhand, music, drama and speech festivals celebrating rich heritage.",
      image: "cultural/cultural-annual-day.svg",
      link: "pages/cultural-activities.html"
    },
    {
      id: "sports",
      title: "Sports Activities",
      category: "Physical Fitness",
      summary: "Track & field athletics, football, volleyball, yoga and inter-house matches instilling teamwork and sporting spirit.",
      image: "sports/sports-track-field.svg",
      link: "pages/sports-activities.html"
    },
    {
      id: "exhibitions",
      title: "Science & Educational Exhibitions",
      category: "Inquiry & Science",
      summary: "Student-crafted working models, environmental displays, innovative engineering prototypes and math expositions.",
      image: "exhibitions/science-exhibition-models.svg",
      link: "pages/exhibitions.html"
    },
    {
      id: "scout-guide",
      title: "Bharat Scouts & Guides",
      category: "Character & Service",
      summary: "Pioneering, camping, discipline, emergency aid and community social outreach cultivating exemplary youth citizenship.",
      image: "gallery/gallery-scout-1.svg",
      link: "pages/scout-guide.html"
    },
    {
      id: "vocational",
      title: "Vocational Activities",
      category: "Career & Life Skills",
      summary: "Applied training, basic technology skills, craftwork and workplace readiness aligned with holistic learning goals.",
      image: "exhibitions/skills-workshop.svg",
      link: "pages/vocational-activities.html"
    }
  ],

  notices: [
    {
      id: 1,
      category: "Academic",
      title: "Commencement of Secondary & Higher Secondary Periodic Assessments",
      date: "12 Nov 2026",
      summary: "Students of Classes 9 to 12 are notified regarding the upcoming periodic unit assessments. Syllabus details are displayed on classroom notice boards.",
      status: "Active",
      fileUrl: "#"
    },
    {
      id: 2,
      category: "Examination",
      title: "JAC Board Examination Form Filling & Verification Schedule [Sample Notice]",
      date: "08 Nov 2026",
      summary: "Sample instructional notice for Class 10 and Class 12 registration verification. Official dates are subject to Jharkhand Academic Council notifications.",
      status: "Notice",
      fileUrl: "#"
    },
    {
      id: 3,
      category: "Cultural",
      title: "Auditions for Annual Cultural Meet & Folk Arts Showcase",
      date: "04 Nov 2026",
      summary: "Interested students from all houses may register with their respective house mentors for folk dance, drama, and vocal music auditions.",
      status: "Registration Open",
      fileUrl: "#"
    },
    {
      id: 4,
      category: "Sports",
      title: "Annual Athletic Trials for Track and Field Events",
      date: "28 Oct 2026",
      summary: "Selection trials for 100m, 200m sprint, long jump, and volleyball will be held on the school sports ground under the physical training instructor.",
      status: "Completed",
      fileUrl: "#"
    },
    {
      id: 5,
      category: "Admission",
      title: "+2 Higher Secondary Stream Guidance & Advisory Desk",
      date: "20 Oct 2026",
      summary: "Information regarding subject combination choices across Arts, Science and Commerce streams for prospective higher secondary entrants.",
      status: "Advisory",
      fileUrl: "#"
    },
    {
      id: 6,
      category: "General",
      title: "SMC Quarterly Meeting on Campus Development & Student Welfare",
      date: "15 Oct 2026",
      summary: "School Management Committee conference convened to review infrastructure development, eco-park maintenance, and academic performance.",
      status: "Minutes Recorded",
      fileUrl: "#"
    }
  ],

  resultsSample: [
    {
      id: "RES-10-2025",
      exam: "JAC Secondary (Class X) Annual Examination",
      session: "2024 - 2025",
      classGrade: "Class 10",
      publishedDate: "[Official Archive]",
      type: "Official Gazette Placeholder",
      note: "Official individual marks-sheets are distributed via the school administrative desk upon JAC Ranchi notification."
    },
    {
      id: "RES-12-2025-SCI",
      exam: "JAC Higher Secondary (Class XII) Science Stream",
      session: "2024 - 2025",
      classGrade: "Class 12 (Science)",
      publishedDate: "[Official Archive]",
      type: "Official Gazette Placeholder",
      note: "Verified institutional result gazette on file in the administrative archive."
    },
    {
      id: "RES-12-2025-ART",
      exam: "JAC Higher Secondary (Class XII) Arts Stream",
      session: "2024 - 2025",
      classGrade: "Class 12 (Arts)",
      publishedDate: "[Official Archive]",
      type: "Official Gazette Placeholder",
      note: "Verified institutional result gazette on file in the administrative archive."
    },
    {
      id: "RES-12-2025-COM",
      exam: "JAC Higher Secondary (Class XII) Commerce Stream",
      session: "2024 - 2025",
      classGrade: "Class 12 (Commerce)",
      publishedDate: "[Official Archive]",
      type: "Official Gazette Placeholder",
      note: "Verified institutional result gazette on file in the administrative archive."
    }
  ],

  smcMembers: [
    { role: "President", name: "[Elected Community Representative - Verified Record Pending]", category: "Community / Parent", tenure: "Active Committee" },
    { role: "Member Secretary", name: "[Principal / Headmaster - Ex-Officio]", category: "Institutional Head", tenure: "Ex-Officio" },
    { role: "Teacher Representative (Secondary)", name: "[Senior Teacher - Nominated]", category: "Teaching Staff", tenure: "Active Committee" },
    { role: "Teacher Representative (+2 Wing)", name: "[PGT / Faculty - Nominated]", category: "Teaching Staff", tenure: "Active Committee" },
    { role: "Parent Member (Female)", name: "[Parent Representative - Nominated]", category: "Parent Category", tenure: "Active Committee" },
    { role: "Parent Member (Male)", name: "[Parent Representative - Nominated]", category: "Parent Category", tenure: "Active Committee" },
    { role: "Panchayat / Local Representative", name: "[Local Ward Member / Mukhiya Nominee]", category: "Local Governance", tenure: "Active Committee" },
    { role: "Educationist / Social Worker", name: "[Local Educationist - Nominated]", category: "Special Invitee", tenure: "Active Committee" }
  ],

  academicStreams: [
    {
      stream: "Higher Secondary Science (+2)",
      description: "Rigorous scientific foundation for aspiring engineers, healthcare professionals, and research scholars.",
      compulsory: ["Core Hindi / English", "Physics", "Chemistry"],
      optional: ["Mathematics", "Biology", "Computer Science / Economics"]
    },
    {
      stream: "Higher Secondary Arts / Humanities (+2)",
      description: "In-depth understanding of history, governance, human behavior, languages and societal structures.",
      compulsory: ["Core Hindi / English", "History", "Political Science"],
      optional: ["Geography", "Economics", "Sociology / Philosophy"]
    },
    {
      stream: "Higher Secondary Commerce (+2)",
      description: "Comprehensive curriculum in financial accounting, business dynamics, trade, and economic principles.",
      compulsory: ["Core Hindi / English", "Accountancy", "Business Studies"],
      optional: ["Economics", "Commercial Mathematics", "Entrepreneurship"]
    },
    {
      stream: "Secondary Wing (Classes 9 & 10)",
      description: "State-prescribed core curriculum developing conceptual mastery across languages and sciences.",
      compulsory: ["Hindi", "English", "Sanskrit / Regional Language", "Mathematics", "Science", "Social Science"],
      optional: ["Physical Education", "Information Technology", "Vocational Studies"]
    }
  ],

  galleryData: [
    { id: 1, category: "campus", title: "Main Academic Complex", desc: "Front architectural view of the multi-story academic building.", file: "campus/campus-main-facade.svg" },
    { id: 2, category: "campus", title: "Panoramic Campus Landscape", desc: "Aerial perspective showcasing the open grounds and surrounding greenery.", file: "campus/campus-aerial-view.svg" },
    { id: 3, category: "campus", title: "Botanical Courtyard & Eco Park", desc: "Courtyard gardens cultivating student appreciation for nature.", file: "campus/campus-garden-courtyard.svg" },
    { id: 4, category: "classrooms", title: "Smart Digital ICT Classroom", desc: "Audio-visual interactive screen technology enhancing everyday learning.", file: "classrooms/smart-classroom.svg" },
    { id: 5, category: "classrooms", title: "Composite Science Laboratory", desc: "Equipped workstations for physics, chemistry and biology experiments.", file: "classrooms/science-laboratory.svg" },
    { id: 6, category: "classrooms", title: "Institutional Library & Reading Hall", desc: "Quiet study spaces stocked with textbooks, journals and reference volumes.", file: "classrooms/library-reading.svg" },
    { id: 7, category: "students", title: "Collaborative Study Circles", desc: "Higher secondary students engaged in structured peer group discussions.", file: "students/students-discussion.svg" },
    { id: 8, category: "students", title: "Morning Assembly & Value Education", desc: "Daily assembly cultivating discipline, national unity and mutual respect.", file: "students/students-assembly.svg" },
    { id: 9, category: "students", title: "Student Excellence & Guidance", desc: "Faculty mentoring learners for state board examinations and competitive goals.", file: "students/students-excellence.svg" },
    { id: 10, category: "cultural", title: "Annual Cultural Day Performances", desc: "Music, classical dance and theatrical presentations on school stage.", file: "cultural/cultural-annual-day.svg" },
    { id: 11, category: "cultural", title: "Jharkhand Folk Dance Heritage", desc: "Celebrating vibrant indigenous culture, Chhau and traditional folk arts.", file: "cultural/cultural-folk-dance.svg" },
    { id: 12, category: "sports", title: "Annual Athletics & Track Races", desc: "100-meter sprint, relay races and field events on the school track.", file: "sports/sports-track-field.svg" },
    { id: 13, category: "sports", title: "Football & Team Sports Arena", desc: "Regular sports coaching fostering athletic fitness and team spirit.", file: "sports/sports-football-ground.svg" },
    { id: 14, category: "exhibitions", title: "Science & Innovation Model Fair", desc: "Working demonstrations in solar energy, hydraulic robotics and eco-solutions.", file: "exhibitions/science-exhibition-models.svg" },
    { id: 15, category: "exhibitions", title: "Vocational Skills & Craft Workshop", desc: "Applied technical skills, handicraft creations and practical ingenuity.", file: "exhibitions/skills-workshop.svg" },
    { id: 16, category: "scout", title: "Bharat Scouts & Guides Camp Training", desc: "Pioneering knots, first aid, flag protocol and outdoor survival practice.", file: "gallery/gallery-scout-1.svg" }
  ]
};

// Freeze object to protect integrity
Object.freeze(SITE_DATA);
