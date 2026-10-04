import os

def get_font_stack():
    return "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"

def get_mono_font():
    return "'SF Mono', Monaco, 'Cascadia Code', 'Fira Code', Menlo, Consolas, monospace"

def generate_browser_bar():
    font = get_font_stack()
    mono = get_mono_font()
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 46" width="1200" height="46" role="img" aria-label="Browser Navigation Bar">
<defs>
  <linearGradient id="bb-beam" x1="0" x2="1">
    <stop offset="0" stop-color="#0969da" stop-opacity="0"/>
    <stop offset="0.5" stop-color="#0969da"/>
    <stop offset="1" stop-color="#0969da" stop-opacity="0"/>
  </linearGradient>
</defs>
<!-- Pure White Seamless Container -->
<rect width="1200" height="46" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1"/>

<!-- Traffic Lights -->
<circle cx="24" cy="23" r="5" fill="#ff5f56"/>
<circle cx="40" cy="23" r="5" fill="#ffbd2e"/>
<circle cx="56" cy="23" r="5" fill="#27c93f"/>

<!-- URL Capsule -->
<g transform="translate(80, 8)">
  <rect width="1016" height="30" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>
  <!-- Lock Icon -->
  <g transform="translate(14, 8)">
    <rect x="1" y="5" width="10" height="8" rx="1.5" fill="#10b981"/>
    <path d="M3.5 5 V3.5 A2.5 2.5 0 0 1 8.5 3.5 V5" fill="none" stroke="#10b981" stroke-width="1.3"/>
  </g>
  <text x="34" y="20" font-family="{mono}" font-size="12" font-weight="500" fill="#0f172a">https://<tspan fill="#0969da" font-weight="600">puneethmanojsai.vercel.app</tspan></text>
</g>

<!-- Status Pill -->
<g transform="translate(1106, 10)">
  <rect width="78" height="26" rx="13" fill="#f0fdf4" stroke="#bbf7d0" stroke-width="1"/>
  <circle cx="14" cy="13" r="3.5" fill="#16a34a">
    <animate attributeName="opacity" values="1;0.3;1" dur="1.8s" repeatCount="indefinite"/>
  </circle>
  <text x="25" y="17" font-family="{font}" font-size="11" font-weight="700" fill="#15803d" letter-spacing="0.5">ONLINE</text>
</g>

<!-- Animated Hairline Scanner at Bottom -->
<rect x="0" y="44" width="1200" height="2" fill="#f1f5f9"/>
<rect x="-300" y="44" width="300" height="2" fill="url(#bb-beam)">
  <animate attributeName="x" values="-300;1200" dur="4s" repeatCount="indefinite"/>
