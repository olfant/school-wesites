/**
 * CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR
 * Centralized Site Data & Verified Information
 * Prompt 08 - Glassmorphism & Digital Campus Portal
 */

const SITE_DATA = {
  school: {
    officialName: "CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR",
    shortName: "CM SOE Haldipokhar",
    hindiName: "हल्दीपोखर, पोटका, पूर्वी सिंहभूम, झारखण्ड – 831002",
    address: {
      village: "हल्दीपोखर (Haldipokhar)",
      block: "पोटका (Potka)",
      district: "पूर्वी सिंहभूम (East Singhbhum)",
      state: "झारखण्ड (Jharkhand)",
      pincode: "831002",
      fullText: "हल्दीपोखर, पोटका, पूर्वी सिंहभूम, झारखण्ड – 831002"
    },
    udiseCode: "20180231602",
    officialEmail: "vnhs.haldipokhar.e.singhbhum@gmail.com",
    educationalLevel: "+2 Higher Secondary",
    affiliations: "Jharkhand Academic Council (JAC) / Dept. of School Education & Literacy, Govt. of Jharkhand",
    schoolType: "Co-educational Government Higher Secondary School",
    establishmentYear: "[Establishment Year - Official Records to be Updated]",
    principalName: "[Principal's Name - Official Record to be Updated]",
    contactPhone: "[Official Phone - To be Updated / Enquire via Email]",
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
  },

  // Official & Verified Notice Portal Placeholders
  notices: [
    {
      id: "NOT-2026-001",
      title: "Commencement of +2 Academic Session & Subject Orientation",
      category: "Academic",
      date: "2026-04-10",
      description: "Class 11 & 12 orientation schedule for Science, Arts, and Commerce streams. Students are advised to review the digital syllabus.",
      status: "Active",
      isDemonstration: true,
      fileUrl: "assets/documents/notices/sample-notice-2026.txt"
    },
    {
      id: "NOT-2026-002",
      title: "Annual Sports & Athletics Meet Registration Notice",
      category: "Sports",
      date: "2026-04-05",
      description: "Inter-house athletic trials for track events, badminton, kabaddi, and volleyball. Submit entries to the Sports Coordinator.",
      status: "Active",
      isDemonstration: true,
      fileUrl: "assets/documents/notices/sample-notice-2026.txt"
    },
    {
      id: "NOT-2026-003",
      title: "Bharat Scouts & Guides Annual Camporee Enrolment",
      category: "Cultural",
      date: "2026-03-28",
      description: "Enrolment open for Scout & Guide unit training camp and community development service badge activities.",
      status: "Active",
      isDemonstration: true,
      fileUrl: "assets/documents/notices/sample-notice-2026.txt"
    },
    {
      id: "NOT-2026-004",
      title: "Quarterly School Management Committee (SMC) Consultation",
      category: "General",
      date: "2026-03-20",
      description: "Scheduled meeting of SMC members regarding digital classroom facilities, campus development, and student welfare.",
      status: "Archived",
      isDemonstration: true,
      fileUrl: "assets/documents/notices/sample-notice-2026.txt"
    },
    {
      id: "NOT-2026-005",
      title: "Science & Vocational Innovation Project Submissions",
      category: "Academic",
      date: "2026-03-15",
      description: "Guidance for upcoming district-level science exhibitions and hands-on skill development project presentations.",
      status: "Active",
      isDemonstration: true,
      fileUrl: "assets/documents/notices/sample-notice-2026.txt"
    },
    {
      id: "NOT-2026-006",
      title: "JAC Board Examination Routine & Admit Card Notice (Demonstration)",
      category: "Examination",
      date: "2026-03-01",
      description: "Demonstration announcement regarding board examination guidelines and roll verification procedures.",
      status: "Archived",
      isDemonstration: true,
      fileUrl: "assets/documents/notices/sample-notice-2026.txt"
    }
  ],

  // Examination Results Portal Placeholders
  results: [
    {
      session: "2024-2025",
      exam: "JAC Class 12 Intermediate Board (Arts/Science/Commerce)",
      classLevel: "Class 12",
      stream: "Combined",
      announcementDate: "May 2025",
      status: "Archived Gazette",
      documentName: "JAC_12th_Result_Gazette_Haldipokhar_Summary.pdf",
      note: "[Demonstration Record - Official verified tabulation sheet accessible at administrative desk]"
    },
    {
      session: "2024-2025",
      exam: "JAC Class 10 Secondary Board Examination",
      classLevel: "Class 10",
      stream: "General",
      announcementDate: "May 2025",
      status: "Archived Gazette",
      documentName: "JAC_10th_Result_Gazette_Haldipokhar_Summary.pdf",
      note: "[Demonstration Record - Official verified marksheets issued directly to enrolled candidates]"
    },
    {
      session: "2023-2024",
      exam: "JAC Class 12 Intermediate Board Examination",
      classLevel: "Class 12",
      stream: "Combined",
      announcementDate: "May 2024",
      status: "Archived Gazette",
      documentName: "JAC_12th_2024_Summary.pdf",
      note: "[Demonstration Record - Official school records maintained in offline register]"
    },
    {
      session: "2023-2024",
      exam: "JAC Class 10 Secondary Examination",
      classLevel: "Class 10",
      stream: "General",
      announcementDate: "May 2024",
      status: "Archived Gazette",
      documentName: "JAC_10th_2024_Summary.pdf",
      note: "[Demonstration Record - Institutional archive]"
    }
  ],

  // SMC Committee Members (Strictly labelled placeholders)
  smcMembers: [
    { sn: 1, name: "[Principal / Ex-officio Member Secretary]", designation: "Member Secretary", category: "School Administration", contact: "Official School Office" },
    { sn: 2, name: "[President - Nominated SMC Parent Representative]", designation: "President / Chairperson", category: "Parent Representative", contact: "Via SMC Desk" },
    { sn: 3, name: "[Vice President - Elected Community Member]", designation: "Vice President", category: "Local Community / PRI", contact: "Via SMC Desk" },
    { sn: 4, name: "[Teacher Representative - Senior Faculty]", designation: "Teacher Member", category: "Faculty Representative", contact: "School Academic Dept" },
    { sn: 5, name: "[Teacher Representative - Science / Language]", designation: "Teacher Member", category: "Faculty Representative", contact: "School Academic Dept" },
    { sn: 6, name: "[Parent Representative - Ward 01]", designation: "Member", category: "Parent (SC/ST/OBC representation)", contact: "Haldipokhar Potka" },
    { sn: 7, name: "[Parent Representative - Ward 02]", designation: "Member", category: "Parent (Women representation)", contact: "Haldipokhar Potka" },
    { sn: 8, name: "[Local PRI / Panchayat Nominee]", designation: "Special Invitee", category: "Local Governance", contact: "Panchayat Haldipokhar" },
    { sn: 9, name: "[Educationist / Civil Society Member]", designation: "Member", category: "Educationist", contact: "East Singhbhum" }
  ],

  // Academic Offerings
  streams: [
    {
      name: "Science Stream (+2 Higher Secondary)",
      code: "SCI-102",
      compulsory: ["Core English / Hindi", "Physics", "Chemistry"],
      electives: ["Mathematics", "Biology", "Computer Science / Information Practice"],
      focus: "STEM inquiry, experimental laboratory work, competitive entrance readiness."
    },
    {
      name: "Arts & Humanities Stream (+2 Higher Secondary)",
      code: "ART-103",
      compulsory: ["Core English / Hindi", "History", "Political Science"],
      electives: ["Geography", "Economics", "Sociology / Philosophy"],
      focus: "Critical analysis, heritage, social awareness, civics and linguistic proficiency."
    },
    {
      name: "Commerce Stream (+2 Higher Secondary)",
      code: "COM-104",
      compulsory: ["Core English / Hindi", "Accountancy", "Business Studies"],
      electives: ["Economics", "Commercial Mathematics", "Entrepreneurship"],
      focus: "Financial literacy, accounting principles, trade economics, and management acumen."
    }
  ]
};

// Global freeze to prevent tampering
if (typeof Object.freeze === "function") {
  Object.freeze(SITE_DATA);
}
