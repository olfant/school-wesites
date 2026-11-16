/**
 * +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय
 * Haldipokhar, Potka, East Singhbhum, Jharkhand – 831002
 * U-DISE Code: 20180231602
 *
 * Global Site Data & Demo Content Store
 * Strictly adheres to rule: No invented official records. All missing official data uses clearly labelled placeholders.
 */

const SchoolData = {
  info: {
    nameHindi: "+2 राजकीयकृत विद्या निकेतन उच्च विद्यालय",
    nameEnglish: "+2 Rajkiyakrit Vidya Niketan Higher Secondary School",
    subtitle: "+2 Higher Secondary School",
    locationHindi: "हल्दीपोखर, पोटका, पूर्वी सिंहभूम, झारखण्ड – 831002",
    locationEnglish: "Haldipokhar, Potka, East Singhbhum, Jharkhand – 831002",
    udise: "20180231602",
    email: "vnhs.haldipokhar.e.singhbhum@gmail.com",
    level: "+2 Higher Secondary (Secondary & Higher Secondary)",
    affiliation: "Jharkhand Academic Council (JAC), Ranchi",
    description: "The school focuses on providing quality education, good values, discipline, life skills and all-round student development.",
    principalPlaceholder: {
      name: "[Principal Name, M.A., B.Ed.]",
      designation: "Headmaster / Principal In-Charge",
      office: "Office of the Principal",
      messageSummary: "Welcome to our institution. Our collective mission is to instill character, scientific temper, and holistic education in every student hailing from Haldipokhar and surrounding regions.",
      messageFull: "Dear students, parents, and community members, Welcome to +2 Rajkiyakrit Vidya Niketan Higher Secondary School, Haldipokhar. We stand firmly dedicated to offering inclusive, value-driven, and empowering education. In addition to rigorous academic curricula aligned with the Jharkhand Academic Council, our focus encompasses community harmony, sportsmanship, environmental conservation, and practical skill development. We urge every student to seize every opportunity to learn, question, and grow with humility and discipline."
    },
    estdPlaceholder: "[Year of Establishment - Official School Record]",
    sessionCurrent: "2024–2025"
  },

  pillars: [
    {
      id: "01",
      title: "Quality Education",
      desc: "Structured syllabus, conceptual clarity, qualified subject educators, and regular academic reviews.",
      icon: "bi-mortarboard-fill",
      link: "academic-overview.html"
    },
    {
      id: "02",
      title: "Character & Values",
      desc: "Inculcating moral integrity, mutual respect, constitutional virtues, and lifelong civic responsibility.",
      icon: "bi-shield-check",
      link: "mission-vision.html"
    },
    {
      id: "03",
      title: "Practical Learning",
      desc: "Hands-on science demonstrations, ICT fundamentals, student exhibitions, and vocational training.",
      icon: "bi-tools",
      link: "teaching-learning.html"
    },
    {
      id: "04",
      title: "Student Development",
      desc: "Comprehensive growth through sports, cultural arts, Bharat Scouts & Guides, and debate clubs.",
      icon: "bi-person-bounding-box",
      link: "achievements.html"
    }
  ],

  campusLife: [
    {
      title: "Cultural Activities",
      subtitle: "Dance, Music, Drama & Heritage",
      image: "assets/img/activities/cultural.svg",
      link: "pages/cultural-activities.html",
      tag: "Tradition"
    },
    {
      title: "Sports Activities",
      subtitle: "Athletics, Football, Volleyball",
      image: "assets/img/activities/sports.svg",
      link: "pages/sports-activities.html",
      tag: "Athletics"
    },
    {
      title: "Science & Art Exhibitions",
      subtitle: "Working Models & Student Projects",
      image: "assets/img/activities/exhibitions.svg",
      link: "pages/exhibitions.html",
      tag: "Innovation"
    },
    {
      title: "Vocational Activities",
      subtitle: "Skill-Based Life Readiness",
      image: "assets/img/activities/vocational.svg",
      link: "pages/vocational-activities.html",
      tag: "Careers"
    },
    {
      title: "Scout & Guide",
      subtitle: "Discipline, Camp & Leadership",
      image: "assets/img/activities/scout-guide.svg",
      link: "pages/scout-guide.html",
      tag: "Service"
    },
    {
      title: "Skills Competition",
      subtitle: "Debates, Quizzes & Creativity",
      image: "assets/img/activities/skills.svg",
      link: "pages/skills-competition.html",
      tag: "Competence"
    }
  ],

  notices: [
    {
      id: 1,
      title: "Notice regarding Annual Academic Session commencement & Textbooks Distribution",
      category: "Academic",
      date: "2024-07-15",
      badge: "Academic",
      summary: "[Sample Notice Placeholder] Distribution of government textbooks for registered secondary students under state welfare scheme.",
      isImportant: true,
      file: "assets/documents/results/official-academic-record.txt"
    },
    {
      id: 2,
      title: "Jharkhand Academic Council (JAC) Board Examination Form Verification",
      category: "Examination",
      date: "2024-08-10",
      badge: "Examination",
      summary: "[Sample Notice Placeholder] Class 10 & 12 students are instructed to verify their registration details and photographs.",
      isImportant: true,
      file: "assets/documents/results/official-academic-record.txt"
    },
    {
      id: 3,
      title: "Information regarding Admission in Class 11 (+2 Higher Secondary)",
      category: "Admission",
      date: "2024-06-20",
      badge: "Admission",
      summary: "[Sample Notice Placeholder] Guidance regarding document submission for Science, Arts and Commerce streams for qualified Class 10 candidates.",
      isImportant: true,
      file: "assets/documents/results/official-academic-record.txt"
    },
    {
      id: 4,
      title: "Independence Day & Annual Flag Hoisting Ceremony Protocol",
      category: "General",
      date: "2024-08-12",
      badge: "General",
      summary: "[Sample Notice Placeholder] Assembly time, uniform instructions and cultural performance schedule for national celebration.",
      isImportant: false,
      file: "assets/documents/results/official-academic-record.txt"
    },
    {
      id: 5,
      title: "Inter-House Sports Meet & Athletics Selection Trials",
      category: "Sports",
      date: "2024-09-05",
      badge: "Sports",
      summary: "[Sample Notice Placeholder] Trials for sprints, high jump, volleyball and football for junior and senior wings.",
      isImportant: false,
      file: "assets/documents/results/official-academic-record.txt"
    },
    {
      id: 6,
      title: "District Science Fair & Student Model Submission Guidelines",
      category: "Cultural",
      date: "2024-10-02",
      badge: "Exhibition",
      summary: "[Sample Notice Placeholder] Students preparing models on solar irrigation and waste management are requested to submit synopses.",
      isImportant: false,
      file: "assets/documents/results/official-academic-record.txt"
    }
  ],

  results: [
    {
      session: "2023-2024",
      exam: "Annual Board Examination (JAC)",
      className: "Class 12 (Arts)",
      status: "Gazette Released by JAC",
      remark: "Official result tabulations available at School Administrative Office. Refer to JAC official portal.",
      link: "assets/documents/results/official-academic-record.txt"
    },
    {
      session: "2023-2024",
      exam: "Annual Board Examination (JAC)",
      className: "Class 12 (Science)",
      status: "Gazette Released by JAC",
      remark: "Official result tabulations available at School Administrative Office. Refer to JAC official portal.",
      link: "assets/documents/results/official-academic-record.txt"
    },
    {
      session: "2023-2024",
      exam: "Annual Board Examination (JAC)",
      className: "Class 12 (Commerce)",
      status: "Gazette Released by JAC",
      remark: "Official result tabulations available at School Administrative Office. Refer to JAC official portal.",
      link: "assets/documents/results/official-academic-record.txt"
    },
    {
      session: "2023-2024",
      exam: "Secondary Board Examination (Class 10)",
      className: "Class 10 (Secondary)",
      status: "Gazette Released by JAC",
      remark: "Students can collect their original provisional certificates and marks sheets in person.",
      link: "assets/documents/results/official-academic-record.txt"
    },
    {
      session: "2024-2025",
      exam: "Half-Yearly Evaluation",
      className: "Class 9 to 12",
      status: "Scheduled as per State Academic Calendar",
      remark: "[Official Examination Dates Placeholder - Will be published upon council directive]",
      link: "assets/documents/results/official-academic-record.txt"
    }
  ],

  smcMembers: [
    { name: "[Official Nominee - School Committee]", role: "President / Chairman", category: "Community Representative", term: "2023–2026" },
    { name: "[Principal / Head of Institution]", role: "Member Secretary", category: "Ex-Officio Member", term: "Ex-Officio" },
    { name: "[Senior Faculty Representative]", role: "Teacher Member", category: "Teaching Staff", term: "2023–2026" },
    { name: "[Senior Science Faculty]", role: "Teacher Member", category: "Teaching Staff", term: "2023–2026" },
    { name: "[Parent Nominee 1]", role: "Parent Member", category: "Parents / Guardian", term: "2023–2026" },
    { name: "[Parent Nominee 2 - Female]", role: "Parent Member", category: "Parents / Guardian", term: "2023–2026" },
    { name: "[Local Gram Panchayat Representative]", role: "Panchayat Nominee", category: "Local Body Representative", term: "2023–2026" },
    { name: "[Educationist / Social Worker Nominee]", role: "Special Invitee", category: "Educationist", term: "2023–2026" }
  ],

  classesAndSubjects: [
    {
      grade: "Class IX & X",
      wing: "Secondary Section",
      curriculum: "Jharkhand Academic Council (JAC) Core Curriculum",
      subjects: "Hindi (Course A/B), English, Mathematics, Science (Physics, Chemistry, Biology), Social Science (History, Civics, Geography, Economics), Sanskrit / Regional Language, Physical & Health Education"
    },
    {
      grade: "Class XI & XII (Arts Stream)",
      wing: "+2 Higher Secondary",
      curriculum: "JAC +2 Higher Secondary Syllabus",
      subjects: "Compulsory Language: Hindi / English; Electives: History, Political Science, Geography, Economics, Sociology / Philosophy / Psychology"
    },
    {
      grade: "Class XI & XII (Science Stream)",
      wing: "+2 Higher Secondary",
      curriculum: "JAC +2 Higher Secondary Syllabus",
      subjects: "Compulsory Language: English / Hindi; Core: Physics, Chemistry, Mathematics, Biology, Computer Science / Vocational Subject"
    },
    {
      grade: "Class XI & XII (Commerce Stream)",
      wing: "+2 Higher Secondary",
      curriculum: "JAC +2 Higher Secondary Syllabus",
      subjects: "Compulsory Language: English / Hindi; Core: Accountancy, Business Studies, Commercial Arithmetic / Mathematics, Economics, Entrepreneurship"
    }
  ],

  galleryItems: [
    {
      id: 1,
      title: "Main Institutional Campus",
      category: "campus",
      categoryName: "Campus",
      image: "assets/img/gallery/gallery-1.svg",
      desc: "Lush green campus grounds and main academic administrative complex in Haldipokhar."
    },
    {
      id: 2,
      title: "Secondary Interactive Classroom",
      category: "classroom",
      categoryName: "Classroom",
      image: "assets/img/gallery/gallery-2.svg",
      desc: "Dedicated student learning environment with disciplined engagement and teacher mentorship."
    },
    {
      id: 3,
      title: "Annual Day Cultural Performance",
      category: "cultural",
      categoryName: "Cultural",
      image: "assets/img/gallery/gallery-3.svg",
      desc: "Vibrant presentations of traditional folk arts and theatrical dramas by students."
    },
    {
      id: 4,
      title: "Annual Sports Day Track Events",
      category: "sports",
      categoryName: "Sports",
      image: "assets/img/gallery/gallery-4.svg",
      desc: "Sprint trials, relay races, and field athletics on the school playground."
    },
    {
      id: 5,
      title: "Science & Sustainable Energy Fair",
      category: "exhibitions",
      categoryName: "Exhibitions",
      image: "assets/img/gallery/gallery-5.svg",
      desc: "Working models demonstrating renewable solar energy and rainwater harvesting."
    },
    {
      id: 6,
      title: "Bharat Scouts & Guides Camp",
      category: "scout-guide",
      categoryName: "Scout & Guide",
      image: "assets/img/gallery/gallery-6.svg",
      desc: "Outdoor bivouac, emergency knots, flag salutations and moral training exercises."
    },
    {
      id: 7,
      title: "Vocational Skills Practical Workshop",
      category: "vocational",
      categoryName: "Vocational",
      image: "assets/img/gallery/gallery-7.svg",
      desc: "Practical hands-on training preparing secondary students for technical vocations."
    },
    {
      id: 8,
      title: "Scholastic Felicitation Ceremony",
      category: "campus",
      categoryName: "Achievements",
      image: "assets/img/gallery/gallery-8.svg",
      desc: "Annual assembly honoring outstanding academic achievers and athletic medalists."
    }
  ]
};

if (typeof module !== 'undefined' && module.exports) {
  module.exports = SchoolData;
}
