import math
import os

def generate_browser_bar():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 52" width="1200" height="52" role="img" aria-label="Browser window: https://puneethmanojsai.vercel.app">
<defs>
  <linearGradient id="bb-line" x1="0" x2="1">
    <stop offset="0" stop-color="#0284c7" stop-opacity="0"/>
    <stop offset=".5" stop-color="#0284c7"/>
    <stop offset="1" stop-color="#0284c7" stop-opacity="0"/>
  </linearGradient>
  <filter id="bb-shadow" x="-5%" y="-10%" width="110%" height="130%">
    <feDropShadow dx="0" dy="1" stdDeviation="2" flood-color="#0f172a" flood-opacity="0.06"/>
  </filter>
</defs>
<path d="M0 52 V16 Q0 0 16 0 H1184 Q1200 0 1200 16 V52 Z" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>
<!-- Window Traffic Controls -->
<circle cx="28" cy="26" r="6.5" fill="#ff5f56" stroke="#e0443e" stroke-width="0.8"/>
<circle cx="50" cy="26" r="6.5" fill="#ffbd2e" stroke="#dea123" stroke-width="0.8"/>
<circle cx="72" cy="26" r="6.5" fill="#27c93f" stroke="#1aab29" stroke-width="0.8"/>
<!-- Address Capsule -->
<rect x="106" y="10" width="988" height="32" rx="16" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2" filter="url(#bb-shadow)"/>
<!-- Lock Icon -->
<path d="M128 22 a4.5 4.5 0 0 1 9 0 v3 h-9z M125 25 h15 v10 h-15z" fill="#10b981" transform="translate(0,-1) scale(0.95)"/>
<text x="154" y="31" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="13.5" font-weight="600" fill="#334155">https://puneethmanojsai.vercel.app</text>
<!-- Live Status Pill -->
<g transform="translate(1096, 12)">
  <rect width="84" height="28" rx="14" fill="#ecfdf5" stroke="#a7f3d0" stroke-width="1"/>
  <circle cx="16" cy="14" r="4" fill="#10b981">
    <animate attributeName="opacity" values="1;.2;1" dur="1.6s" repeatCount="indefinite"/>
  </circle>
  <text x="30" y="19" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="11.5" font-weight="800" fill="#047857" letter-spacing="0.5">LIVE</text>
</g>
<!-- Hairline Scanner -->
<rect x="0" y="50" width="1200" height="2" fill="#e2e8f0"/>
<rect x="-300" y="50" width="300" height="2" fill="url(#bb-line)">
  <animate attributeName="x" values="-300;1200" dur="3.5s" repeatCount="indefinite"/>
</rect>
</svg>'''

def generate_banner():
    # Read animated 3D sphere polyhedra from existing banner to preserve exact geometric keyframe smoothness
    # and re-theme with ultra-crisp light mode gradient colors
    with open("assets/banner.svg", "r", encoding="utf-8") as f:
        orig = f.read()

    # Extract polygon animations
    poly_start = orig.find("<polygon")
    poly_end = orig.rfind("</polygon>") + 10
    polys = orig[poly_start:poly_end]

    # Transform dark polygons to light palette
    polys_light = polys.replace('fill="#16496c"', 'fill="#bae6fd"')
    polys_light = polys_light.replace('fill="#4487ac"', 'fill="#7dd3fc"')
    polys_light = polys_light.replace('fill="#6cbde5"', 'fill="#e0f2fe"')
    polys_light = polys_light.replace('fill="#347196"', 'fill="#93c5fd"')
    polys_light = polys_light.replace('stroke="#67e8f9"', 'stroke="#0284c7"')
    polys_light = polys_light.replace('stroke-opacity=".35"', 'stroke-opacity=".55"')

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 380" width="1200" height="380" role="img" aria-label="Puneeth Manoj Sai - Front-End &amp; Full Stack Engineer">
<defs>
  <linearGradient id="bg-light" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#ffffff"/>
    <stop offset="35%" stop-color="#f8fafc"/>
    <stop offset="75%" stop-color="#f0f9ff"/>
    <stop offset="100%" stop-color="#e0f2fe"/>
  </linearGradient>
  <linearGradient id="tx-dark" x1="0" x2="1">
    <stop offset="0%" stop-color="#0f172a"/>
    <stop offset="60%" stop-color="#1e3a8a"/>
    <stop offset="100%" stop-color="#0284c7"/>
  </linearGradient>
  <linearGradient id="bar-grad" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#0284c7"/>
    <stop offset="50%" stop-color="#6366f1"/>
    <stop offset="100%" stop-color="#a855f7"/>
  </linearGradient>
  <radialGradient id="glow-light">
    <stop offset="0%" stop-color="#0284c7" stop-opacity=".18"/>
    <stop offset="60%" stop-color="#38bdf8" stop-opacity=".06"/>
    <stop offset="100%" stop-color="#38bdf8" stop-opacity="0"/>
  </radialGradient>
  <filter id="card-shadow" x="-10%" y="-20%" width="120%" height="150%">
    <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0f172a" flood-opacity="0.08"/>
  </filter>
  <clipPath id="c-banner"><rect width="1200" height="380" rx="20"/></clipPath>
</defs>
<g clip-path="url(#c-banner)">
  <rect width="1200" height="380" fill="url(#bg-light)" stroke="#cbd5e1" stroke-width="1.8"/>
  
  <!-- Subtle Blueprint Grid -->
  <g stroke="#0284c7" stroke-opacity=".05" stroke-width="1">
    <line x1="0" y1="0" x2="0" y2="380"/><line x1="40" y1="0" x2="40" y2="380"/><line x1="80" y1="0" x2="80" y2="380"/><line x1="120" y1="0" x2="120" y2="380"/><line x1="160" y1="0" x2="160" y2="380"/><line x1="200" y1="0" x2="200" y2="380"/><line x1="240" y1="0" x2="240" y2="380"/><line x1="280" y1="0" x2="280" y2="380"/><line x1="320" y1="0" x2="320" y2="380"/><line x1="360" y1="0" x2="360" y2="380"/><line x1="400" y1="0" x2="400" y2="380"/><line x1="440" y1="0" x2="440" y2="380"/><line x1="480" y1="0" x2="480" y2="380"/><line x1="520" y1="0" x2="520" y2="380"/><line x1="560" y1="0" x2="560" y2="380"/><line x1="600" y1="0" x2="600" y2="380"/><line x1="640" y1="0" x2="640" y2="380"/><line x1="680" y1="0" x2="680" y2="380"/><line x1="720" y1="0" x2="720" y2="380"/><line x1="760" y1="0" x2="760" y2="380"/><line x1="800" y1="0" x2="800" y2="380"/><line x1="840" y1="0" x2="840" y2="380"/><line x1="880" y1="0" x2="880" y2="380"/><line x1="920" y1="0" x2="920" y2="380"/><line x1="960" y1="0" x2="960" y2="380"/><line x1="1000" y1="0" x2="1000" y2="380"/><line x1="1040" y1="0" x2="1040" y2="380"/><line x1="1080" y1="0" x2="1080" y2="380"/><line x1="1120" y1="0" x2="1120" y2="380"/><line x1="1160" y1="0" x2="1160" y2="380"/>
    <line x1="0" y1="0" x2="1200" y2="0"/><line x1="0" y1="40" x2="1200" y2="40"/><line x1="0" y1="80" x2="1200" y2="80"/><line x1="0" y1="120" x2="1200" y2="120"/><line x1="0" y1="160" x2="1200" y2="160"/><line x1="0" y1="200" x2="1200" y2="200"/><line x1="0" y1="240" x2="1200" y2="240"/><line x1="0" y1="280" x2="1200" y2="280"/><line x1="0" y1="320" x2="1200" y2="320"/><line x1="0" y1="360" x2="1200" y2="360"/>
  </g>

  <!-- Glowing Aura for 3D Geometry -->
  <circle cx="960" cy="190" r="220" fill="url(#glow-light)">
    <animate attributeName="r" values="190;240;190" dur="7s" repeatCount="indefinite"/>
  </circle>
  <ellipse cx="960" cy="190" rx="210" ry="60" fill="none" stroke="#0284c7" stroke-opacity=".35" stroke-dasharray="4 8">
    <animate attributeName="stroke-dashoffset" values="0;-96" dur="6s" repeatCount="indefinite"/>
  </ellipse>
  <ellipse cx="960" cy="190" rx="250" ry="84" fill="none" stroke="#8b5cf6" stroke-opacity=".3" stroke-dasharray="4 10"/>

  <!-- 3D Polyhedral Sphere -->
  {polys_light}

  <!-- Orbiting Satellites -->
  <circle r="4.5" fill="#0284c7"><animateMotion dur="9s" repeatCount="indefinite" begin="-0s" path="M750,190 a210,60 0 1,0 420,0 a210,60 0 1,0 -420,0"/></circle>
  <circle r="5.5" fill="#8b5cf6"><animateMotion dur="13s" repeatCount="indefinite" begin="-3s" path="M710,190 a250,84 0 1,0 500,0 a250,84 0 1,0 -500,0"/></circle>
  <circle r="5" fill="#10b981"><animateMotion dur="7s" repeatCount="indefinite" begin="-6s" path="M780,190 a180,40 0 1,0 360,0 a180,40 0 1,0 -360,0"/></circle>

  <!-- Left Accent Bar -->
  <rect x="0" y="0" width="8" height="380" fill="url(#bar-grad)"/>

  <!-- Left Content -->
  <text x="62" y="86" font-family="'Fira Code',Consolas,'Courier New',monospace" font-size="15" font-weight="700" fill="#0284c7" letter-spacing="3">HELLO WORLD, I'M</text>
  <text x="62" y="158" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="68" font-weight="900" fill="url(#tx-dark)">Puneeth Manoj Sai</text>
  <text x="64" y="198" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="25" fill="#475569" font-weight="600">Front-End &amp; Full Stack Engineer  ·  Web3  ·  Security</text>

  <!-- Animated Rotating Typewriter -->
  <g>
    <clipPath id="t0"><rect x="64" y="228" height="34" width="0"><animate attributeName="width" dur="16s" repeatCount="indefinite" keyTimes="0;0.0000;0.0875;0.2350;0.2500;1" values="0;0;462;462;0;0"/></rect></clipPath>
    <text x="64" y="252" font-family="'Fira Code',Consolas,'Courier New',monospace" font-size="19" font-weight="700" fill="#0369a1" clip-path="url(#t0)">React · Next.js · TypeScript · Node.js</text>
    <rect x="64" y="232" width="2.5" height="24" fill="#0284c7"><animate attributeName="x" dur="16s" repeatCount="indefinite" keyTimes="0;0.0000;0.0875;0.2350;0.2500;1" values="64;64;526;526;64;64"/><animate attributeName="opacity" values="1;0;1" dur=".9s" repeatCount="indefinite"/></rect>
  </g>
  <g>
    <clipPath id="t1"><rect x="64" y="228" height="34" width="0"><animate attributeName="width" dur="16s" repeatCount="indefinite" keyTimes="0;0.2500;0.3375;0.4850;0.5000;1" values="0;0;402;402;0;0"/></rect></clipPath>
    <text x="64" y="252" font-family="'Fira Code',Consolas,'Courier New',monospace" font-size="19" font-weight="700" fill="#0369a1" clip-path="url(#t1)">Web3 · Solidity · IPFS · Algorand</text>
    <rect x="64" y="232" width="2.5" height="24" fill="#0284c7"><animate attributeName="x" dur="16s" repeatCount="indefinite" keyTimes="0;0.2500;0.3375;0.4850;0.5000;1" values="64;64;466;466;64;64"/><animate attributeName="opacity" values="1;0;1" dur=".9s" repeatCount="indefinite"/></rect>
  </g>
  <g>
    <clipPath id="t2"><rect x="64" y="228" height="34" width="0"><animate attributeName="width" dur="16s" repeatCount="indefinite" keyTimes="0;0.5000;0.5875;0.7350;0.7500;1" values="0;0;438;438;0;0"/></rect></clipPath>
    <text x="64" y="252" font-family="'Fira Code',Consolas,'Courier New',monospace" font-size="19" font-weight="700" fill="#0369a1" clip-path="url(#t2)">AES-256 · AWS KMS · Secure by design</text>
    <rect x="64" y="232" width="2.5" height="24" fill="#0284c7"><animate attributeName="x" dur="16s" repeatCount="indefinite" keyTimes="0;0.5000;0.5875;0.7350;0.7500;1" values="64;64;502;502;64;64"/><animate attributeName="opacity" values="1;0;1" dur=".9s" repeatCount="indefinite"/></rect>
  </g>
  <g>
    <clipPath id="t3"><rect x="64" y="228" height="34" width="0"><animate attributeName="width" dur="16s" repeatCount="indefinite" keyTimes="0;0.7500;0.8375;0.9850;1.0000;1" values="0;0;486;486;0;0"/></rect></clipPath>
    <text x="64" y="252" font-family="'Fira Code',Consolas,'Courier New',monospace" font-size="19" font-weight="700" fill="#0369a1" clip-path="url(#t3)">Provisional Patent Filed · AWS Certified</text>
    <rect x="64" y="232" width="2.5" height="24" fill="#0284c7"><animate attributeName="x" dur="16s" repeatCount="indefinite" keyTimes="0;0.7500;0.8375;0.9850;1.0000;1" values="64;64;550;550;64;64"/><animate attributeName="opacity" values="1;0;1" dur=".9s" repeatCount="indefinite"/></rect>
  </g>

  <!-- Interactive Light Badges -->
  <g transform="translate(64, 296)" filter="url(#card-shadow)">
    <rect width="138" height="36" rx="18" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
    <circle cx="16" cy="18" r="4.5" fill="#10b981"><animate attributeName="opacity" values="1;.3;1" dur="2s" repeatCount="indefinite"/></circle>
    <text x="30" y="23" font-size="13.5" font-weight="700" fill="#0f172a" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif">Patent Filed</text>
  </g>
  <g transform="translate(214, 296)" filter="url(#card-shadow)">
    <rect width="168" height="36" rx="18" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
    <circle cx="16" cy="18" r="4.5" fill="#0284c7"><animate attributeName="opacity" values="1;.3;1" dur="2s" repeatCount="indefinite"/></circle>
    <text x="30" y="23" font-size="13.5" font-weight="700" fill="#0f172a" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif">AWS Certified x2</text>
  </g>
  <g transform="translate(394, 296)" filter="url(#card-shadow)">
    <rect width="178" height="36" rx="18" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
    <circle cx="16" cy="18" r="4.5" fill="#8b5cf6"><animate attributeName="opacity" values="1;.3;1" dur="2s" repeatCount="indefinite"/></circle>
    <text x="30" y="23" font-size="13.5" font-weight="700" fill="#0f172a" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif">800+ users served</text>
  </g>
  <g transform="translate(584, 296)" filter="url(#card-shadow)">
    <rect width="122" height="36" rx="18" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
    <circle cx="16" cy="18" r="4.5" fill="#f59e0b"><animate attributeName="opacity" values="1;.3;1" dur="2s" repeatCount="indefinite"/></circle>
    <text x="30" y="23" font-size="13.5" font-weight="700" fill="#0f172a" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif">Tech Lead</text>
  </g>
</g>
</svg>'''

def generate_metrics():
    metrics = [
        {"val": "800+", "title": "user interactions", "sub": "IEEE branch website", "color": "#0284c7", "x": 0, "dur": "5.0s"},
        {"val": "300+", "title": "GitHub commits", "sub": "high-velocity builder", "color": "#0d9488", "x": 204, "dur": "5.4s"},
        {"val": "10+", "title": "role dashboards", "sub": "Ojas Raksha dApp", "color": "#16a34a", "x": 408, "dur": "5.8s"},
        {"val": "50%", "title": "faster page load", "sub": "performance & CI/CD", "color": "#d97706", "x": 612, "dur": "6.2s"},
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
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 96" width="1200" height="96" role="img" aria-label="{title}">
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
<text x="52" y="76" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="30" font-weight="900" fill="#0f172a">{title}</text>
<text x="1172" y="58" text-anchor="end" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="15" font-weight="600" fill="#64748b">{sub}</text>
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
    # 6 Categorized stack cards in light mode
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
            "role": "Web Master & Graphic Designer",
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
</defs>
<rect width="1200" height="330" rx="20" fill="url(#certs-bg)" stroke="#cbd5e1" stroke-width="1.5"/>

<!-- Card 1: AWS Cloud Practitioner -->
<g transform="translate(45,30)" filter="url(#cert-sh)">
  <animateTransform attributeName="transform" type="translate" values="45,34;45,26;45,34" dur="5.0s" repeatCount="indefinite"/>
  <rect width="255" height="150" rx="16" fill="#ffffff" stroke="#ea580c" stroke-width="1.5"/>
  <rect width="255" height="4" rx="2" fill="#ea580c"/>
  <g transform="translate(18,30)">
    <path d="M28 0 L54 9 V34 C54 50 42 58 28 64 C14 58 2 50 2 34 V9 Z" fill="#fff7ed" stroke="#ea580c" stroke-width="2"/>
    <path d="M15 32 l9 10 l17 -20" fill="none" stroke="#ea580c" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
  <text x="92" y="44" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="13" fill="#ea580c" font-weight="800">AWS Certified</text>
  <text x="92" y="68" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="16" fill="#0f172a" font-weight="900">Cloud</text>
  <text x="92" y="88" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="16" fill="#0f172a" font-weight="900">Practitioner</text>
  <rect x="20" y="108" width="215" height="1" fill="#e2e8f0"/>
  <text x="20" y="132" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="13" font-weight="600" fill="#64748b">Amazon Web Services</text>
</g>

<!-- Card 2: AWS Solutions Architect -->
<g transform="translate(330,30)" filter="url(#cert-sh)">
  <animateTransform attributeName="transform" type="translate" values="330,34;330,26;330,34" dur="5.6s" repeatCount="indefinite"/>
  <rect width="255" height="150" rx="16" fill="#ffffff" stroke="#d97706" stroke-width="1.5"/>
  <rect width="255" height="4" rx="2" fill="#d97706"/>
  <g transform="translate(18,30)">
    <path d="M28 0 L54 9 V34 C54 50 42 58 28 64 C14 58 2 50 2 34 V9 Z" fill="#fffbeb" stroke="#d97706" stroke-width="2"/>
    <path d="M15 32 l9 10 l17 -20" fill="none" stroke="#d97706" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
  <text x="92" y="44" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="13" fill="#d97706" font-weight="800">AWS Certified</text>
  <text x="92" y="68" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="16" fill="#0f172a" font-weight="900">Solutions Architect</text>
  <text x="92" y="88" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="16" fill="#0f172a" font-weight="900">Associate</text>
  <rect x="20" y="108" width="215" height="1" fill="#e2e8f0"/>
  <text x="20" y="132" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="13" font-weight="600" fill="#64748b">Amazon Web Services</text>
</g>

<!-- Card 3: MongoDB Certified -->
<g transform="translate(615,30)" filter="url(#cert-sh)">
  <animateTransform attributeName="transform" type="translate" values="615,34;615,26;615,34" dur="6.2s" repeatCount="indefinite"/>
  <rect width="255" height="150" rx="16" fill="#ffffff" stroke="#16a34a" stroke-width="1.5"/>
  <rect width="255" height="4" rx="2" fill="#16a34a"/>
  <g transform="translate(18,30)">
    <path d="M28 0 L54 9 V34 C54 50 42 58 28 64 C14 58 2 50 2 34 V9 Z" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
    <path d="M15 32 l9 10 l17 -20" fill="none" stroke="#16a34a" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
  <text x="92" y="44" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="13" fill="#16a34a" font-weight="800">MongoDB Certified</text>
  <text x="92" y="68" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="16" fill="#0f172a" font-weight="900">Associate</text>
  <text x="92" y="88" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="16" fill="#0f172a" font-weight="900">Developer</text>
  <rect x="20" y="108" width="215" height="1" fill="#e2e8f0"/>
  <text x="20" y="132" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="13" font-weight="600" fill="#64748b">MongoDB University</text>
</g>

<!-- Card 4: Salesforce Agentforce -->
<g transform="translate(900,30)" filter="url(#cert-sh)">
  <animateTransform attributeName="transform" type="translate" values="900,34;900,26;900,34" dur="6.8s" repeatCount="indefinite"/>
  <rect width="255" height="150" rx="16" fill="#ffffff" stroke="#0284c7" stroke-width="1.5"/>
  <rect width="255" height="4" rx="2" fill="#0284c7"/>
  <g transform="translate(18,30)">
    <path d="M28 0 L54 9 V34 C54 50 42 58 28 64 C14 58 2 50 2 34 V9 Z" fill="#f0f9ff" stroke="#0284c7" stroke-width="2"/>
    <path d="M15 32 l9 10 l17 -20" fill="none" stroke="#0284c7" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
  <text x="92" y="44" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="13" fill="#0284c7" font-weight="800">Salesforce</text>
  <text x="92" y="68" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="16" fill="#0f172a" font-weight="900">Agentforce</text>
  <text x="92" y="88" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="16" fill="#0f172a" font-weight="900">Specialist</text>
  <rect x="20" y="108" width="215" height="1" fill="#e2e8f0"/>
  <text x="20" y="132" font-family="Inter,'Segoe UI',Helvetica,Arial,sans-serif" font-size="13" font-weight="600" fill="#64748b">Salesforce</text>
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
