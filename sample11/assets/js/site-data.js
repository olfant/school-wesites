/* ==========================================================================
   CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR
   CENTRAL REUSABLE SITE DATA & CONSTANTS
   ========================================================================== */

const SCHOOL_DATA = {
  name: "CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR",
  hindiAddress: "हल्दीपोखर, पोटका, पूर्वी सिंहभूम, झारखण्ड – 831002",
  udiseCode: "20180231602",
  officialEmail: "vnhs.haldipokhar.e.singhbhum@gmail.com",
  level: "+2 Higher Secondary",
  educationalFocus: [
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
  ]
};

/* Demonstration Notices (Clearly labelled demo content) */
const SITE_NOTICES = [
  {
    id: 1,
    date: "15-11-2026",
    category: "Admission",
    title: "[Demonstration] Guidelines for Intermediate (+2) Admission Process",
    description: "Information regarding the upcoming academic admission procedure and document verification schedule.",
    file: "assets/documents/notices/admission-notice-2026.txt"
  },
  {
    id: 2,
    date: "10-11-2026",
    category: "Academic",
    title: "[Demonstration] Mid-Term Assessment & Practical Demonstration Schedule",
    description: "Detailed session schedule for science and vocational practical evaluations.",
    file: "#"
  },
  {
    id: 3,
    date: "04-11-2026",
    category: "Cultural",
    title: "[Demonstration] Annual Jharkhand State Heritage & Cultural Meet",
    description: "Auditions for folk dance, tribal music, drama and cultural celebrations.",
    file: "#"
  },
  {
    id: 4,
    date: "28-10-2026",
    category: "Sports",
    title: "[Demonstration] Inter-School Athletics Meet & Football Trials",
    description: "Selection trials for 100m, 400m sprint, relay race and school football squad.",
    file: "#"
  },
  {
    id: 5,
    date: "20-10-2026",
    category: "Examination",
    title: "[Demonstration] JAC Board Evaluation & Pre-Board Notification",
    description: "Subject-wise timetable and examination instructions for Class 10 and Class 12.",
    file: "assets/documents/results/sample-result-notice.txt"
  },
  {
    id: 6,
    date: "14-10-2026",
    category: "General",
    title: "[Demonstration] School Management Committee (SMC) Quarterly Meeting",
    description: "Meeting of SMC members, teachers and parent representatives for school development.",
    file: "#"
  }
];

/* Demonstration Examination Results (Verified structure, no fabricated student data) */
const SITE_RESULTS = [
  {
    roll: "12001",
    name: "[Student Name Placeholder]",
    cls: "Class 12 (Science)",
    exam: "Annual Intermediate Exam",
    session: "2025-26",
    status: "Verified",
    pdf: "assets/documents/results/sample-result-notice.txt"
  },
  {
    roll: "12002",
    name: "[Student Name Placeholder]",
    cls: "Class 12 (Arts)",
    exam: "Annual Intermediate Exam",
    session: "2025-26",
    status: "Verified",
    pdf: "assets/documents/results/sample-result-notice.txt"
  },
  {
    roll: "12003",
    name: "[Student Name Placeholder]",
    cls: "Class 12 (Commerce)",
    exam: "Annual Intermediate Exam",
    session: "2025-26",
    status: "Verified",
    pdf: "assets/documents/results/sample-result-notice.txt"
  },
  {
    roll: "10001",
    name: "[Student Name Placeholder]",
    cls: "Class 10 (Secondary)",
    exam: "Secondary Board Exam",
    session: "2024-25",
    status: "Archived",
    pdf: "assets/documents/results/sample-result-notice.txt"
  }
];

/* SMC Committee Members Demonstration Structure */
const SMC_MEMBERS_DATA = [
  { sno: 1, name: "[President Name Placeholder]", designation: "President", category: "Parent / Community Representative", contact: "Official School Office" },
  { sno: 2, name: "[Principal / In-Charge Placeholder]", designation: "Member Secretary", category: "Ex-Officio Principal", contact: "Official Email" },
  { sno: 3, name: "[Teacher Representative Placeholder]", designation: "Teacher Member", category: "Faculty Representative", contact: "School Campus" },
  { sno: 4, name: "[Local Representative Placeholder]", designation: "Panchayat Representative", category: "Local Governance", contact: "Haldipokhar, Potka" },
  { sno: 5, name: "[Parent Member Placeholder]", designation: "Parent Member", category: "Parent Representative", contact: "—" },
  { sno: 6, name: "[Parent Member Placeholder]", designation: "Parent Member (Female)", category: "Parent Representative", contact: "—" }
];

/* Classes & Academic Streams Structure */
const ACADEMIC_STREAMS = [
  {
    stream: "Higher Secondary Science (+2)",
    classes: "Class 11 & Class 12",
    compulsory: "General English, Core Language (Hindi / Regional)",
    electives: "Physics, Chemistry, Mathematics, Biology, Computer Science",
    practical: "Physics Lab, Chemistry Lab, Biology Lab, STEM Experiments"
  },
  {
    stream: "Higher Secondary Arts (+2)",
    classes: "Class 11 & Class 12",
    compulsory: "General English, Core Language (Hindi / Regional)",
    electives: "History, Political Science, Economics, Geography, Sociology",
    practical: "Map Work, Field Projects, Socio-Economic Surveys"
  },
  {
    stream: "Higher Secondary Commerce (+2)",
    classes: "Class 11 & Class 12",
    compulsory: "General English, Core Language",
    electives: "Accountancy, Business Studies, Commercial Mathematics, Economics",
    practical: "Tally, Ledger Training, Banking & Financial Case Studies"
  },
  {
    stream: "Secondary Level (High School)",
    classes: "Class 9 & Class 10",
    compulsory: "Hindi, English, Sanskrit / Regional Language",
    electives: "Mathematics, Science (Physics/Chemistry/Bio), Social Science",
    practical: "Science Practical, ICT, Physical & Health Education"
  }
];

/* Gallery Master Dataset */
const SITE_GALLERY = [
  { id: 1, title: "School Academic Block", category: "campus", src: "assets/img/gallery/gal-1.svg", caption: "Main academic building of CM SOE Haldipokhar" },
  { id: 2, title: "Modern Smart Classroom", category: "classrooms", src: "assets/img/gallery/gal-2.svg", caption: "Interactive digital classroom session" },
  { id: 3, title: "STEM & Science Laboratory", category: "classrooms", src: "assets/img/gallery/gal-3.svg", caption: "Students practical science experimentation facility" },
  { id: 4, title: "Disciplined Morning Assembly", category: "students", src: "assets/img/gallery/gal-4.svg", caption: "Morning prayer and value-building student assembly" },
  { id: 5, title: "Jharkhand Cultural Dance", category: "cultural", src: "assets/img/gallery/gal-5.svg", caption: "Traditional folk dance during annual festival" },
  { id: 6, title: "Annual Athletic Competitions", category: "sports", src: "assets/img/gallery/gal-6.svg", caption: "Student track and field sports day" },
  { id: 7, title: "Science & Innovation Fair", category: "exhibitions", src: "assets/img/gallery/gal-7.svg", caption: "Student working models and science exhibition" },
  { id: 8, title: "Bharat Scouts & Guides Camp", category: "scout", src: "assets/img/gallery/gal-8.svg", caption: "Leadership, service and outdoor scout training" }
];