</rect>
</svg>'''

def generate_banner():
    font = get_font_stack()
    mono = get_mono_font()
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-label="Puneeth Manoj Sai - Developer Profile">
<defs>
  <filter id="soft-card-sh" x="-5%" y="-5%" width="110%" height="115%">
    <feDropShadow dx="0" dy="3" stdDeviation="6" flood-color="#0f172a" flood-opacity="0.05"/>
    <feDropShadow dx="0" dy="1" stdDeviation="2" flood-color="#0f172a" flood-opacity="0.03"/>
  </filter>
  <linearGradient id="name-grad" x1="0" x2="1">
    <stop offset="0%" stop-color="#0f172a"/>
    <stop offset="70%" stop-color="#1e293b"/>
    <stop offset="100%" stop-color="#0969da"/>
  </linearGradient>
</defs>

<!-- Pure Clean White Background Card -->
<rect width="1200" height="370" rx="12" fill="#ffffff" stroke="#e2e8f0" stroke-width="1" filter="url(#soft-card-sh)"/>

<!-- ==================== LEFT COLUMN: DEVELOPER IDENTITY ==================== -->
<!-- Availability Badge -->
<g transform="translate(48, 36)">
  <rect width="246" height="26" rx="13" fill="#f0fdf4" stroke="#bbf7d0" stroke-width="1"/>
  <circle cx="14" cy="13" r="3.5" fill="#16a34a">
    <animate attributeName="opacity" values="1;0.4;1" dur="1.8s" repeatCount="indefinite"/>
  </circle>
  <text x="26" y="17" font-family="{font}" font-size="11.5" font-weight="600" fill="#15803d">Available for Roles &amp; Internships</text>
</g>

<!-- Name -->
<text x="48" y="104" font-family="{font}" font-size="40" font-weight="800" fill="url(#name-grad)" letter-spacing="-0.5">Puneeth Manoj Sai</text>

<!-- Title & Bio -->
<text x="48" y="138" font-family="{font}" font-size="16.5" font-weight="600" fill="#0969da">Front-End &amp; Full Stack Software Engineer</text>
<text x="48" y="164" font-family="{font}" font-size="13.5" font-weight="400" fill="#475569">KL University '27 · Computer Science &amp; Information Technology</text>
<text x="48" y="186" font-family="{font}" font-size="13" font-weight="400" fill="#64748b">Specialized in high-performance web systems, cloud infrastructure &amp; Web3.</text>

<!-- Key Highlight Badges -->
<g transform="translate(48, 212)">
  <!-- Badge 1: Patent -->
  <g transform="translate(0, 0)">
    <rect width="245" height="32" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>
    <circle cx="16" cy="16" r="4" fill="#8250df"/>
    <text x="30" y="20.5" font-family="{font}" font-size="11.5" font-weight="600" fill="#334155">Provisional Patent Filed (2025)</text>
  </g>
  <!-- Badge 2: AWS Cert -->
  <g transform="translate(255, 0)">
    <rect width="255" height="32" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>
    <circle cx="16" cy="16" r="4" fill="#d97706"/>
    <text x="30" y="20.5" font-family="{font}" font-size="11.5" font-weight="600" fill="#334155">AWS Solutions Architect Certified</text>
  </g>
</g>

<!-- Dynamic Terminal Prompt Bar -->
<g transform="translate(48, 260)">
  <rect width="510" height="42" rx="8" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>
  <text x="16" y="26" font-family="{mono}" font-size="13" font-weight="700" fill="#0969da">❯</text>
  
  <g>
    <clipPath id="typ1"><rect x="36" y="6" height="30" width="0"><animate attributeName="width" dur="15s" repeatCount="indefinite" keyTimes="0;0.00;0.12;0.30;0.33;1" values="0;0;460;460;0;0"/></rect></clipPath>
    <text x="36" y="26" font-family="{mono}" font-size="12.5" font-weight="500" fill="#0f172a" clip-path="url(#typ1)">stack: ["React", "Next.js", "TypeScript", "Tailwind", "Node"]</text>
    <rect x="36" y="12" width="2" height="18" fill="#0969da"><animate attributeName="x" dur="15s" repeatCount="indefinite" keyTimes="0;0.00;0.12;0.30;0.33;1" values="36;36;445;445;36;36"/><animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite"/></rect>
  </g>
  <g>
    <clipPath id="typ2"><rect x="36" y="6" height="30" width="0"><animate attributeName="width" dur="15s" repeatCount="indefinite" keyTimes="0;0.33;0.45;0.63;0.66;1" values="0;0;460;460;0;0"/></rect></clipPath>
    <text x="36" y="26" font-family="{mono}" font-size="12.5" font-weight="500" fill="#0f172a" clip-path="url(#typ2)">cloud: ["AWS KMS", "S3", "Lambda", "Docker", "CI/CD"]</text>
    <rect x="36" y="12" width="2" height="18" fill="#0969da"><animate attributeName="x" dur="15s" repeatCount="indefinite" keyTimes="0;0.33;0.45;0.63;0.66;1" values="36;36;390;390;36;36"/><animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite"/></rect>
  </g>
  <g>
    <clipPath id="typ3"><rect x="36" y="6" height="30" width="0"><animate attributeName="width" dur="15s" repeatCount="indefinite" keyTimes="0;0.66;0.78;0.96;1;1" values="0;0;460;460;0;0"/></rect></clipPath>
    <text x="36" y="26" font-family="{mono}" font-size="12.5" font-weight="500" fill="#0f172a" clip-path="url(#typ3)">research: ["Ojas Raksha", "IPFS", "Solidity", "HealthTech"]</text>
    <rect x="36" y="12" width="2" height="18" fill="#0969da"><animate attributeName="x" dur="15s" repeatCount="indefinite" keyTimes="0;0.66;0.78;0.96;1;1" values="36;36;445;445;36;36"/><animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite"/></rect>
  </g>
</g>

<!-- ==================== RIGHT COLUMN: FLOATING REALISTIC CODE CARD ==================== -->
<g transform="translate(615, 32)">
  <!-- Floating Card Outer -->
  <rect width="537" height="306" rx="10" fill="#ffffff" stroke="#e2e8f0" stroke-width="1" filter="url(#soft-card-sh)"/>
  
  <!-- Editor Tab Bar -->
  <path d="M0 34 H537 M0 0 H537 V34 H0 Z" fill="#f8fafc"/>
  <rect x="0" y="33" width="537" height="1" fill="#e2e8f0"/>
  
  <!-- Active Tab -->
  <rect x="12" y="7" width="144" height="27" rx="5" fill="#ffffff" stroke="#e2e8f0" stroke-width="1"/>
  <circle cx="26" cy="20.5" r="3" fill="#3b82f6"/>
  <text x="36" y="24" font-family="{mono}" font-size="11.5" font-weight="600" fill="#0f172a">developer.ts</text>

  <!-- Live Status in Editor -->
  <g transform="translate(450, 9)">
    <rect width="74" height="22" rx="11" fill="#f0fdf4" stroke="#bbf7d0" stroke-width="1"/>
    <circle cx="12" cy="11" r="3" fill="#16a34a"/>
    <text x="22" y="15" font-family="{mono}" font-size="10" font-weight="700" fill="#15803d">ACTIVE</text>
  </g>

  <!-- Line Numbers & Code Content -->
  <g font-family="{mono}" font-size="11.5" xml:space="preserve">
    <!-- Line numbers -->
    <g fill="#94a3b8" text-anchor="end">
      <text x="32" y="60">1</text>
      <text x="32" y="79">2</text>
      <text x="32" y="98">3</text>
      <text x="32" y="117">4</text>
      <text x="32" y="136">5</text>
      <text x="32" y="155">6</text>
      <text x="32" y="174">7</text>
      <text x="32" y="193">8</text>
      <text x="32" y="212">9</text>
      <text x="32" y="231">10</text>
      <text x="32" y="250">11</text>
      <text x="32" y="269">12</text>
      <text x="32" y="288">13</text>
    </g>
    
    <!-- Code Lines -->
    <text x="46" y="60"><tspan fill="#cf222e" font-weight="600">export const</tspan> <tspan fill="#953800" font-weight="600">engineer</tspan>: <tspan fill="#0969da">Developer</tspan> = &#123;</text>
    <text x="46" y="79">  name: <tspan fill="#0a3069">"Puneeth Manoj Sai"</tspan>,</text>
    <text x="46" y="98">  role: <tspan fill="#0a3069">"Full-Stack &amp; Front-End Engineer"</tspan>,</text>
    <text x="46" y="117">  location: <tspan fill="#0a3069">"Hyderabad, India"</tspan>,</text>
    <text x="46" y="136">  university: <tspan fill="#0a3069">"KL University (2023–2027)"</tspan>,</text>
    <text x="46" y="155">  focus: [</text>
    <text x="46" y="174">    <tspan fill="#0a3069">"Scalable Web Apps"</tspan>, <tspan fill="#0a3069">"Cloud &amp; AWS KMS"</tspan>,</text>
    <text x="46" y="193">    <tspan fill="#0a3069">"EVM &amp; Algorand Smart Contracts"</tspan></text>
    <text x="46" y="212">  ],</text>
    <text x="46" y="231">  patent: <tspan fill="#0a3069">"Ojas Raksha · Healthcare Consent"</tspan>,</text>
    <text x="46" y="250">  openToWork: <tspan fill="#cf222e" font-weight="600">true</tspan>,</text>
    <text x="46" y="269">  contact: () =&gt; <tspan fill="#8250df">"2320090028csit@gmail.com"</tspan></text>
    <text x="46" y="288">&#125;;</text>
  </g>
</g>
</svg>'''

