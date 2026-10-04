import math
import random
import os

def generate_light_solar_system():
    width = 1200
    height = 620
    cx, cy = 600, 300
    steps = 90

    random.seed(9999)
    stars = []
    for _ in range(140):
        sx = random.randint(15, width - 15)
        sy = random.randint(15, height - 15)
        if math.hypot(sx - cx, sy - cy) < 115:
            continue
        sr = random.choice([0.8, 1.2, 1.5, 1.8, 2.2])
        sdur = round(random.uniform(2.0, 5.0), 1)
        sbegin = round(random.uniform(0.0, 4.0), 1)
        sop = random.choice([0.35, 0.55, 0.75, 0.9])
        scolor = random.choice(["#0284c7", "#6366f1", "#d97706", "#059669", "#ec4899", "#8b5cf6", "#38bdf8"])
        stars.append((sx, sy, sr, sdur, sbegin, sop, scolor))

    planets_def = [
        # Orbit 1 (Inner - Frontend)
        {
            "id": "react",
            "name": "React.js",
            "icon_type": "react_atom",
            "emoji": "⚛️",
            "color": "#0284c7",
            "bg_color": "#e0f2fe",
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
            "color": "#2563eb",
            "bg_color": "#dbeafe",
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
            "color": "#0f172a",
            "bg_color": "#f1f5f9",
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
            "color": "#0891b2",
            "bg_color": "#cffafe",
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
            "color": "#16a34a",
            "bg_color": "#dcfce7",
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
            "color": "#d97706",
            "bg_color": "#fef3c7",
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
            "color": "#db2777",
            "bg_color": "#fce7f3",
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
            "color": "#ca8a04",
            "bg_color": "#fef9c3",
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
            "color": "#7c3aed",
            "bg_color": "#ede9fe",
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
            "color": "#2563eb",
            "bg_color": "#dbeafe",
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
            "color": "#16a34a",
            "bg_color": "#dcfce7",
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
            "color": "#0d9488",
            "bg_color": "#ccfbf1",
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
            "color": "#ea580c",
            "bg_color": "#ffedd5",
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
            "color": "#0284c7",
            "bg_color": "#e0f2fe",
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
            "color": "#ea580c",
            "bg_color": "#ffedd5",
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
            "color": "#475569",
            "bg_color": "#f1f5f9",
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

    planets_computed = []
    for p in planets_def:
        rx = p["rx"]
        ry = p["ry"]
        tilt_rad = math.radians(p["tilt_deg"])
        cos_t = math.cos(tilt_rad)
        sin_t = math.sin(tilt_rad)
        dur_val = p["dur"]
        phase_0 = p["phase"]
        
        xs, ys, scales, opacities = [], [], [], []
        for i in range(steps + 1):
            fraction = i / steps
            theta = phase_0 + fraction * 2 * math.pi
            px_raw = rx * math.cos(theta)
            py_raw = ry * math.sin(theta)
            px = px_raw * cos_t - py_raw * sin_t
            py = px_raw * sin_t + py_raw * cos_t
            screen_x = cx + px
            screen_y = cy + py
            depth_factor = math.sin(theta)
            scale = 0.90 + 0.25 * depth_factor
            opacity = 0.80 + 0.20 * depth_factor
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

    def render_emblem(icon_type, pr, color):
        s = pr * 0.55
        if icon_type == "react_atom":
            return f'''<g transform="scale({s/12:.2f})">
              <ellipse rx="11" ry="4.2" fill="none" stroke="{color}" stroke-width="1.8"/>
              <ellipse rx="11" ry="4.2" fill="none" stroke="{color}" stroke-width="1.8" transform="rotate(60)"/>
              <ellipse rx="11" ry="4.2" fill="none" stroke="{color}" stroke-width="1.8" transform="rotate(120)"/>
              <circle r="2.2" fill="{color}"/>
            </g>'''
        elif icon_type == "ts_badge":
            return f'''<g transform="scale({s/12:.2f})">
              <rect x="-10" y="-10" width="20" height="20" rx="3.5" fill="{color}"/>
              <text x="-4" y="6" font-family="Inter,sans-serif" font-size="11" font-weight="900" fill="#ffffff">TS</text>
            </g>'''
        elif icon_type == "next_badge":
            return f'''<g transform="scale({s/12:.2f})">
              <circle r="10" fill="#0f172a"/>
              <polygon points="-4,-6 5,6 3,6 -6,-6" fill="#ffffff"/>
              <polygon points="2,-6 5,-6 5,6 2,6" fill="#ffffff"/>
            </g>'''
        elif icon_type == "tailwind_wave":
            return f'''<g transform="scale({s/12:.2f})">
              <path d="M-9,2 C-6,-5 -1,-5 2,-1 C5,3 8,3 10,0 C8,6 3,6 0,2 C-3,-2 -6,-2 -9,2 Z" fill="{color}"/>
            </g>'''
        elif icon_type == "node_hex":
            return f'''<g transform="scale({s/12:.2f})">
              <polygon points="0,-10 9,-5 9,5 0,10 -9,5 -9,-5" fill="{color}" opacity="0.9"/>
              <text x="0" y="4" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="900" fill="#ffffff">N</text>
            </g>'''
        elif icon_type == "python_snake":
            return f'''<g transform="scale({s/12:.2f})">
              <path d="M-8,-8 h10 v6 h-4 v2 h10 v6 h-10 v-6 h4 v-2 h-10 z" fill="{color}"/>
              <circle cx="-3" cy="-5" r="1.2" fill="#ffffff"/>
              <circle cx="3" cy="3" r="1.2" fill="#ffffff"/>
            </g>'''
        elif icon_type == "express_bolt":
            return f'''<g transform="scale({s/12:.2f})">
              <polygon points="1,-9 -7,1 -1,1 -3,9 7,-1 1,-1" fill="{color}"/>
            </g>'''
        elif icon_type == "js_badge":
            return f'''<g transform="scale({s/12:.2f})">
              <rect x="-10" y="-10" width="20" height="20" rx="3.5" fill="{color}"/>
              <text x="0" y="6" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="900" fill="#0f172a">JS</text>
            </g>'''
        elif icon_type == "eth_diamond":
            return f'''<g transform="scale({s/12:.2f})">
              <polygon points="0,-10 8,0 0,4 -8,0" fill="{color}" opacity="0.95"/>
              <polygon points="0,5 8,1 0,10 -8,1" fill="{color}" opacity="0.75"/>
            </g>'''
        elif icon_type == "postgres_elephant":
            return f'''<g transform="scale({s/12:.2f})">
              <ellipse rx="8.5" ry="7.5" fill="{color}"/>
              <circle cx="5" cy="-2" r="1.4" fill="#ffffff"/>
              <path d="M5,1 C7,3 7,7 4,8" fill="none" stroke="#ffffff" stroke-width="1.8" stroke-linecap="round"/>
            </g>'''
        elif icon_type == "mongo_leaf":
            return f'''<g transform="scale({s/12:.2f})">
              <path d="M0,-10 C5,-5 8,0 5,7 C3,10 0,11 0,11 C0,11 -3,10 -5,7 C-8,0 -5,-5 0,-10 Z" fill="{color}"/>
              <line x1="0" y1="-8" x2="0" y2="10" stroke="#ffffff" stroke-width="1"/>
            </g>'''
        elif icon_type == "ipfs_cube":
            return f'''<g transform="scale({s/12:.2f})">
              <polygon points="0,-9 8,-4 0,1 -8,-4" fill="{color}" opacity="0.95"/>
              <polygon points="-8,-4 0,1 0,9 -8,4" fill="{color}" opacity="0.75"/>
              <polygon points="8,-4 0,1 0,9 8,4" fill="{color}" opacity="0.85"/>
            </g>'''
        elif icon_type == "aws_cloud":
            return f'''<g transform="scale({s/12:.2f})">
              <path d="M-6,3 a5,5 0 0,1 1,-7 a6,6 0 0,1 10,1 a4,4 0 0,1 1,6 z" fill="{color}"/>
              <path d="M-6,7 Q0,11 6,7" fill="none" stroke="{color}" stroke-width="1.8" stroke-linecap="round"/>
            </g>'''
        elif icon_type == "docker_whale":
            return f'''<g transform="scale({s/12:.2f})">
              <path d="M-8,1 h16 c0,4 -4,7 -8,7 c-5,0 -8,-3 -8,-7 z" fill="{color}"/>
              <rect x="-6" y="-3" width="3" height="3" fill="{color}"/>
              <rect x="-2" y="-3" width="3" height="3" fill="{color}"/>
              <rect x="2" y="-3" width="3" height="3" fill="{color}"/>
            </g>'''
        elif icon_type == "metamask_fox":
            return f'''<g transform="scale({s/12:.2f})">
              <polygon points="-8,-8 -3,-2 -6,4" fill="{color}"/>
              <polygon points="8,-8 3,-2 6,4" fill="{color}"/>
              <polygon points="0,-2 -4,4 4,4" fill="#ca8a04"/>
              <polygon points="0,8 -3,4 3,4" fill="#0f172a"/>
            </g>'''
        elif icon_type == "github_octo":
            return f'''<g transform="scale({s/12:.2f})">
              <circle r="8.5" fill="{color}"/>
              <path d="M-4,-2 C-3,-6 -1,-6 0,-3 C1,-6 3,-6 4,-2" fill="none" stroke="#ffffff" stroke-width="1.6"/>
              <circle cx="-3" cy="0" r="1.3" fill="#ffffff"/>
              <circle cx="3" cy="0" r="1.3" fill="#ffffff"/>
            </g>'''
        return f'<circle r="{s*0.6:.1f}" fill="{color}"/>'

    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img" aria-label="Interactive 3D Planetary Tech Universe (Light Mode)">')
    svg.append('''<defs>
<!-- Light Sky Tech Background -->
<linearGradient id="light-cosmos" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#ffffff"/>
  <stop offset="30%" stop-color="#f8fafc"/>
  <stop offset="70%" stop-color="#f0f9ff"/>
  <stop offset="100%" stop-color="#e0f2fe"/>
</linearGradient>

<!-- Soft Nebulae (Light Glows) -->
<radialGradient id="neb-cyan-light" cx="20%" cy="25%" r="65%">
  <stop offset="0%" stop-color="#0284c7" stop-opacity="0.12"/>
  <stop offset="50%" stop-color="#38bdf8" stop-opacity="0.04"/>
  <stop offset="100%" stop-color="#38bdf8" stop-opacity="0"/>
</radialGradient>

<radialGradient id="neb-indigo-light" cx="80%" cy="75%" r="70%">
  <stop offset="0%" stop-color="#6366f1" stop-opacity="0.12"/>
  <stop offset="50%" stop-color="#818cf8" stop-opacity="0.04"/>
  <stop offset="100%" stop-color="#6366f1" stop-opacity="0"/>
</radialGradient>

<radialGradient id="neb-amber-light" cx="50%" cy="50%" r="45%">
  <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.15"/>
  <stop offset="100%" stop-color="#f59e0b" stop-opacity="0"/>
</radialGradient>

<!-- Central Sun Core Gradients -->
<radialGradient id="sun-corona-light" cx="50%" cy="50%" r="50%">
  <stop offset="0%" stop-color="#ffffff" stop-opacity="1.0"/>
  <stop offset="25%" stop-color="#fef08a" stop-opacity="0.95"/>
  <stop offset="55%" stop-color="#f59e0b" stop-opacity="0.65"/>
  <stop offset="80%" stop-color="#0284c7" stop-opacity="0.25"/>
  <stop offset="100%" stop-color="#0284c7" stop-opacity="0"/>
</radialGradient>

<radialGradient id="sun-body-light" cx="34%" cy="32%" r="68%">
  <stop offset="0%" stop-color="#ffffff"/>
  <stop offset="20%" stop-color="#fef08a"/>
  <stop offset="55%" stop-color="#f59e0b"/>
  <stop offset="85%" stop-color="#ea580c"/>
  <stop offset="100%" stop-color="#c2410c"/>
</radialGradient>

<radialGradient id="avatar-chamber-light" cx="50%" cy="50%" r="50%">
  <stop offset="0%" stop-color="#ffffff" stop-opacity="0.98"/>
  <stop offset="70%" stop-color="#f8fafc" stop-opacity="0.95"/>
  <stop offset="100%" stop-color="#f1f5f9" stop-opacity="0.99"/>
</radialGradient>

<!-- Planet Spherical Lighting for Light Mode -->
<radialGradient id="sph-shading-light" cx="28%" cy="22%" r="78%">
  <stop offset="0%" stop-color="#ffffff" stop-opacity="0.8"/>
  <stop offset="45%" stop-color="#ffffff" stop-opacity="0.0"/>
  <stop offset="80%" stop-color="#0f172a" stop-opacity="0.22"/>
  <stop offset="100%" stop-color="#0f172a" stop-opacity="0.45"/>
</radialGradient>

<radialGradient id="sph-specular-light" cx="26%" cy="20%" r="35%">
  <stop offset="0%" stop-color="#ffffff" stop-opacity="0.95"/>
  <stop offset="100%" stop-color="#ffffff" stop-opacity="0.0"/>
</radialGradient>

<!-- Soft Drop Shadows -->
<filter id="shadow-badge" x="-20%" y="-20%" width="140%" height="140%">
  <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0f172a" flood-opacity="0.12"/>
</filter>

<filter id="shadow-dock" x="-10%" y="-20%" width="120%" height="150%">
  <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#0f172a" flood-opacity="0.08"/>
</filter>

<filter id="glow-sun-light" x="-80%" y="-80%" width="260%" height="260%">
  <feGaussianBlur in="SourceGraphic" stdDeviation="14" result="blur1"/>
  <feGaussianBlur in="SourceGraphic" stdDeviation="28" result="blur2"/>
  <feMerge>
    <feMergeNode in="blur2"/>
    <feMergeNode in="blur1"/>
    <feMergeNode in="SourceGraphic"/>
  </feMerge>
</filter>

<clipPath id="viewport-clip">
  <rect width="1200" height="620" rx="22"/>
</clipPath>
</defs>''')

    svg.append('<g clip-path="url(#viewport-clip)">')
    # Background Canvas
    svg.append(f'<rect width="{width}" height="{height}" fill="url(#light-cosmos)" stroke="#cbd5e1" stroke-width="1.8"/>')
    svg.append(f'<rect width="{width}" height="{height}" fill="url(#neb-cyan-light)"/>')
    svg.append(f'<rect width="{width}" height="{height}" fill="url(#neb-indigo-light)"/>')
    svg.append(f'<rect width="{width}" height="{height}" fill="url(#neb-amber-light)"/>')

    # Grid / Blueprint Lines
    svg.append('<!-- Blueprint Astronomical Guides -->')
    svg.append('<g stroke="#0284c7" stroke-opacity="0.06" stroke-width="1">')
    for x in range(0, width + 1, 60):
        svg.append(f'<line x1="{x}" y1="0" x2="{x}" y2="{height}"/>')
    for y in range(0, height + 1, 60):
        svg.append(f'<line x1="0" y1="{y}" x2="{width}" y2="{y}"/>')
    svg.append('</g>')

    # Constellation Dots
    svg.append('<!-- Constellation Starfield -->')
    svg.append('<g id="starfield">')
    for (sx, sy, sr, sdur, sbegin, sop, scolor) in stars:
        svg.append(f'<circle cx="{sx}" cy="{sy}" r="{sr}" fill="{scolor}" opacity="{sop}"><animate attributeName="opacity" values="{sop*0.3:.2f};{min(1.0, sop*1.8):.2f};{sop*0.3:.2f}" dur="{sdur}s" begin="{sbegin}s" repeatCount="indefinite"/></circle>')
    
    sparkles = [(140, 75), (1060, 95), (100, 520), (1100, 500), (600, 50)]
    for spx, spy in sparkles:
        svg.append(f'''<g transform="translate({spx},{spy})">
  <path d="M 0,-10 L 0,10 M -10,0 L 10,0" stroke="#0284c7" stroke-width="1.5" stroke-opacity="0.7">
    <animate attributeName="stroke-opacity" values="0.2;0.9;0.2" dur="3.0s" repeatCount="indefinite"/>
  </path>
  <circle r="2" fill="#0284c7"/>
</g>''')
    svg.append('</g>')

    # Orbital Ellipses
    svg.append('''<!-- Orbital Guides -->
<g transform="translate(600, 300)">
  <!-- Orbit 1 -->
  <g transform="rotate(-7)">
    <ellipse rx="215" ry="84" fill="none" stroke="#0284c7" stroke-width="1.8" stroke-opacity="0.35" stroke-dasharray="8 6">
      <animate attributeName="stroke-dashoffset" values="0;-140" dur="22s" repeatCount="indefinite"/>
    </ellipse>
  </g>
  <!-- Orbit 2 -->
  <g transform="rotate(5)">
    <ellipse rx="335" ry="130" fill="none" stroke="#16a34a" stroke-width="1.8" stroke-opacity="0.32" stroke-dasharray="10 8">
      <animate attributeName="stroke-dashoffset" values="0;-180" dur="32s" repeatCount="indefinite"/>
    </ellipse>
  </g>
  <!-- Orbit 3 -->
  <g transform="rotate(-4)">
    <ellipse rx="455" ry="175" fill="none" stroke="#7c3aed" stroke-width="1.8" stroke-opacity="0.30" stroke-dasharray="12 9">
      <animate attributeName="stroke-dashoffset" values="0;-210" dur="44s" repeatCount="indefinite"/>
    </ellipse>
  </g>
  <!-- Orbit 4 -->
  <g transform="rotate(3)">
    <ellipse rx="555" ry="215" fill="none" stroke="#ea580c" stroke-width="1.8" stroke-opacity="0.28" stroke-dasharray="14 10">
      <animate attributeName="stroke-dashoffset" values="0;-240" dur="58s" repeatCount="indefinite"/>
    </ellipse>
  </g>
</g>''')

    # Central Sun Star
    svg.append('''<!-- ==================== CENTRAL SUN ==================== -->
<g transform="translate(600, 300)">
  <!-- Solar Corona Flares -->
  <circle cx="0" cy="0" r="105" fill="url(#sun-corona-light)" opacity="0.85">
    <animate attributeName="r" values="95;115;95" dur="4.0s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.75;0.95;0.75" dur="4.0s" repeatCount="indefinite"/>
  </circle>

  <circle cx="0" cy="0" r="76" fill="#f59e0b" opacity="0.30" filter="url(#glow-sun-light)">
    <animate attributeName="r" values="72;84;72" dur="3.0s" repeatCount="indefinite"/>
  </circle>

  <!-- Sun Sphere -->
  <circle cx="0" cy="0" r="58" fill="url(#sun-body-light)" stroke="#fbbf24" stroke-width="2.5"/>

  <!-- Sun Rays Flare Ring -->
  <g>
    <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="360 0 0" dur="40s" repeatCount="indefinite"/>
    <circle cx="0" cy="0" r="66" fill="none" stroke="#fbbf24" stroke-width="2.5" stroke-dasharray="14 18" stroke-opacity="0.8"/>
  </g>
  <g>
    <animateTransform attributeName="transform" type="rotate" from="360 0 0" to="0 0 0" dur="28s" repeatCount="indefinite"/>
    <circle cx="0" cy="0" r="72" fill="none" stroke="#f59e0b" stroke-width="1.4" stroke-dasharray="8 24" stroke-opacity="0.6"/>
  </g>

  <!-- Core White Identity Chamber -->
  <circle cx="0" cy="0" r="42" fill="url(#avatar-chamber-light)" stroke="#f59e0b" stroke-width="2.2"/>
  
  <!-- Developer Avatar -->
  <g transform="translate(0, 4)">
    <text x="0" y="-8" text-anchor="middle" font-size="34">👨‍💻</text>
    <text x="0" y="16" text-anchor="middle" font-family="'Segoe UI',Inter,-apple-system,sans-serif" font-size="9.5" font-weight="900" fill="#0f172a" letter-spacing="1">PUNEETH</text>
    <text x="0" y="27" text-anchor="middle" font-family="'Segoe UI',Inter,-apple-system,sans-serif" font-size="7.5" font-weight="700" fill="#0284c7">KL UNIVERSITY</text>
  </g>
</g>''')

    # Planets
    for p_obj in planets_computed:
        meta = p_obj["meta"]
        tag = meta["name"]
        emoji = meta["emoji"]
        color = meta["color"]
        bg_col = meta["bg_color"]
        pr = meta["radius"]
        has_ring = meta["has_ring"]
        has_moon = meta["has_moon"]
        dur_val = p_obj["dur"]
        icon_type = meta["icon_type"]
        xs_str = p_obj["xs"]
        ys_str = p_obj["ys"]
        scales_str = p_obj["scales"]
        opacities_str = p_obj["opacities"]

        badge_w = max(80, len(tag) * 7.5 + 36)
        badge_h = 24
        badge_x = -badge_w / 2
        badge_y = pr + 8

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
        svg.append(f'    <circle cx="0" cy="0" r="{pr + 6}" fill="{color}" opacity="0.22"/>')

        # Planetary rings
        if has_ring:
            svg.append(f'    <ellipse cx="0" cy="0" rx="{pr * 2.1:.1f}" ry="{pr * 0.65:.1f}" fill="none" stroke="{color}" stroke-width="2.8" stroke-opacity="0.85" stroke-dasharray="10 3" transform="rotate(-18)"/>')
            svg.append(f'    <ellipse cx="0" cy="0" rx="{pr * 2.3:.1f}" ry="{pr * 0.72:.1f}" fill="none" stroke="{color}" stroke-width="1.2" stroke-opacity="0.5" transform="rotate(-18)"/>')

        # Spherical Globe Body
        svg.append(f'    <circle cx="0" cy="0" r="{pr}" fill="{bg_col}" stroke="{color}" stroke-width="2.2"/>')
        
        # Tech Emblem
        svg.append(f'    {render_emblem(icon_type, pr, color)}')

        # 3D Shading & Specular
        svg.append(f'    <circle cx="0" cy="0" r="{pr}" fill="url(#sph-shading-light)"/>')
        svg.append(f'    <circle cx="{-pr*0.35:.1f}" cy="{-pr*0.35:.1f}" r="{pr*0.5:.1f}" fill="url(#sph-specular-light)"/>')

        # Orbiting Natural Moon
        if has_moon:
            moon_dist = pr + 13
            svg.append(f'''    <g>
      <circle cx="{moon_dist}" cy="0" r="3.6" fill="#f8fafc" stroke="{color}" stroke-width="1.2">
        <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="360 0 0" dur="{round(dur_val*0.18, 1)}s" repeatCount="indefinite"/>
      </circle>
    </g>''')

        # Planet Name Label Pill (Clean White Light Mode Card)
        svg.append(f'    <g filter="url(#shadow-badge)">')
        svg.append(f'      <rect x="{badge_x:.1f}" y="{badge_y:.1f}" width="{badge_w:.1f}" height="{badge_h}" rx="12" fill="#ffffff" stroke="{color}" stroke-width="1.5"/>')
        svg.append(f'      <text x="{badge_x + 14:.1f}" y="{badge_y + 16.5:.1f}" font-size="12">{emoji}</text>')
        svg.append(f'      <text x="{badge_x + 30:.1f}" y="{badge_y + 16.5:.1f}" font-family="Inter,\'Segoe UI\',-apple-system,sans-serif" font-size="11.5" font-weight="800" fill="#0f172a" letter-spacing="0.3">{tag}</text>')
        svg.append(f'    </g>')

        svg.append(f'  </g>')
        svg.append(f'</g>')

    # Bottom Floating Dock HUD
    svg.append('''<!-- Bottom Tech Legend Dock HUD -->
<g transform="translate(42, 564)" filter="url(#shadow-dock)">
  <rect width="1116" height="40" rx="20" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="26" y="25" font-family="'Segoe UI',sans-serif" font-size="12.5" font-weight="900" fill="#0284c7">⚡ ORBIT 1:</text>
  <text x="108" y="25" font-family="'Segoe UI',sans-serif" font-size="12" font-weight="700" fill="#334155">React (⚛️) · TypeScript (TS) · Next.js (▲) · Tailwind (🌊)</text>
  
  <text x="490" y="25" font-family="'Segoe UI',sans-serif" font-size="12.5" font-weight="900" fill="#16a34a">⚙️ ORBIT 2:</text>
  <text x="572" y="25" font-family="'Segoe UI',sans-serif" font-size="12" font-weight="700" fill="#334155">Node (⬢) · Python (🐍) · Express (⚡) · JS (🟨)</text>

  <text x="890" y="25" font-family="'Segoe UI',sans-serif" font-size="12.5" font-weight="900" fill="#7c3aed">🔐 ORBIT 3 &amp; 4:</text>
  <text x="996" y="25" font-family="'Segoe UI',sans-serif" font-size="12" font-weight="700" fill="#334155">AWS (☁️) · Solidity (💎) · Docker (🐳) · Postgres (🐘)</text>
</g>''')

    svg.append('</g>')
    svg.append('</svg>')
    
    return "\n".join(svg)

if __name__ == "__main__":
    svg_content = generate_light_solar_system()
    with open("assets/skills-globe.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated light mode skills solar system ({len(svg_content)} bytes)")
