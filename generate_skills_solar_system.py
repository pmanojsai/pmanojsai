import math
import random

def generate_official_emojis_solar_system():
    width = 1200
    height = 620
    cx, cy = 600, 300
    steps = 90  # 90 smooth keyframes for 60fps loop

    # Random seed for cosmic stars
    random.seed(9999)
    stars = []
    for _ in range(160):
        sx = random.randint(10, width - 10)
        sy = random.randint(10, height - 10)
        if math.hypot(sx - cx, sy - cy) < 115:
            continue
        sr = random.choice([0.7, 1.0, 1.3, 1.6, 2.0, 2.4])
        sdur = round(random.uniform(2.0, 5.5), 1)
        sbegin = round(random.uniform(0.0, 4.5), 1)
        sop = random.choice([0.3, 0.5, 0.75, 0.95])
        scolor = random.choice(["#38bdf8", "#a78bfa", "#f59e0b", "#ffffff", "#67e8f9", "#f472b6", "#e0f2fe", "#34d399"])
        stars.append((sx, sy, sr, sdur, sbegin, sop, scolor))

    # Planetary definitions with authentic official emojis and tech emblems
    planets_def = [
        # Orbit 1 (Inner - Core Frontend)
        {
            "id": "react",
            "name": "React.js",
            "icon_type": "react_atom",
            "emoji": "⚛️",
            "color": "#61dafb",
            "bg_color": "#082f49",
            "radius": 25,
            "has_ring": True,
            "has_moon": True,
            "rx": 215,
            "ry": 84,
            "tilt_deg": -7,
            "phase": 0.0,
            "dur": 22.0
        },
        {
            "id": "typescript",
            "name": "TypeScript",
            "icon_type": "ts_badge",
            "emoji": "🔷",
            "color": "#3178c6",
            "bg_color": "#1e3a8a",
            "radius": 24,
            "has_ring": False,
            "has_moon": True,
            "rx": 215,
            "ry": 84,
            "tilt_deg": -7,
            "phase": math.pi * 0.5,
            "dur": 22.0
        },
        {
            "id": "nextjs",
            "name": "Next.js",
            "icon_type": "next_badge",
            "emoji": "▲",
            "color": "#ffffff",
            "bg_color": "#020617",
            "radius": 23,
            "has_ring": False,
            "has_moon": False,
            "rx": 215,
            "ry": 84,
            "tilt_deg": -7,
            "phase": math.pi,
            "dur": 22.0
        },
        {
            "id": "tailwind",
            "name": "Tailwind",
            "icon_type": "tailwind_wave",
            "emoji": "🌊",
            "color": "#38bdf8",
            "bg_color": "#0c4a6e",
            "radius": 22,
            "has_ring": False,
            "has_moon": False,
            "rx": 215,
            "ry": 84,
            "tilt_deg": -7,
            "phase": math.pi * 1.5,
            "dur": 22.0
        },

        # Orbit 2 (Mid-Inner - Backend & Core)
        {
            "id": "nodejs",
            "name": "Node.js",
            "icon_type": "node_hex",
            "emoji": "⬢",
            "color": "#5fa04e",
            "bg_color": "#064e3b",
            "radius": 26,
            "has_ring": True,
            "has_moon": True,
            "rx": 335,
            "ry": 130,
            "tilt_deg": 5,
            "phase": 0.4,
            "dur": 32.0
        },
        {
            "id": "python",
            "name": "Python",
            "icon_type": "python_snake",
            "emoji": "🐍",
            "color": "#ffd43b",
            "bg_color": "#1e3a8a",
            "radius": 25,
            "has_ring": False,
            "has_moon": True,
            "rx": 335,
            "ry": 130,
            "tilt_deg": 5,
            "phase": 0.4 + (math.pi * 2 / 4) * 1,
            "dur": 32.0
        },
        {
            "id": "express",
            "name": "Express.js",
            "icon_type": "express_bolt",
            "emoji": "⚡",
            "color": "#f472b6",
            "bg_color": "#831843",
            "radius": 22,
            "has_ring": False,
            "has_moon": False,
            "rx": 335,
            "ry": 130,
            "tilt_deg": 5,
            "phase": 0.4 + (math.pi * 2 / 4) * 2,
            "dur": 32.0
        },
        {
            "id": "javascript",
            "name": "JavaScript",
            "icon_type": "js_badge",
            "emoji": "🟨",
            "color": "#f7df1e",
            "bg_color": "#713f12",
            "radius": 23,
            "has_ring": False,
            "has_moon": False,
            "rx": 335,
            "ry": 130,
            "tilt_deg": 5,
            "phase": 0.4 + (math.pi * 2 / 4) * 3,
            "dur": 32.0
        },

        # Orbit 3 (Mid-Outer - Web3 & Data)
        {
            "id": "solidity",
            "name": "Solidity",
            "icon_type": "eth_diamond",
            "emoji": "💎",
            "color": "#a78bfa",
            "bg_color": "#3b0764",
            "radius": 27,
            "has_ring": True,
            "has_moon": True,
            "rx": 455,
            "ry": 175,
            "tilt_deg": -4,
            "phase": 0.9,
            "dur": 44.0
        },
        {
            "id": "postgres",
            "name": "PostgreSQL",
            "icon_type": "postgres_elephant",
            "emoji": "🐘",
            "color": "#336791",
            "bg_color": "#082f49",
            "radius": 26,
            "has_ring": True,
            "has_moon": True,
            "rx": 455,
            "ry": 175,
            "tilt_deg": -4,
            "phase": 0.9 + (math.pi * 2 / 4) * 1,
            "dur": 44.0
        },
        {
            "id": "mongodb",
            "name": "MongoDB",
            "icon_type": "mongo_leaf",
            "emoji": "🍃",
            "color": "#47a248",
            "bg_color": "#064e3b",
            "radius": 23,
            "has_ring": False,
            "has_moon": False,
            "rx": 455,
            "ry": 175,
            "tilt_deg": -4,
            "phase": 0.9 + (math.pi * 2 / 4) * 2,
            "dur": 44.0
        },
        {
            "id": "ipfs",
            "name": "IPFS Storage",
            "icon_type": "ipfs_cube",
            "emoji": "📦",
            "color": "#2dd4bf",
            "bg_color": "#134e4a",
            "radius": 23,
            "has_ring": False,
            "has_moon": False,
            "rx": 455,
            "ry": 175,
            "tilt_deg": -4,
            "phase": 0.9 + (math.pi * 2 / 4) * 3,
            "dur": 44.0
        },

        # Orbit 4 (Outer - Cloud & DevOps)
        {
            "id": "aws",
            "name": "AWS Cloud",
            "icon_type": "aws_cloud",
            "emoji": "☁️",
            "color": "#ff9900",
            "bg_color": "#78350f",
            "radius": 30,
            "has_ring": True,
            "has_moon": True,
            "rx": 555,
            "ry": 215,
            "tilt_deg": 3,
            "phase": 1.4,
            "dur": 58.0
        },
        {
            "id": "docker",
            "name": "Docker",
            "icon_type": "docker_whale",
            "emoji": "🐳",
            "color": "#2496ed",
            "bg_color": "#0c4a6e",
            "radius": 24,
            "has_ring": False,
            "has_moon": True,
            "rx": 555,
            "ry": 215,
            "tilt_deg": 3,
            "phase": 1.4 + (math.pi * 2 / 4) * 1,
            "dur": 58.0
        },
        {
            "id": "metamask",
            "name": "MetaMask",
            "icon_type": "metamask_fox",
            "emoji": "🦊",
            "color": "#f6851b",
            "bg_color": "#7c2d12",
            "radius": 24,
            "has_ring": False,
            "has_moon": False,
            "rx": 555,
            "ry": 215,
            "tilt_deg": 3,
            "phase": 1.4 + (math.pi * 2 / 4) * 2,
            "dur": 58.0
        },
        {
            "id": "github",
            "name": "GitHub / Git",
            "icon_type": "github_octo",
            "emoji": "🐙",
            "color": "#c084fc",
            "bg_color": "#3b0764",
            "radius": 23,
            "has_ring": False,
            "has_moon": False,
            "rx": 555,
            "ry": 215,
            "tilt_deg": 3,
            "phase": 1.4 + (math.pi * 2 / 4) * 3,
            "dur": 58.0
        }
    ]

    # Precalculate 3D orbit trajectory for each planet
    planets_computed = []
    for p in planets_def:
        rx = p["rx"]
        ry = p["ry"]
        tilt_rad = math.radians(p["tilt_deg"])
        cos_t = math.cos(tilt_rad)
        sin_t = math.sin(tilt_rad)
        
        dur_val = p["dur"]
        phase_0 = p["phase"]
        
        xs = []
        ys = []
        scales = []
        opacities = []
        
        for i in range(steps + 1):
            fraction = i / steps
            theta = phase_0 + fraction * 2 * math.pi
            
            px_raw = rx * math.cos(theta)
            py_raw = ry * math.sin(theta)
            
            px = px_raw * cos_t - py_raw * sin_t
            py = px_raw * sin_t + py_raw * cos_t
            
            screen_x = cx + px
            screen_y = cy + py
            
            depth_factor = math.sin(theta)  # -1 (back) to +1 (front)
            scale = 0.88 + 0.28 * depth_factor  # 0.60 to 1.16
            opacity = 0.72 + 0.28 * depth_factor  # 0.44 to 1.00
            
            xs.append(f"{screen_x:.1f}")
            ys.append(f"{screen_y:.1f}")
            scales.append(f"{scale:.2f}")
            opacities.append(f"{opacity:.2f}")
            
        planets_computed.append({
            "meta": p,
            "xs": ";".join(xs),
            "ys": ";".join(ys),
            "scales": ";".join(scales),
            "opacities": ";".join(opacities),
            "dur": dur_val
        })

    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img" aria-label="3D Solar System with Real Tech Emblems and Central Developer Person Emoji">')
    
    # DEFS SECTION
    svg.append('''<defs>
<!-- Cosmos Background -->
<linearGradient id="deep-cosmos" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#01040f"/>
  <stop offset="25%" stop-color="#040a1c"/>
  <stop offset="65%" stop-color="#091330"/>
  <stop offset="100%" stop-color="#020512"/>
</linearGradient>

<!-- Nebulae -->
<radialGradient id="neb-cyan" cx="15%" cy="25%" r="65%">
  <stop offset="0%" stop-color="#0284c7" stop-opacity="0.30"/>
  <stop offset="50%" stop-color="#0284c7" stop-opacity="0.08"/>
  <stop offset="100%" stop-color="#0284c7" stop-opacity="0"/>
</radialGradient>

<radialGradient id="neb-purple" cx="85%" cy="80%" r="70%">
  <stop offset="0%" stop-color="#7c3aed" stop-opacity="0.28"/>
  <stop offset="50%" stop-color="#6366f1" stop-opacity="0.09"/>
  <stop offset="100%" stop-color="#7c3aed" stop-opacity="0"/>
</radialGradient>

<radialGradient id="neb-gold" cx="50%" cy="50%" r="45%">
  <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.18"/>
  <stop offset="100%" stop-color="#f59e0b" stop-opacity="0"/>
</radialGradient>

<!-- Sun Gradients -->
<radialGradient id="sun-corona-core" cx="50%" cy="50%" r="50%">
  <stop offset="0%" stop-color="#ffffff" stop-opacity="1.0"/>
  <stop offset="20%" stop-color="#fef08a" stop-opacity="0.95"/>
  <stop offset="45%" stop-color="#f59e0b" stop-opacity="0.85"/>
  <stop offset="70%" stop-color="#ea580c" stop-opacity="0.45"/>
  <stop offset="90%" stop-color="#38bdf8" stop-opacity="0.15"/>
  <stop offset="100%" stop-color="#38bdf8" stop-opacity="0"/>
</radialGradient>

<radialGradient id="sun-body" cx="36%" cy="34%" r="66%">
  <stop offset="0%" stop-color="#ffffff"/>
  <stop offset="15%" stop-color="#fef08a"/>
  <stop offset="40%" stop-color="#f59e0b"/>
  <stop offset="75%" stop-color="#d97706"/>
  <stop offset="95%" stop-color="#b45309"/>
  <stop offset="100%" stop-color="#7c2d12"/>
</radialGradient>

<radialGradient id="avatar-chamber" cx="50%" cy="50%" r="50%">
  <stop offset="0%" stop-color="#0f172a" stop-opacity="0.97"/>
  <stop offset="60%" stop-color="#1e293b" stop-opacity="0.94"/>
  <stop offset="100%" stop-color="#020617" stop-opacity="0.99"/>
</radialGradient>

<!-- 3D Spherical Planet Lighting -->
<radialGradient id="sph-shading" cx="30%" cy="25%" r="75%">
  <stop offset="0%" stop-color="#ffffff" stop-opacity="0.6"/>
  <stop offset="40%" stop-color="#ffffff" stop-opacity="0.0"/>
  <stop offset="75%" stop-color="#000000" stop-opacity="0.55"/>
  <stop offset="100%" stop-color="#000000" stop-opacity="0.95"/>
</radialGradient>

<radialGradient id="sph-specular" cx="28%" cy="22%" r="35%">
  <stop offset="0%" stop-color="#ffffff" stop-opacity="0.9"/>
  <stop offset="100%" stop-color="#ffffff" stop-opacity="0.0"/>
</radialGradient>

<!-- Glow Filters -->
<filter id="glow-sun-core" x="-80%" y="-80%" width="260%" height="260%">
  <feGaussianBlur in="SourceGraphic" stdDeviation="16" result="blur1"/>
  <feGaussianBlur in="SourceGraphic" stdDeviation="36" result="blur2"/>
  <feMerge>
    <feMergeNode in="blur2"/>
    <feMergeNode in="blur1"/>
    <feMergeNode in="SourceGraphic"/>
  </feMerge>
</filter>

<filter id="glow-badge" x="-20%" y="-20%" width="140%" height="140%">
  <feGaussianBlur in="SourceGraphic" stdDeviation="4" result="blur"/>
  <feComposite in="SourceGraphic" in2="blur" operator="over"/>
</filter>

<clipPath id="viewport-clip">
  <rect width="1200" height="620" rx="22"/>
</clipPath>
</defs>''')

    svg.append('<g clip-path="url(#viewport-clip)">')
    # Backgrounds
    svg.append(f'<rect width="{width}" height="{height}" fill="url(#deep-cosmos)" stroke="#1e3a8a" stroke-width="1.8" stroke-opacity="0.6"/>')
    svg.append(f'<rect width="{width}" height="{height}" fill="url(#neb-cyan)"/>')
    svg.append(f'<rect width="{width}" height="{height}" fill="url(#neb-purple)"/>')
    svg.append(f'<rect width="{width}" height="{height}" fill="url(#neb-gold)"/>')

    # Starfield
    svg.append('<!-- Starfield -->')
    svg.append('<g id="starfield">')
    for (sx, sy, sr, sdur, sbegin, sop, scolor) in stars:
        svg.append(f'<circle cx="{sx}" cy="{sy}" r="{sr}" fill="{scolor}" opacity="{sop}"><animate attributeName="opacity" values="{sop*0.25:.2f};{min(1.0, sop*1.9):.2f};{sop*0.25:.2f}" dur="{sdur}s" begin="{sbegin}s" repeatCount="indefinite"/></circle>')
    
    # 4-point cross diffraction stars
    sparkle_coords = [(140, 75), (1060, 95), (100, 520), (1100, 500), (600, 50)]
    for spx, spy in sparkle_coords:
        svg.append(f'''<g transform="translate({spx},{spy})">
  <path d="M 0,-11 L 0,11 M -11,0 L 11,0" stroke="#7dd3fc" stroke-width="1.4" stroke-opacity="0.9">
    <animate attributeName="stroke-opacity" values="0.3;1;0.3" dur="3.2s" repeatCount="indefinite"/>
  </path>
  <circle r="2.5" fill="#ffffff"/>
</g>''')
    svg.append('</g>')

    # HUD Header
    svg.append('''<!-- Top Title HUD -->
<g transform="translate(42, 28)">
  <rect width="230" height="32" rx="16" fill="#0f172a" fill-opacity="0.9" stroke="#38bdf8" stroke-width="1.4" stroke-opacity="0.65"/>
  <circle cx="18" cy="16" r="5" fill="#38bdf8">
    <animate attributeName="opacity" values="0.3;1;0.3" dur="2s" repeatCount="indefinite"/>
  </circle>
  <text x="32" y="21.5" font-family="'Segoe UI',-apple-system,BlinkMacSystemFont,sans-serif" font-size="11.5" font-weight="800" fill="#38bdf8" letter-spacing="1.5">3D SKILL SOLAR SYSTEM</text>
</g>
<text x="42" y="84" font-family="'Segoe UI',-apple-system,BlinkMacSystemFont,sans-serif" font-size="22" font-weight="800" fill="#ffffff" letter-spacing="0.5">Technology Solar Universe</text>
<text x="42" y="106" font-family="'Segoe UI',-apple-system,BlinkMacSystemFont,sans-serif" font-size="13" font-weight="500" fill="#94a3b8">Official technology emojis &amp; emblems orbiting the developer person core</text>

<g transform="translate(960, 28)">
  <rect width="200" height="32" rx="16" fill="#0f172a" fill-opacity="0.9" stroke="#a78bfa" stroke-width="1.4" stroke-opacity="0.65"/>
  <circle cx="18" cy="16" r="5" fill="#a78bfa">
    <animate attributeName="opacity" values="0.3;1;0.3" dur="2.4s" repeatCount="indefinite"/>
  </circle>
  <text x="32" y="21.5" font-family="'Segoe UI',-apple-system,BlinkMacSystemFont,sans-serif" font-size="11.5" font-weight="700" fill="#c084fc" letter-spacing="1.2">REAL-TIME 3D ORBITS</text>
</g>''')

    # Orbital Elliptical Rings
    svg.append('<!-- 3D Orbital Tracks -->')
    rings_data = [
        (215, 84, -7, "#38bdf8", 0.55),
        (335, 130, 5, "#34d399", 0.45),
        (455, 175, -4, "#a78bfa", 0.38),
        (555, 215, 3, "#fb923c", 0.32),
    ]
    for (rx, ry, tilt, col, op) in rings_data:
        svg.append(f'<g transform="translate({cx},{cy}) rotate({tilt})"><ellipse cx="0" cy="0" rx="{rx}" ry="{ry}" fill="none" stroke="{col}" stroke-opacity="{op}" stroke-width="1.6" stroke-dasharray="6 8"/></g>')

    # Central Sun / Core with Person Emoji
    svg.append(f'''<!-- Central Giant Glowing Sun & Developer Core -->
<g id="central-sun-universe">
  <!-- Massive Solar Corona Flare -->
  <circle cx="{cx}" cy="{cy}" r="125" fill="url(#sun-corona-core)">
    <animate attributeName="r" values="112;140;112" dur="4.5s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.85;1.0;0.85" dur="4.5s" repeatCount="indefinite"/>
  </circle>

  <!-- Golden Solar Filaments (Rotating Ring 1) -->
  <circle cx="{cx}" cy="{cy}" r="84" fill="none" stroke="#f59e0b" stroke-opacity="0.65" stroke-width="2.5" stroke-dasharray="8 16">
    <animateTransform attributeName="transform" type="rotate" from="0 {cx} {cy}" to="360 {cx} {cy}" dur="16s" repeatCount="indefinite"/>
  </circle>
  
  <!-- Counter-Rotating Cyan Shield (Ring 2) -->
  <circle cx="{cx}" cy="{cy}" r="98" fill="none" stroke="#38bdf8" stroke-opacity="0.5" stroke-width="2.0" stroke-dasharray="6 20">
    <animateTransform attributeName="transform" type="rotate" from="360 {cx} {cy}" to="0 {cx} {cy}" dur="24s" repeatCount="indefinite"/>
  </circle>

  <!-- Glowing Sun Body Sphere -->
  <circle cx="{cx}" cy="{cy}" r="64" fill="url(#sun-body)" filter="url(#glow-sun-core)"/>
  
  <!-- High-Tech Glass Avatar Chamber -->
  <circle cx="{cx}" cy="{cy}" r="50" fill="url(#avatar-chamber)" stroke="#f59e0b" stroke-width="3.2" stroke-opacity="0.98"/>
  <circle cx="{cx}" cy="{cy}" r="46.5" fill="none" stroke="#38bdf8" stroke-width="1.8" stroke-opacity="0.9"/>

  <!-- PERSON EMOJI at the center of the Universe -->
  <text x="{cx}" y="{cy + 17}" text-anchor="middle" font-size="48" font-family="'Segoe UI Emoji','Apple Color Emoji','Noto Color Emoji',sans-serif">👨‍💻</text>
  
  <!-- Sun Core Floating Badge -->
  <g transform="translate({cx - 72}, {cy + 58})">
    <rect width="144" height="26" rx="13" fill="#020617" fill-opacity="0.96" stroke="#f59e0b" stroke-width="1.8" stroke-opacity="0.95"/>
    <circle cx="16" cy="13" r="4" fill="#22c55e">
      <animate attributeName="opacity" values="0.4;1;0.4" dur="1.6s" repeatCount="indefinite"/>
    </circle>
    <text x="78" y="17.5" text-anchor="middle" font-family="'Segoe UI',-apple-system,BlinkMacSystemFont,sans-serif" font-size="11" font-weight="800" fill="#fbbf24" letter-spacing="1.4">PUNEETH · CORE</text>
  </g>
</g>''')

    # Function to generate official vector emblem / emoji inside each planet
    def render_emblem(icon_type, pr, color):
        if icon_type == "react_atom":
            return f'''<ellipse cx="0" cy="0" rx="{pr*0.75:.1f}" ry="{pr*0.28:.1f}" fill="none" stroke="#61dafb" stroke-width="1.8" transform="rotate(0)"/>
<ellipse cx="0" cy="0" rx="{pr*0.75:.1f}" ry="{pr*0.28:.1f}" fill="none" stroke="#61dafb" stroke-width="1.8" transform="rotate(60)"/>
<ellipse cx="0" cy="0" rx="{pr*0.75:.1f}" ry="{pr*0.28:.1f}" fill="none" stroke="#61dafb" stroke-width="1.8" transform="rotate(120)"/>
<circle cx="0" cy="0" r="{pr*0.2:.1f}" fill="#61dafb"/>'''
        elif icon_type == "ts_badge":
            return f'''<rect x="{-pr*0.65:.1f}" y="{-pr*0.65:.1f}" width="{pr*1.3:.1f}" height="{pr*1.3:.1f}" rx="{pr*0.2:.1f}" fill="#3178c6"/>
<text x="{pr*0.05:.1f}" y="{pr*0.35:.1f}" text-anchor="middle" font-family="'Segoe UI',Inter,sans-serif" font-size="{pr*0.8:.1f}" font-weight="900" fill="#ffffff">TS</text>'''
        elif icon_type == "js_badge":
            return f'''<rect x="{-pr*0.65:.1f}" y="{-pr*0.65:.1f}" width="{pr*1.3:.1f}" height="{pr*1.3:.1f}" rx="{pr*0.2:.1f}" fill="#f7df1e"/>
<text x="{pr*0.05:.1f}" y="{pr*0.35:.1f}" text-anchor="middle" font-family="'Segoe UI',Inter,sans-serif" font-size="{pr*0.8:.1f}" font-weight="900" fill="#000000">JS</text>'''
        elif icon_type == "next_badge":
            return f'''<circle cx="0" cy="0" r="{pr*0.7:.1f}" fill="#000000" stroke="#ffffff" stroke-width="1.2"/>
<text x="0" y="{pr*0.32:.1f}" text-anchor="middle" font-family="'Segoe UI',Inter,sans-serif" font-size="{pr*0.75:.1f}" font-weight="900" fill="#ffffff">▲</text>'''
        elif icon_type == "node_hex":
            return f'''<polygon points="0,{-pr*0.7:.1f} {pr*0.65:.1f},{-pr*0.35:.1f} {pr*0.65:.1f},{pr*0.35:.1f} 0,{pr*0.7:.1f} {-pr*0.65:.1f},{pr*0.35:.1f} {-pr*0.65:.1f},{-pr*0.35:.1f}" fill="#5fa04e"/>
<text x="0" y="{pr*0.3:.1f}" text-anchor="middle" font-family="'Segoe UI',Inter,sans-serif" font-size="{pr*0.65:.1f}" font-weight="900" fill="#ffffff">⬢</text>'''
        elif icon_type == "python_snake":
            return f'''<text x="0" y="{pr*0.4:.1f}" text-anchor="middle" font-size="{pr*1.2:.1f}" font-family="'Segoe UI Emoji','Apple Color Emoji',sans-serif">🐍</text>'''
        elif icon_type == "eth_diamond":
            return f'''<polygon points="0,{-pr*0.75:.1f} {pr*0.5:.1f},0 0,{pr*0.25:.1f} {-pr*0.5:.1f},0" fill="#c084fc"/>
<polygon points="0,{pr*0.35:.1f} {pr*0.5:.1f},0.05 0,{pr*0.75:.1f} {-pr*0.5:.1f},0.05" fill="#a855f7"/>'''
        elif icon_type == "aws_cloud":
            return f'''<text x="0" y="{pr*0.35:.1f}" text-anchor="middle" font-size="{pr*1.1:.1f}" font-family="'Segoe UI Emoji','Apple Color Emoji',sans-serif">☁️</text>'''
        elif icon_type == "docker_whale":
            return f'''<text x="0" y="{pr*0.35:.1f}" text-anchor="middle" font-size="{pr*1.1:.1f}" font-family="'Segoe UI Emoji','Apple Color Emoji',sans-serif">🐳</text>'''
        elif icon_type == "postgres_elephant":
            return f'''<text x="0" y="{pr*0.35:.1f}" text-anchor="middle" font-size="{pr*1.1:.1f}" font-family="'Segoe UI Emoji','Apple Color Emoji',sans-serif">🐘</text>'''
        elif icon_type == "mongo_leaf":
            return f'''<text x="0" y="{pr*0.35:.1f}" text-anchor="middle" font-size="{pr*1.1:.1f}" font-family="'Segoe UI Emoji','Apple Color Emoji',sans-serif">🍃</text>'''
        elif icon_type == "ipfs_cube":
            return f'''<polygon points="0,{-pr*0.7:.1f} {pr*0.6:.1f},{-pr*0.35:.1f} {pr*0.6:.1f},{pr*0.35:.1f} 0,{pr*0.7:.1f} {-pr*0.6:.1f},{pr*0.35:.1f} {-pr*0.6:.1f},{-pr*0.35:.1f}" fill="#14b8a6"/>
<line x1="0" y1="0" x2="0" y2="{pr*0.7:.1f}" stroke="#042f2e" stroke-width="1.2"/>
<line x1="0" y1="0" x2="{pr*0.6:.1f}" y2="{-pr*0.35:.1f}" stroke="#042f2e" stroke-width="1.2"/>
<line x1="0" y1="0" x2="{-pr*0.6:.1f}" y2="{-pr*0.35:.1f}" stroke="#042f2e" stroke-width="1.2"/>'''
        elif icon_type == "metamask_fox":
            return f'''<text x="0" y="{pr*0.35:.1f}" text-anchor="middle" font-size="{pr*1.1:.1f}" font-family="'Segoe UI Emoji','Apple Color Emoji',sans-serif">🦊</text>'''
        elif icon_type == "github_octo":
            return f'''<text x="0" y="{pr*0.35:.1f}" text-anchor="middle" font-size="{pr*1.1:.1f}" font-family="'Segoe UI Emoji','Apple Color Emoji',sans-serif">🐙</text>'''
        elif icon_type == "express_bolt":
            return f'''<text x="0" y="{pr*0.35:.1f}" text-anchor="middle" font-size="{pr*1.1:.1f}" font-family="'Segoe UI Emoji','Apple Color Emoji',sans-serif">⚡</text>'''
        elif icon_type == "tailwind_wave":
            return f'''<text x="0" y="{pr*0.35:.1f}" text-anchor="middle" font-size="{pr*1.1:.1f}" font-family="'Segoe UI Emoji','Apple Color Emoji',sans-serif">🌊</text>'''
        else:
            return f'''<circle cx="0" cy="0" r="{pr*0.6:.1f}" fill="{color}"/>'''

    # Planets with Emblems
    svg.append('<!-- Orbiting Tech Planets -->')

    for item in planets_computed:
        meta = item["meta"]
        name = meta["id"]
        tag = meta["name"]
        emoji = meta["emoji"]
        icon_type = meta["icon_type"]
        color = meta["color"]
        bg_col = meta["bg_color"]
        pr = meta["radius"]
        has_ring = meta["has_ring"]
        has_moon = meta["has_moon"]
        
        dur_val = item["dur"]
        xs_str = item["xs"]
        ys_str = item["ys"]
        scales_str = item["scales"]
        opacities_str = item["opacities"]
        
        # Badge sizing
        text_len = len(tag)
        badge_w = text_len * 7.8 + 36
        badge_h = 24
        badge_x = -badge_w / 2
        badge_y = pr + 6

        svg.append(f'<!-- ==================== {tag} ==================== -->')
        first_x = xs_str.split(";")[0]
        first_y = ys_str.split(";")[0]
        first_op = opacities_str.split(";")[0]
        first_scale = scales_str.split(";")[0]

        svg.append(f'<g transform="translate({first_x},{first_y})" opacity="{first_op}">')
        svg.append(f'  <animateTransform attributeName="transform" type="translate" dur="{dur_val}s" repeatCount="indefinite" values="{";".join([f"{x},{y}" for x,y in zip(xs_str.split(";"), ys_str.split(";"))])}"/>')
        svg.append(f'  <animate attributeName="opacity" dur="{dur_val}s" repeatCount="indefinite" values="{opacities_str}"/>')
        
        svg.append(f'  <g transform="scale({first_scale})">')
        svg.append(f'    <animateTransform attributeName="transform" type="scale" dur="{dur_val}s" repeatCount="indefinite" values="{scales_str}" additive="replace"/>')

        # Outer planetary aura
        svg.append(f'    <circle cx="0" cy="0" r="{pr + 8}" fill="{color}" opacity="0.38"/>')

        # Planetary rings
        if has_ring:
            svg.append(f'    <!-- Saturn Ring System -->')
            svg.append(f'    <ellipse cx="0" cy="0" rx="{pr * 2.1:.1f}" ry="{pr * 0.65:.1f}" fill="none" stroke="{color}" stroke-width="3" stroke-opacity="0.9" stroke-dasharray="12 3" transform="rotate(-18)"/>')
            svg.append(f'    <ellipse cx="0" cy="0" rx="{pr * 2.3:.1f}" ry="{pr * 0.72:.1f}" fill="none" stroke="{color}" stroke-width="1.2" stroke-opacity="0.6" transform="rotate(-18)"/>')

        # Spherical Globe Body
        svg.append(f'    <circle cx="0" cy="0" r="{pr}" fill="{bg_col}" stroke="{color}" stroke-width="2.2" stroke-opacity="0.95"/>')
        
        # Tech Emblem / Logo
        svg.append(f'    <!-- Authentic Tech Emblem -->')
        svg.append(f'    {render_emblem(icon_type, pr, color)}')

        # 3D Shading & Specular
        svg.append(f'    <circle cx="0" cy="0" r="{pr}" fill="url(#sph-shading)"/>')
        svg.append(f'    <circle cx="{-pr*0.35:.1f}" cy="{-pr*0.35:.1f}" r="{pr*0.5:.1f}" fill="url(#sph-specular)"/>')

        # Orbiting Natural Moon
        if has_moon:
            moon_dist = pr + 14
            svg.append(f'''    <!-- Orbiting Natural Moon -->
    <g>
      <circle cx="{moon_dist}" cy="0" r="3.8" fill="#e2e8f0" stroke="#0ea5e9" stroke-width="0.9">
        <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="360 0 0" dur="{round(dur_val*0.18, 1)}s" repeatCount="indefinite"/>
      </circle>
    </g>''')

        # Planet Name Label Pill
        svg.append(f'    <!-- Planet Label Pill -->')
        svg.append(f'    <g filter="url(#glow-badge)">')
        svg.append(f'      <rect x="{badge_x:.1f}" y="{badge_y:.1f}" width="{badge_w:.1f}" height="{badge_h}" rx="12" fill="#020617" fill-opacity="0.96" stroke="{color}" stroke-width="1.6" stroke-opacity="0.95"/>')
        svg.append(f'      <text x="{badge_x + 14:.1f}" y="{badge_y + 16.5:.1f}" font-size="12">{emoji}</text>')
        svg.append(f'      <text x="{badge_x + 30:.1f}" y="{badge_y + 16.5:.1f}" font-family="Inter,\'Segoe UI\',-apple-system,sans-serif" font-size="11.5" font-weight="800" fill="#ffffff" letter-spacing="0.3">{tag}</text>')
        svg.append(f'    </g>')

        svg.append(f'  </g>')
        svg.append(f'</g>')

    # Bottom Legend HUD
    svg.append('''<!-- Bottom Tech Legend HUD -->
<g transform="translate(42, 566)">
  <rect width="1116" height="38" rx="19" fill="#0b132b" fill-opacity="0.96" stroke="#1e3a8a" stroke-width="1.6" stroke-opacity="0.8"/>
  <text x="24" y="24" font-family="'Segoe UI',sans-serif" font-size="12.5" font-weight="800" fill="#38bdf8">⚡ ORBIT 1:</text>
  <text x="104" y="24" font-family="'Segoe UI',sans-serif" font-size="12" font-weight="600" fill="#cbd5e1">React (⚛️) · TypeScript (TS) · Next.js (▲) · Tailwind (🌊)</text>
  
  <text x="490" y="24" font-family="'Segoe UI',sans-serif" font-size="12.5" font-weight="800" fill="#34d399">⚙️ ORBIT 2:</text>
  <text x="570" y="24" font-family="'Segoe UI',sans-serif" font-size="12" font-weight="600" fill="#cbd5e1">Node (⬢) · Python (🐍) · Express (⚡) · JS (🟨)</text>

  <text x="890" y="24" font-family="'Segoe UI',sans-serif" font-size="12.5" font-weight="800" fill="#a78bfa">🔐 ORBIT 3 &amp; 4:</text>
  <text x="990" y="24" font-family="'Segoe UI',sans-serif" font-size="12" font-weight="600" fill="#cbd5e1">AWS (☁️) · Solidity (💎) · Docker (🐳) · Postgres (🐘)</text>
</g>''')

    svg.append('</g>')
    svg.append('</svg>')
    
    return "\n".join(svg)

if __name__ == "__main__":
    svg_content = generate_official_emojis_solar_system()
    with open("assets/skills-globe.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated official emojis solar system ({len(svg_content)} bytes)")