def generate_metrics():
    font = get_font_stack()
    mono = get_mono_font()
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 96" width="1200" height="96" role="img" aria-label="Key Impact Metrics">
<defs>
  <filter id="kpi-soft" x="0" y="0" width="100%" height="100%">
    <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.04"/>
  </filter>
</defs>

<!-- Card 1: Users Scaled -->
<g transform="translate(0, 0)">
  <rect width="285" height="96" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1" filter="url(#kpi-soft)"/>
  <rect x="0" y="0" width="4" height="96" rx="2" fill="#0969da"/>
  <text x="24" y="42" font-family="{font}" font-size="30" font-weight="800" fill="#0f172a" letter-spacing="-0.5">800+</text>
  <text x="24" y="64" font-family="{font}" font-size="12.5" font-weight="600" fill="#334155">Concurrent Users Scaled</text>
  <text x="24" y="80" font-family="{font}" font-size="11" font-weight="400" fill="#64748b">IEEE Summit Platform</text>
</g>

<!-- Card 2: Performance Boost -->
<g transform="translate(305, 0)">
  <rect width="285" height="96" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1" filter="url(#kpi-soft)"/>
  <rect x="0" y="0" width="4" height="96" rx="2" fill="#16a34a"/>
  <text x="24" y="42" font-family="{font}" font-size="30" font-weight="800" fill="#0f172a" letter-spacing="-0.5">50%</text>
  <text x="24" y="64" font-family="{font}" font-size="12.5" font-weight="600" fill="#334155">Faster Page Load</text>
  <text x="24" y="80" font-family="{font}" font-size="11" font-weight="400" fill="#64748b">Bundle splitting &amp; CI/CD</text>
</g>

<!-- Card 3: Role Dashboards -->
<g transform="translate(610, 0)">
  <rect width="285" height="96" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1" filter="url(#kpi-soft)"/>
  <rect x="0" y="0" width="4" height="96" rx="2" fill="#8250df"/>
  <text x="24" y="42" font-family="{font}" font-size="30" font-weight="800" fill="#0f172a" letter-spacing="-0.5">10+</text>
  <text x="24" y="64" font-family="{font}" font-size="12.5" font-weight="600" fill="#334155">Granular Role Dashboards</text>
  <text x="24" y="80" font-family="{font}" font-size="11" font-weight="400" fill="#64748b">Ojas Raksha Architecture</text>
</g>

<!-- Card 4: Credentials & Patents -->
<g transform="translate(915, 0)">
  <rect width="285" height="96" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1" filter="url(#kpi-soft)"/>
  <rect x="0" y="0" width="4" height="96" rx="2" fill="#d97706"/>
  <text x="24" y="42" font-family="{font}" font-size="30" font-weight="800" fill="#0f172a" letter-spacing="-0.5">4x</text>
  <text x="24" y="64" font-family="{font}" font-size="12.5" font-weight="600" fill="#334155">Certifications &amp; Patents</text>
  <text x="24" y="80" font-family="{font}" font-size="11" font-weight="400" fill="#64748b">AWS, Mongo, Salesforce &amp; Patent</text>
</g>
</svg>'''

def generate_header(num, title, subtitle, accent_color):
    font = get_font_stack()
    mono = get_mono_font()
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 48" width="1200" height="48" role="img" aria-label="{num} {title}">
<g transform="translate(0, 10)">
  <!-- Number Badge -->
  <rect width="36" height="26" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>
  <text x="18" y="17.5" text-anchor="middle" font-family="{mono}" font-size="11.5" font-weight="700" fill="{accent_color}">{num.replace(' /', '')}</text>
  
  <!-- Title -->
  <text x="48" y="19" font-family="{font}" font-size="18" font-weight="700" fill="#0f172a">{title}</text>
  
  <!-- Subtitle Tag -->
  <text x="320" y="18" font-family="{font}" font-size="12.5" font-weight="400" fill="#64748b">{subtitle}</text>
  
  <!-- Seamless Hairline divider -->
  <line x1="560" y1="14" x2="1200" y2="14" stroke="#e2e8f0" stroke-width="1"/>
</g>
</svg>'''

def generate_ojas_architecture():
    font = get_font_stack()
    mono = get_mono_font()
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 240" width="1200" height="240" role="img" aria-label="Ojas Raksha System Architecture">
<defs>
  <filter id="arch-sh" x="0" y="0" width="100%" height="100%">
    <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0f172a" flood-opacity="0.04"/>
  </filter>
  <marker id="arr" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 1 L 8 5 L 0 9 z" fill="#0969da"/>
  </marker>
</defs>

<!-- Pure White Clean Canvas -->
<rect width="1200" height="240" rx="10" fill="#ffffff" stroke="#e2e8f0" stroke-width="1"/>

<!-- Header bar -->
<rect width="1200" height="36" rx="10" fill="#f8fafc"/>
<rect x="0" y="35" width="1200" height="1" fill="#e2e8f0"/>
<circle cx="20" cy="18" r="4" fill="#8250df"/>
<text x="32" y="22" font-family="{mono}" font-size="11.5" font-weight="600" fill="#0f172a">Ojas Raksha · Decentralized Health Architecture (Patent Filed 2025)</text>

<!-- Flow Connection Lines with Animated Signal Pulses -->
<line x1="260" y1="135" x2="355" y2="135" stroke="#0969da" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#arr)"/>
<circle cx="300" cy="135" r="3" fill="#0969da">
  <animate attributeName="cx" values="265;350" dur="2s" repeatCount="indefinite"/>
  <animate attributeName="opacity" values="0;1;0" dur="2s" repeatCount="indefinite"/>
</circle>

<line x1="560" y1="135" x2="655" y2="135" stroke="#0969da" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#arr)"/>
<circle cx="600" cy="135" r="3" fill="#0969da">
  <animate attributeName="cx" values="565;650" dur="2s" repeatCount="indefinite"/>
  <animate attributeName="opacity" values="0;1;0" dur="2s" repeatCount="indefinite"/>
</circle>

<line x1="860" y1="135" x2="955" y2="135" stroke="#0969da" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#arr)"/>
<circle cx="900" cy="135" r="3" fill="#0969da">
  <animate attributeName="cx" values="865;950" dur="2s" repeatCount="indefinite"/>
  <animate attributeName="opacity" values="0;1;0" dur="2s" repeatCount="indefinite"/>
</circle>

<!-- Block 1: Client Tier -->
<g transform="translate(40, 60)" filter="url(#arch-sh)">
  <rect width="220" height="150" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1"/>
  <rect x="0" y="0" width="220" height="30" rx="8" fill="#f8fafc"/>
  <rect x="0" y="29" width="220" height="1" fill="#e2e8f0"/>
  <text x="14" y="20" font-family="{font}" font-size="12" font-weight="700" fill="#0f172a">1. Client &amp; Role Portals</text>
  
  <text x="14" y="55" font-family="{mono}" font-size="11" font-weight="600" fill="#0969da">React · Next.js · Ethers</text>
  <text x="14" y="78" font-family="{font}" font-size="11" fill="#475569">• 10+ Granular Role Portals</text>
  <text x="14" y="98" font-family="{font}" font-size="11" fill="#475569">• Patient Consent Management</text>
  <text x="14" y="118" font-family="{font}" font-size="11" fill="#475569">• MetaMask Web3 Signer</text>
  <text x="14" y="136" font-family="{font}" font-size="10.5" fill="#16a34a" font-weight="600">✓ Zero-Knowledge Auth</text>
</g>

<!-- Block 2: Cloud & KMS Tier -->
<g transform="translate(340, 60)" filter="url(#arch-sh)">
  <rect width="220" height="150" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1"/>
  <rect x="0" y="0" width="220" height="30" rx="8" fill="#f8fafc"/>
  <rect x="0" y="29" width="220" height="1" fill="#e2e8f0"/>
  <text x="14" y="20" font-family="{font}" font-size="12" font-weight="700" fill="#0f172a">2. Security &amp; AWS KMS</text>
  
  <text x="14" y="55" font-family="{mono}" font-size="11" font-weight="600" fill="#d97706">AWS KMS · AES-256-GCM</text>
  <text x="14" y="78" font-family="{font}" font-size="11" fill="#475569">• Envelope Encryption</text>
  <text x="14" y="98" font-family="{font}" font-size="11" fill="#475569">• Dynamic DEK Generation</text>
  <text x="14" y="118" font-family="{font}" font-size="11" fill="#475569">• Microservice Gateway</text>
  <text x="14" y="136" font-family="{font}" font-size="10.5" fill="#16a34a" font-weight="600">✓ Cryptographic Privacy</text>
</g>

<!-- Block 3: Decentralized Storage -->
<g transform="translate(640, 60)" filter="url(#arch-sh)">
  <rect width="220" height="150" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1"/>
  <rect x="0" y="0" width="220" height="30" rx="8" fill="#f8fafc"/>
  <rect x="0" y="29" width="220" height="1" fill="#e2e8f0"/>
  <text x="14" y="20" font-family="{font}" font-size="12" font-weight="700" fill="#0f172a">3. Decentralized Storage</text>
  
  <text x="14" y="55" font-family="{mono}" font-size="11" font-weight="600" fill="#0284c7">IPFS · Content Addressing</text>
  <text x="14" y="78" font-family="{font}" font-size="11" fill="#475569">• Encrypted Health Records</text>
  <text x="14" y="98" font-family="{font}" font-size="11" fill="#475569">• Deterministic CIDs</text>
  <text x="14" y="118" font-family="{font}" font-size="11" fill="#475569">• Pinning &amp; Replication</text>
  <text x="14" y="136" font-family="{font}" font-size="10.5" fill="#16a34a" font-weight="600">✓ Tamper-Proof Storage</text>
</g>

<!-- Block 4: Smart Contracts -->
<g transform="translate(940, 60)" filter="url(#arch-sh)">
  <rect width="220" height="150" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1"/>
  <rect x="0" y="0" width="220" height="30" rx="8" fill="#f8fafc"/>
  <rect x="0" y="29" width="220" height="1" fill="#e2e8f0"/>
  <text x="14" y="20" font-family="{font}" font-size="12" font-weight="700" fill="#0f172a">4. Blockchain Layer</text>
  
  <text x="14" y="55" font-family="{mono}" font-size="11" font-weight="600" fill="#8250df">Solidity · EVM / Algorand</text>
  <text x="14" y="78" font-family="{font}" font-size="11" fill="#475569">• grantConsent() Logic</text>
  <text x="14" y="98" font-family="{font}" font-size="11" fill="#475569">• revokeConsent() Control</text>
  <text x="14" y="118" font-family="{font}" font-size="11" fill="#475569">• Immutable Audit Trail</text>
  <text x="14" y="136" font-family="{font}" font-size="10.5" fill="#16a34a" font-weight="600">✓ Non-Repudiation</text>
</g>
</svg>'''

def generate_stack():
    font = get_font_stack()
    mono = get_mono_font()
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 230" width="1200" height="230" role="img" aria-label="Categorized Tech Stack">
<!-- Container -->
<rect width="1200" height="230" rx="10" fill="#ffffff" stroke="#e2e8f0" stroke-width="1"/>

<!-- Header -->
<rect width="1200" height="36" rx="10" fill="#f8fafc"/>
<rect x="0" y="35" width="1200" height="1" fill="#e2e8f0"/>
<text x="24" y="22" font-family="{mono}" font-size="12" font-weight="600" fill="#0f172a">CORE TECHNICAL CAPABILITIES &amp; TOOLING</text>

<!-- Category 1: Frontend & UI -->
<g transform="translate(24, 52)">
  <text x="0" y="14" font-family="{font}" font-size="13" font-weight="700" fill="#0969da">Front-End &amp; UI Architecture</text>
  <g transform="translate(0, 24)">
    <g transform="translate(0,0)"><rect width="80" height="28" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/><text x="40" y="18" text-anchor="middle" font-family="{font}" font-size="12" font-weight="600" fill="#334155">React.js</text></g>
    <g transform="translate(88,0)"><rect width="80" height="28" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/><text x="40" y="18" text-anchor="middle" font-family="{font}" font-size="12" font-weight="600" fill="#334155">Next.js</text></g>
    <g transform="translate(176,0)"><rect width="96" height="28" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/><text x="48" y="18" text-anchor="middle" font-family="{font}" font-size="12" font-weight="600" fill="#334155">TypeScript</text></g>
    <g transform="translate(280,0)"><rect width="90" height="28" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/><text x="45" y="18" text-anchor="middle" font-family="{font}" font-size="12" font-weight="600" fill="#334155">JavaScript</text></g>
    <g transform="translate(378,0)"><rect width="102" height="28" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/><text x="51" y="18" text-anchor="middle" font-family="{font}" font-size="12" font-weight="600" fill="#334155">Tailwind CSS</text></g>
    <g transform="translate(488,0)"><rect width="86" height="28" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/><text x="43" y="18" text-anchor="middle" font-family="{font}" font-size="12" font-weight="600" fill="#334155">HTML5/CSS3</text></g>
  </g>
</g>

<!-- Category 2: Backend & Cloud -->
<g transform="translate(620, 52)">
  <text x="0" y="14" font-family="{font}" font-size="13" font-weight="700" fill="#16a34a">Backend &amp; Cloud Infrastructure</text>
  <g transform="translate(0, 24)">
    <g transform="translate(0,0)"><rect width="78" height="28" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/><text x="39" y="18" text-anchor="middle" font-family="{font}" font-size="12" font-weight="600" fill="#334155">Node.js</text></g>
    <g transform="translate(86,0)"><rect width="78" height="28" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/><text x="39" y="18" text-anchor="middle" font-family="{font}" font-size="12" font-weight="600" fill="#334155">Python</text></g>
    <g transform="translate(172,0)"><rect width="90" height="28" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/><text x="45" y="18" text-anchor="middle" font-family="{font}" font-size="12" font-weight="600" fill="#334155">AWS Cloud</text></g>
    <g transform="translate(270,0)"><rect width="86" height="28" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/><text x="43" y="18" text-anchor="middle" font-family="{font}" font-size="12" font-weight="600" fill="#334155">MongoDB</text></g>
    <g transform="translate(364,0)"><rect width="86" height="28" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/><text x="43" y="18" text-anchor="middle" font-family="{font}" font-size="12" font-weight="600" fill="#334155">PostgreSQL</text></g>
    <g transform="translate(458,0)"><rect width="86" height="28" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/><text x="43" y="18" text-anchor="middle" font-family="{font}" font-size="12" font-weight="600" fill="#334155">REST APIs</text></g>
  </g>
</g>

<!-- Category 3: Blockchain & Security -->
<g transform="translate(24, 134)">
  <text x="0" y="14" font-family="{font}" font-size="13" font-weight="700" fill="#8250df">Blockchain &amp; Decentralized Systems</text>
  <g transform="translate(0, 24)">
    <g transform="translate(0,0)"><rect width="78" height="28" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/><text x="39" y="18" text-anchor="middle" font-family="{font}" font-size="12" font-weight="600" fill="#334155">Solidity</text></g>
    <g transform="translate(86,0)"><rect width="66" height="28" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/><text x="33" y="18" text-anchor="middle" font-family="{font}" font-size="12" font-weight="600" fill="#334155">IPFS</text></g>
    <g transform="translate(160,0)"><rect width="78" height="28" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/><text x="39" y="18" text-anchor="middle" font-family="{font}" font-size="12" font-weight="600" fill="#334155">Ethers.js</text></g>
    <g transform="translate(246,0)"><rect width="78" height="28" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/><text x="39" y="18" text-anchor="middle" font-family="{font}" font-size="12" font-weight="600" fill="#334155">Algorand</text></g>
    <g transform="translate(332,0)"><rect width="84" height="28" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/><text x="42" y="18" text-anchor="middle" font-family="{font}" font-size="12" font-weight="600" fill="#334155">MetaMask</text></g>
    <g transform="translate(424,0)"><rect width="86" height="28" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/><text x="43" y="18" text-anchor="middle" font-family="{font}" font-size="12" font-weight="600" fill="#334155">AWS KMS</text></g>
  </g>
</g>

<!-- Category 4: DevOps & Testing -->
<g transform="translate(620, 134)">
  <text x="0" y="14" font-family="{font}" font-size="13" font-weight="700" fill="#d97706">DevOps, Tooling &amp; Testing</text>
  <g transform="translate(0, 24)">
    <g transform="translate(0,0)"><rect width="58" height="28" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/><text x="29" y="18" text-anchor="middle" font-family="{font}" font-size="12" font-weight="600" fill="#334155">Git</text></g>
    <g transform="translate(66,0)"><rect width="72" height="28" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/><text x="36" y="18" text-anchor="middle" font-family="{font}" font-size="12" font-weight="600" fill="#334155">GitHub</text></g>
    <g transform="translate(146,0)"><rect width="118" height="28" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/><text x="59" y="18" text-anchor="middle" font-family="{font}" font-size="12" font-weight="600" fill="#334155">GitHub Actions</text></g>
    <g transform="translate(272,0)"><rect width="70" height="28" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/><text x="35" y="18" text-anchor="middle" font-family="{font}" font-size="12" font-weight="600" fill="#334155">Docker</text></g>
    <g transform="translate(350,0)"><rect width="78" height="28" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/><text x="39" y="18" text-anchor="middle" font-family="{font}" font-size="12" font-weight="600" fill="#334155">Postman</text></g>
    <g transform="translate(436,0)"><rect width="66" height="28" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/><text x="33" y="18" text-anchor="middle" font-family="{font}" font-size="12" font-weight="600" fill="#334155">Vercel</text></g>
  </g>
</g>
</svg>'''

def generate_timeline():
    font = get_font_stack()
    mono = get_mono_font()
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 210" width="1200" height="210" role="img" aria-label="Experience Timeline">
<!-- Container -->
<rect width="1200" height="210" rx="10" fill="#ffffff" stroke="#e2e8f0" stroke-width="1"/>

<!-- Header -->
<rect width="1200" height="34" rx="10" fill="#f8fafc"/>
<rect x="0" y="33" width="1200" height="1" fill="#e2e8f0"/>
<text x="24" y="21" font-family="{mono}" font-size="11.5" font-weight="600" fill="#0f172a">PROFESSIONAL TIMELINE &amp; LEADERSHIP</text>

<!-- Git Commit Track Line -->
<line x1="60" y1="60" x2="1140" y2="60" stroke="#e2e8f0" stroke-width="2"/>

<!-- Node 1: Good Health 24/7 -->
<g transform="translate(60, 50)">
  <circle cx="0" cy="10" r="7" fill="#ffffff" stroke="#0969da" stroke-width="3"/>
  <rect x="-10" y="28" width="245" height="106" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>
  <text x="6" y="48" font-family="{font}" font-size="12" font-weight="700" fill="#0969da">Open Source Fellow</text>
  <text x="6" y="66" font-family="{font}" font-size="12" font-weight="600" fill="#0f172a">Good Health 24/7</text>
  <text x="6" y="84" font-family="{mono}" font-size="10.5" fill="#64748b">Dec 2024 – Present</text>
  <text x="6" y="104" font-family="{font}" font-size="11" fill="#475569">• Full stack healthcare modules</text>
  <text x="6" y="122" font-family="{font}" font-size="11" fill="#475569">• Automated CI/CD &amp; code reviews</text>
</g>

<!-- Node 2: Algorand Club Lead -->
<g transform="translate(340, 50)">
  <circle cx="0" cy="10" r="7" fill="#ffffff" stroke="#8250df" stroke-width="3"/>
  <rect x="-10" y="28" width="245" height="106" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>
  <text x="6" y="48" font-family="{font}" font-size="12" font-weight="700" fill="#8250df">Technical Lead</text>
  <text x="6" y="66" font-family="{font}" font-size="12" font-weight="600" fill="#0f172a">Algorand Developers Club</text>
  <text x="6" y="84" font-family="{mono}" font-size="10.5" fill="#64748b">Aug 2024 – Present</text>
  <text x="6" y="104" font-family="{font}" font-size="11" fill="#475569">• Mentoring 200+ developers</text>
  <text x="6" y="122" font-family="{font}" font-size="11" fill="#475569">• Smart contract hackathons</text>
</g>

<!-- Node 3: IEEE Student Branch -->
<g transform="translate(620, 50)">
  <circle cx="0" cy="10" r="7" fill="#ffffff" stroke="#16a34a" stroke-width="3"/>
  <rect x="-10" y="28" width="245" height="106" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>
  <text x="6" y="48" font-family="{font}" font-size="12" font-weight="700" fill="#16a34a">Web Master &amp; Designer</text>
  <text x="6" y="66" font-family="{font}" font-size="12" font-weight="600" fill="#0f172a">KLEF IEEE Student Branch</text>
  <text x="6" y="84" font-family="{mono}" font-size="10.5" fill="#64748b">Aug 2024 – Present</text>
  <text x="6" y="104" font-family="{font}" font-size="11" fill="#475569">• Scaled to 800+ users</text>
  <text x="6" y="122" font-family="{font}" font-size="11" fill="#475569">• IEEE Belt Performer Award</text>
</g>

<!-- Node 4: KL University -->
<g transform="translate(900, 50)">
  <circle cx="0" cy="10" r="7" fill="#ffffff" stroke="#d97706" stroke-width="3"/>
  <rect x="-10" y="28" width="245" height="106" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>
  <text x="6" y="48" font-family="{font}" font-size="12" font-weight="700" fill="#d97706">B.Tech CS &amp; IT</text>
  <text x="6" y="66" font-family="{font}" font-size="12" font-weight="600" fill="#0f172a">KL University Hyderabad</text>
  <text x="6" y="84" font-family="{mono}" font-size="10.5" fill="#64748b">2023 – 2027</text>
  <text x="6" y="104" font-family="{font}" font-size="11" fill="#475569">• Provisional Patent Filed</text>
  <text x="6" y="122" font-family="{font}" font-size="11" fill="#475569">• Focus: Cloud &amp; Distributed Sys</text>
</g>
</svg>'''

def generate_certs():
    font = get_font_stack()
    mono = get_mono_font()
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 240" width="1200" height="240" role="img" aria-label="Certifications &amp; Credentials">
<!-- Container -->
<rect width="1200" height="240" rx="10" fill="#ffffff" stroke="#e2e8f0" stroke-width="1"/>

<!-- Header -->
<rect width="1200" height="34" rx="10" fill="#f8fafc"/>
<rect x="0" y="33" width="1200" height="1" fill="#e2e8f0"/>
<text x="24" y="21" font-family="{mono}" font-size="11.5" font-weight="600" fill="#0f172a">VERIFIED CREDENTIALS &amp; ACADEMIC RECOGNITION</text>

<!-- 4 Cards -->
<!-- Card 1: AWS Cloud Practitioner -->
<g transform="translate(24, 48)">
  <rect width="270" height="110" rx="8" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>
  <circle cx="28" cy="30" r="14" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
  <text x="28" y="34" text-anchor="middle" font-family="{font}" font-size="12" font-weight="800" fill="#d97706">AWS</text>
  <text x="52" y="28" font-family="{font}" font-size="12.5" font-weight="700" fill="#0f172a">Cloud Practitioner</text>
  <text x="52" y="44" font-family="{font}" font-size="11" font-weight="500" fill="#64748b">Amazon Web Services</text>
  <rect x="14" y="60" width="242" height="1" fill="#e2e8f0"/>
  <text x="14" y="78" font-family="{mono}" font-size="10.5" fill="#0969da">✓ Verified Certificate</text>
  <text x="14" y="96" font-family="{font}" font-size="10.5" fill="#64748b">Issued: Oct 2024</text>
</g>

<!-- Card 2: AWS Solutions Architect -->
<g transform="translate(314, 48)">
  <rect width="270" height="110" rx="8" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>
  <circle cx="28" cy="30" r="14" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
  <text x="28" y="34" text-anchor="middle" font-family="{font}" font-size="12" font-weight="800" fill="#d97706">AWS</text>
  <text x="52" y="28" font-family="{font}" font-size="12.5" font-weight="700" fill="#0f172a">Solutions Architect</text>
  <text x="52" y="44" font-family="{font}" font-size="11" font-weight="500" fill="#64748b">Amazon Web Services</text>
  <rect x="14" y="60" width="242" height="1" fill="#e2e8f0"/>
  <text x="14" y="78" font-family="{mono}" font-size="10.5" fill="#0969da">✓ Associate Level</text>
  <text x="14" y="96" font-family="{font}" font-size="10.5" fill="#64748b">Issued: 2024</text>
</g>

<!-- Card 3: MongoDB Associate Developer -->
<g transform="translate(604, 48)">
  <rect width="270" height="110" rx="8" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>
  <circle cx="28" cy="30" r="14" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
  <text x="28" y="34" text-anchor="middle" font-family="{font}" font-size="11" font-weight="800" fill="#16a34a">MDB</text>
  <text x="52" y="28" font-family="{font}" font-size="12.5" font-weight="700" fill="#0f172a">Associate Developer</text>
  <text x="52" y="44" font-family="{font}" font-size="11" font-weight="500" fill="#64748b">MongoDB University</text>
  <rect x="14" y="60" width="242" height="1" fill="#e2e8f0"/>
  <text x="14" y="78" font-family="{mono}" font-size="10.5" fill="#16a34a">✓ Verified Credential</text>
  <text x="14" y="96" font-family="{font}" font-size="10.5" fill="#64748b">Database Modeling &amp; Queries</text>
</g>

<!-- Card 4: Salesforce Agentforce -->
<g transform="translate(894, 48)">
  <rect width="282" height="110" rx="8" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>
  <circle cx="28" cy="30" r="14" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.5"/>
  <text x="28" y="34" text-anchor="middle" font-family="{font}" font-size="11" font-weight="800" fill="#0284c7">SF</text>
  <text x="52" y="28" font-family="{font}" font-size="12.5" font-weight="700" fill="#0f172a">Agentforce Specialist</text>
  <text x="52" y="44" font-family="{font}" font-size="11" font-weight="500" fill="#64748b">Salesforce</text>
  <rect x="14" y="60" width="254" height="1" fill="#e2e8f0"/>
  <text x="14" y="78" font-family="{mono}" font-size="10.5" fill="#0284c7">✓ AI Agent Architecture</text>
  <text x="14" y="96" font-family="{font}" font-size="10.5" fill="#64748b">Issued: 2025</text>
</g>

<!-- Recognition Pill Strip -->
<g transform="translate(24, 172)">
  <!-- Pill 1: Patent -->
  <g transform="translate(0, 0)">
    <rect width="365" height="32" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>
    <circle cx="16" cy="16" r="4" fill="#8250df"/>
    <text x="30" y="20.5" font-family="{font}" font-size="12" font-weight="600" fill="#0f172a">Provisional Patent Filed · Ojas Raksha (2025)</text>
  </g>
  <!-- Pill 2: Paper -->
  <g transform="translate(380, 0)">
    <rect width="365" height="32" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>
    <circle cx="16" cy="16" r="4" fill="#0969da"/>
    <text x="30" y="20.5" font-family="{font}" font-size="12" font-weight="600" fill="#0f172a">Research Paper Under Review (2026)</text>
  </g>
  <!-- Pill 3: IEEE Award -->
  <g transform="translate(760, 0)">
    <rect width="392" height="32" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>
    <circle cx="16" cy="16" r="4" fill="#16a34a"/>
    <text x="30" y="20.5" font-family="{font}" font-size="12" font-weight="600" fill="#0f172a">IEEE Student Branch Belt Performer Award</text>
  </g>
</g>
</svg>'''

def generate_footer():
    font = get_font_stack()
    mono = get_mono_font()
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 130" width="1200" height="130" role="img" aria-label="Footer &amp; Contact">
<rect width="1200" height="130" rx="10" fill="#ffffff" stroke="#e2e8f0" stroke-width="1"/>

<g transform="translate(48, 32)">
  <text x="0" y="20" font-family="{font}" font-size="22" font-weight="800" fill="#0f172a">Let's build something great together.</text>
  <text x="0" y="44" font-family="{font}" font-size="13" font-weight="400" fill="#64748b">Open to software engineering roles, internships &amp; collaborative research.</text>
</g>

<g transform="translate(780, 42)">
  <g transform="translate(0, 0)">
    <rect width="115" height="34" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>
    <text x="57" y="21.5" text-anchor="middle" font-family="{font}" font-size="12" font-weight="600" fill="#0969da">Portfolio ↗</text>
  </g>
  <g transform="translate(125, 0)">
    <rect width="115" height="34" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>
    <text x="57" y="21.5" text-anchor="middle" font-family="{font}" font-size="12" font-weight="600" fill="#0f172a">LinkedIn ↗</text>
  </g>
  <g transform="translate(250, 0)">
    <rect width="115" height="34" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>
    <text x="57" y="21.5" text-anchor="middle" font-family="{font}" font-size="12" font-weight="600" fill="#ea580c">Email ↗</text>
  </g>
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
        "assets/h-about.svg": generate_header("01 /", "About Me", "Full Stack Engineer &amp; Cloud Architect", "#0969da"),
        "assets/h-work.svg": generate_header("02 /", "Featured Work", "Production platforms &amp; research", "#8250df"),
        "assets/h-exp.svg": generate_header("03 /", "Experience", "Leadership &amp; organizational roles", "#16a34a"),
        "assets/h-stack.svg": generate_header("04 /", "Tech Matrix", "Core engineering capabilities", "#d97706"),
        "assets/h-certs.svg": generate_header("05 /", "Certifications", "Verified credentials &amp; honors", "#0284c7"),
        "assets/h-stats.svg": generate_header("06 /", "Activity &amp; Metrics", "Commit streaks &amp; GitHub activity", "#0969da")
    }

    for path, content in files.items():
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {path} ({len(content)} bytes)")
