import math
import os

def generate_browser_bar():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 52" width="1200" height="52" role="img" aria-label="Browser Navigation Bar">
<defs>
  <linearGradient id="bb-sweep" x1="0" x2="1">
    <stop offset="0" stop-color="#0284c7" stop-opacity="0"/>
    <stop offset=".5" stop-color="#0284c7"/>
    <stop offset="1" stop-color="#0284c7" stop-opacity="0"/>
  </linearGradient>
  <filter id="rb-sh" x="-5%" y="-10%" width="110%" height="130%">
    <feDropShadow dx="0" dy="1" stdDeviation="2" flood-color="#0f172a" flood-opacity="0.05"/>
  </filter>
</defs>
<path d="M0 52 V16 Q0 0 16 0 H1184 Q1200 0 1200 16 V52 Z" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>
<!-- Window Traffic Controls -->
<circle cx="28" cy="26" r="6" fill="#ff5f56" stroke="#e0443e" stroke-width="0.7"/>
<circle cx="48" cy="26" r="6" fill="#ffbd2e" stroke="#dea123" stroke-width="0.7"/>
<circle cx="68" cy="26" r="6" fill="#27c93f" stroke="#1aab29" stroke-width="0.7"/>
<!-- Address Capsule -->
<rect x="96" y="10" width="1008" height="32" rx="16" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2" filter="url(#rb-sh)"/>
<path d="M118 22 a4.5 4.5 0 0 1 9 0 v3 h-9z M115 25 h15 v10 h-15z" fill="#10b981" transform="translate(0,-1) scale(0.95)"/>
<text x="142" y="31" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="13.5" font-weight="600" fill="#334155">https://puneethmanojsai.vercel.app</text>
<!-- Live Status Pill -->
<g transform="translate(1106, 12)">
  <rect width="78" height="28" rx="14" fill="#ecfdf5" stroke="#a7f3d0" stroke-width="1"/>
  <circle cx="16" cy="14" r="4" fill="#10b981">
    <animate attributeName="opacity" values="1;.2;1" dur="1.6s" repeatCount="indefinite"/>
  </circle>
  <text x="30" y="19" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="11.5" font-weight="800" fill="#047857" letter-spacing="0.5">LIVE</text>
</g>
<!-- Hairline Scanner -->
<rect x="0" y="50" width="1200" height="2" fill="#e2e8f0"/>
<rect x="-300" y="50" width="300" height="2" fill="url(#bb-sweep)">
  <animate attributeName="x" values="-300;1200" dur="3.5s" repeatCount="indefinite"/>
</rect>
</svg>'''

def generate_banner():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 380" width="1200" height="380" role="img" aria-label="Puneeth Manoj Sai - Front-End &amp; Full Stack Engineer">
<defs>
  <linearGradient id="hero-bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#ffffff"/>
    <stop offset="40%" stop-color="#f8fafc"/>
    <stop offset="80%" stop-color="#f0f9ff"/>
    <stop offset="100%" stop-color="#e0f2fe"/>
  </linearGradient>

  <linearGradient id="hero-tx" x1="0" x2="1">
    <stop offset="0%" stop-color="#0f172a"/>
    <stop offset="60%" stop-color="#1e3a8a"/>
    <stop offset="100%" stop-color="#0284c7"/>
  </linearGradient>

  <linearGradient id="bar-accent" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#0284c7"/>
    <stop offset="50%" stop-color="#6366f1"/>
    <stop offset="100%" stop-color="#a855f7"/>
  </linearGradient>

  <radialGradient id="spotlight-hero" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#0284c7" stop-opacity="0.10"/>
    <stop offset="70%" stop-color="#38bdf8" stop-opacity="0.02"/>
    <stop offset="100%" stop-color="#38bdf8" stop-opacity="0"/>
  </radialGradient>

  <filter id="hero-card-sh" x="-10%" y="-15%" width="120%" height="135%">
    <feDropShadow dx="0" dy="4" stdDeviation="10" flood-color="#0f172a" flood-opacity="0.07"/>
    <feDropShadow dx="0" dy="1" stdDeviation="2" flood-color="#0f172a" flood-opacity="0.04"/>
  </filter>

  <pattern id="hero-grid" x="0" y="0" width="32" height="32" patternUnits="userSpaceOnUse">
    <path d="M 32 0 L 0 0 0 32" fill="none" stroke="#0284c7" stroke-opacity="0.04" stroke-width="1"/>
  </pattern>

  <clipPath id="hero-clip"><rect width="1200" height="380" rx="20"/></clipPath>
</defs>

<g clip-path="url(#hero-clip)">
  <!-- Background Canvas -->
  <rect width="1200" height="380" fill="url(#hero-bg)" stroke="#cbd5e1" stroke-width="1.5"/>
  <rect width="1200" height="380" fill="url(#hero-grid)"/>
  
  <!-- Ambient Spotlight Glows -->
  <circle cx="260" cy="180" r="300" fill="url(#spotlight-hero)"/>
  <circle cx="920" cy="190" r="280" fill="url(#spotlight-hero)"/>

  <!-- Left Accent Bar -->
  <rect x="0" y="0" width="7" height="380" fill="url(#bar-accent)"/>

  <!-- ==================== LEFT COLUMN: HERO IDENTITY ==================== -->
  <g transform="translate(56, 36)">
    <rect width="186" height="26" rx="13" fill="#f0f9ff" stroke="#bae6fd" stroke-width="1"/>
    <circle cx="13" cy="13" r="3.5" fill="#0284c7">
      <animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite"/>
    </circle>
    <text x="25" y="17" font-family="'Fira Code',monospace" font-size="11" font-weight="700" fill="#0369a1" letter-spacing="1">SOFTWARE ENGINEER</text>
  </g>

  <!-- Name -->
  <text x="56" y="112" font-family="Inter,-apple-system,sans-serif" font-size="52" font-weight="900" fill="url(#hero-tx)">Puneeth Manoj Sai</text>
  
  <!-- Subtitle Lines -->
  <text x="56" y="148" font-family="Inter,-apple-system,sans-serif" font-size="18" fill="#1e293b" font-weight="800">Front-End &amp; Full Stack Engineer</text>
  <text x="56" y="172" font-family="Inter,-apple-system,sans-serif" font-size="13.5" fill="#64748b" font-weight="600">Building scalable web systems, cloud infrastructure &amp; Web3.</text>

  <!-- Animated Dynamic Typewriter Terminal Pill -->
  <g transform="translate(56, 202)">
    <rect width="560" height="42" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2" filter="url(#hero-card-sh)"/>
    <text x="18" y="26" font-family="'Fira Code',monospace" font-size="14" font-weight="700" fill="#0284c7">➜</text>
    
    <g>
      <clipPath id="ht0"><rect x="38" y="6" height="30" width="0"><animate attributeName="width" dur="16s" repeatCount="indefinite" keyTimes="0;0.0000;0.0875;0.2350;0.2500;1" values="0;0;490;490;0;0"/></rect></clipPath>
      <text x="38" y="26" font-family="'Fira Code',monospace" font-size="13.5" font-weight="600" fill="#0f172a" clip-path="url(#ht0)">React.js · Next.js · TypeScript · Tailwind CSS</text>
      <rect x="38" y="11" width="2" height="20" fill="#0284c7"><animate attributeName="x" dur="16s" repeatCount="indefinite" keyTimes="0;0.0000;0.0875;0.2350;0.2500;1" values="38;38;440;440;38;38"/><animate attributeName="opacity" values="1;0;1" dur=".9s" repeatCount="indefinite"/></rect>
    </g>
    <g>
      <clipPath id="ht1"><rect x="38" y="6" height="30" width="0"><animate attributeName="width" dur="16s" repeatCount="indefinite" keyTimes="0;0.2500;0.3375;0.4850;0.5000;1" values="0;0;490;490;0;0"/></rect></clipPath>
      <text x="38" y="26" font-family="'Fira Code',monospace" font-size="13.5" font-weight="600" fill="#0f172a" clip-path="url(#ht1)">AWS Certified Solutions Architect &amp; Cloud Practitioner</text>
      <rect x="38" y="11" width="2" height="20" fill="#0284c7"><animate attributeName="x" dur="16s" repeatCount="indefinite" keyTimes="0;0.2500;0.3375;0.4850;0.5000;1" values="38;38;510;510;38;38"/><animate attributeName="opacity" values="1;0;1" dur=".9s" repeatCount="indefinite"/></rect>
    </g>
    <g>
      <clipPath id="ht2"><rect x="38" y="6" height="30" width="0"><animate attributeName="width" dur="16s" repeatCount="indefinite" keyTimes="0;0.5000;0.5875;0.7350;0.7500;1" values="0;0;490;490;0;0"/></rect></clipPath>
      <text x="38" y="26" font-family="'Fira Code',monospace" font-size="13.5" font-weight="600" fill="#0f172a" clip-path="url(#ht2)">Solidity · IPFS · AES-256 Envelope Encryption</text>
      <rect x="38" y="11" width="2" height="20" fill="#0284c7"><animate attributeName="x" dur="16s" repeatCount="indefinite" keyTimes="0;0.5000;0.5875;0.7350;0.7500;1" values="38;38;440;440;38;38"/><animate attributeName="opacity" values="1;0;1" dur=".9s" repeatCount="indefinite"/></rect>
    </g>
    <g>
      <clipPath id="ht3"><rect x="38" y="6" height="30" width="0"><animate attributeName="width" dur="16s" repeatCount="indefinite" keyTimes="0;0.7500;0.8375;0.9850;1.0000;1" values="0;0;490;490;0;0"/></rect></clipPath>
      <text x="38" y="26" font-family="'Fira Code',monospace" font-size="13.5" font-weight="600" fill="#0f172a" clip-path="url(#ht3)">Provisional Patent Filed (2025) · Research (2026)</text>
      <rect x="38" y="11" width="2" height="20" fill="#0284c7"><animate attributeName="x" dur="16s" repeatCount="indefinite" keyTimes="0;0.7500;0.8375;0.9850;1.0000;1" values="38;38;470;470;38;38"/><animate attributeName="opacity" values="1;0;1" dur=".9s" repeatCount="indefinite"/></rect>
    </g>
  </g>

  <!-- 4 Spotlight Micro Badges -->
  <g transform="translate(56, 268)">
    <g transform="translate(0, 0)">
      <rect width="116" height="32" rx="16" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
      <circle cx="15" cy="16" r="4" fill="#10b981"><animate attributeName="opacity" values="1;.3;1" dur="2s" repeatCount="indefinite"/></circle>
      <text x="27" y="21" font-size="12.5" font-weight="700" fill="#0f172a" font-family="Inter,sans-serif">Patent Filed</text>
    </g>
    <g transform="translate(126, 0)">
      <rect width="144" height="32" rx="16" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
      <circle cx="15" cy="16" r="4" fill="#0284c7"><animate attributeName="opacity" values="1;.3;1" dur="2s" repeatCount="indefinite"/></circle>
      <text x="27" y="21" font-size="12.5" font-weight="700" fill="#0f172a" font-family="Inter,sans-serif">AWS Certified x2</text>
    </g>
    <g transform="translate(280, 0)">
      <rect width="154" height="32" rx="16" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
      <circle cx="15" cy="16" r="4" fill="#8b5cf6"><animate attributeName="opacity" values="1;.3;1" dur="2s" repeatCount="indefinite"/></circle>
      <text x="27" y="21" font-size="12.5" font-weight="700" fill="#0f172a" font-family="Inter,sans-serif">800+ Users Served</text>
    </g>
    <g transform="translate(444, 0)">
      <rect width="112" height="32" rx="16" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
      <circle cx="15" cy="16" r="4" fill="#f59e0b"><animate attributeName="opacity" values="1;.3;1" dur="2s" repeatCount="indefinite"/></circle>
      <text x="27" y="21" font-size="12.5" font-weight="700" fill="#0f172a" font-family="Inter,sans-serif">Tech Lead</text>
    </g>
  </g>

  <!-- ==================== RIGHT COLUMN: REACT BITS TERMINAL CARD ==================== -->
  <g transform="translate(654, 36)" filter="url(#hero-card-sh)">
    <rect width="490" height="308" rx="16" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
    <rect x="0" y="0" width="490" height="4" rx="2" fill="url(#bar-accent)"/>
    
    <g transform="translate(20, 18)">
      <circle cx="6" cy="8" r="4" fill="#ff5f56"/>
      <circle cx="20" cy="8" r="4" fill="#ffbd2e"/>
      <circle cx="34" cy="8" r="4" fill="#27c93f"/>
      <text x="60" y="12" font-family="'Fira Code',monospace" font-size="12" font-weight="700" fill="#64748b">engineer.config.ts</text>
      <rect x="376" y="0" width="74" height="20" rx="10" fill="#ecfdf5"/>
      <text x="413" y="14" text-anchor="middle" font-family="'Fira Code',monospace" font-size="10" font-weight="700" fill="#047857">ACTIVE</text>
    </g>
    <line x1="0" y1="44" x2="490" y2="44" stroke="#f1f5f9" stroke-width="1.2"/>

    <g transform="translate(20, 68)" font-family="'Fira Code',Consolas,monospace" font-size="12" font-weight="600">
      <text x="0" y="0" fill="#64748b"><tspan fill="#7c3aed">const</tspan> engineer <tspan fill="#0284c7">=</tspan> {</text>
      <text x="18" y="24" fill="#0f172a">name: <tspan fill="#059669">'Puneeth Manoj Sai'</tspan>,</text>
      <text x="18" y="48" fill="#0f172a">role: <tspan fill="#059669">'Software Engineer'</tspan>,</text>
      <text x="18" y="72" fill="#0f172a">university: <tspan fill="#059669">'KL University, Hyderabad'</tspan>,</text>
      <text x="18" y="96" fill="#0f172a">certifications: [<tspan fill="#d97706">'AWS-SAA'</tspan>, <tspan fill="#d97706">'AWS-CP'</tspan>, <tspan fill="#d97706">'MongoDB'</tspan>],</text>
      <text x="18" y="120" fill="#0f172a">patent: <tspan fill="#0284c7">'Ojas Raksha Consent Architecture'</tspan>,</text>
      <text x="18" y="144" fill="#0f172a">status: <tspan fill="#10b981">'Open to Internships &amp; Roles'</tspan></text>
      <text x="0" y="168" fill="#64748b">};</text>
    </g>

    <g transform="translate(20, 260)">
      <rect width="450" height="30" rx="8" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>
      <text x="14" y="19" font-family="'Fira Code',monospace" font-size="11" font-weight="700" fill="#0284c7">STACK BUS:</text>
      <text x="96" y="19" font-family="Inter,sans-serif" font-size="11.5" font-weight="700" fill="#334155">React 18 · Next.js · Node.js · AWS · Solidity · IPFS</text>
    </g>
  </g>
</g>
</svg>'''

def generate_metrics():
    metrics = [
        {"val": "800+", "title": "user interactions", "sub": "IEEE branch website", "color": "#0284c7", "x": 0, "dur": "5.0s"},
        {"val": "300+", "title": "GitHub commits", "sub": "high-velocity builder", "color": "#0d9488", "x": 204, "dur": "5.4s"},
        {"val": "10+", "title": "role dashboards", "sub": "Ojas Raksha dApp", "color": "#16a34a", "x": 408, "dur": "5.8s"},
        {"val": "50%", "title": "faster page load", "sub": "performance &amp; CI/CD", "color": "#d97706", "x": 612, "dur": "6.2s"},
        {"val": "4+", "title": "certifications", "sub": "AWS · Mongo · SF", "color": "#7c3aed", "x": 816, "dur": "6.6s"},
        {"val": "1", "title": "provisional patent", "sub": "filed 2025", "color": "#db2777", "x": 1020, "dur": "7.0s"}
    ]

    cards_svg = []
    for m in metrics:
        cards_svg.append(f'''<g transform="translate({m['x']},0)" filter="url(#card-sh)">
  <rect width="180" height="170" rx="16" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
  <rect x="0" y="0" width="180" height="4" rx="2" fill="{m['color']}"/>
  <circle cx="150" cy="30" r="46" fill="{m['color']}" opacity=".08">
    <animate attributeName="r" values="38;52;38" dur="4.0s" repeatCount="indefinite"/>
  </circle>
  <text x="20" y="80" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="48" font-weight="900" fill="{m['color']}">{m['val']}</text>
  <text x="20" y="108" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="14" font-weight="800" fill="#0f172a">{m['title']}</text>
  <text x="20" y="130" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="12" font-weight="500" fill="#64748b">{m['sub']}</text>
  <rect x="20" y="146" width="140" height="4" rx="2" fill="#f1f5f9"/>
  <rect x="20" y="146" width="40" height="4" rx="2" fill="{m['color']}">
    <animate attributeName="width" values="20;140;20" dur="{m['dur']}" repeatCount="indefinite"/>
  </rect>
</g>''')

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 170" width="1200" height="170" role="img" aria-label="Key impact metrics">
<defs>
  <filter id="card-sh" x="-10%" y="-10%" width="120%" height="130%">
    <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.06"/>
  </filter>
</defs>
{"".join(cards_svg)}
</svg>'''

def generate_header(num, title, sub, color):
    # Escape XML entities for attributes
    escaped_title = title.replace("&", "&amp;")
    escaped_sub = sub.replace("&", "&amp;")
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 96" width="1200" height="96" role="img" aria-label="{escaped_title}">
<defs>
  <linearGradient id="h-bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#ffffff"/>
    <stop offset="100%" stop-color="#f8fafc"/>
  </linearGradient>
  <linearGradient id="h-laser" x1="0" x2="1">
    <stop offset="0" stop-color="{color}" stop-opacity="0"/>
    <stop offset=".5" stop-color="{color}"/>
    <stop offset="1" stop-color="{color}" stop-opacity="0"/>
  </linearGradient>
  <filter id="h-shadow" x="-5%" y="-10%" width="110%" height="130%">
    <feDropShadow dx="0" dy="1" stdDeviation="3" flood-color="#0f172a" flood-opacity="0.05"/>
  </filter>
</defs>
<rect width="1200" height="96" rx="16" fill="url(#h-bg)" stroke="#cbd5e1" stroke-width="1.2" filter="url(#h-shadow)"/>
<rect x="28" y="24" width="6" height="48" rx="3" fill="{color}">
  <animate attributeName="opacity" values="1;.5;1" dur="3s" repeatCount="indefinite"/>
</rect>
<text x="52" y="46" font-family="'Fira Code',Consolas,'Courier New',monospace" font-size="15" font-weight="700" fill="{color}" letter-spacing="2">{num}</text>
<text x="52" y="76" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="30" font-weight="900" fill="#0f172a">{escaped_title}</text>
<text x="1172" y="58" text-anchor="end" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="15" font-weight="600" fill="#64748b">{escaped_sub}</text>
<rect x="0" y="93" width="1200" height="3" fill="#e2e8f0"/>
<rect x="-300" y="93" width="300" height="3" fill="url(#h-laser)">
  <animate attributeName="x" values="-300;1200" dur="4.0s" repeatCount="indefinite"/>
</rect>
</svg>'''

def generate_ojas_architecture():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 420" width="1200" height="420" role="img" aria-label="Ojas Raksha architecture diagram">
<defs>
  <linearGradient id="ojas-bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#ffffff"/>
    <stop offset="60%" stop-color="#f8fafc"/>
    <stop offset="100%" stop-color="#f0f9ff"/>
  </linearGradient>
  <filter id="ojas-sh" x="-10%" y="-15%" width="120%" height="140%">
    <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.08"/>
  </filter>
</defs>
<rect width="1200" height="420" rx="20" fill="url(#ojas-bg)" stroke="#cbd5e1" stroke-width="1.5"/>

<!-- Header -->
<text x="40" y="52" font-family="'Fira Code',Consolas,'Courier New',monospace" font-size="14" font-weight="700" fill="#6366f1" letter-spacing="3">FEATURED CASE STUDY</text>
<text x="40" y="82" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="26" font-weight="900" fill="#0f172a">Ojas Raksha · DPDP-Compliant Healthcare Consent</text>

<!-- Patent Badge -->
<g transform="translate(890, 30)">
  <rect width="270" height="36" rx="18" fill="#0284c7"/>
  <text x="135" y="23" text-anchor="middle" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="13.5" font-weight="900" fill="#ffffff" letter-spacing="0.5">PROVISIONAL PATENT FILED</text>
</g>

<!-- Animated Flow Connection Lines -->
<path d="M290 143 L330 143" fill="none" stroke="#94a3b8" stroke-width="2.5" stroke-dasharray="5 6">
  <animate attributeName="stroke-dashoffset" values="0;-22" dur="1.2s" repeatCount="indefinite"/>
</path>
<path d="M580 143 L620 143" fill="none" stroke="#94a3b8" stroke-width="2.5" stroke-dasharray="5 6">
  <animate attributeName="stroke-dashoffset" values="0;-22" dur="1.2s" repeatCount="indefinite"/>
</path>
<path d="M870 143 L910 143" fill="none" stroke="#94a3b8" stroke-width="2.5" stroke-dasharray="5 6">
  <animate attributeName="stroke-dashoffset" values="0;-22" dur="1.2s" repeatCount="indefinite"/>
</path>
<path d="M745 186 C745 230 455 226 455 270" fill="none" stroke="#94a3b8" stroke-width="2.5" stroke-dasharray="5 6">
  <animate attributeName="stroke-dashoffset" values="0;-22" dur="1.2s" repeatCount="indefinite"/>
</path>
<path d="M580 313 L620 313" fill="none" stroke="#94a3b8" stroke-width="2.5" stroke-dasharray="5 6">
  <animate attributeName="stroke-dashoffset" values="0;-22" dur="1.2s" repeatCount="indefinite"/>
</path>
<path d="M870 313 L910 313" fill="none" stroke="#94a3b8" stroke-width="2.5" stroke-dasharray="5 6">
  <animate attributeName="stroke-dashoffset" values="0;-22" dur="1.2s" repeatCount="indefinite"/>
</path>
<path d="M1035 270 L1035 186" fill="none" stroke="#94a3b8" stroke-width="2.5" stroke-dasharray="5 6">
  <animate attributeName="stroke-dashoffset" values="0;-22" dur="1.2s" repeatCount="indefinite"/>
</path>

<!-- Flowing Data Packet Beads -->
<circle r="5.5" fill="#0284c7"><animateMotion dur="2.6s" begin="0.00s" repeatCount="indefinite" path="M290 143 L330 143"/></circle>
<circle r="5.5" fill="#0284c7"><animateMotion dur="2.6s" begin="0.35s" repeatCount="indefinite" path="M580 143 L620 143"/></circle>
<circle r="5.5" fill="#0284c7"><animateMotion dur="2.6s" begin="0.70s" repeatCount="indefinite" path="M870 143 L910 143"/></circle>
<circle r="5.5" fill="#0284c7"><animateMotion dur="2.6s" begin="1.05s" repeatCount="indefinite" path="M745 186 C745 230 455 226 455 270"/></circle>
<circle r="5.5" fill="#0284c7"><animateMotion dur="2.6s" begin="1.40s" repeatCount="indefinite" path="M580 313 L620 313"/></circle>
<circle r="5.5" fill="#0284c7"><animateMotion dur="2.6s" begin="1.75s" repeatCount="indefinite" path="M870 313 L910 313"/></circle>
<circle r="5.5" fill="#0284c7"><animateMotion dur="2.6s" begin="2.10s" repeatCount="indefinite" path="M1035 270 L1035 186"/></circle>

<!-- Row 1 Cards -->
<g transform="translate(40,100)" filter="url(#ojas-sh)">
  <rect width="250" height="86" rx="14" fill="#ffffff" stroke="#d97706" stroke-width="1.5"/>
  <rect width="6" height="86" rx="3" fill="#d97706"/>
  <text x="24" y="36" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="18" font-weight="900" fill="#0f172a">Wallet Login</text>
  <text x="24" y="60" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="13" font-weight="600" fill="#64748b">MetaMask signature + nonce</text>
  <circle cx="228" cy="22" r="5" fill="#d97706"><animate attributeName="opacity" values="1;.3;1" dur="2s" repeatCount="indefinite"/></circle>
</g>

<g transform="translate(330,100)" filter="url(#ojas-sh)">
  <rect width="250" height="86" rx="14" fill="#ffffff" stroke="#0284c7" stroke-width="1.5"/>
  <rect width="6" height="86" rx="3" fill="#0284c7"/>
  <text x="24" y="36" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="18" font-weight="900" fill="#0f172a">React dApp</text>
  <text x="24" y="60" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="13" font-weight="600" fill="#64748b">10+ role-based dashboards</text>
  <circle cx="228" cy="22" r="5" fill="#0284c7"><animate attributeName="opacity" values="1;.3;1" dur="2s" repeatCount="indefinite"/></circle>
</g>

<g transform="translate(620,100)" filter="url(#ojas-sh)">
  <rect width="250" height="86" rx="14" fill="#ffffff" stroke="#16a34a" stroke-width="1.5"/>
  <rect width="6" height="86" rx="3" fill="#16a34a"/>
  <text x="24" y="36" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="18" font-weight="900" fill="#0f172a">Node.js API</text>
  <text x="24" y="60" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="13" font-weight="600" fill="#64748b">auth · audit tracking</text>
  <circle cx="228" cy="22" r="5" fill="#16a34a"><animate attributeName="opacity" values="1;.3;1" dur="2s" repeatCount="indefinite"/></circle>
</g>

<g transform="translate(910,100)" filter="url(#ojas-sh)">
  <rect width="250" height="86" rx="14" fill="#ffffff" stroke="#7c3aed" stroke-width="1.5"/>
  <rect width="6" height="86" rx="3" fill="#7c3aed"/>
  <text x="24" y="36" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="18" font-weight="900" fill="#0f172a">Solidity Contract</text>
  <text x="24" y="60" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="13" font-weight="600" fill="#64748b">grant · revoke · verifyAccess</text>
  <circle cx="228" cy="22" r="5" fill="#7c3aed"><animate attributeName="opacity" values="1;.3;1" dur="2s" repeatCount="indefinite"/></circle>
</g>

<!-- Row 2 Cards -->
<g transform="translate(330,270)" filter="url(#ojas-sh)">
  <rect width="250" height="86" rx="14" fill="#ffffff" stroke="#0891b2" stroke-width="1.5"/>
  <rect width="6" height="86" rx="3" fill="#0891b2"/>
  <text x="24" y="36" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="18" font-weight="900" fill="#0f172a">AES-256 Envelope</text>
  <text x="24" y="60" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="13" font-weight="600" fill="#64748b">unique DEK per document</text>
  <circle cx="228" cy="22" r="5" fill="#0891b2"><animate attributeName="opacity" values="1;.3;1" dur="2s" repeatCount="indefinite"/></circle>
</g>

<g transform="translate(620,270)" filter="url(#ojas-sh)">
  <rect width="250" height="86" rx="14" fill="#ffffff" stroke="#ea580c" stroke-width="1.5"/>
  <rect width="6" height="86" rx="3" fill="#ea580c"/>
  <text x="24" y="36" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="18" font-weight="900" fill="#0f172a">AWS KMS</text>
  <text x="24" y="60" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="13" font-weight="600" fill="#64748b">controlled key management</text>
  <circle cx="228" cy="22" r="5" fill="#ea580c"><animate attributeName="opacity" values="1;.3;1" dur="2s" repeatCount="indefinite"/></circle>
</g>

<g transform="translate(910,270)" filter="url(#ojas-sh)">
  <rect width="250" height="86" rx="14" fill="#ffffff" stroke="#db2777" stroke-width="1.5"/>
  <rect width="6" height="86" rx="3" fill="#db2777"/>
  <text x="24" y="36" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="18" font-weight="900" fill="#0f172a">IPFS</text>
  <text x="24" y="60" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="13" font-weight="600" fill="#64748b">encrypted off-chain storage</text>
  <circle cx="228" cy="22" r="5" fill="#db2777"><animate attributeName="opacity" values="1;.3;1" dur="2s" repeatCount="indefinite"/></circle>
</g>

<!-- Footer Annotations -->
<text x="40" y="238" font-family="'Fira Code',Consolas,'Courier New',monospace" font-size="12" font-weight="700" fill="#64748b">hash reference on-chain ↑ · encrypted document off-chain ↓</text>
<text x="40" y="386" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="14" font-weight="600" fill="#475569">React.js · Node.js · Solidity · MetaMask · IPFS · AWS KMS · AES-256 envelope encryption · blockchain integrity verification</text>
</svg>'''

def generate_stack():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 510" width="1200" height="510" role="img" aria-label="Tech stack by category">
<defs>
  <filter id="st-sh" x="-10%" y="-10%" width="120%" height="130%">
    <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.06"/>
  </filter>
</defs>

<!-- Frontend -->
<g transform="translate(0,0)" filter="url(#st-sh)">
  <rect width="380" height="240" rx="16" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
  <rect x="0" y="0" width="380" height="4" rx="2" fill="#0284c7"/>
  <text x="22" y="40" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="19" font-weight="900" fill="#0f172a">Frontend</text>
  <circle cx="352" cy="34" r="5" fill="#0284c7"/>
  <g transform="translate(22,62)"><rect width="85" height="28" rx="14" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.2"/><text x="42" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#0369a1">React.js</text></g>
  <g transform="translate(115,62)"><rect width="77" height="28" rx="14" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.2"/><text x="39" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#0369a1">Next.js</text></g>
  <g transform="translate(200,62)"><rect width="100" height="28" rx="14" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.2"/><text x="50" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#0369a1">TypeScript</text></g>
  <g transform="translate(22,100)"><rect width="100" height="28" rx="14" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.2"/><text x="50" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#0369a1">JavaScript</text></g>
  <g transform="translate(130,100)"><rect width="62" height="28" rx="14" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.2"/><text x="31" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#0369a1">HTML5</text></g>
  <g transform="translate(200,100)"><rect width="54" height="28" rx="14" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.2"/><text x="27" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#0369a1">CSS3</text></g>
  <g transform="translate(22,138)"><rect width="115" height="28" rx="14" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.2"/><text x="58" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#0369a1">Tailwind CSS</text></g>
  <g transform="translate(145,138)"><rect width="123" height="28" rx="14" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.2"/><text x="61" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#0369a1">Accessibility</text></g>
  <g transform="translate(22,176)"><rect width="108" height="28" rx="14" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.2"/><text x="54" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#0369a1">Performance</text></g>
</g>

<!-- Backend -->
<g transform="translate(410,0)" filter="url(#st-sh)">
  <rect width="380" height="240" rx="16" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
  <rect x="0" y="0" width="380" height="4" rx="2" fill="#16a34a"/>
  <text x="22" y="40" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="19" font-weight="900" fill="#0f172a">Backend</text>
  <circle cx="352" cy="34" r="5" fill="#16a34a"/>
  <g transform="translate(22,62)"><rect width="77" height="28" rx="14" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.2"/><text x="39" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#15803d">Node.js</text></g>
  <g transform="translate(107,62)"><rect width="100" height="28" rx="14" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.2"/><text x="50" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#15803d">Express.js</text></g>
  <g transform="translate(215,62)"><rect width="54" height="28" rx="14" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.2"/><text x="27" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#15803d">Java</text></g>
  <g transform="translate(22,100)"><rect width="108" height="28" rx="14" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.2"/><text x="54" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#15803d">Spring Boot</text></g>
  <g transform="translate(138,100)"><rect width="70" height="28" rx="14" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.2"/><text x="35" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#15803d">Python</text></g>
  <g transform="translate(215,100)"><rect width="62" height="28" rx="14" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.2"/><text x="31" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#15803d">Flask</text></g>
  <g transform="translate(22,138)"><rect width="92" height="28" rx="14" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.2"/><text x="46" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#15803d">REST APIs</text></g>
  <g transform="translate(122,138)"><rect width="123" height="28" rx="14" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.2"/><text x="61" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#15803d">Microservices</text></g>
</g>

<!-- Databases -->
<g transform="translate(820,0)" filter="url(#st-sh)">
  <rect width="380" height="240" rx="16" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
  <rect x="0" y="0" width="380" height="4" rx="2" fill="#d97706"/>
  <text x="22" y="40" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="19" font-weight="900" fill="#0f172a">Databases</text>
  <circle cx="352" cy="34" r="5" fill="#d97706"/>
  <g transform="translate(22,62)"><rect width="88" height="28" rx="14" fill="#fffbeb" stroke="#d97706" stroke-width="1.2"/><text x="44" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#b45309">MongoDB</text></g>
  <g transform="translate(118,62)"><rect width="100" height="28" rx="14" fill="#fffbeb" stroke="#d97706" stroke-width="1.2"/><text x="50" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#b45309">PostgreSQL</text></g>
  <g transform="translate(226,62)"><rect width="62" height="28" rx="14" fill="#fffbeb" stroke="#d97706" stroke-width="1.2"/><text x="31" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#b45309">MySQL</text></g>
  <g transform="translate(22,100)"><rect width="85" height="28" rx="14" fill="#fffbeb" stroke="#d97706" stroke-width="1.2"/><text x="42" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#b45309">Firebase</text></g>
  <g transform="translate(115,100)"><rect width="62" height="28" rx="14" fill="#fffbeb" stroke="#d97706" stroke-width="1.2"/><text x="31" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#b45309">Redis</text></g>
</g>

<!-- Cloud & DevOps -->
<g transform="translate(0,270)" filter="url(#st-sh)">
  <rect width="380" height="240" rx="16" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
  <rect x="0" y="0" width="380" height="4" rx="2" fill="#ea580c"/>
  <text x="22" y="40" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="19" font-weight="900" fill="#0f172a">Cloud &amp; DevOps</text>
  <circle cx="352" cy="34" r="5" fill="#ea580c"/>
  <g transform="translate(22,62)"><rect width="85" height="28" rx="14" fill="#fff7ed" stroke="#ea580c" stroke-width="1.2"/><text x="42" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#c2410c">AWS EC2</text></g>
  <g transform="translate(115,62)"><rect width="45" height="28" rx="14" fill="#fff7ed" stroke="#ea580c" stroke-width="1.2"/><text x="22" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#c2410c">S3</text></g>
  <g transform="translate(168,62)"><rect width="75" height="28" rx="14" fill="#fff7ed" stroke="#ea580c" stroke-width="1.2"/><text x="37" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#c2410c">Lambda</text></g>
  <g transform="translate(250,62)"><rect width="70" height="28" rx="14" fill="#fff7ed" stroke="#ea580c" stroke-width="1.2"/><text x="35" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#c2410c">Docker</text></g>
  <g transform="translate(22,100)"><rect width="130" height="28" rx="14" fill="#fff7ed" stroke="#ea580c" stroke-width="1.2"/><text x="65" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#c2410c">GitHub Actions</text></g>
  <g transform="translate(160,100)"><rect width="70" height="28" rx="14" fill="#fff7ed" stroke="#ea580c" stroke-width="1.2"/><text x="35" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#c2410c">Vercel</text></g>
  <g transform="translate(238,100)"><rect width="77" height="28" rx="14" fill="#fff7ed" stroke="#ea580c" stroke-width="1.2"/><text x="39" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#c2410c">Netlify</text></g>
  <g transform="translate(22,138)"><rect width="70" height="28" rx="14" fill="#fff7ed" stroke="#ea580c" stroke-width="1.2"/><text x="35" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#c2410c">Render</text></g>
  <g transform="translate(100,138)"><rect width="62" height="28" rx="14" fill="#fff7ed" stroke="#ea580c" stroke-width="1.2"/><text x="31" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#c2410c">Linux</text></g>
</g>

<!-- Web3 & Security -->
<g transform="translate(410,270)" filter="url(#st-sh)">
  <rect width="380" height="240" rx="16" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
  <rect x="0" y="0" width="380" height="4" rx="2" fill="#7c3aed"/>
  <text x="22" y="40" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="19" font-weight="900" fill="#0f172a">Web3 &amp; Security</text>
  <circle cx="352" cy="34" r="5" fill="#7c3aed"/>
  <g transform="translate(22,62)"><rect width="85" height="28" rx="14" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.2"/><text x="42" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#6d28d9">Solidity</text></g>
  <g transform="translate(115,62)"><rect width="92" height="28" rx="14" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.2"/><text x="46" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#6d28d9">Ethers.js</text></g>
  <g transform="translate(215,62)"><rect width="77" height="28" rx="14" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.2"/><text x="39" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#6d28d9">Web3.js</text></g>
  <g transform="translate(300,62)"><rect width="54" height="28" rx="14" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.2"/><text x="27" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#6d28d9">IPFS</text></g>
  <g transform="translate(22,100)"><rect width="115" height="28" rx="14" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.2"/><text x="58" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#6d28d9">Algorand SDK</text></g>
  <g transform="translate(145,100)"><rect width="85" height="28" rx="14" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.2"/><text x="42" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#6d28d9">MetaMask</text></g>
  <g transform="translate(238,100)"><rect width="123" height="28" rx="14" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.2"/><text x="61" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#6d28d9">WalletConnect</text></g>
  <g transform="translate(22,138)"><rect width="77" height="28" rx="14" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.2"/><text x="39" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#6d28d9">AES-256</text></g>
  <g transform="translate(107,138)"><rect width="77" height="28" rx="14" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.2"/><text x="39" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#6d28d9">AWS KMS</text></g>
  <g transform="translate(192,138)"><rect width="130" height="28" rx="14" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.2"/><text x="65" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#6d28d9">Applied Crypto</text></g>
</g>

<!-- Tools & AI -->
<g transform="translate(820,270)" filter="url(#st-sh)">
  <rect width="380" height="240" rx="16" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
  <rect x="0" y="0" width="380" height="4" rx="2" fill="#db2777"/>
  <text x="22" y="40" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="19" font-weight="900" fill="#0f172a">Tools &amp; AI</text>
  <circle cx="352" cy="34" r="5" fill="#db2777"/>
  <g transform="translate(22,62)"><rect width="47" height="28" rx="14" fill="#fdf2f8" stroke="#db2777" stroke-width="1.2"/><text x="23" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#be185d">Git</text></g>
  <g transform="translate(77,62)"><rect width="70" height="28" rx="14" fill="#fdf2f8" stroke="#db2777" stroke-width="1.2"/><text x="35" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#be185d">GitHub</text></g>
  <g transform="translate(154,62)"><rect width="77" height="28" rx="14" fill="#fdf2f8" stroke="#db2777" stroke-width="1.2"/><text x="39" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#be185d">Postman</text></g>
  <g transform="translate(240,62)"><rect width="62" height="28" rx="14" fill="#fdf2f8" stroke="#db2777" stroke-width="1.2"/><text x="31" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#be185d">Figma</text></g>
  <g transform="translate(22,100)"><rect width="77" height="28" rx="14" fill="#fdf2f8" stroke="#db2777" stroke-width="1.2"/><text x="39" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#be185d">VS Code</text></g>
  <g transform="translate(107,100)"><rect width="108" height="28" rx="14" fill="#fdf2f8" stroke="#db2777" stroke-width="1.2"/><text x="54" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#be185d">Prompt Eng.</text></g>
  <g transform="translate(223,100)"><rect width="138" height="28" rx="14" fill="#fdf2f8" stroke="#db2777" stroke-width="1.2"/><text x="69" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#be185d">AI-assisted Dev</text></g>
  <g transform="translate(22,138)"><rect width="123" height="28" rx="14" fill="#fdf2f8" stroke="#db2777" stroke-width="1.2"/><text x="61" y="19" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#be185d">Agile / Scrum</text></g>
</g>
</svg>'''

def generate_timeline():
    items = [
        {
            "role": "Open Source AI Fellow",
            "org": "Good Health 24/7 (MedPilot) · Remote",
            "desc": "Core product development and engineering deliverables for the MedPilot digital healthcare product.",
            "date": "Jul 2026 – Present",
            "color": "#0284c7",
            "y": 20,
            "begin": "0.0s"
        },
        {
            "role": "Cybersecurity Intern",
            "org": "Vaults of Code · Remote",
            "desc": "Application security, secure software development and security practices through hands-on technical tasks.",
            "date": "May 2026 – Jul 2026",
            "color": "#db2777",
            "y": 132,
            "begin": "0.4s"
        },
        {
            "role": "Tech Lead",
            "org": "Algorand Club · Hyderabad",
            "desc": "Led Algorand SDK / Solidity work, mentored a 10-member team and ran 5+ Web3 workshops (+40% participation).",
            "date": "Mar 2025 – Present",
            "color": "#7c3aed",
            "y": 244,
            "begin": "0.8s"
        },
        {
            "role": "AI Developer",
            "org": "Viswam AI · Remote",
            "desc": "Built AI-powered applications and datasets with intelligent features for real-world use cases.",
            "date": "May 2025 – Aug 2025",
            "color": "#d97706",
            "y": 356,
            "begin": "1.2s"
        },
        {
            "role": "Web Master &amp; Graphic Designer",
            "org": "IEEE Student Branch · Hyderabad",
            "desc": "React/Tailwind event sites cutting page load by 50%; GitHub Actions + Vercel CI/CD and visual branding.",
            "date": "Dec 2024 – Present",
            "color": "#16a34a",
            "y": 468,
            "begin": "1.6s"
        }
    ]

    cards_svg = []
    for it in items:
        cards_svg.append(f'''<g transform="translate(0,{it['y']})">
  <circle cx="70" cy="42" r="14" fill="{it['color']}" opacity=".15">
    <animate attributeName="r" values="12;22;12" dur="3s" begin="{it['begin']}" repeatCount="indefinite"/>
  </circle>
  <circle cx="70" cy="42" r="8" fill="{it['color']}"/>
  <g filter="url(#time-sh)">
    <rect x="120" y="0" width="1060" height="92" rx="14" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
    <rect x="120" y="0" width="6" height="92" rx="3" fill="{it['color']}"/>
    <text x="148" y="34" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="21" font-weight="900" fill="#0f172a">{it['role']}</text>
    <text x="148" y="58" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="14.5" fill="{it['color']}" font-weight="700">{it['org']}</text>
    <text x="148" y="80" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="13" font-weight="500" fill="#64748b">{it['desc']}</text>
    <g transform="translate(1010,16)">
      <rect width="150" height="28" rx="14" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1"/>
      <text x="75" y="19" text-anchor="middle" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="12.5" font-weight="700" fill="#334155">{it['date']}</text>
    </g>
  </g>
</g>''')

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 590" width="1200" height="590" role="img" aria-label="Experience timeline">
<defs>
  <filter id="time-sh" x="-5%" y="-10%" width="110%" height="130%">
    <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.06"/>
  </filter>
</defs>
<line x1="70" y1="30" x2="70" y2="550" stroke="#cbd5e1" stroke-width="3"/>
<line x1="70" y1="30" x2="70" y2="550" stroke="#0284c7" stroke-width="3" stroke-dasharray="14 200">
  <animate attributeName="stroke-dashoffset" values="0;-214" dur="5s" repeatCount="indefinite"/>
</line>
{"".join(cards_svg)}
</svg>'''

def generate_certs():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 330" width="1200" height="330" role="img" aria-label="Certifications and recognition">
<defs>
  <linearGradient id="certs-bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#ffffff"/>
    <stop offset="100%" stop-color="#f8fafc"/>
  </linearGradient>
  <filter id="cert-sh" x="-10%" y="-10%" width="120%" height="130%">
    <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.06"/>
  </filter>

  <!-- AWS Logo Def -->
  <g id="logo-aws">
    <g fill="#232F3E">
      <path d="M11.2 15.9c-1.1 0-2-.3-2.7-.8-.7-.5-1-1.3-1-2.2 0-1 .4-1.8 1-2.3.6-.5 1.6-.8 2.7-.8 1 0 1.8.1 2.5.5v-.8c0-.7-.2-1.2-.5-1.5-.4-.3-.9-.5-1.7-.5-.7 0-1.4.1-2 .4-.3.1-.6.2-.7.2-.2 0-.3-.1-.4-.3l-.6-1.1c-.1-.2 0-.3.1-.5.1-.1.4-.2.7-.3 1-.4 2.1-.6 3.3-.6 1.3 0 2.4.3 3.1 1.1.7.7 1.1 1.7 1.1 3v6.1c0 .3.1.5.2.6.1.1.3.1.6.1.1 0 .3 0 .4 0 .1 0 .2 0 .3.1.1.1.1.2.1.4v1c0 .2-.1.3-.2.4-.3.2-.7.3-1.2.3-.6 0-1.1-.2-1.5-.5-.3-.4-.5-.9-.6-1.5-.8 1.1-1.9 1.7-3.4 1.7zm.5-2c.8 0 1.6-.3 2.1-.9.5-.6.8-1.3.8-2.2v-.7c-.6-.3-1.3-.4-2-.4-.7 0-1.3.1-1.7.5-.4.3-.6.8-.6 1.4 0 .6.2 1 .5 1.4.4.6.8.9 1.4.9z"/>
      <path d="M26.1 15.7c-.2 0-.4-.1-.5-.3L22.2 7.7c-.1-.2 0-.4.2-.5.1 0 .2 0 .3 0h1.6c.2 0 .4.1.5.3l2 5.6 1.9-5.6c.1-.2.2-.3.5-.3h1.4c.2 0 .4.1.5.3l1.9 5.6 2-5.6c.1-.2.3-.3.5-.3h1.6c.2 0 .4.1.5.2.1.1.1.3 0 .5L34.6 15.4c-.1.2-.3.3-.5.3h-1.4c-.2 0-.4-.1-.5-.3L30.2 9.7l-1.9 5.6c-.1.2-.3.3-.5.3h-1.7z"/>
      <path d="M42.2 15.9c-1.2 0-2.3-.2-3.3-.7-.3-.1-.4-.3-.4-.5 0-.1.1-.3.2-.4l.8-1c.1-.1.3-.2.5-.1.1 0 .3.1.5.1.6.3 1.2.4 1.8.4.5 0 1-.1 1.3-.3.3-.2.4-.5.4-.9 0-.3-.1-.5-.4-.8-.2-.2-.7-.4-1.3-.7-1-.4-1.8-.8-2.3-1.4-.5-.5-.7-1.2-.7-1.9 0-.9.3-1.7 1-2.3.7-.6 1.6-.9 2.8-.9 1 0 1.9.2 2.8.5.3.1.4.2.4.4 0 .1-.1.3-.2.4l-.8.9c-.1.1-.3.2-.4.1-.1 0-.3-.1-.4-.1-.5-.2-1-.3-1.5-.3-.5 0-.9.1-1.2.3-.3.2-.4.4-.4.8 0 .2.1.5.4.7.2.2.7.4 1.4.7 1 .4 1.8.8 2.3 1.3.5.5.7 1.2.7 2 0 1-.3 1.8-1 2.3-.7.7-1.7 1.1-2.9 1.1z"/>
    </g>
    <path d="M42.4 22.7c-4.4 3.2-10.9 5-16.5 5-7.8 0-14.8-3-20.1-7.9-.4-.4 0-1 .5-.6 5.1 3.2 11.7 5.2 18.5 5.2 5.3 0 11.4-1.5 16.8-4.7.7-.5 1.5.4.8 1z" fill="#FF9900"/>
    <path d="M44.3 20.4c-.5-.7-3.7-.8-5.1-.2-.2.1-.1-.2 0-.4 1.5-1 5.3-.7 5.7-.1.4.6.1 4.4-1.3 5.6-.2.1-.4 0-.3-.1.6-1.3 1.5-4.1.9-4.8z" fill="#FF9900"/>
  </g>

  <!-- MongoDB Logo Def -->
  <g id="logo-mongodb">
    <path d="M24.9 1.0C23.6 2.4 16.8 9.6 16.3 19.7c-.4 8.8 4.1 15.9 7.4 20.3.9 1.2 1.1 1.5 1.2 3.3 0 .5.1 1.1.1 1.6 0 .2.2.3.4.3.2 0 .3-.2.3-.4 0-.8-.2-2.4.2-3.2 3.5-7.3 8.2-13.5 7.8-21.9-.4-8.8-6.8-16.4-8.3-18.8z" fill="#00ED64"/>
    <path d="M25.0 1.0c-.1 0-.3 0-.4.1-1.5 2.4-7.9 10-8.2 18.5-.4 8.3 4.3 14.5 7.8 21.9.4.8.2 2.4.2 3.2 0 .2.1.3.3.4.2 0 .4-.1.4-.3 0-.5-.1-1.1-.1-1.6-.1-1.8-.3-2.1-1.2-3.3-3.3-4.4-7.8-11.5-7.4-20.3.4-10.1 7.2-17.3 8.5-18.7.1 0 .1-.1.1-.1V1.0z" fill="#00684A"/>
    <path d="M25.1 0.9c0 0-.1-.1-.2 0-.1 0-.1.1-.1.2-.1 3 .2 6.4.7 9.4.8 4.9 2.1 9.6 2.1 14.6 0 5.6-1.5 11-3.6 16.2-.1.2-.1.5 0 .8 0 .2.1.5.4.6.2.1.4.1.6 0 .2-.1.3-.3.4-.5 2.1-5.4 3.8-11.1 3.8-17.1 0-5.2-1.3-10.1-2.2-15.2-.5-3.2-.9-6.6-.8-9.8 0-.1 0-.3-.2-.4z" fill="#001E2B" opacity="0.3"/>
  </g>

  <!-- Salesforce Logo Def -->
  <g id="logo-salesforce">
    <path d="M21.1 5.1c2.3-2.7 5.8-4.5 9.7-4.5 6 0 11.1 4.2 12.4 9.8 2 1 3.6 2.7 4.3 4.9 1 2.8.7 5.8-.7 8.4-1.4 2.5-3.8 4.3-6.6 4.9-1 .2-1.9.3-2.9.3H12.2c-2.4 0-4.8-.8-6.6-2.4C3.2 24.6 1.7 22.2 1.3 19.6c-.4-2.6.3-5.3 1.9-7.5 1.6-2.1 4-3.5 6.7-3.8 1-.1 2.1 0 3.1.2 1.8-2 4.4-3.3 8-3.3z" fill="#00A1E0"/>
    <path d="M14.2 17.3c-.3-.5-.4-1.1-.4-1.7 0-1.8 1.3-3.1 3.2-3.1 1.2 0 2.1.5 2.6 1.2l-1.2.9c-.3-.4-.8-.7-1.4-.7-.9 0-1.6.7-1.6 1.7 0 .9.6 1.6 1.6 1.6.6 0 1.1-.2 1.4-.7l1.2.9c-.6.8-1.5 1.3-2.6 1.3-1.1 0-2-.4-2.5-1.4zm7.7 1.3h-1.6v-7.5h1.6v7.5zm5.3-4.7c-.3-.2-.6-.3-1.1-.3-.8 0-1.4.5-1.4 1.3 0 .7.5 1 1.1 1.3l.6.2c1.2.4 1.9 1.1 1.9 2.3 0 1.4-1.2 2.4-2.8 2.4-1 0-1.8-.3-2.4-.9l.9-1c.4.4.9.7 1.4.7.8 0 1.3-.4 1.3-1.1 0-.7-.4-1-1.2-1.3l-.6-.2c-1.1-.4-1.8-1-1.8-2.2 0-1.4 1.1-2.4 2.7-2.4.8 0 1.6.2 2.1.7l-.7 1.2zm5 4.7h-1.6v-7.5h1.6v7.5zm4.2-2.1h2.7v1.4h-2.7v3.2h-1.6v-7.5h4.5v1.4h-2.9v2.2z" fill="#ffffff"/>
  </g>
</defs>
<rect width="1200" height="330" rx="20" fill="url(#certs-bg)" stroke="#cbd5e1" stroke-width="1.5"/>

<!-- Card 1: AWS Cloud Practitioner -->
<g transform="translate(45,30)" filter="url(#cert-sh)">
  <animateTransform attributeName="transform" type="translate" values="45,34;45,26;45,34" dur="5.0s" repeatCount="indefinite"/>
  <rect width="255" height="150" rx="16" fill="#ffffff" stroke="#ea580c" stroke-width="1.5"/>
  <rect width="255" height="4" rx="2" fill="#ea580c"/>
  
  <!-- Authentic AWS Logo -->
  <g transform="translate(18,24) scale(1.15)">
    <rect width="52" height="34" rx="8" fill="#fff7ed" stroke="#fdba74" stroke-width="1"/>
    <use href="#logo-aws" x="3" y="3"/>
  </g>
  
  <text x="86" y="44" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="13" fill="#ea580c" font-weight="800">AWS Certified</text>
  <text x="86" y="66" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="15" fill="#0f172a" font-weight="900">Cloud Practitioner</text>
  <text x="86" y="84" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="12" fill="#64748b" font-weight="600">Foundational</text>
  
  <rect x="18" y="104" width="219" height="1" fill="#e2e8f0"/>
  <text x="18" y="126" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="11.5" font-weight="600" fill="#0369a1">✓ Verified Credential</text>
  <text x="18" y="142" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="11" font-weight="500" fill="#64748b">Amazon Web Services · 2024</text>
</g>

<!-- Card 2: AWS Solutions Architect -->
<g transform="translate(330,30)" filter="url(#cert-sh)">
  <animateTransform attributeName="transform" type="translate" values="330,34;330,26;330,34" dur="5.6s" repeatCount="indefinite"/>
  <rect width="255" height="150" rx="16" fill="#ffffff" stroke="#d97706" stroke-width="1.5"/>
  <rect width="255" height="4" rx="2" fill="#d97706"/>
  
  <!-- Authentic AWS Logo -->
  <g transform="translate(18,24) scale(1.15)">
    <rect width="52" height="34" rx="8" fill="#fffbeb" stroke="#fde68a" stroke-width="1"/>
    <use href="#logo-aws" x="3" y="3"/>
  </g>
  
  <text x="86" y="44" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="13" fill="#d97706" font-weight="800">AWS Certified</text>
  <text x="86" y="66" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="15" fill="#0f172a" font-weight="900">Solutions Architect</text>
  <text x="86" y="84" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="12" fill="#64748b" font-weight="600">Associate Level</text>
  
  <rect x="18" y="104" width="219" height="1" fill="#e2e8f0"/>
  <text x="18" y="126" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="11.5" font-weight="600" fill="#0369a1">✓ Verified Credential</text>
  <text x="18" y="142" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="11" font-weight="500" fill="#64748b">Amazon Web Services · 2024</text>
</g>

<!-- Card 3: MongoDB Certified -->
<g transform="translate(615,30)" filter="url(#cert-sh)">
  <animateTransform attributeName="transform" type="translate" values="615,34;615,26;615,34" dur="6.2s" repeatCount="indefinite"/>
  <rect width="255" height="150" rx="16" fill="#ffffff" stroke="#16a34a" stroke-width="1.5"/>
  <rect width="255" height="4" rx="2" fill="#16a34a"/>
  
  <!-- Authentic MongoDB Logo -->
  <g transform="translate(18,24)">
    <rect width="52" height="46" rx="8" fill="#f0fdf4" stroke="#bbf7d0" stroke-width="1"/>
    <use href="#logo-mongodb" x="1" y="0"/>
  </g>
  
  <text x="82" y="44" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="13" fill="#16a34a" font-weight="800">MongoDB Certified</text>
  <text x="82" y="66" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="15" fill="#0f172a" font-weight="900">Associate Developer</text>
  <text x="82" y="84" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="12" fill="#64748b" font-weight="600">Database Modeling</text>
  
  <rect x="18" y="104" width="219" height="1" fill="#e2e8f0"/>
  <text x="18" y="126" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="11.5" font-weight="600" fill="#15803d">✓ Verified Credential</text>
  <text x="18" y="142" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="11" font-weight="500" fill="#64748b">MongoDB University · 2024</text>
</g>

<!-- Card 4: Salesforce Agentforce -->
<g transform="translate(900,30)" filter="url(#cert-sh)">
  <animateTransform attributeName="transform" type="translate" values="900,34;900,26;900,34" dur="6.8s" repeatCount="indefinite"/>
  <rect width="255" height="150" rx="16" fill="#ffffff" stroke="#0284c7" stroke-width="1.5"/>
  <rect width="255" height="4" rx="2" fill="#0284c7"/>
  
  <!-- Authentic Salesforce Logo -->
  <g transform="translate(18,24)">
    <rect width="52" height="46" rx="8" fill="#f0f9ff" stroke="#bae6fd" stroke-width="1"/>
    <use href="#logo-salesforce" x="1" y="8"/>
  </g>
  
  <text x="82" y="44" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="13" fill="#0284c7" font-weight="800">Salesforce</text>
  <text x="82" y="66" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="15" fill="#0f172a" font-weight="900">Agentforce Specialist</text>
  <text x="82" y="84" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="12" fill="#64748b" font-weight="600">AI Agent Architect</text>
  
  <rect x="18" y="104" width="219" height="1" fill="#e2e8f0"/>
  <text x="18" y="126" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="11.5" font-weight="600" fill="#0369a1">✓ Verified Specialist</text>
  <text x="18" y="142" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="11" font-weight="500" fill="#64748b">Salesforce · 2025</text>
</g>

<!-- Recognition Badges -->
<g transform="translate(30,230)">
  <rect width="404" height="36" rx="18" fill="#eff6ff" stroke="#0284c7" stroke-width="1.2"/>
  <text x="202" y="23" text-anchor="middle" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="13.5" font-weight="700" fill="#0369a1">Provisional Patent Filed · Ojas Raksha (2025)</text>
</g>
<g transform="translate(448,230)">
  <rect width="315" height="36" rx="18" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.2"/>
  <text x="158" y="23" text-anchor="middle" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="13.5" font-weight="700" fill="#6d28d9">Research Paper Under Review (2026)</text>
</g>
<g transform="translate(778,230)">
  <rect width="307" height="36" rx="18" fill="#ecfdf5" stroke="#16a34a" stroke-width="1.2"/>
  <text x="154" y="23" text-anchor="middle" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="13.5" font-weight="700" fill="#15803d">IEEE Student Belt Performer Award</text>
</g>
<g transform="translate(30,276)">
  <rect width="356" height="36" rx="18" fill="#fdf2f8" stroke="#db2777" stroke-width="1.2"/>
  <text x="178" y="23" text-anchor="middle" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="13.5" font-weight="700" fill="#be185d">Best Volunteering Medal · KL University</text>
</g>
</svg>'''

def generate_footer():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 190" width="1200" height="190" role="img" aria-label="Let's build something great together">
<defs>
  <linearGradient id="ft-bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#ffffff"/>
    <stop offset="100%" stop-color="#f0f9ff"/>
  </linearGradient>
  <linearGradient id="ft-tx" x1="0" x2="1">
    <stop offset="0%" stop-color="#0f172a"/>
    <stop offset="60%" stop-color="#1e40af"/>
    <stop offset="100%" stop-color="#0284c7"/>
  </linearGradient>
  <clipPath id="c-ft"><rect width="1200" height="190" rx="20"/></clipPath>
</defs>
<g clip-path="url(#c-ft)">
  <rect width="1200" height="190" fill="url(#ft-bg)" stroke="#cbd5e1" stroke-width="1.5"/>
  
  <!-- Wave 1 (Sky Light) -->
  <path d="M0 128 L0 128.0 L20 131.1 L40 134.0 L60 136.7 L80 138.9 L100 140.5 L120 141.6 L140 142.0 L160 141.7 L180 140.7 L200 139.1 L220 137.0 L240 134.4 L260 131.5 L280 128.4 L300 125.3 L320 122.4 L340 119.7 L360 117.4 L380 115.6 L400 114.5 L420 114.0 L440 114.2 L460 115.1 L480 116.6 L500 118.7 L520 121.2 L540 124.1 L560 127.1 L580 130.2 L600 133.2 L620 136.0 L640 138.3 L660 140.1 L680 141.4 L700 142.0 L720 141.9 L740 141.1 L760 139.6 L780 137.6 L800 135.1 L820 132.3 L840 129.3 L860 126.2 L880 123.2 L900 120.4 L920 118.0 L940 116.1 L960 114.8 L980 114.1 L1000 114.1 L1020 114.8 L1040 116.1 L1060 118.1 L1080 120.5 L1100 123.3 L1120 126.3 L1140 129.4 L1160 132.4 L1180 135.3 L1200 137.7 L1220 139.7 L1240 141.1 L1260 141.9 L1280 141.9 L1300 141.3 L1320 140.1 L1340 138.2 L1360 135.9 L1380 133.1 L1400 130.1 L1420 127.0 L1440 124.0 L1460 121.1 L1480 118.6 L1500 116.5 L1520 115.1 L1540 114.2 L1560 114.0 L1580 114.5 L1600 115.7 L1620 117.5 L1640 119.8 L1660 122.5 L1680 125.5 L1700 128.6 L1720 131.6 L1740 134.5 L1760 137.1 L1780 139.2 L1800 140.8 L1820 141.7 L1840 142.0 L1860 141.6 L1880 140.5 L1900 138.8 L1920 136.6 L1940 133.9 L1960 131.0 L1980 127.9 L2000 124.8 L2020 121.9 L2040 119.2 L2060 117.1 L2080 115.4 L2100 114.4 L2120 114.0 L2140 114.3 L2160 115.3 L2180 116.9 L2200 119.1 L2220 121.7 L2240 124.6 L2260 127.7 L2280 130.8 L2300 133.7 L2320 136.4 L2340 138.7 L2360 140.4 L2380 141.5 L2400 142.0 L2420 141.8 L2440 190 L0 190 Z" fill="#0284c7" fill-opacity=".18">
    <animateTransform attributeName="transform" type="translate" values="0,0;-565,0" dur="14s" repeatCount="indefinite"/>
  </path>

  <!-- Wave 2 (Indigo Light) -->
  <path d="M0 128 L0 137.1 L20 136.0 L40 134.4 L60 132.6 L80 130.5 L100 128.3 L120 126.1 L140 124.0 L160 122.1 L180 120.4 L200 119.2 L220 118.4 L240 118.0 L260 118.2 L280 118.8 L300 119.9 L320 121.3 L340 123.2 L360 125.2 L380 127.4 L400 129.6 L420 131.7 L440 133.7 L460 135.4 L480 136.7 L500 137.6 L520 138.0 L540 137.9 L560 137.3 L580 136.3 L600 134.9 L620 133.1 L640 131.1 L660 128.9 L680 126.7 L700 124.5 L720 122.6 L740 120.8 L760 119.5 L780 118.5 L800 118.1 L820 118.1 L840 118.6 L860 119.5 L880 120.9 L900 122.6 L920 124.6 L940 126.8 L960 129.0 L980 131.2 L1000 133.2 L1020 134.9 L1040 136.4 L1060 137.4 L1080 137.9 L1100 138.0 L1120 137.5 L1140 136.6 L1160 135.3 L1180 133.6 L1200 131.7 L1220 129.5 L1240 127.3 L1260 125.1 L1280 123.1 L1300 121.3 L1320 119.8 L1340 118.8 L1360 118.1 L1380 118.0 L1400 118.4 L1420 119.2 L1440 120.5 L1460 122.1 L1480 124.1 L1500 126.2 L1520 128.4 L1540 130.6 L1560 132.7 L1580 134.5 L1600 136.0 L1620 137.1 L1640 137.8 L1660 138.0 L1680 137.7 L1700 136.9 L1720 135.7 L1740 134.1 L1760 132.2 L1780 130.1 L1800 127.9 L1820 125.7 L1840 123.6 L1860 121.7 L1880 120.2 L1900 119.0 L1920 118.3 L1940 118.0 L1960 118.2 L1980 118.9 L2000 120.1 L2020 121.6 L2040 123.5 L2060 125.6 L2080 127.8 L2100 130.0 L2120 132.1 L2140 134.0 L2160 135.6 L2180 136.9 L2200 137.7 L2220 138.0 L2240 137.8 L2260 137.2 L2280 136.1 L2300 134.6 L2320 132.8 L2340 130.7 L2360 128.5 L2380 126.3 L2400 124.2 L2420 122.2 L2440 190 L0 190 Z" fill="#6366f1" fill-opacity=".18">
    <animateTransform attributeName="transform" type="translate" values="-565,0;0,0" dur="18s" repeatCount="indefinite"/>
  </path>

  <text x="600" y="70" text-anchor="middle" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="34" font-weight="900" fill="url(#ft-tx)">Let's build something great together.</text>
  <text x="600" y="104" text-anchor="middle" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="16" font-weight="700" fill="#0284c7">Open to internships and full-time roles  ·  Hyderabad, India</text>
</g>
</svg>'''

if __name__ == "__main__":
    os.makedirs("assets", exist_ok=True)
    
    files = {
        "assets/browser-bar.svg": generate_browser_bar(),
        "assets/banner.svg": generate_banner(),
        "assets/metrics.svg": generate_metrics(),
        "assets/ojas-architecture.svg": generate_ojas_architecture(),
        "assets/stack.svg": generate_stack(),
        "assets/timeline.svg": generate_timeline(),
        "assets/certs.svg": generate_certs(),
        "assets/footer.svg": generate_footer(),
        "assets/h-about.svg": generate_header("01 /", "About Me", "Engineer · builder · researcher", "#0284c7"),
        "assets/h-work.svg": generate_header("02 /", "Featured Work", "Shipped products and research", "#7c3aed"),
        "assets/h-exp.svg": generate_header("03 /", "Experience", "Roles and leadership", "#16a34a"),
        "assets/h-stack.svg": generate_header("04 /", "Tech Stack", "What I build with", "#d97706"),
        "assets/h-certs.svg": generate_header("05 /", "Certifications & Recognition", "Verified credentials", "#db2777"),
        "assets/h-stats.svg": generate_header("06 /", "Impact & Activity", "Numbers that matter", "#2563eb")
    }

    for path, content in files.items():
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {path} ({len(content)} bytes)")
