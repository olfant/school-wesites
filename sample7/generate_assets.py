import os

base_dir = r"D:\school-website-v6\assets\img"

svgs = {}

# 1. School Logo
svgs["logo/school-logo.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <defs>
    <linearGradient id="logoBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#105A34"/>
      <stop offset="100%" stop-color="#063E27"/>
    </linearGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FCD34D"/>
      <stop offset="100%" stop-color="#F59E0B"/>
    </linearGradient>
    <filter id="shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#082D1E" flood-opacity="0.25"/>
    </filter>
  </defs>
  <circle cx="100" cy="100" r="94" fill="url(#logoBg)" stroke="#D9F0E0" stroke-width="4" filter="url(#shadow)"/>
  <circle cx="100" cy="100" r="84" fill="none" stroke="#36A66D" stroke-width="2" stroke-dasharray="4 3"/>
  <!-- Sun Rays of Knowledge -->
  <g opacity="0.4" stroke="#FCD34D" stroke-width="2">
    <line x1="100" y1="26" x2="100" y2="36"/>
    <line x1="126" y1="33" x2="120" y2="42"/>
    <line x1="147" y1="51" x2="139" y2="58"/>
    <line x1="156" y1="74" x2="146" y2="78"/>
    <line x1="74" y1="33" x2="80" y2="42"/>
    <line x1="53" y1="51" x2="61" y2="58"/>
    <line x1="44" y1="74" x2="54" y2="78"/>
  </g>
  <!-- Flame / Torch -->
  <path d="M100 40 C106 52 114 62 110 74 C107 81 99 84 96 79 C93 75 97 70 96 66 C93 72 88 77 89 83 C90 92 101 96 100 102 C96 98 94 92 90 90 C84 86 86 74 91 67 C97 59 96 48 100 40 Z" fill="url(#goldGrad)"/>
  <!-- Open Book of Wisdom -->
  <path d="M100 120 C85 108 55 110 42 115 C40 116 38 118 38 121 L38 148 C55 142 84 140 100 152 C116 140 145 142 162 148 L162 121 C162 118 160 116 158 115 C145 110 115 108 100 120 Z" fill="#FFFFFF"/>
  <path d="M100 120 L100 152" stroke="#105A34" stroke-width="2"/>
  <path d="M50 126 C65 122 83 124 94 130" stroke="#D9F0E0" stroke-width="2" fill="none"/>
  <path d="M50 134 C65 130 83 132 94 138" stroke="#D9F0E0" stroke-width="2" fill="none"/>
  <path d="M150 126 C135 122 117 124 106 130" stroke="#D9F0E0" stroke-width="2" fill="none"/>
  <path d="M150 134 C135 130 117 132 106 138" stroke="#D9F0E0" stroke-width="2" fill="none"/>
  <!-- Sprouting Nature Leaves -->
  <path d="M100 108 C108 98 124 100 128 108 C122 114 108 114 100 108 Z" fill="#36A66D"/>
  <path d="M100 108 C92 98 76 100 72 108 C78 114 92 114 100 108 Z" fill="#36A66D"/>
  <!-- Outer Banner Text Arcs -->
  <path id="textArcTop" d="M 30,100 A 70,70 0 1,1 170,100" fill="none"/>
  <text font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="8.5" fill="#D9F0E0" letter-spacing="1.2">
    <textPath href="#textArcTop" startOffset="50%" text-anchor="middle">
      CM SOE VNIKETAN HALDIPOKHAR
    </textPath>
  </text>
  <path id="textArcBottom" d="M 170,100 A 70,70 0 0,1 30,100" fill="none"/>
  <text font-family="'Plus Jakarta Sans', sans-serif" font-weight="600" font-size="8" fill="#FCD34D" letter-spacing="1.5">
    <textPath href="#textArcBottom" startOffset="50%" text-anchor="middle">
      GOVT +2 HIGH SCHOOL • POTKA
    </textPath>
  </text>
  <!-- Small Star Badges -->
  <polygon points="26,100 28,103 31,103 29,105 30,108 26,106 22,108 23,105 21,103 24,103" fill="#FCD34D"/>
  <polygon points="174,100 176,103 179,103 177,105 178,108 174,106 170,108 171,105 169,103 172,103" fill="#FCD34D"/>
</svg>'''

# 2. Hero Organic Illustration
svgs["hero/hero-organic-illustration.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 650" width="100%" height="100%">
  <defs>
    <linearGradient id="heroBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#D9F0E0"/>
      <stop offset="50%" stop-color="#EDF7EF"/>
      <stop offset="100%" stop-color="#FFFFFF"/>
    </linearGradient>
    <linearGradient id="foliageGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#36A66D"/>
      <stop offset="100%" stop-color="#105A34"/>
    </linearGradient>
    <linearGradient id="foliageGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#55C788"/>
      <stop offset="100%" stop-color="#16864A"/>
    </linearGradient>
    <linearGradient id="trunkGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#5D4037"/>
      <stop offset="100%" stop-color="#3E2723"/>
    </linearGradient>
    <filter id="softGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <!-- Large Nature-Inspired Organic Clip-Path / Pebble Background -->
  <path d="M 220,40 C 450,-30 680,60 740,220 C 800,380 750,540 600,600 C 450,660 250,640 120,530 C -10,420 10,240 70,140 C 130,40 180,50 220,40 Z" fill="url(#heroBg)" stroke="#DCE8DF" stroke-width="3"/>

  <!-- Distant Hill & Sun -->
  <circle cx="560" cy="180" r="90" fill="#FCD34D" opacity="0.35"/>
  <path d="M 80,480 Q 250,370 500,430 T 780,420 L 780,640 L 80,640 Z" fill="#EDF7EF" opacity="0.7"/>
  <path d="M 20,520 Q 300,440 600,490 T 800,470 L 800,650 L 20,650 Z" fill="#D9F0E0" opacity="0.8"/>

  <!-- School Heritage Building Silhouette -->
  <g transform="translate(180, 240)" opacity="0.85">
    <rect x="80" y="70" width="220" height="110" rx="6" fill="#082D1E"/>
    <polygon points="190,10 70,70 310,70" fill="#105A34"/>
    <!-- Central Clock Tower & Flag -->
    <rect x="160" y="-30" width="60" height="50" rx="4" fill="#105A34"/>
    <polygon points="190,-70 150,-30 230,-30" fill="#063E27"/>
    <circle cx="190" cy="-10" r="14" fill="#FFFFFF"/>
    <circle cx="190" cy="-10" r="12" fill="#082D1E"/>
    <line x1="190" y1="-10" x2="190" y2="-18" stroke="#FCD34D" stroke-width="2"/>
    <line x1="190" y1="-10" x2="196" y2="-10" stroke="#FCD34D" stroke-width="2"/>
    <!-- Indian National Tricolor Flagpole -->
    <line x1="190" y1="-70" x2="190" y2="-110" stroke="#475569" stroke-width="3"/>
    <path d="M 190,-110 L 222,-104 L 222,-90 L 190,-96 Z" fill="#FF9933"/>
    <path d="M 190,-104 L 222,-98 L 222,-88 L 190,-94 Z" fill="#FFFFFF"/>
    <path d="M 190,-98 L 222,-92 L 222,-82 L 190,-88 Z" fill="#138808"/>
    <!-- Windows & Arches -->
    <g fill="#D9F0E0" opacity="0.8">
      <rect x="100" y="90" width="24" height="34" rx="12"/>
      <rect x="140" y="90" width="24" height="34" rx="12"/>
      <rect x="216" y="90" width="24" height="34" rx="12"/>
      <rect x="256" y="90" width="24" height="34" rx="12"/>
      <path d="M 175,180 L 175,135 Q 190,125 205,135 L 205,180 Z" fill="#FCD34D"/>
    </g>
  </g>

  <!-- Big Green Banyan Tree of Wisdom (Left Side) -->
  <g>
    <!-- Trunk -->
    <path d="M 80,620 C 100,500 70,440 100,340 C 110,310 140,290 120,240 C 100,200 80,180 90,140" stroke="url(#trunkGrad)" stroke-width="32" stroke-linecap="round" fill="none"/>
    <path d="M 115,330 C 160,300 200,280 230,260" stroke="url(#trunkGrad)" stroke-width="16" stroke-linecap="round" fill="none"/>
    <path d="M 90,400 C 60,380 40,360 20,340" stroke="url(#trunkGrad)" stroke-width="14" stroke-linecap="round" fill="none"/>
    <!-- Aerial Roots (Organic Nature Concept) -->
    <path d="M 120,290 Q 130,420 110,580" stroke="#795548" stroke-width="4" stroke-dasharray="8 4" fill="none"/>
    <path d="M 150,300 Q 165,450 145,600" stroke="#795548" stroke-width="3" stroke-dasharray="6 3" fill="none"/>
    <!-- Lush Foliage Puffs -->
    <circle cx="100" cy="140" r="85" fill="url(#foliageGrad1)"/>
    <circle cx="170" cy="180" r="75" fill="url(#foliageGrad2)"/>
    <circle cx="60" cy="220" r="70" fill="url(#foliageGrad1)"/>
    <circle cx="140" cy="240" r="65" fill="url(#foliageGrad2)"/>
    <circle cx="210" cy="220" r="55" fill="url(#foliageGrad1)"/>
  </g>

  <!-- Front Student Characters (Study & Growth) -->
  <g transform="translate(420, 360)">
    <ellipse cx="60" cy="210" rx="45" ry="10" fill="#082D1E" opacity="0.2"/>
    <path d="M 35,110 L 85,110 L 95,200 L 25,200 Z" fill="#105A34"/>
    <path d="M 40,55 L 80,55 L 85,110 L 35,110 Z" fill="#FFFFFF" stroke="#DCE8DF" stroke-width="2"/>
    <polygon points="58,62 62,62 64,95 60,102 56,95" fill="#16864A"/>
    <circle cx="60" cy="35" r="20" fill="#DEB887"/>
    <path d="M 42,32 C 40,15 78,12 80,32 C 78,38 72,42 60,42 C 48,42 43,36 42,32 Z" fill="#2E1C0C"/>
    <path d="M 44,28 C 30,30 20,45 22,60 C 26,62 34,50 38,40 Z" fill="#2E1C0C"/>
    <path d="M 28,100 L 60,110 L 92,100 L 90,135 L 60,140 L 30,135 Z" fill="#EDF7EF" stroke="#105A34" stroke-width="2"/>
    <path d="M 60,110 L 60,140" stroke="#105A34" stroke-width="2"/>
    <path d="M 38,65 Q 26,90 35,108" stroke="#DEB887" stroke-width="8" stroke-linecap="round" fill="none"/>
    <path d="M 82,65 Q 94,90 85,108" stroke="#DEB887" stroke-width="8" stroke-linecap="round" fill="none"/>
  </g>

  <g transform="translate(560, 380)">
    <ellipse cx="60" cy="190" rx="42" ry="9" fill="#082D1E" opacity="0.2"/>
    <rect x="42" y="115" width="16" height="75" rx="4" fill="#082D1E"/>
    <rect x="62" y="115" width="16" height="75" rx="4" fill="#082D1E"/>
    <path d="M 40,55 L 80,55 L 82,118 L 38,118 Z" fill="#FFFFFF" stroke="#DCE8DF" stroke-width="2"/>
    <polygon points="58,62 62,62 64,95 60,102 56,95" fill="#16864A"/>
    <circle cx="60" cy="35" r="19" fill="#D2A679"/>
    <path d="M 42,30 C 42,14 78,14 78,30 C 76,22 66,18 58,18 C 50,18 44,22 42,30 Z" fill="#1A1A1A"/>
    <circle cx="95" cy="88" r="22" fill="#36A66D" stroke="#063E27" stroke-width="3"/>
    <path d="M 82,88 Q 95,78 108,88 Q 95,98 82,88 Z" fill="#D9F0E0"/>
    <line x1="95" y1="64" x2="95" y2="114" stroke="#FCD34D" stroke-width="3"/>
    <path d="M 90,114 L 100,114" stroke="#FCD34D" stroke-width="4"/>
  </g>

  <!-- Sprouting Sapling in foreground -->
  <g transform="translate(330, 480)">
    <path d="M 40,70 Q 40,40 20,20 Q 50,25 40,70 Z" fill="#36A66D"/>
    <path d="M 40,65 Q 45,30 65,15 Q 45,35 40,65 Z" fill="#55C788"/>
    <path d="M 40,70 L 40,90" stroke="#105A34" stroke-width="4"/>
    <ellipse cx="40" cy="92" rx="20" ry="6" fill="#5D4037"/>
  </g>

  <!-- Floating Butterflies -->
  <g transform="translate(260, 180) rotate(-15)">
    <path d="M 0,0 C 14,-22 36,-10 20,10 C 6,12 0,0 0,0 Z" fill="#FF7043" opacity="0.85"/>
    <path d="M 0,0 C -14,-22 -36,-10 -20,10 C -6,12 0,0 0,0 Z" fill="#FF7043" opacity="0.85"/>
    <path d="M 0,0 C 10,18 26,16 15,28 C 4,26 0,0 0,0 Z" fill="#FCD34D" opacity="0.85"/>
    <path d="M 0,0 C -10,18 -26,16 -15,28 C -4,26 0,0 0,0 Z" fill="#FCD34D" opacity="0.85"/>
  </g>
  <g transform="translate(680, 240) rotate(25)">
    <path d="M 0,0 C 10,-16 28,-8 16,8 C 4,10 0,0 0,0 Z" fill="#36A66D" opacity="0.8"/>
    <path d="M 0,0 C -10,-16 -28,-8 -16,8 C -4,10 0,0 0,0 Z" fill="#36A66D" opacity="0.8"/>
  </g>
</svg>'''

# 3. Campus Views
svgs["campus/campus-view.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 450" width="100%" height="100%">
  <defs>
    <linearGradient id="skyGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#E0F2FE"/>
      <stop offset="100%" stop-color="#EDF7EF"/>
    </linearGradient>
    <linearGradient id="bldgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#E2E8F0"/>
    </linearGradient>
  </defs>
  <rect width="700" height="450" fill="url(#skyGrad)"/>
  <circle cx="120" cy="80" r="45" fill="#FEF08A" opacity="0.7"/>
  <path d="M 0,260 Q 180,180 380,240 T 700,210 L 700,450 L 0,450 Z" fill="#D9F0E0"/>
  <path d="M 0,290 Q 240,240 520,290 T 700,270 L 700,450 L 0,450 Z" fill="#BBF7D0"/>

  <g transform="translate(100, 160)">
    <rect x="0" y="50" width="500" height="150" rx="8" fill="url(#bldgGrad)" stroke="#105A34" stroke-width="3"/>
    <rect x="-10" y="40" width="520" height="16" rx="4" fill="#105A34"/>
    <rect x="-5" y="115" width="510" height="8" fill="#16864A"/>
    <rect x="200" y="20" width="100" height="180" fill="#FFFFFF" stroke="#105A34" stroke-width="2"/>
    <polygon points="250,-15 180,22 320,22" fill="#063E27"/>
    <line x1="250" y1="-15" x2="250" y2="-55" stroke="#334155" stroke-width="3"/>
    <rect x="250" y="-55" width="28" height="16" fill="#FF9933"/>
    <rect x="250" y="-47" width="28" height="6" fill="#FFFFFF"/>
    <circle cx="264" cy="-44" r="2.5" fill="#000080"/>
    <rect x="250" y="-41" width="28" height="6" fill="#138808"/>
    <rect x="210" y="32" width="80" height="12" rx="3" fill="#D9F0E0"/>
    <text x="250" y="41" font-family="sans-serif" font-size="7" font-weight="bold" fill="#082D1E" text-anchor="middle">CM SOE GOVT +2</text>
    <g fill="#105A34" opacity="0.85">
      <rect x="30" y="65" width="30" height="40" rx="4"/>
      <rect x="80" y="65" width="30" height="40" rx="4"/>
      <rect x="130" y="65" width="30" height="40" rx="4"/>
      <rect x="340" y="65" width="30" height="40" rx="4"/>
      <rect x="390" y="65" width="30" height="40" rx="4"/>
      <rect x="440" y="65" width="30" height="40" rx="4"/>
      <rect x="30" y="135" width="30" height="45" rx="4"/>
      <rect x="80" y="135" width="30" height="45" rx="4"/>
      <rect x="130" y="135" width="30" height="45" rx="4"/>
      <rect x="340" y="135" width="30" height="45" rx="4"/>
      <rect x="390" y="135" width="30" height="45" rx="4"/>
      <rect x="440" y="135" width="30" height="45" rx="4"/>
      <path d="M 230,200 L 230,135 Q 250,115 270,135 L 270,200 Z" fill="#063E27"/>
      <path d="M 236,196 L 236,140 Q 250,126 264,140 L 264,196 Z" fill="#FCD34D" opacity="0.3"/>
    </g>
  </g>

  <path d="M 0,360 Q 350,340 700,360 L 700,450 L 0,450 Z" fill="#16864A"/>
  <path d="M 330,360 C 340,380 330,410 260,450 L 420,450 C 370,410 370,380 370,360 Z" fill="#E2E8F0"/>
  <circle cx="60" cy="340" r="40" fill="#105A34"/>
  <circle cx="90" cy="330" r="30" fill="#36A66D"/>
  <circle cx="620" cy="340" r="45" fill="#105A34"/>
  <circle cx="580" cy="350" r="35" fill="#36A66D"/>

  <g transform="translate(540, 40)">
    <rect width="130" height="36" rx="18" fill="#FFFFFF" stroke="#36A66D" stroke-width="2" filter="drop-shadow(0 4px 6px rgba(0,0,0,0.08))"/>
    <circle cx="20" cy="18" r="10" fill="#D9F0E0"/>
    <path d="M 16,18 Q 20,11 24,18 Q 20,25 16,18 Z" fill="#105A34"/>
    <text x="38" y="22" font-family="sans-serif" font-size="10" font-weight="700" fill="#105A34">Green Campus</text>
  </g>
</svg>'''

svgs["campus/campus-wide.svg"] = svgs["campus/campus-view.svg"]

# 4. Students
svgs["students/students-learning.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <defs>
    <linearGradient id="stuBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#EDF7EF"/>
      <stop offset="100%" stop-color="#D9F0E0"/>
    </linearGradient>
  </defs>
  <rect width="600" height="400" rx="24" fill="url(#stuBg)"/>
  <circle cx="500" cy="80" r="120" fill="#FFFFFF" opacity="0.5"/>
  <path d="M 50,330 Q 300,310 550,330 L 550,400 L 50,400 Z" fill="#105A34"/>
  <rect x="120" y="270" width="360" height="15" rx="6" fill="#8D6E63"/>
  <rect x="140" y="285" width="12" height="45" fill="#5D4037"/>
  <rect x="440" y="285" width="12" height="45" fill="#5D4037"/>

  <!-- Student Left -->
  <g transform="translate(140, 160)">
    <circle cx="40" cy="30" r="18" fill="#F5D0A9"/>
    <path d="M 25,25 C 25,12 55,12 55,25 C 55,30 50,36 40,36 C 30,36 25,30 25,25 Z" fill="#2D3748"/>
    <path d="M 20,50 L 60,50 L 65,115 L 15,115 Z" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <polygon points="38,55 42,55 44,80 40,86 36,80" fill="#16864A"/>
    <rect x="18" y="115" width="44" height="40" fill="#082D1E"/>
    <rect x="42" y="75" width="28" height="35" rx="3" fill="#FEF08A" stroke="#CA8A04" stroke-width="1.5"/>
  </g>

  <!-- Student Middle -->
  <g transform="translate(260, 140)">
    <circle cx="40" cy="30" r="18" fill="#E2B184"/>
    <path d="M 22,28 C 22,10 58,10 58,28 C 55,34 40,36 22,28 Z" fill="#1A202C"/>
    <path d="M 58,25 C 70,30 75,45 68,55" stroke="#1A202C" stroke-width="6" stroke-linecap="round" fill="none"/>
    <path d="M 20,50 L 60,50 L 65,115 L 15,115 Z" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <polygon points="38,55 42,55 44,80 40,86 36,80" fill="#16864A"/>
    <rect x="15" y="115" width="50" height="50" fill="#105A34"/>
    <rect x="25" y="70" width="30" height="40" rx="4" fill="#0F172A"/>
    <rect x="27" y="73" width="26" height="34" rx="2" fill="#38BDF8"/>
  </g>

  <!-- Student Right -->
  <g transform="translate(380, 160)">
    <circle cx="40" cy="30" r="18" fill="#FCD34D"/>
    <path d="M 24,24 C 24,12 56,12 56,24 C 56,32 50,35 40,35 C 30,35 24,32 24,24 Z" fill="#4B5563"/>
    <path d="M 20,50 L 60,50 L 65,115 L 15,115 Z" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <polygon points="38,55 42,55 44,80 40,86 36,80" fill="#16864A"/>
    <rect x="18" y="115" width="44" height="40" fill="#082D1E"/>
    <line x1="15" y1="85" x2="35" y2="95" stroke="#F59E0B" stroke-width="4" stroke-linecap="round"/>
  </g>

  <!-- Floating Leaf badges -->
  <g transform="translate(40, 40)">
    <rect width="180" height="38" rx="19" fill="#FFFFFF" stroke="#36A66D" stroke-width="1.5" filter="drop-shadow(0 4px 6px rgba(0,0,0,0.06))"/>
    <circle cx="22" cy="19" r="11" fill="#D9F0E0"/>
    <path d="M 18,19 Q 22,13 26,19 Q 22,25 18,19 Z" fill="#16864A"/>
    <text x="42" y="24" font-family="sans-serif" font-size="11" font-weight="700" fill="#105A34">Collaborative Learning</text>
  </g>
</svg>'''

svgs["students/student-growth.svg"] = svgs["students/students-learning.svg"]

# 5. Principal
svgs["principal/principal-placeholder.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 600" width="100%" height="100%">
  <defs>
    <linearGradient id="prBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#D9F0E0"/>
      <stop offset="50%" stop-color="#EDF7EF"/>
      <stop offset="100%" stop-color="#FFFFFF"/>
    </linearGradient>
    <linearGradient id="suitGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#105A34"/>
      <stop offset="100%" stop-color="#063E27"/>
    </linearGradient>
    <filter id="prDrop" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#082D1E" flood-opacity="0.15"/>
    </filter>
  </defs>

  <path d="M 120,40 C 300,-10 440,50 470,220 C 500,390 440,540 280,580 C 120,620 40,500 30,340 C 20,180 60,60 120,40 Z" fill="url(#prBg)" stroke="#36A66D" stroke-width="3" filter="url(#prDrop)"/>

  <g opacity="0.3" fill="#105A34">
    <rect x="80" y="100" width="14" height="60" rx="2"/>
    <rect x="98" y="110" width="12" height="50" rx="2"/>
    <rect x="114" y="95" width="16" height="65" rx="2"/>
    <rect x="360" y="105" width="14" height="55" rx="2"/>
    <rect x="378" y="90" width="18" height="70" rx="2"/>
  </g>

  <g transform="translate(150, 130)">
    <ellipse cx="100" cy="110" rx="45" ry="55" fill="#E2B184"/>
    <path d="M 52,100 C 50,60 150,60 148,100 C 145,75 130,68 100,68 C 70,68 55,75 52,100 Z" fill="#374151"/>
    <rect x="70" y="95" width="24" height="18" rx="4" fill="none" stroke="#1F2937" stroke-width="3"/>
    <rect x="106" y="95" width="24" height="18" rx="4" fill="none" stroke="#1F2937" stroke-width="3"/>
    <line x1="94" y1="104" x2="106" y2="104" stroke="#1F2937" stroke-width="3"/>
    <polygon points="75,175 100,210 125,175" fill="#FFFFFF"/>
    <polygon points="95,190 105,190 108,270 100,285 92,270" fill="#16864A"/>
    <path d="M 20,200 L 75,175 L 95,280 L 10,340 Z" fill="url(#suitGrad)"/>
    <path d="M 180,200 L 125,175 L 105,280 L 190,340 Z" fill="url(#suitGrad)"/>
    <path d="M 10,340 L 75,370 L 125,370 L 190,340 L 200,430 L 0,430 Z" fill="#082D1E"/>
  </g>

  <g transform="translate(110, 480)">
    <rect width="280" height="70" rx="35" fill="#FFFFFF" stroke="#105A34" stroke-width="2" filter="url(#prDrop)"/>
    <circle cx="40" cy="35" r="22" fill="#D9F0E0"/>
    <path d="M 40,22 L 44,30 L 53,31 L 46,38 L 48,47 L 40,42 L 32,47 L 34,38 L 27,31 L 36,30 Z" fill="#16864A"/>
    <text x="75" y="32" font-family="sans-serif" font-size="14" font-weight="700" fill="#082D1E">[Principal's Name]</text>
    <text x="75" y="50" font-family="sans-serif" font-size="11" font-weight="500" fill="#16864A">Official Desk • Placeholder</text>
  </g>
</svg>'''

# 6. Classrooms & Labs
svgs["classroom/smart-classroom.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <defs>
    <linearGradient id="clBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#F1F5F9"/>
      <stop offset="100%" stop-color="#E2E8F0"/>
    </linearGradient>
  </defs>
  <rect width="600" height="400" fill="url(#clBg)"/>
  <rect x="120" y="40" width="360" height="200" rx="8" fill="#082D1E" stroke="#16864A" stroke-width="6"/>
  <rect x="130" y="50" width="340" height="180" rx="4" fill="#063E27"/>
  <text x="150" y="80" font-family="monospace" font-size="14" fill="#D9F0E0">E = mc²  |  (a + b)² = a² + 2ab + b²</text>
  <text x="150" y="105" font-family="sans-serif" font-size="13" font-weight="bold" fill="#FCD34D">CM SOE SMART CLASSROOM • HALDIPOKHAR</text>
  <line x1="160" y1="190" x2="300" y2="190" stroke="#36A66D" stroke-width="2"/>
  <line x1="180" y1="210" x2="180" y2="120" stroke="#36A66D" stroke-width="2"/>
  <path d="M 180,190 Q 220,130 280,140" stroke="#38BDF8" stroke-width="3" fill="none"/>
  <path d="M 360,130 Q 380,150 400,130 T 440,130" stroke="#F43F5E" stroke-width="3" fill="none"/>
  <path d="M 360,150 Q 380,130 400,150 T 440,150" stroke="#10B981" stroke-width="3" fill="none"/>

  <rect x="80" y="240" width="90" height="130" rx="6" fill="#8D6E63" stroke="#5D4037" stroke-width="2"/>

  <g transform="translate(180, 260)">
    <rect x="0" y="20" width="380" height="25" rx="4" fill="#A1887F"/>
    <rect x="20" y="45" width="12" height="70" fill="#5D4037"/>
    <rect x="340" y="45" width="12" height="70" fill="#5D4037"/>
    <rect x="40" y="5" width="50" height="35" rx="3" fill="#3B82F6"/>
    <rect x="180" y="10" width="40" height="30" rx="2" fill="#FEF08A"/>
    <rect x="280" y="5" width="50" height="35" rx="3" fill="#10B981"/>
  </g>
</svg>'''

svgs["classroom/science-lab.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <rect width="600" height="400" fill="#EDF7EF"/>
  <rect x="50" y="200" width="500" height="180" rx="8" fill="#FFFFFF" stroke="#105A34" stroke-width="3"/>
  <rect x="40" y="185" width="520" height="20" rx="4" fill="#082D1E"/>
  <path d="M 120,185 L 135,140 L 135,110 L 145,110 L 145,140 L 160,185 Z" fill="#38BDF8" opacity="0.6" stroke="#0284C7" stroke-width="2"/>
  <ellipse cx="140" cy="170" rx="15" ry="5" fill="#0284C7"/>
  <g transform="translate(200, 110)">
    <rect x="0" y="50" width="120" height="25" rx="4" fill="#D9F0E0" stroke="#105A34" stroke-width="2"/>
    <rect x="15" y="10" width="12" height="50" rx="6" fill="#F43F5E" opacity="0.8"/>
    <rect x="40" y="5" width="12" height="55" rx="6" fill="#10B981" opacity="0.8"/>
    <rect x="65" y="15" width="12" height="45" rx="6" fill="#F59E0B" opacity="0.8"/>
    <rect x="90" y="10" width="12" height="50" rx="6" fill="#8B5CF6" opacity="0.8"/>
  </g>
  <g transform="translate(380, 70)">
    <rect x="30" y="110" width="50" height="8" rx="2" fill="#334155"/>
    <path d="M 50,110 L 50,50 L 30,30 L 60,30 L 70,50 L 70,110 Z" fill="#063E27"/>
    <circle cx="50" cy="50" r="14" fill="#FCD34D"/>
    <line x1="20" y1="20" x2="40" y2="40" stroke="#082D1E" stroke-width="8"/>
  </g>
</svg>'''

svgs["classroom/library-study.svg"] = svgs["classroom/smart-classroom.svg"]

# 7. Activities
svgs["activities/cultural.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <defs>
    <linearGradient id="culBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFBEB"/>
      <stop offset="100%" stop-color="#EDF7EF"/>
    </linearGradient>
  </defs>
  <rect width="600" height="400" rx="20" fill="url(#culBg)"/>
  <path d="M 0,0 Q 80,120 0,260 L 0,0 Z" fill="#105A34"/>
  <path d="M 600,0 Q 520,120 600,260 L 600,0 Z" fill="#105A34"/>
  <path d="M 0,0 Q 300,80 600,0 L 600,30 Q 300,100 0,30 Z" fill="#063E27"/>
  <g transform="translate(180, 90)">
    <circle cx="120" cy="50" r="24" fill="#F59E0B"/>
    <polygon points="120,15 105,35 135,35" fill="#D97706"/>
    <path d="M 120,74 L 120,170" stroke="#B45309" stroke-width="12" stroke-linecap="round"/>
    <path d="M 80,95 Q 120,80 160,95" stroke="#B45309" stroke-width="10" stroke-linecap="round" fill="none"/>
    <path d="M 80,95 Q 60,60 50,75" stroke="#B45309" stroke-width="8" stroke-linecap="round" fill="none"/>
    <path d="M 160,95 Q 180,60 190,75" stroke="#B45309" stroke-width="8" stroke-linecap="round" fill="none"/>
    <path d="M 120,150 L 80,210 Q 120,230 160,210 Z" fill="#DC2626"/>
    <path d="M 120,170 L 90,250 L 70,250" stroke="#B45309" stroke-width="8" stroke-linecap="round" fill="none"/>
    <path d="M 120,170 L 150,220 L 150,250" stroke="#B45309" stroke-width="8" stroke-linecap="round" fill="none"/>
  </g>
  <g transform="translate(380, 240)">
    <ellipse cx="40" cy="50" rx="30" ry="20" fill="#78350F"/>
    <ellipse cx="40" cy="46" rx="24" ry="14" fill="#FEF3C7" stroke="#1F2937" stroke-width="2"/>
    <circle cx="40" cy="46" r="8" fill="#1F2937"/>
    <ellipse cx="105" cy="55" rx="35" ry="24" fill="#92400E"/>
    <ellipse cx="105" cy="50" rx="28" ry="17" fill="#FEF3C7" stroke="#1F2937" stroke-width="2"/>
    <circle cx="105" cy="50" r="10" fill="#1F2937"/>
  </g>
</svg>'''

svgs["activities/sports.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <rect width="600" height="400" rx="20" fill="#EDF7EF"/>
  <path d="M 0,380 C 180,350 420,350 600,380 L 600,400 L 0,400 Z" fill="#DC2626"/>
  <path d="M 0,330 C 180,290 420,290 600,330" stroke="#FFFFFF" stroke-width="3" stroke-dasharray="10 8" fill="none"/>
  <path d="M 0,280 C 180,240 420,240 600,280" stroke="#FFFFFF" stroke-width="3" fill="none"/>
  <circle cx="120" cy="270" r="35" fill="#FFFFFF" stroke="#0F172A" stroke-width="3"/>
  <polygon points="120,255 130,263 126,275 114,275 110,263" fill="#0F172A"/>
  <g transform="translate(260, 80)">
    <circle cx="50" cy="40" r="20" fill="#105A34"/>
    <path d="M 50,60 L 65,120 L 40,165 L 15,160" stroke="#105A34" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
    <path d="M 65,120 L 95,150 L 115,190" stroke="#105A34" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
    <path d="M 50,75 L 20,105 L 10,95" stroke="#105A34" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
    <path d="M 50,75 L 85,90 L 95,115" stroke="#105A34" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
  </g>
  <g transform="translate(430, 180)">
    <ellipse cx="60" cy="50" rx="30" ry="38" fill="none" stroke="#2563EB" stroke-width="4"/>
    <line x1="60" y1="88" x2="60" y2="170" stroke="#1E293B" stroke-width="6" stroke-linecap="round"/>
    <circle cx="110" cy="60" r="10" fill="#F8FAFC" stroke="#94A3B8" stroke-width="2"/>
    <polygon points="110,60 125,40 135,50" fill="#E2E8F0"/>
  </g>
</svg>'''

svgs["activities/exhibitions.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <rect width="600" height="400" rx="20" fill="#F0FDF4"/>
  <rect x="60" y="80" width="480" height="260" rx="12" fill="#FFFFFF" stroke="#36A66D" stroke-width="3"/>
  <rect x="50" y="60" width="500" height="30" rx="6" fill="#105A34"/>
  <text x="300" y="82" font-family="sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">ANNUAL SCIENCE &amp; ART EXHIBITION</text>
  <g transform="translate(130, 140)">
    <circle cx="80" cy="80" r="28" fill="#F59E0B"/>
    <ellipse cx="80" cy="80" rx="70" ry="25" fill="none" stroke="#94A3B8" stroke-width="2" stroke-dasharray="4 3"/>
    <circle cx="130" cy="70" r="10" fill="#38BDF8"/>
    <ellipse cx="80" cy="80" rx="95" ry="36" fill="none" stroke="#94A3B8" stroke-width="2" stroke-dasharray="4 3"/>
    <circle cx="30" cy="95" r="12" fill="#EF4444"/>
    <rect x="76" y="108" width="8" height="50" fill="#475569"/>
    <rect x="55" y="158" width="50" height="8" rx="2" fill="#334155"/>
  </g>
  <g transform="translate(360, 150)">
    <rect x="40" y="20" width="60" height="50" rx="8" fill="#475569"/>
    <circle cx="55" cy="40" r="6" fill="#38BDF8"/>
    <circle cx="85" cy="40" r="6" fill="#38BDF8"/>
    <rect x="30" y="75" width="80" height="70" rx="8" fill="#1E293B"/>
    <line x1="15" y1="90" x2="30" y2="90" stroke="#F59E0B" stroke-width="8" stroke-linecap="round"/>
    <line x1="110" y1="90" x2="125" y2="90" stroke="#F59E0B" stroke-width="8" stroke-linecap="round"/>
  </g>
</svg>'''

svgs["activities/skills-competition.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <rect width="600" height="400" rx="20" fill="#EDF7EF"/>
  <g transform="translate(200, 150)" fill="#105A34">
    <circle cx="80" cy="80" r="60" fill="#36A66D" opacity="0.8"/>
    <circle cx="80" cy="80" r="30" fill="#EDF7EF"/>
  </g>
  <g transform="translate(310, 90)">
    <circle cx="60" cy="60" r="45" fill="#16864A"/>
    <circle cx="60" cy="60" r="22" fill="#EDF7EF"/>
  </g>
  <g transform="translate(240, 40)">
    <path d="M 60,30 C 35,30 20,50 25,75 C 30,90 45,100 45,115 L 75,115 C 75,100 90,90 95,75 C 100,50 85,30 60,30 Z" fill="#FCD34D" stroke="#D97706" stroke-width="3"/>
    <rect x="47" y="118" width="26" height="6" fill="#6B7280"/>
    <rect x="50" y="126" width="20" height="6" fill="#6B7280"/>
  </g>
  <g transform="translate(140, 270)">
    <rect width="320" height="50" rx="25" fill="#FFFFFF" stroke="#105A34" stroke-width="2"/>
    <text x="160" y="32" font-family="sans-serif" font-size="14" font-weight="bold" fill="#082D1E" text-anchor="middle">CREATIVITY • LOGIC • INNOVATION</text>
  </g>
</svg>'''

svgs["activities/vocational.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <rect width="600" height="400" rx="20" fill="#F0FDF4"/>
  <rect x="80" y="240" width="440" height="120" rx="6" fill="#78350F"/>
  <rect x="60" y="220" width="480" height="24" rx="4" fill="#92400E"/>
  <g transform="translate(130, 130)">
    <rect x="10" y="10" width="120" height="80" rx="6" fill="#0F172A"/>
    <rect x="16" y="16" width="108" height="68" rx="3" fill="#10B981"/>
    <polygon points="0,95 140,95 130,105 10,105" fill="#64748B"/>
  </g>
  <g transform="translate(320, 110)">
    <polygon points="50,10 180,10 150,110 20,110" fill="#1E3A8A" stroke="#3B82F6" stroke-width="3"/>
    <line x1="85" y1="10" x2="55" y2="110" stroke="#60A5FA" stroke-width="2"/>
    <line x1="120" y1="10" x2="90" y2="110" stroke="#60A5FA" stroke-width="2"/>
    <line x1="155" y1="10" x2="125" y2="110" stroke="#60A5FA" stroke-width="2"/>
  </g>
</svg>'''

svgs["activities/scout-guide.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <defs>
    <linearGradient id="scBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#D9F0E0"/>
      <stop offset="100%" stop-color="#EDF7EF"/>
    </linearGradient>
  </defs>
  <rect width="600" height="400" rx="20" fill="url(#scBg)"/>
  <g transform="translate(180, 140)">
    <polygon points="120,30 20,180 220,180" fill="#105A34"/>
    <polygon points="120,30 120,180 220,180" fill="#063E27"/>
    <polygon points="120,50 80,180 160,180" fill="#FCD34D"/>
    <line x1="120" y1="30" x2="120" y2="5" stroke="#FFFFFF" stroke-width="3"/>
    <polygon points="120,5 145,15 120,25" fill="#EF4444"/>
  </g>
  <g transform="translate(420, 240)">
    <line x1="20" y1="80" x2="80" y2="50" stroke="#78350F" stroke-width="10" stroke-linecap="round"/>
    <line x1="20" y1="50" x2="80" y2="80" stroke="#78350F" stroke-width="10" stroke-linecap="round"/>
    <path d="M 50,70 C 40,55 35,40 50,15 C 65,40 60,55 50,70 Z" fill="#EF4444"/>
    <path d="M 50,68 C 45,55 42,45 50,30 C 58,45 55,55 50,68 Z" fill="#F59E0B"/>
  </g>
  <g transform="translate(70, 70)">
    <circle cx="50" cy="50" r="45" fill="#FFFFFF" stroke="#16864A" stroke-width="3"/>
    <path d="M 50,20 C 56,36 64,48 50,70 C 36,48 44,36 50,20 Z" fill="#16864A"/>
    <path d="M 50,55 C 65,45 78,55 70,68 C 60,65 54,62 50,70 Z" fill="#16864A"/>
    <path d="M 50,55 C 35,45 22,55 30,68 C 40,65 46,62 50,70 Z" fill="#16864A"/>
  </g>
</svg>'''

# 8. Achievements
svgs["achievements/trophy-merit.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <linearGradient id="goldTr" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FDE047"/>
      <stop offset="50%" stop-color="#EAB308"/>
      <stop offset="100%" stop-color="#CA8A04"/>
    </linearGradient>
  </defs>
  <rect width="500" height="500" rx="24" fill="#EDF7EF"/>
  <g stroke="#16864A" stroke-width="6" fill="none" opacity="0.7">
    <path d="M 120,320 C 80,220 120,120 220,90"/>
    <path d="M 380,320 C 420,220 380,120 280,90"/>
  </g>
  <g transform="translate(150, 110)">
    <path d="M 30,50 C -20,50 -20,130 30,130" stroke="url(#goldTr)" stroke-width="14" fill="none"/>
    <path d="M 170,50 C 220,50 220,130 170,130" stroke="url(#goldTr)" stroke-width="14" fill="none"/>
    <path d="M 20,40 L 180,40 C 180,140 130,180 100,180 C 70,180 20,140 20,40 Z" fill="url(#goldTr)" stroke="#A16207" stroke-width="4"/>
    <polygon points="100,80 105,95 120,95 108,105 112,120 100,110 88,120 92,105 80,95 95,95" fill="#FFFFFF"/>
    <rect x="90" y="180" width="20" height="50" fill="url(#goldTr)"/>
    <polygon points="60,230 140,230 150,260 50,260" fill="url(#goldTr)"/>
    <rect x="40" y="260" width="120" height="50" rx="6" fill="#082D1E"/>
    <rect x="55" y="275" width="90" height="20" rx="3" fill="#D9F0E0"/>
    <text x="100" y="290" font-family="sans-serif" font-size="10" font-weight="bold" fill="#082D1E" text-anchor="middle">EXCELLENCE</text>
  </g>
</svg>'''

svgs["achievements/academic-excellence.svg"] = svgs["achievements/trophy-merit.svg"]

# 9. Gallery
gallery_titles = [
  ("gallery-1.svg", "Campus Green Quadrangle", "#105A34"),
  ("gallery-2.svg", "High School Science Laboratory", "#063E27"),
  ("gallery-3.svg", "Smart Interactive Classroom", "#16864A"),
  ("gallery-4.svg", "Annual Sports Track & Field", "#DC2626"),
  ("gallery-5.svg", "State Cultural Festival Folk Dance", "#D97706"),
  ("gallery-6.svg", "Bharat Scouts & Guides Camporee", "#082D1E"),
  ("gallery-7.svg", "Science & Eco Innovation Fair", "#36A66D"),
  ("gallery-8.svg", "School Central Library & Reading Room", "#78350F"),
  ("gallery-9.svg", "Plantation & Nature Conservation Drive", "#15803D"),
  ("gallery-10.svg", "Computer & Digital Literacy Lab", "#2563EB"),
  ("gallery-11.svg", "Art, Craft & Skills Exhibition", "#9333EA"),
  ("gallery-12.svg", "Morning Assembly & Moral Education", "#0F766E")
]

for filename, title, color in gallery_titles:
  svgs[f"gallery/{filename}"] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 420" width="100%" height="100%">
  <defs>
    <linearGradient id="gGrad_{filename[:9].replace('.','_')}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#EDF7EF"/>
      <stop offset="60%" stop-color="#D9F0E0"/>
      <stop offset="100%" stop-color="{color}"/>
    </linearGradient>
  </defs>
  <rect width="600" height="420" rx="16" fill="url(#gGrad_{filename[:9].replace('.','_')})"/>
  <circle cx="300" cy="180" r="110" fill="#FFFFFF" opacity="0.4"/>
  <g transform="translate(240, 120)">
    <circle cx="60" cy="60" r="50" fill="{color}" opacity="0.9"/>
    <path d="M 40,60 L 55,75 L 85,45" stroke="#FFFFFF" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
  </g>
  <rect x="0" y="320" width="600" height="100" fill="#082D1E" opacity="0.92"/>
  <text x="40" y="360" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="700" fill="#FFFFFF">{title}</text>
  <text x="40" y="388" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" fill="#D9F0E0">CM SOE UPG GOVT+2 SCHOOL VNIKETAN HALDIPOKHAR</text>
  <circle cx="540" cy="370" r="20" fill="{color}"/>
  <polygon points="536,362 546,370 536,378" fill="#FFFFFF"/>
</svg>'''

# 10. Decorative Elements
svgs["decorative/leaf-cluster.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <path d="M 50,90 Q 50,50 15,30 Q 60,35 50,90 Z" fill="#36A66D" opacity="0.85"/>
  <path d="M 50,85 Q 55,45 85,25 Q 55,40 50,85 Z" fill="#16864A" opacity="0.75"/>
  <circle cx="50" cy="20" r="5" fill="#FCD34D"/>
</svg>'''

svgs["decorative/organic-blob.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <path d="M 50,30 C 120,5 180,40 190,110 C 200,180 140,200 80,180 C 20,160 -10,100 15,50 C 25,30 40,35 50,30 Z" fill="#D9F0E0" opacity="0.6"/>
</svg>'''

svgs["decorative/leaf-pattern.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" width="60" height="60" viewBox="0 0 60 60">
  <path d="M 10,50 Q 25,20 50,10 Q 35,40 10,50 Z" fill="#36A66D" opacity="0.12"/>
</svg>'''

for rel_path, content in svgs.items():
  full_path = os.path.join(base_dir, rel_path)
  os.makedirs(os.path.dirname(full_path), exist_ok=True)
  with open(full_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Generated {len(svgs)} SVG files successfully.")
