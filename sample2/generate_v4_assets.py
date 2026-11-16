import os

base_dir = r"c:\Users\ACER\OneDrive\Desktop\school\school-website-v4\assets\img"

def save_svg(relative_path, content):
    full_path = os.path.join(base_dir, relative_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Created: {relative_path}")

# 1. School Logo
logo_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <linearGradient id="logoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#063E27"/>
      <stop offset="40%" stop-color="#105A34"/>
      <stop offset="100%" stop-color="#16864A"/>
    </linearGradient>
    <linearGradient id="goldRing" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FBBF24"/>
      <stop offset="50%" stop-color="#D97706"/>
      <stop offset="100%" stop-color="#B45309"/>
    </linearGradient>
    <filter id="dropShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-opacity="0.3"/>
    </filter>
  </defs>

  <!-- Outer Ring -->
  <circle cx="250" cy="250" r="240" fill="none" stroke="#105A34" stroke-width="4" stroke-dasharray="10 5"/>
  <circle cx="250" cy="250" r="230" fill="url(#goldRing)" filter="url(#dropShadow)"/>
  <circle cx="250" cy="250" r="222" fill="#063E27"/>
  <circle cx="250" cy="250" r="185" fill="#FFFFFF"/>
  <circle cx="250" cy="250" r="180" fill="none" stroke="#16864A" stroke-width="2"/>

  <!-- Curved Text Paths -->
  <path id="topArc" d="M 75 250 A 175 175 0 0 1 425 250" fill="none"/>
  <path id="bottomArc" d="M 425 250 A 175 175 0 0 1 75 250" fill="none"/>

  <text font-family="'Noto Sans Devanagari', 'Segoe UI', sans-serif" font-size="20" font-weight="800" fill="#F8FAFC" letter-spacing="1.5">
    <textPath href="#topArc" startOffset="50%" text-anchor="middle">
      +2 राजकीयकृत विद्या निकेतन उच्च विद्यालय
    </textPath>
  </text>
  <text font-family="'Plus Jakarta Sans', 'Segoe UI', sans-serif" font-size="14" font-weight="700" fill="#FDE68A" letter-spacing="2">
    <textPath href="#bottomArc" startOffset="50%" text-anchor="middle">
      HALDIPOKHAR • POTKA • EAST SINGHBHUM
    </textPath>
  </text>

  <!-- Center Emblem -->
  <g transform="translate(250, 250)">
    <circle cx="0" cy="0" r="120" fill="#EAF5ED" stroke="#105A34" stroke-width="3"/>
    
    <!-- Sun Rays & Rising Sun -->
    <path d="M 0 -75 L 0 -100 M 35 -65 L 55 -85 M -35 -65 L -55 -85 M 70 -30 L 95 -35 M -70 -30 L -95 -35" stroke="#F59E0B" stroke-width="3" stroke-linecap="round"/>
    <circle cx="0" cy="-20" r="45" fill="#F59E0B" opacity="0.9"/>
    
    <!-- Open Book -->
    <path d="M -60 25 C -25 15 -10 25 0 35 C 10 25 25 15 60 25 L 60 55 C 25 45 10 55 0 65 C -10 55 -25 45 -60 55 Z" fill="#FFFFFF" stroke="#063E27" stroke-width="3"/>
    <line x1="0" y1="35" x2="0" y2="65" stroke="#063E27" stroke-width="3"/>
    <path d="M -50 33 C -25 25 -10 33 0 42" stroke="#105A34" stroke-width="1.5" fill="none"/>
    <path d="M 50 33 C 25 25 10 33 0 42" stroke="#105A34" stroke-width="1.5" fill="none"/>

    <!-- Lamp of Knowledge (Deepam) -->
    <path d="M -22 15 C -22 2 22 2 22 15 C 22 25 -22 25 -22 15 Z" fill="#D97706"/>
    <path d="M 0 -12 C 8 2 0 15 0 15 C 0 15 -8 2 0 -12 Z" fill="#EF4444"/>
    <circle cx="0" cy="3" r="3" fill="#FDE047"/>

    <!-- Motto Ribbon -->
    <rect x="-85" y="78" width="170" height="26" rx="6" fill="#105A34"/>
    <text x="0" y="96" font-family="'Noto Sans Devanagari', sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">
      विद्या ददाति विनयं
    </text>
  </g>
</svg>"""
save_svg("logo/school-logo.svg", logo_svg)

# Helper template generator for cinematic SVG artwork
def make_cinematic_svg(title, subtitle, category_tag, accent_theme="green", scene_type="campus"):
    color_map = {
        "green": ("#063E27", "#105A34", "#16864A", "#35A66B"),
        "emerald": ("#082E20", "#0D5C3A", "#1FA86A", "#6EE7B7"),
        "gold": ("#063E27", "#105A34", "#D97706", "#F59E0B"),
        "blue": ("#062E3B", "#0F526B", "#16864A", "#38BDF8")
    }
    c1, c2, c3, c4 = color_map.get(accent_theme, color_map["green"])

    # Architectural & Scene Shapes based on scene_type
    scene_elements = ""
    if scene_type == "hero":
        scene_elements = f"""
        <!-- Sky & Atmosphere -->
        <rect width="1920" height="1080" fill="url(#heroSky)"/>
        <circle cx="1550" cy="220" r="180" fill="#FDE68A" opacity="0.4" filter="url(#glow)"/>
        
        <!-- Mountains & Green Hills -->
        <path d="M 0 650 Q 400 480 900 620 T 1920 540 L 1920 1080 L 0 1080 Z" fill="#0C4A2B" opacity="0.8"/>
        <path d="M 0 720 Q 550 560 1200 700 T 1920 660 L 1920 1080 L 0 1080 Z" fill="#083821"/>

        <!-- School Building Architecture -->
        <rect x="350" y="440" width="1220" height="380" rx="8" fill="#FFFFFF"/>
        <rect x="350" y="420" width="1220" height="30" fill="#105A34"/>
        <polygon points="960,300 320,430 1600,430" fill="#063E27"/>
        
        <!-- Columns & Arches -->
        <g fill="#EAF5ED" stroke="#105A34" stroke-width="2">
            <rect x="420" y="460" width="50" height="340"/>
            <rect x="540" y="460" width="50" height="340"/>
            <rect x="660" y="460" width="50" height="340"/>
            <rect x="780" y="460" width="50" height="340"/>
            <rect x="1090" y="460" width="50" height="340"/>
            <rect x="1210" y="460" width="50" height="340"/>
            <rect x="1330" y="460" width="50" height="340"/>
            <rect x="1450" y="460" width="50" height="340"/>
        </g>
        
        <!-- Grand Portico & Clock Tower -->
        <rect x="860" y="340" width="200" height="480" fill="#F8FAFC" stroke="#16864A" stroke-width="4"/>
        <circle cx="960" cy="400" r="35" fill="#E2E8F0" stroke="#063E27" stroke-width="4"/>
        <line x1="960" y1="400" x2="960" y2="380" stroke="#063E27" stroke-width="4"/>
        <line x1="960" y1="400" x2="975" y2="400" stroke="#063E27" stroke-width="4"/>
        
        <!-- Indian National Tricolor Flag -->
        <line x1="960" y1="300" x2="960" y2="210" stroke="#64748B" stroke-width="6"/>
        <path d="M 960 215 C 990 205 1020 225 1050 215 L 1050 255 C 1020 265 990 245 960 255 Z" fill="#FF9933"/>
        <path d="M 960 230 C 990 220 1020 240 1050 230 L 1050 245 C 1020 255 990 235 960 245 Z" fill="#FFFFFF"/>
        <circle cx="1005" cy="237" r="5" fill="#000080"/>
        <path d="M 960 245 C 990 235 1020 255 1050 245 L 1050 260 C 1020 270 990 250 960 260 Z" fill="#138808"/>

        <!-- Foreground Lawn & Trees -->
        <rect x="0" y="800" width="1920" height="280" fill="#0A4226"/>
        <path d="M 0 880 C 400 840 1400 840 1920 880 L 1920 1080 L 0 1080 Z" fill="#063E27"/>
        
        <!-- Pathway -->
        <polygon points="960,820 650,1080 1270,1080" fill="#E2E8F0" opacity="0.3"/>
        
        <!-- Cinematic Trees -->
        <g fill="#16864A" opacity="0.95">
          <circle cx="200" cy="780" r="140"/>
          <circle cx="280" cy="720" r="110"/>
          <circle cx="140" cy="740" r="90"/>
          <rect x="190" y="860" width="25" height="150" fill="#451A03"/>

          <circle cx="1720" cy="780" r="150"/>
          <circle cx="1640" cy="710" r="120"/>
          <circle cx="1800" cy="730" r="100"/>
          <rect x="1710" y="860" width="28" height="150" fill="#451A03"/>
        </g>
        """
    elif scene_type == "campus":
        scene_elements = f"""
        <!-- Campus Architecture Illustration -->
        <rect width="1200" height="800" fill="url(#heroSky)"/>
        <path d="M 0 450 Q 300 380 600 430 T 1200 400 L 1200 800 L 0 800 Z" fill="#0E4A2D"/>
        
        <!-- School Complex -->
        <rect x="150" y="320" width="900" height="340" fill="#FFFFFF" rx="6"/>
        <rect x="150" y="300" width="900" height="25" fill="#105A34"/>
        <polygon points="600,200 120,310 1080,310" fill="#063E27"/>
        
        <!-- Windows and Architecture -->
        <g fill="#063E27" opacity="0.75">
            <rect x="220" y="360" width="60" height="80" rx="3"/>
            <rect x="320" y="360" width="60" height="80" rx="3"/>
            <rect x="420" y="360" width="60" height="80" rx="3"/>
            <rect x="720" y="360" width="60" height="80" rx="3"/>
            <rect x="820" y="360" width="60" height="80" rx="3"/>
            <rect x="920" y="360" width="60" height="80" rx="3"/>

            <rect x="220" y="480" width="60" height="80" rx="3"/>
            <rect x="320" y="480" width="60" height="80" rx="3"/>
            <rect x="420" y="480" width="60" height="80" rx="3"/>
            <rect x="720" y="480" width="60" height="80" rx="3"/>
            <rect x="820" y="480" width="60" height="80" rx="3"/>
            <rect x="920" y="480" width="60" height="80" rx="3"/>
        </g>
        
        <!-- Center Arch Entrance -->
        <path d="M 540 660 L 540 450 A 60 60 0 0 1 660 450 L 660 660 Z" fill="#063E27"/>
        
        <!-- Flagpost -->
        <line x1="600" y1="200" x2="600" y2="120" stroke="#CBD5E1" stroke-width="4"/>
        <rect x="600" y="125" width="55" height="35" fill="#FF9933"/>
        
        <!-- Lawn & Pathways -->
        <rect x="0" y="650" width="1200" height="150" fill="#105A34"/>
        <path d="M 600 660 L 400 800 L 800 800 Z" fill="#E2E8F0" opacity="0.3"/>
        
        <!-- Trees -->
        <circle cx="80" cy="620" r="90" fill="#16864A"/>
        <circle cx="1120" cy="620" r="90" fill="#16864A"/>
        """
    elif scene_type == "students":
        scene_elements = f"""
        <!-- Students Learning Scene -->
        <rect width="1200" height="800" fill="url(#heroSky)"/>
        <circle cx="600" cy="750" r="500" fill="#EAF5ED" opacity="0.8"/>
        
        <!-- Modern Learning Pod / Table -->
        <ellipse cx="600" cy="580" rx="420" ry="90" fill="#FFFFFF" stroke="#DCE7DE" stroke-width="4"/>
        <ellipse cx="600" cy="580" rx="380" ry="70" fill="#F1F8F3"/>
        
        <!-- Laptops, Books & Notepads on Table -->
        <rect x="540" y="540" width="120" height="60" rx="6" fill="#334155"/>
        <polygon points="530,600 670,600 680,620 520,620" fill="#64748B"/>
        <rect x="360" y="550" width="70" height="50" rx="3" fill="#105A34"/>
        <rect x="760" y="555" width="80" height="45" rx="3" fill="#D97706"/>
        
        <!-- Student Avatars / Silhouettes -->
        <!-- Student 1 (Left) -->
        <circle cx="340" cy="380" r="45" fill="#063E27"/>
        <path d="M 270 510 C 270 440 310 430 340 430 C 370 430 410 440 410 510 Z" fill="#105A34"/>
        
        <!-- Student 2 (Center) -->
        <circle cx="600" cy="350" r="48" fill="#063E27"/>
        <path d="M 520 490 C 520 410 560 400 600 400 C 640 400 680 410 680 490 Z" fill="#16864A"/>
        
        <!-- Student 3 (Right) -->
        <circle cx="860" cy="380" r="45" fill="#063E27"/>
        <path d="M 790 510 C 790 440 830 430 860 430 C 890 430 930 440 930 510 Z" fill="#105A34"/>
        """
    elif scene_type == "principal":
        scene_elements = f"""
        <!-- Principal Desk Setup -->
        <rect width="1200" height="800" fill="url(#heroSky)"/>
        
        <!-- Office Wall & Bookshelf Background -->
        <rect x="100" y="150" width="1000" height="420" rx="8" fill="#063E27" opacity="0.9"/>
        <g fill="#DCE7DE" opacity="0.3">
            <rect x="140" y="200" width="200" height="15" />
            <rect x="140" y="280" width="200" height="15" />
            <rect x="140" y="360" width="200" height="15" />
            <rect x="860" y="200" width="200" height="15" />
            <rect x="860" y="280" width="200" height="15" />
            <rect x="860" y="360" width="200" height="15" />
        </g>
        
        <!-- Executive Desk -->
        <rect x="250" y="520" width="700" height="200" rx="8" fill="#1E293B"/>
        <rect x="230" y="500" width="740" height="30" rx="4" fill="#334155"/>
        
        <!-- Desk Items: Globe, Pen Stand, Official Files, Emblem -->
        <circle cx="340" cy="460" r="30" fill="#38BDF8" opacity="0.8"/>
        <path d="M 340 430 A 30 30 0 0 1 340 490 Z" fill="#16864A"/>
        <rect x="335" y="490" width="10" height="20" fill="#94A3B8"/>
        
        <rect x="780" y="460" width="80" height="45" rx="3" fill="#D97706"/>
        <rect x="790" y="450" width="80" height="45" rx="3" fill="#105A34"/>
        
        <!-- Dignified Leader Silhouette / Desk Presence -->
        <circle cx="600" cy="340" r="60" fill="#E2E8F0"/>
        <path d="M 480 500 C 480 410 540 400 600 400 C 660 400 720 410 720 500 Z" fill="#0F172A"/>
        <polygon points="600,430 585,480 615,480" fill="#DC2626"/>
        """
    elif scene_type == "classrooms":
        scene_elements = f"""
        <!-- Smart Classroom / Science Lab -->
        <rect width="1200" height="800" fill="url(#heroSky)"/>
        
        <!-- Digital Interactive Board -->
        <rect x="250" y="160" width="700" height="340" rx="12" fill="#063E27" stroke="#16864A" stroke-width="6"/>
        <rect x="270" y="180" width="660" height="300" rx="6" fill="#082E20"/>
        
        <!-- Scientific Equations & Diagram on Board -->
        <text x="320" y="250" font-family="'Plus Jakarta Sans', monospace" font-size="28" font-weight="700" fill="#6EE7B7">E = mc²  |  H₂O + CO₂ → C₆H₁₂O₆ + O₂</text>
        <circle cx="780" cy="330" r="60" fill="none" stroke="#FBBF24" stroke-width="3" stroke-dasharray="8 4"/>
        <circle cx="780" cy="330" r="15" fill="#EF4444"/>
        <circle cx="830" cy="300" r="8" fill="#38BDF8"/>
        <circle cx="730" cy="350" r="8" fill="#38BDF8"/>

        <!-- Lab Apparatus / Desks -->
        <rect x="150" y="550" width="900" height="200" fill="#FFFFFF" stroke="#DCE7DE" stroke-width="4"/>
        <!-- Microscope -->
        <path d="M 320 540 L 320 480 L 350 480 L 360 450 L 380 460 L 370 490 L 340 500 L 340 540 Z" fill="#334155"/>
        <circle cx="330" cy="545" r="20" fill="#64748B"/>
        <!-- Flask & Beakers with vibrant liquids -->
        <polygon points="500,540 480,480 490,480 490,450 510,450 510,480 520,480" fill="#38BDF8" opacity="0.8"/>
        <rect x="580" y="470" width="40" height="70" rx="4" fill="#105A34" opacity="0.8"/>
        <polygon points="680,540 660,490 670,490 670,460 690,460 690,490 700,490" fill="#F59E0B" opacity="0.8"/>
        """
    elif scene_type == "cultural":
        scene_elements = f"""
        <!-- Vibrant Cultural Arts Stage -->
        <rect width="1200" height="800" fill="#082E20"/>
        
        <!-- Stage Spotlights -->
        <polygon points="200,0 50,800 450,800" fill="#FBBF24" opacity="0.15"/>
        <polygon points="1000,0 750,800 1150,800" fill="#38BDF8" opacity="0.15"/>
        <polygon points="600,0 350,800 850,800" fill="#34D399" opacity="0.18"/>
        
        <!-- Stage Platform -->
        <polygon points="100,600 1100,600 1200,800 0,800" fill="#063E27"/>
        <line x1="0" y1="600" x2="1200" y2="600" stroke="#F59E0B" stroke-width="4"/>

        <!-- Dancers & Musicians Silhouettes -->
        <!-- Center Classical / Folk Dancer -->
        <circle cx="600" cy="400" r="35" fill="#FDE047"/>
        <path d="M 570 460 Q 600 440 630 460 L 640 580 L 560 580 Z" fill="#EF4444"/>
        <!-- Graceful Raised Arms -->
        <path d="M 575 460 Q 520 420 540 370" stroke="#FDE047" stroke-width="12" fill="none" stroke-linecap="round"/>
        <path d="M 625 460 Q 680 420 660 370" stroke="#FDE047" stroke-width="12" fill="none" stroke-linecap="round"/>

        <!-- Traditional Drums / Musical Instruments (Mandar / Dhol) -->
        <ellipse cx="400" cy="540" rx="45" ry="30" fill="#D97706"/>
        <circle cx="400" cy="450" r="30" fill="#FDE047"/>
        <rect x="385" y="480" width="30" height="60" fill="#105A34"/>

        <ellipse cx="800" cy="540" rx="45" ry="30" fill="#D97706"/>
        <circle cx="800" cy="450" r="30" fill="#FDE047"/>
        <rect x="785" y="480" width="30" height="60" fill="#105A34"/>
        """
    elif scene_type == "sports":
        scene_elements = f"""
        <!-- Sports Stadium & Athletic Track -->
        <rect width="1200" height="800" fill="url(#heroSky)"/>
        
        <!-- Running Track Lanes -->
        <path d="M 0 500 C 300 480 900 480 1200 500 L 1200 800 L 0 800 Z" fill="#B91C1C"/>
        <path d="M 0 560 C 300 540 900 540 1200 560" stroke="#FFFFFF" stroke-width="4" stroke-dasharray="25 15" fill="none"/>
        <path d="M 0 630 C 300 610 900 610 1200 630" stroke="#FFFFFF" stroke-width="4" stroke-dasharray="25 15" fill="none"/>
        <path d="M 0 710 C 300 690 900 690 1200 710" stroke="#FFFFFF" stroke-width="5" fill="none"/>

        <!-- Center Football / Sports Field Turf -->
        <path d="M 150 480 Q 600 430 1050 480 L 1000 350 Q 600 320 200 350 Z" fill="#105A34"/>
        <!-- Goalpost -->
        <rect x="520" y="320" width="160" height="70" fill="none" stroke="#FFFFFF" stroke-width="4"/>
        
        <!-- Athlete Runner Silhouettes -->
        <g transform="translate(620, 480) scale(0.9)">
            <circle cx="0" cy="0" r="28" fill="#FDE047"/>
            <path d="M -10 30 L 15 65 L 45 60" stroke="#105A34" stroke-width="14" fill="none" stroke-linecap="round"/>
            <path d="M -5 30 L -30 75 L -55 95" stroke="#063E27" stroke-width="14" fill="none" stroke-linecap="round"/>
            <path d="M 0 30 L -25 50 L -45 40" stroke="#FDE047" stroke-width="10" fill="none" stroke-linecap="round"/>
            <path d="M 0 30 L 25 45 L 45 30" stroke="#FDE047" stroke-width="10" fill="none" stroke-linecap="round"/>
        </g>
        <circle cx="780" cy="520" r="16" fill="#FFFFFF" stroke="#063E27" stroke-width="3"/>
        """
    elif scene_type == "exhibitions":
        scene_elements = f"""
        <!-- Science Exhibition & Skills Showcase -->
        <rect width="1200" height="800" fill="url(#heroSky)"/>
        
        <!-- Exhibition Booths -->
        <rect x="120" y="240" width="440" height="420" rx="8" fill="#FFFFFF" stroke="#105A34" stroke-width="4"/>
        <rect x="640" y="240" width="440" height="420" rx="8" fill="#FFFFFF" stroke="#105A34" stroke-width="4"/>
        
        <!-- Booth Banners -->
        <rect x="120" y="240" width="440" height="60" rx="8" fill="#105A34"/>
        <text x="340" y="280" font-family="'Plus Jakarta Sans', sans-serif" font-size="20" font-weight="700" fill="#FFFFFF" text-anchor="middle">RENEWABLE ENERGY &amp; ROBOTICS</text>

        <rect x="640" y="240" width="440" height="60" rx="8" fill="#063E27"/>
        <text x="860" y="280" font-family="'Plus Jakarta Sans', sans-serif" font-size="20" font-weight="700" fill="#FFFFFF" text-anchor="middle">VOCATIONAL SKILLS &amp; CRAFTS</text>

        <!-- Project Displays -->
        <!-- Windmill & Solar Model -->
        <line x1="340" y1="520" x2="340" y2="380" stroke="#64748B" stroke-width="8"/>
        <circle cx="340" cy="380" r="12" fill="#D97706"/>
        <line x1="340" y1="380" x2="300" y2="340" stroke="#38BDF8" stroke-width="6"/>
        <line x1="340" y1="380" x2="380" y2="340" stroke="#38BDF8" stroke-width="6"/>
        <line x1="340" y1="380" x2="340" y2="430" stroke="#38BDF8" stroke-width="6"/>
        
        <!-- Solar Panel Grid -->
        <polygon points="220,530 280,530 270,570 200,570" fill="#1E3A8A" stroke="#93C5FD" stroke-width="2"/>
        
        <!-- Gear / Circuit Innovation on Right -->
        <circle cx="860" cy="460" r="70" fill="none" stroke="#D97706" stroke-width="12" stroke-dasharray="20 10"/>
        <circle cx="860" cy="460" r="40" fill="#105A34"/>
        <circle cx="860" cy="460" r="15" fill="#FDE047"/>
        """
    else: # Default cinematic
        scene_elements = f"""
        <rect width="1200" height="800" fill="url(#heroSky)"/>
        <circle cx="600" cy="400" r="280" fill="#EAF5ED" opacity="0.6"/>
        <rect x="200" y="300" width="800" height="300" rx="8" fill="#063E27" opacity="0.8"/>
        """

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {1920 if scene_type=='hero' else 1200} {1080 if scene_type=='hero' else 800}" width="100%" height="100%">
  <defs>
    <linearGradient id="heroSky" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{c1}"/>
      <stop offset="60%" stop-color="{c2}"/>
      <stop offset="100%" stop-color="{c3}"/>
    </linearGradient>
    <linearGradient id="cinematicVignette" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#000000" stop-opacity="0.2"/>
      <stop offset="60%" stop-color="#000000" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#063E27" stop-opacity="0.95"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="30" result="blur"/>
    </filter>
  </defs>

  {scene_elements}

  <!-- Dark Green Cinematic Vignette Overlay -->
  <rect width="{1920 if scene_type=='hero' else 1200}" height="{1080 if scene_type=='hero' else 800}" fill="url(#cinematicVignette)"/>

  <!-- Artistic Lower Third Title Badge -->
  <g transform="translate(60, {900 if scene_type=='hero' else 650})">
    <rect x="0" y="0" width="180" height="32" rx="16" fill="{c4}" opacity="0.9"/>
    <text x="90" y="21" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" font-weight="800" fill="#FFFFFF" text-anchor="middle" letter-spacing="1.5">
      {category_tag.upper()}
    </text>
    <text x="0" y="65" font-family="'Plus Jakarta Sans', 'Segoe UI', sans-serif" font-size="28" font-weight="800" fill="#FFFFFF" letter-spacing="0.5">
      {title}
    </text>
    <text x="0" y="92" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="500" fill="#E2E8F0">
      {subtitle}
    </text>
  </g>
</svg>"""
    return svg

# Generate all needed SVGs
save_svg("hero/hero-campus-cinematic.svg", make_cinematic_svg(
    "+2 राजकीयकृत विद्या निकेतन उच्च विद्यालय", 
    "Empowering Minds • Building Futures • Haldipokhar Campus", 
    "Cinematic Campus", 
    "green", 
    "hero"
))

save_svg("campus/campus-main-facade.svg", make_cinematic_svg(
    "Majestic Main Academic Complex", 
    "Modern Architecture Amid Lush Natural Greenery", 
    "Campus Architecture", 
    "green", 
    "campus"
))

save_svg("campus/campus-aerial-view.svg", make_cinematic_svg(
    "Panoramic Campus Landscape", 
    "Expansive Sports Grounds & Educational Infrastructure", 
    "Aerial View", 
    "emerald", 
    "campus"
))

save_svg("campus/campus-garden-courtyard.svg", make_cinematic_svg(
    "Eco Courtyard & Serene Green Spaces", 
    "Nurturing Curiosity and Peaceful Academic Reflection", 
    "Green Campus", 
    "green", 
    "campus"
))

save_svg("students/students-discussion.svg", make_cinematic_svg(
    "Collaborative Academic Discovery", 
    "Dedicated Students Preparing for Future Leadership", 
    "Student Life", 
    "green", 
    "students"
))

save_svg("students/students-assembly.svg", make_cinematic_svg(
    "Morning Discipline & Value Education", 
    "Fostering National Pride, Integrity and Lifelong Ethics", 
    "Assembly", 
    "gold", 
    "students"
))

save_svg("students/students-excellence.svg", make_cinematic_svg(
    "Academic Diligence & All-Round Development", 
    "Guiding Secondary & Higher Secondary Students to Success", 
    "Excellence", 
    "emerald", 
    "students"
))

save_svg("principal/principal-desk-portrait.svg", make_cinematic_svg(
    "Office of the Head of Institution", 
    "Visionary Leadership Guiding Institutional Excellence", 
    "Leadership", 
    "gold", 
    "principal"
))

save_svg("classrooms/smart-classroom.svg", make_cinematic_svg(
    "ICT-Enabled Smart Classrooms", 
    "Modern Audio-Visual Digital Teaching & Interactive Pedagogy", 
    "Modern Learning", 
    "blue", 
    "classrooms"
))

save_svg("classrooms/science-laboratory.svg", make_cinematic_svg(
    "Equipped Composite Science Laboratories", 
    "Physics, Chemistry and Biology Hands-on Scientific Inquiry", 
    "Practical Labs", 
    "emerald", 
    "classrooms"
))

save_svg("classrooms/library-reading.svg", make_cinematic_svg(
    "Institutional Library & Learning Resource Center", 
    "Vast Collection of Reference Literature, Textbooks and Journals", 
    "Library", 
    "green", 
    "classrooms"
))

save_svg("cultural/cultural-annual-day.svg", make_cinematic_svg(
    "Annual Day Celebrations & Performing Arts", 
    "Expressing Rich Cultural Heritage, Classical & Folk Arts", 
    "Cultural Arts", 
    "gold", 
    "cultural"
))

save_svg("cultural/cultural-folk-dance.svg", make_cinematic_svg(
    "Jharkhand Cultural Heritage & Youth Fest", 
    "Fostering Pride in Regional Tribal Art, Music & Traditions", 
    "Heritage Arts", 
    "gold", 
    "cultural"
))

save_svg("sports/sports-track-field.svg", make_cinematic_svg(
    "Annual Athletic Meet & Track Events", 
    "Instilling Sportsmanship, Endurance, Stamina and Fitness", 
    "Athletics", 
    "green", 
    "sports"
))

save_svg("sports/sports-football-ground.svg", make_cinematic_svg(
    "Football & Team Sports Arena", 
    "Expansive Field for Football, Cricket, Volleyball and Yoga", 
    "Outdoor Sports", 
    "emerald", 
    "sports"
))

save_svg("exhibitions/science-exhibition-models.svg", make_cinematic_svg(
    "Annual Science & Innovation Fair", 
    "Student-Made Working Models in Renewable Energy & Engineering", 
    "Innovation", 
    "blue", 
    "exhibitions"
))

save_svg("exhibitions/skills-workshop.svg", make_cinematic_svg(
    "Vocational & Craft Skills Showcase", 
    "Fostering Hands-on Technical, Creative & Applied Competencies", 
    "Skill Development", 
    "gold", 
    "exhibitions"
))

# Gallery Collection (12 comprehensive items)
gallery_items = [
    ("gallery/gallery-campus-1.svg", "Main Academic Block", "Architectural entrance of +2 Rajkiyakrit Vidya Niketan", "Campus", "green", "campus"),
    ("gallery/gallery-campus-2.svg", "Botanical Courtyard & Eco Park", "Green spaces promoting environmental harmony", "Campus", "emerald", "campus"),
    ("gallery/gallery-class-1.svg", "Science & Discovery Laboratory", "Students conducting guided experimental investigations", "Classrooms", "blue", "classrooms"),
    ("gallery/gallery-class-2.svg", "Smart Digital ICT Learning Center", "Computer-aided instruction and digital literacy", "Classrooms", "emerald", "classrooms"),
    ("gallery/gallery-students-1.svg", "Discipline & Morning Prayer", "Values and character formation during daily assembly", "Students", "gold", "students"),
    ("gallery/gallery-students-2.svg", "Collaborative Student Study Circles", "Peer learning and academic discussions", "Students", "green", "students"),
    ("gallery/gallery-cultural-1.svg", "National Independence & Republic Day", "Patriotic presentations and ceremonial parades", "Cultural", "gold", "cultural"),
    ("gallery/gallery-cultural-2.svg", "Tribal & Folk Dance Presentations", "Celebration of Jharkhand folk culture and arts", "Cultural", "gold", "cultural"),
    ("gallery/gallery-sports-1.svg", "Inter-House Sprint & Track Tournament", "Annual athletic competitions fostering teamwork", "Sports", "green", "sports"),
    ("gallery/gallery-sports-2.svg", "Volleyball & Football Championship", "Outdoor sports coaching and student participation", "Sports", "emerald", "sports"),
    ("gallery/gallery-exhibitions-1.svg", "District Science & Tech Exhibition", "Student innovation projects and scientific models", "Exhibitions", "blue", "exhibitions"),
    ("gallery/gallery-scout-1.svg", "Bharat Scouts & Guides Training Camp", "Outdoor survival skills, pioneer badge and discipline", "Scout & Guide", "green", "students")
]

for filename, title, subtitle, tag, theme, scene in gallery_items:
    save_svg(filename, make_cinematic_svg(title, subtitle, tag, theme, scene))

print("All visual assets created successfully!")
