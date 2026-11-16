import os

base_dir = r"D:\school-website-v3\assets\img"

def create_svg(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Created: {path}")

# 1. School Logo
logo_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 240" width="100%" height="100%">
  <defs>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F9E076"/>
      <stop offset="50%" stop-color="#D4AF37"/>
      <stop offset="100%" stop-color="#AA771C"/>
    </linearGradient>
    <linearGradient id="greenGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#16864A"/>
      <stop offset="100%" stop-color="#063F27"/>
    </linearGradient>
    <filter id="shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#063F27" flood-opacity="0.3"/>
    </filter>
  </defs>

  <!-- Outer Ring -->
  <circle cx="120" cy="120" r="114" fill="none" stroke="url(#goldGrad)" stroke-width="5" filter="url(#shadow)"/>
  <circle cx="120" cy="120" r="106" fill="url(#greenGrad)" stroke="#D4AF37" stroke-width="2"/>
  <circle cx="120" cy="120" r="82" fill="#FFFFFF" stroke="url(#goldGrad)" stroke-width="2.5"/>

  <!-- Curved Text Path -->
  <path id="textPathTop" d="M 30,120 A 90,90 0 1,1 210,120" fill="none" stroke="none"/>
  <path id="textPathBottom" d="M 206,126 A 86,86 0 0,1 34,126" fill="none" stroke="none"/>

  <text font-family="'Noto Sans Devanagari', 'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="700" fill="#FFFFFF" letter-spacing="1">
    <textPath href="#textPathTop" startOffset="50%" text-anchor="middle">
      +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय
    </textPath>
  </text>
  <text font-family="'Plus Jakarta Sans', sans-serif" font-size="9" font-weight="700" fill="#F9E076" letter-spacing="1.5">
    <textPath href="#textPathBottom" startOffset="50%" text-anchor="middle">
      HALDIPOKHAR • POTKA • JHARKHAND
    </textPath>
  </text>

  <!-- Central Shield -->
  <g transform="translate(120, 118)">
    <!-- Foliage Wreath -->
    <path d="M-60,5 C-60,35 -30,60 0,68 C30,60 60,35 60,5 C50,-10 40,-5 35,0 C38,20 18,48 0,55 C-18,48 -38,20 -35,0 C-40,-5 -50,-10 -60,5 Z" fill="#D9F0DF"/>
    
    <!-- Shield Background -->
    <path d="M-45,-45 L45,-45 L45,10 C45,38 15,55 0,60 C-15,55 -45,38 -45,10 Z" fill="#F5F9F6" stroke="#105A34" stroke-width="2.5"/>
    <path d="M-40,-40 L40,-40 L40,8 C40,34 14,49 0,54 C-14,49 -40,34 -40,8 Z" fill="#FFFFFF"/>

    <!-- Lamp of Knowledge (Deepak) -->
    <g transform="translate(0, -18)">
      <ellipse cx="0" cy="12" rx="22" ry="7" fill="url(#goldGrad)"/>
      <path d="M-22,12 Q0,26 22,12 Q14,24 -14,24 Z" fill="#AA771C"/>
      <path d="M-10,24 L10,24 L6,30 L-6,30 Z" fill="url(#goldGrad)"/>
      <ellipse cx="0" cy="30" rx="14" ry="3" fill="#D4AF37"/>
      <!-- Flame -->
      <path d="M0,7 C-6,-2 -7,-12 0,-22 C7,-12 6,-2 0,7 Z" fill="#FF5722"/>
      <path d="M0,6 C-3,-1 -4,-8 0,-16 C4,-8 3,-1 0,6 Z" fill="#FFC107"/>
      <circle cx="0" cy="-2" r="3" fill="#FFF9C4"/>
    </g>

    <!-- Open Book -->
    <g transform="translate(0, 22)">
      <!-- Left Page -->
      <path d="M-28,4 C-18,-4 -8,0 0,4 L0,18 C-8,14 -18,10 -28,18 Z" fill="#105A34"/>
      <path d="M-26,5 C-17,-2 -8,2 -2,5 L-2,16 C-8,13 -17,9 -26,16 Z" fill="#FFFFFF"/>
      <line x1="-22" y1="8" x2="-6" y2="6" stroke="#105A34" stroke-width="1.2"/>
      <line x1="-22" y1="11" x2="-6" y2="9" stroke="#105A34" stroke-width="1.2"/>
      <line x1="-22" y1="14" x2="-8" y2="12" stroke="#105A34" stroke-width="1.2"/>

      <!-- Right Page -->
      <path d="M28,4 C18,-4 8,0 0,4 L0,18 C8,14 18,10 28,18 Z" fill="#105A34"/>
      <path d="M26,5 C17,-2 8,2 2,5 L2,16 C8,13 17,9 26,16 Z" fill="#FFFFFF"/>
      <line x1="22" y1="8" x2="6" y2="6" stroke="#105A34" stroke-width="1.2"/>
      <line x1="22" y1="11" x2="6" y2="9" stroke="#105A34" stroke-width="1.2"/>
      <line x1="22" y1="14" x2="8" y2="12" stroke="#105A34" stroke-width="1.2"/>
    </g>

    <!-- Small Stars -->
    <path d="M-30,-28 L-28,-23 L-23,-23 L-27,-20 L-25,-15 L-30,-18 L-35,-15 L-33,-20 L-37,-23 L-32,-23 Z" fill="url(#goldGrad)"/>
    <path d="M30,-28 L32,-23 L37,-23 L33,-20 L35,-15 L30,-18 L25,-15 L27,-20 L23,-23 L28,-23 Z" fill="url(#goldGrad)"/>
  </g>

  <!-- Motto Banner -->
  <g transform="translate(120, 198)">
    <rect x="-65" y="-10" width="130" height="20" rx="10" fill="url(#goldGrad)" stroke="#063F27" stroke-width="1.5"/>
    <text font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="800" fill="#063F27" text-anchor="middle" y="3.5" letter-spacing="1.2">
      VIDYA DADATI VINAYAM
    </text>
  </g>
</svg>"""

create_svg(os.path.join(base_dir, "logo", "school-logo.svg"), logo_svg)

def make_campus_svg(title, subtitle, tag, color_accent="#16864A", icon_type="campus"):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" width="100%" height="100%">
  <defs>
    <linearGradient id="skyGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#E1F0E7"/>
      <stop offset="60%" stop-color="#F5F9F6"/>
      <stop offset="100%" stop-color="#D9F0DF"/>
    </linearGradient>
    <linearGradient id="buildingGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="50%" stop-color="#F5F9F6"/>
      <stop offset="100%" stop-color="#E2ECE5"/>
    </linearGradient>
    <linearGradient id="greenRoof" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#16864A"/>
      <stop offset="100%" stop-color="#105A34"/>
    </linearGradient>
    <linearGradient id="overlayGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="rgba(6, 63, 39, 0.1)"/>
      <stop offset="50%" stop-color="rgba(6, 63, 39, 0.4)"/>
      <stop offset="100%" stop-color="rgba(6, 63, 39, 0.92)"/>
    </linearGradient>
    <pattern id="gridPattern" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(16, 90, 52, 0.04)" stroke-width="1"/>
    </pattern>
  </defs>

  <!-- Sky & Grid -->
  <rect width="1200" height="800" fill="url(#skyGrad)"/>
  <rect width="1200" height="800" fill="url(#gridPattern)"/>

  <!-- Distant Hills & Trees -->
  <path d="M0,520 Q200,480 400,510 T800,490 T1200,515 L1200,800 L0,800 Z" fill="#D2E8DA"/>
  <path d="M0,545 Q300,510 600,540 T1200,530 L1200,800 L0,800 Z" fill="#B7DCC2"/>

  <!-- Background Trees -->
  <g fill="#43A76D" opacity="0.6">
    <circle cx="80" cy="540" r="45"/>
    <circle cx="130" cy="530" r="55"/>
    <circle cx="180" cy="545" r="40"/>
    <circle cx="1020" cy="535" r="50"/>
    <circle cx="1070" cy="520" r="60"/>
    <circle cx="1120" cy="540" r="45"/>
  </g>

  <!-- School Main Academic Building -->
  <g id="main-building">
    <!-- Center Block -->
    <rect x="360" y="320" width="480" height="260" rx="6" fill="url(#buildingGrad)" stroke="#DCE8DF" stroke-width="2"/>
    <rect x="340" y="300" width="520" height="25" rx="4" fill="url(#greenRoof)"/>
    
    <!-- Central Portico / Entrance -->
    <rect x="520" y="270" width="160" height="310" rx="6" fill="#FFFFFF" stroke="#DCE8DF" stroke-width="2"/>
    <!-- Triangular Pediment -->
    <polygon points="510,270 600,190 690,270" fill="url(#greenRoof)"/>
    <circle cx="600" cy="240" r="18" fill="#F9E076" stroke="#063F27" stroke-width="2"/>

    <!-- School Name Plaque on Building -->
    <rect x="535" y="280" width="130" height="26" rx="4" fill="#105A34"/>
    <text x="600" y="297" font-family="'Noto Sans Devanagari', sans-serif" font-size="10" font-weight="700" fill="#FFFFFF" text-anchor="middle">
      विद्या निकेतन
    </text>

    <!-- Pillars -->
    <rect x="535" y="320" width="16" height="240" fill="#E2ECE5"/>
    <rect x="575" y="320" width="16" height="240" fill="#E2ECE5"/>
    <rect x="610" y="320" width="16" height="240" fill="#E2ECE5"/>
    <rect x="650" y="320" width="16" height="240" fill="#E2ECE5"/>

    <!-- Arch Doors -->
    <path d="M575,560 L575,470 Q600,450 625,470 L625,560 Z" fill="#063F27"/>

    <!-- Left Wing Windows -->
    <g fill="#105A34" opacity="0.85">
      <rect x="385" y="350" width="45" height="50" rx="3"/>
      <rect x="450" y="350" width="45" height="50" rx="3"/>
      <rect x="385" y="420" width="45" height="50" rx="3"/>
      <rect x="450" y="420" width="45" height="50" rx="3"/>
      <rect x="385" y="490" width="45" height="50" rx="3"/>
      <rect x="450" y="490" width="45" height="50" rx="3"/>
      <!-- Right Wing Windows -->
      <rect x="705" y="350" width="45" height="50" rx="3"/>
      <rect x="770" y="350" width="45" height="50" rx="3"/>
      <rect x="705" y="420" width="45" height="50" rx="3"/>
      <rect x="770" y="420" width="45" height="50" rx="3"/>
      <rect x="705" y="490" width="45" height="50" rx="3"/>
      <rect x="770" y="490" width="45" height="50" rx="3"/>
    </g>

    <!-- Side Wings -->
    <rect x="180" y="380" width="190" height="200" fill="#F1F6F3" stroke="#DCE8DF"/>
    <rect x="170" y="365" width="210" height="18" fill="url(#greenRoof)"/>
    <rect x="205" y="405" width="40" height="45" rx="3" fill="#105A34" opacity="0.8"/>
    <rect x="260" y="405" width="40" height="45" rx="3" fill="#105A34" opacity="0.8"/>
    <rect x="315" y="405" width="40" height="45" rx="3" fill="#105A34" opacity="0.8"/>
    <rect x="205" y="475" width="40" height="45" rx="3" fill="#105A34" opacity="0.8"/>
    <rect x="260" y="475" width="40" height="45" rx="3" fill="#105A34" opacity="0.8"/>
    <rect x="315" y="475" width="40" height="45" rx="3" fill="#105A34" opacity="0.8"/>

    <rect x="830" y="380" width="190" height="200" fill="#F1F6F3" stroke="#DCE8DF"/>
    <rect x="820" y="365" width="210" height="18" fill="url(#greenRoof)"/>
    <rect x="850" y="405" width="40" height="45" rx="3" fill="#105A34" opacity="0.8"/>
    <rect x="905" y="405" width="40" height="45" rx="3" fill="#105A34" opacity="0.8"/>
    <rect x="960" y="405" width="40" height="45" rx="3" fill="#105A34" opacity="0.8"/>
    <rect x="850" y="475" width="40" height="45" rx="3" fill="#105A34" opacity="0.8"/>
    <rect x="905" y="475" width="40" height="45" rx="3" fill="#105A34" opacity="0.8"/>
    <rect x="960" y="475" width="40" height="45" rx="3" fill="#105A34" opacity="0.8"/>
  </g>

  <!-- National Flag Mast in Courtyard -->
  <g transform="translate(600, 540)">
    <rect x="-18" y="30" width="36" height="10" rx="3" fill="#063F27"/>
    <rect x="-12" y="22" width="24" height="8" rx="2" fill="#D4AF37"/>
    <line x1="0" y1="22" x2="0" y2="-170" stroke="#718075" stroke-width="4"/>
    <circle cx="0" cy="-172" r="5" fill="#D4AF37"/>
    <!-- Indian Tiranga -->
    <g transform="translate(2, -170)">
      <rect x="0" y="0" width="60" height="12" fill="#FF9933"/>
      <rect x="0" y="12" width="60" height="12" fill="#FFFFFF"/>
      <rect x="0" y="24" width="60" height="12" fill="#138808"/>
      <circle cx="30" cy="18" r="5" fill="none" stroke="#000080" stroke-width="1"/>
    </g>
  </g>

  <!-- Lush Campus Forecourt and Lawn -->
  <path d="M0,575 L450,575 L520,800 L0,800 Z" fill="#105A34"/>
  <path d="M1200,575 L750,575 L680,800 L1200,800 Z" fill="#105A34"/>
  <!-- Central Pathway -->
  <polygon points="450,575 750,575 680,800 520,800" fill="#E8F1EC"/>
  <!-- Lawn Highlights -->
  <ellipse cx="230" cy="650" rx="160" ry="40" fill="#16864A"/>
  <ellipse cx="970" cy="650" rx="160" ry="40" fill="#16864A"/>

  <!-- Forecourt Trees and Flowerbeds -->
  <g>
    <!-- Left Tree -->
    <path d="M140,650 Q130,580 120,530" stroke="#5D4037" stroke-width="8" stroke-linecap="round"/>
    <circle cx="115" cy="500" r="48" fill="#16864A"/>
    <circle cx="140" cy="485" r="42" fill="#43A76D"/>
    <!-- Right Tree -->
    <path d="M1060,650 Q1070,580 1080,530" stroke="#5D4037" stroke-width="8" stroke-linecap="round"/>
    <circle cx="1085" cy="500" r="48" fill="#16864A"/>
    <circle cx="1060" cy="485" r="42" fill="#43A76D"/>
  </g>

  <!-- Modern Bento Image Overlay -->
  <rect width="1200" height="800" fill="url(#overlayGrad)"/>

  <!-- Decorative Badge and Title Overlay -->
  <g transform="translate(80, 620)">
    <!-- Pill Badge -->
    <rect x="0" y="0" width="180" height="32" rx="16" fill="#16864A"/>
    <circle cx="16" cy="16" r="5" fill="#D9F0DF"/>
    <text x="32" y="21" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="800" fill="#FFFFFF" letter-spacing="1.5">
      {tag.upper()}
    </text>

    <!-- Main Title -->
    <text x="0" y="75" font-family="'Plus Jakarta Sans', sans-serif" font-size="38" font-weight="800" fill="#FFFFFF">
      {title}
    </text>
    <!-- Subtitle -->
    <text x="0" y="110" font-family="'Plus Jakarta Sans', sans-serif" font-size="18" font-weight="500" fill="#D9F0DF">
      {subtitle}
    </text>
  </g>
</svg>"""

# Hero & Campus images
create_svg(os.path.join(base_dir, "hero", "bento-campus.svg"), make_campus_svg("CAMPUS HEADQUARTERS", "+2 Higher Secondary School, Haldipokhar", "LEARN • GROW • ACHIEVE"))
create_svg(os.path.join(base_dir, "hero", "bento-students.svg"), make_campus_svg("STUDENT ACADEMIC LIFE", "Empowering Future Leaders through Values & Education", "CAMPUS EXCELLENCE"))
create_svg(os.path.join(base_dir, "campus", "campus-main.svg"), make_campus_svg("MAIN INSTITUTIONAL CAMPUS", "Potka, East Singhbhum, Jharkhand", "CAMPUS OVERVIEW"))
create_svg(os.path.join(base_dir, "campus", "campus-building.svg"), make_campus_svg("SENIOR SECONDARY WING", "Classrooms, Science Wings & Administrative Offices", "INFRASTRUCTURE"))
create_svg(os.path.join(base_dir, "campus", "campus-library.svg"), make_campus_svg("KNOWLEDGE RESOURCE CENTER", "Curated Reference Books, Journals & Study Spaces", "LIBRARY & READING"))
create_svg(os.path.join(base_dir, "campus", "campus-lab.svg"), make_campus_svg("MODERN SCIENCE & IT LABS", "Hands-on Practical Training & Scientific Discovery", "LABORATORIES"))
create_svg(os.path.join(base_dir, "campus", "campus-ground.svg"), make_campus_svg("SPORTS ARENA & PLAYGROUND", "Athletics, Team Sports & Physical Fitness Grounds", "SPORTS GROUND"))

def make_activity_svg(title, subtitle, tag, theme_icon="palette", primary_col="#105A34", sec_col="#43A76D"):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad_{tag}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#063F27"/>
      <stop offset="60%" stop-color="{primary_col}"/>
      <stop offset="100%" stop-color="#16864A"/>
    </linearGradient>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="rgba(255,255,255,0.15)"/>
      <stop offset="100%" stop-color="rgba(255,255,255,0.02)"/>
    </linearGradient>
    <pattern id="pat_{tag}" width="30" height="30" patternUnits="userSpaceOnUse">
      <circle cx="15" cy="15" r="1.5" fill="rgba(255,255,255,0.15)"/>
    </pattern>
  </defs>

  <rect width="800" height="600" fill="url(#bgGrad_{tag})"/>
  <rect width="800" height="600" fill="url(#pat_{tag})"/>

  <!-- Stylized Geometric Circles & Curves -->
  <circle cx="700" cy="100" r="220" fill="none" stroke="rgba(217, 240, 223, 0.15)" stroke-width="40"/>
  <circle cx="100" cy="500" r="180" fill="none" stroke="rgba(67, 167, 109, 0.2)" stroke-width="25"/>
  <circle cx="680" cy="480" r="120" fill="rgba(67, 167, 109, 0.1)"/>

  <!-- Centered Artistic Display Card -->
  <rect x="80" y="80" width="640" height="440" rx="20" fill="url(#cardGrad)" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>

  <!-- Thematic Center Illustration / Symbolism -->
  <g transform="translate(400, 250)">
    <!-- Decorative Glowing Aura -->
    <circle cx="0" cy="0" r="95" fill="rgba(217, 240, 223, 0.12)"/>
    <circle cx="0" cy="0" r="75" fill="rgba(255, 255, 255, 0.18)" stroke="#D9F0DF" stroke-width="2"/>
    
    <!-- Central Icon Badge -->
    <circle cx="0" cy="0" r="55" fill="#FFFFFF"/>
    <circle cx="0" cy="0" r="48" fill="{primary_col}"/>

    <!-- Icon Graphic -->
    <path d="M-18,12 L0,-24 L18,12 L8,12 L0,-4 L-8,12 Z" fill="#F9E076"/>
    <circle cx="0" cy="-28" r="5" fill="#F9E076"/>
    <circle cx="-16" cy="18" r="4" fill="#D9F0DF"/>
    <circle cx="0" cy="22" r="4" fill="#D9F0DF"/>
    <circle cx="16" cy="18" r="4" fill="#D9F0DF"/>
  </g>

  <!-- Typography & Information -->
  <g transform="translate(120, 390)">
    <!-- Badge -->
    <rect x="0" y="0" width="160" height="28" rx="14" fill="{sec_col}"/>
    <text x="80" y="18" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="800" fill="#FFFFFF" text-anchor="middle" letter-spacing="1.5">
      {tag.upper()}
    </text>

    <!-- Heading -->
    <text x="0" y="65" font-family="'Plus Jakarta Sans', sans-serif" font-size="30" font-weight="800" fill="#FFFFFF">
      {title}
    </text>
    <!-- Subtitle -->
    <text x="0" y="95" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="500" fill="#D9F0DF">
      {subtitle}
    </text>
  </g>
</svg>"""

# Activities
create_svg(os.path.join(base_dir, "activities", "cultural.svg"), make_activity_svg("CULTURAL ACTIVITIES", "Music, Dance, Drama, Folk Art & Heritage Celebrations", "CULTURE"))
create_svg(os.path.join(base_dir, "activities", "sports.svg"), make_activity_svg("SPORTS & ATHLETICS", "Track, Football, Volleyball, Badminton & Annual Sports Day", "SPORTS"))
create_svg(os.path.join(base_dir, "activities", "exhibitions.svg"), make_activity_svg("SCIENCE & ART EXHIBITIONS", "Student Working Models, Creative Innovation & Science Fairs", "EXHIBITIONS"))
create_svg(os.path.join(base_dir, "activities", "skills.svg"), make_activity_svg("SKILLS COMPETITION", "Creative Thinking, Problem Solving & Project Competitions", "SKILLS"))
create_svg(os.path.join(base_dir, "activities", "vocational.svg"), make_activity_svg("VOCATIONAL ACTIVITIES", "Skill-Based Learning, Hands-on Practical Life Competencies", "VOCATIONAL"))
create_svg(os.path.join(base_dir, "activities", "scout-guide.svg"), make_activity_svg("SCOUT & GUIDE TROOP", "Discipline, Leadership, Outdoor Survival & Community Service", "SCOUT & GUIDE"))

# Students
create_svg(os.path.join(base_dir, "students", "students-classroom.svg"), make_activity_svg("INTERACTIVE CLASSROOMS", "Engaging Curriculum, Concept Clarity & Academic Mentorship", "CLASSROOM"))
create_svg(os.path.join(base_dir, "students", "students-lab.svg"), make_activity_svg("LABORATORY PRACTICALS", "Scientific Inquisitiveness, Experimentation & Discovery", "PRACTICAL"))
create_svg(os.path.join(base_dir, "students", "students-assembly.svg"), make_activity_svg("MORNING ASSEMBLY", "Moral Values, Unity, Daily Motivation & National Anthem", "ASSEMBLY"))
create_svg(os.path.join(base_dir, "students", "students-group.svg"), make_activity_svg("PEER COLLABORATION", "Group Discussions, Team Projects & Cooperative Learning", "COLLABORATION"))

# Principal
principal_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 700" width="100%" height="100%">
  <defs>
    <linearGradient id="pGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#063F27"/>
      <stop offset="60%" stop-color="#105A34"/>
      <stop offset="100%" stop-color="#16864A"/>
    </linearGradient>
  </defs>
  <rect width="600" height="700" fill="url(#pGrad)"/>
  
  <!-- Architectural office background -->
  <rect x="50" y="50" width="500" height="600" rx="16" fill="rgba(255,255,255,0.06)" stroke="rgba(255,255,255,0.15)"/>
  <rect x="90" y="90" width="120" height="180" rx="4" fill="#063F27" opacity="0.6"/>
  <!-- Bookshelf lines -->
  <line x1="90" y1="130" x2="210" y2="130" stroke="#43A76D" stroke-width="2"/>
  <line x1="90" y1="170" x2="210" y2="170" stroke="#43A76D" stroke-width="2"/>
  <line x1="90" y1="210" x2="210" y2="210" stroke="#43A76D" stroke-width="2"/>

  <!-- Principal Silhouette & Desk -->
  <g transform="translate(300, 360)">
    <!-- Halo glow -->
    <circle cx="0" cy="-60" r="100" fill="rgba(217, 240, 223, 0.1)"/>
    <!-- Head -->
    <circle cx="0" cy="-80" r="50" fill="#E8F1EC"/>
    <!-- Torso / Suit -->
    <path d="M-90,90 C-80,-10 80,-10 90,90 Z" fill="#063F27"/>
    <!-- Shirt & Tie -->
    <polygon points="-15,10 0,-15 15,10" fill="#FFFFFF"/>
    <polygon points="-5,10 5,10 8,50 0,65 -8,50" fill="#AA771C"/>
    
    <!-- Executive Desk -->
    <rect x="-220" y="80" width="440" height="140" rx="6" fill="#063F27" stroke="#43A76D" stroke-width="2"/>
    <rect x="-240" y="70" width="480" height="20" rx="4" fill="#105A34"/>
    <!-- Desk Nameplate -->
    <rect x="-90" y="110" width="180" height="35" rx="4" fill="#D4AF37"/>
    <text x="0" y="132" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="800" fill="#063F27" text-anchor="middle" letter-spacing="1">
      OFFICE OF THE PRINCIPAL
    </text>
  </g>

  <!-- Bottom Information -->
  <g transform="translate(60, 580)">
    <rect x="0" y="0" width="190" height="28" rx="14" fill="#43A76D"/>
    <text x="95" y="18" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="800" fill="#FFFFFF" text-anchor="middle" letter-spacing="1">
      OFFICIAL PLACEHOLDER
    </text>
    <text x="0" y="55" font-family="'Plus Jakarta Sans', sans-serif" font-size="20" font-weight="700" fill="#FFFFFF">
      [Principal Name, M.A., B.Ed.]
    </text>
    <text x="0" y="78" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="500" fill="#D9F0DF">
      Head of Institution • +2 Vidya Niketan High School
    </text>
  </g>
</svg>"""

create_svg(os.path.join(base_dir, "principal", "principal-desk.svg"), principal_svg)

# Achievements
create_svg(os.path.join(base_dir, "achievements", "achievement-academic.svg"), make_activity_svg("ACADEMIC MERIT & AWARDS", "Board Examination Excellence & Scholastic Felicitations", "AWARDS"))
create_svg(os.path.join(base_dir, "achievements", "achievement-sports.svg"), make_activity_svg("SPORTS TROPHIES & MEDALS", "District & Block Level Athletic Championships", "CHAMPIONSHIP"))
create_svg(os.path.join(base_dir, "achievements", "achievement-cultural.svg"), make_activity_svg("CULTURAL & TALENT HONORS", "State & Inter-School Cultural Competitions", "EXCELLENCE"))

# Gallery Images 1 to 8
gallery_data = [
    ("CAMPUS ARCHITECTURE", "Green Institutional Entrance & Academic Wings", "CAMPUS"),
    ("MODERN SCIENCE LAB", "Secondary Students Physics & Chemistry Practicals", "CLASSROOM"),
    ("ANNUAL CULTURAL FESTIVAL", "Traditional Jharkhand Folk Dance Performance", "CULTURAL"),
    ("DISTRICT ATHLETIC MEET", "High School Sprint & Relay Races", "SPORTS"),
    ("DISTRICT SCIENCE FAIR", "Solar Energy & Sustainable Village Model", "EXHIBITIONS"),
    ("SCOUT & GUIDE CONTINGENT", "Morning Flag Drill & Disciplined March Past", "SCOUT & GUIDE"),
    ("VOCATIONAL SKILLS WORKSHOP", "Hands-on Practical Technical Skill Training", "VOCATIONAL"),
    ("SCHOLASTIC MERIT CEREMONY", "Honoring Outstanding Academic Performance", "ACHIEVEMENTS")
]

for i, (g_title, g_sub, g_cat) in enumerate(gallery_data, 1):
    create_svg(os.path.join(base_dir, "gallery", f"gallery-{i}.svg"), make_activity_svg(g_title, g_sub, g_cat))

print("All SVG artwork generated successfully!")
