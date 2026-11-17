/**
 * CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR
 * Architectural Geometry + Isometric Campus Design System
 * Global Site Data & Verified Information Repository
 */

const SCHOOL_DATA = {
  name: "CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR",
  shortName: "CM SOE VNIKETAN HALDIPOKHAR",
  udiseCode: "20180231602",
  addressHindi: "हल्दीपोखर, पोटका, पूर्वी सिंहभूम, झारखण्ड – 831002",
  addressEnglish: "Haldipokhar, Potka, East Singhbhum, Jharkhand – 831002",
  email: "vnhs.haldipokhar.e.singhbhum@gmail.com",
  educationalLevel: "+2 Higher Secondary",
  focusAreas: [
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
  disclaimer: "Data Accuracy Notice: Official records, dates, and administrative statistics are updated only upon formal release by the school authority. Demonstration content is strictly marked."
};

// Verified / Demonstration Notices Data
const NOTICES_DATA = [
  {
    id: "NOT-001",
    date: "14 Nov 2026",
    category: "Academic",
    title: "Commencement of Second Term Continuous Formative Assessment",
    description: "Formative evaluations across secondary and higher secondary streams will follow the verified state academic framework.",
    badge: "Official Schedule",
    isDemo: true
  },
  {
    id: "NOT-002",
    date: "08 Nov 2026",
    category: "General",
    title: "Parent-Teacher SMC Consultative Meeting Notice",
    description: "School Management Committee and parents consultative interaction regarding student welfare and campus development.",
    badge: "Meeting Circular",
    isDemo: true
  },
  {
    id: "NOT-003",
    date: "28 Oct 2026",
    category: "Exhibition",
    title: "Annual Science and Mathematical Innovation Exhibit",
    description: "Students are invited to register scientific working models, engineering concepts, and mathematical problem-solving exhibits.",
    badge: "Science Forum",
    isDemo: true
  },
  {
    id: "NOT-004",
    date: "15 Oct 2026",
    category: "Sports",
    title: "Inter-House Athletic & Sports Selection Trials",
    description: "Selection trials for track and field, athletics, badminton, and outdoor disciplines under the physical education department.",
    badge: "Sports Dept",
    isDemo: true
  },
  {
    id: "NOT-005",
    date: "02 Oct 2026",
    category: "Cultural",
    title: "Observance of National Values and Heritage Assembly",
    description: "Special morning assembly and essay presentation celebrating patriotic service, moral ethics, and community contribution.",
    badge: "Cultural Cell",
    isDemo: true
  },
  {
    id: "NOT-006",
    date: "20 Sep 2026",
    category: "Admission",
    title: "General Information on Academic Session Admissions",
    description: "Advisory note for parents regarding admission verification criteria, government documentation guidelines, and stream eligibility.",
    badge: "Advisory",
    isDemo: true
  }
];

// Examination & Academic Results Records
const RESULTS_DATA = [
  {
    session: "2025-2026",
    examType: "Higher Secondary Terminal",
    streamClass: "Class 12 (+2)",
    status: "Verified Document Record",
    date: "June 2026",
    docLink: "assets/documents/results/academic_record_placeholder.txt",
    note: "Official examination records are verified and published through school administration."
  },
  {
    session: "2025-2026",
    examType: "Secondary Board Pre-Test",
    streamClass: "Class 10 (Secondary)",
    status: "Verified Document Record",
    date: "May 2026",
    docLink: "assets/documents/results/academic_record_placeholder.txt",
    note: "Individual mark sheets are distributed directly via institution record registry."
  },
  {
    session: "2024-2025",
    examType: "Annual Evaluation Assessment",
    streamClass: "Class 11 (+2)",
    status: "Archived Record",
    date: "April 2025",
    docLink: "assets/documents/results/academic_record_placeholder.txt",
    note: "Archived academic records maintained under U-DISE Code 20180231602."
  },
  {
    session: "2024-2025",
    examType: "Annual School Evaluation",
    streamClass: "Class 9 (Secondary)",
    status: "Archived Record",
    date: "April 2025",
    docLink: "assets/documents/results/academic_record_placeholder.txt",
    note: "Available for parent consultation during official administrative hours."
  }
];

// School Gallery Items
const GALLERY_DATA = [
  {
    id: 1,
    title: "Main Campus Academic Block",
    category: "campus",
    image: "assets/img/campus/campus-main.svg",
    caption: "Modern geometric architectural facade of the Haldipokhar institution."
  },
  {
    id: 2,
    title: "Interactive Classroom Learning",
    category: "academics",
    image: "assets/img/students/students-learning.svg",
    caption: "Fostering conceptual clarity, discipline and collaborative academic inquiry."
  },
  {
    id: 3,
    title: "Science & Technology Exhibition",
    category: "exhibitions",
    image: "assets/img/exhibitions/science-exhibition.svg",
    caption: "Students presenting experimental models and innovative scientific solutions."
  },
  {
    id: 4,
    title: "Athletic Ground & Sports Meet",
    category: "sports",
    image: "assets/img/sports/sports-athletics.svg",
    caption: "Cultivating physical stamina, endurance, team spirit and sportsmanship."
  },
  {
    id: 5,
    title: "Cultural Heritage Performance",
    category: "cultural",
    image: "assets/img/cultural/cultural-dance.svg",
    caption: "Celebrating cultural diversity and folk traditions during school assemblies."
  },
  {
    id: 6,
    title: "Bharat Scouts and Guides Wing",
    category: "scout",
    image: "assets/img/students/scout-guide.svg",
    caption: "Instilling selfless service, leadership, moral duty and wilderness skills."
  },
  {
    id: 7,
    title: "Institutional Knowledge & Library Center",
    category: "campus",
    image: "assets/img/campus/campus-library.svg",
    caption: "Dedicated reference resource repository for secondary and +2 scholars."
  },
  {
    id: 8,
    title: "Science Laboratory & Practical Research",
    category: "academics",
    image: "assets/img/campus/campus-lab.svg",
    caption: "Hands-on laboratory testing upholding scientific inquiry and safety."
  },
  {
    id: 9,
    title: "Art, Craft & Design Exhibition",
    category: "exhibitions",
    image: "assets/img/exhibitions/art-exhibition.svg",
    caption: "Creative craftsmanship, geometrical drawings and environmental exhibits."
  },
  {
    id: 10,
    title: "Indoor Chess & Cognitive Games",
    category: "sports",
    image: "assets/img/sports/sports-indoor.svg",
    caption: "Promoting strategic mental acuity, composure and focused sportsmanship."
  },
  {
    id: 11,
    title: "Music & Performing Arts Ensemble",
    category: "cultural",
    image: "assets/img/cultural/cultural-music.svg",
    caption: "Rhythmic expression, vocal harmony and musical stage presentations."
  },
  {
    id: 12,
    title: "Academic Merit Recognition",
    category: "academics",
    image: "assets/img/achievements/award-ceremony.svg",
    caption: "Recognizing dedication, scholastic honesty and ethical leadership."
  }
];

// SMC Members Verified Placeholders
const SMC_MEMBERS_DATA = [
  { sNo: "01", name: "[Official SMC President - Record on File]", designation: "President", category: "Community Representative", contact: "Via School Office" },
  { sNo: "02", name: "[Principal / Ex-Officio Member]", designation: "Secretary (Ex-Officio)", category: "Institutional Head", contact: "vnhs.haldipokhar.e.singhbhum@gmail.com" },
  { sNo: "03", name: "[Senior Teacher Representative]", designation: "Teacher Member", category: "Academic Faculty", contact: "School Campus" },
  { sNo: "04", name: "[Parent Representative - Secondary]", designation: "Parent Member", category: "Parent Community", contact: "Haldipokhar Local" },
  { sNo: "05", name: "[Parent Representative - Higher Sec]", designation: "Parent Member", category: "Parent Community", contact: "Potka Block" },
  { sNo: "06", name: "[Elected Local Authority Member]", designation: "Panchayat Representative", category: "Local Self-Govt", contact: "Local Panchayat" },
  { sNo: "07", name: "[Educationist / Nominated Specialist]", designation: "Special Invitee", category: "Educationist", contact: "East Singhbhum" }
];

// Export to window
if (typeof window !== "undefined") {
  window.SCHOOL_DATA = SCHOOL_DATA;
  window.NOTICES_DATA = NOTICES_DATA;
  window.RESULTS_DATA = RESULTS_DATA;
  window.GALLERY_DATA = GALLERY_DATA;
  window.SMC_MEMBERS_DATA = SMC_MEMBERS_DATA;
}
