<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>AI Facial Emotion Recognition System</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;700;800&display=swap" rel="stylesheet"/>
<style>
  :root {
    --bg: #0a0a0f;
    --surface: #111118;
    --card: #16161f;
    --border: #1e1e2e;
    --accent: #7c3aed;
    --accent2: #06b6d4;
    --accent3: #f59e0b;
    --text: #e2e8f0;
    --muted: #64748b;
    --green: #10b981;
    --red: #ef4444;
    --pink: #ec4899;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Syne', sans-serif;
    min-height: 100vh;
    overflow-x: hidden;
  }

  /* Noise texture overlay */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
    pointer-events: none;
    z-index: 0;
    opacity: 0.3;
  }

  .container {
    max-width: 960px;
    margin: 0 auto;
    padding: 0 24px 80px;
    position: relative;
    z-index: 1;
  }

  /* ── HERO ── */
  .hero {
    text-align: center;
    padding: 80px 0 60px;
    position: relative;
  }

  .hero-glow {
    position: absolute;
    top: 0; left: 50%; transform: translateX(-50%);
    width: 600px; height: 300px;
    background: radial-gradient(ellipse, rgba(124,58,237,0.18) 0%, transparent 70%);
    pointer-events: none;
  }

  .badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(124,58,237,0.15);
    border: 1px solid rgba(124,58,237,0.4);
    color: #a78bfa;
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.1em;
    padding: 6px 14px;
    border-radius: 100px;
    margin-bottom: 28px;
    animation: fadeDown 0.6s ease both;
  }

  .badge-dot {
    width: 6px; height: 6px;
    background: #7c3aed;
    border-radius: 50%;
    animation: pulse 1.8s ease-in-out infinite;
  }

  @keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.4; transform: scale(0.7); }
  }

  h1 {
    font-size: clamp(2.2rem, 5vw, 3.6rem);
    font-weight: 800;
    line-height: 1.1;
    letter-spacing: -0.03em;
    margin-bottom: 20px;
    animation: fadeDown 0.6s 0.1s ease both;
  }

  h1 .line1 { display: block; color: var(--text); }
  h1 .line2 {
    display: block;
    background: linear-gradient(135deg, #7c3aed, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }

  .hero-desc {
    color: var(--muted);
    font-size: 1.05rem;
    max-width: 580px;
    margin: 0 auto 36px;
    line-height: 1.7;
    animation: fadeDown 0.6s 0.2s ease both;
  }

  /* stat bar */
  .stats-row {
    display: flex;
    justify-content: center;
    gap: 0;
    margin-top: 40px;
    animation: fadeDown 0.6s 0.3s ease both;
    border: 1px solid var(--border);
    border-radius: 16px;
    overflow: hidden;
    max-width: 560px;
    margin-left: auto;
    margin-right: auto;
  }

  .stat {
    flex: 1;
    padding: 20px 16px;
    background: var(--card);
    text-align: center;
    border-right: 1px solid var(--border);
    transition: background 0.2s;
  }
  .stat:last-child { border-right: none; }
  .stat:hover { background: rgba(124,58,237,0.08); }

  .stat-num {
    display: block;
    font-size: 1.7rem;
    font-weight: 800;
    color: var(--text);
    letter-spacing: -0.03em;
  }

  .stat-num span { color: var(--accent2); }

  .stat-label {
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    color: var(--muted);
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-top: 2px;
    display: block;
  }

  /* ── SECTION TITLE ── */
  .section {
    margin-top: 64px;
    animation: fadeUp 0.5s ease both;
  }

  .section-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 24px;
  }

  .section-icon {
    width: 36px; height: 36px;
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 18px;
    flex-shrink: 0;
  }

  .section-title {
    font-size: 1.3rem;
    font-weight: 700;
    color: var(--text);
    letter-spacing: -0.02em;
  }

  .section-line {
    flex: 1;
    height: 1px;
    background: linear-gradient(to right, var(--border), transparent);
  }

  /* ── EMOTION GRID ── */
  .emotion-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
    gap: 12px;
  }

  .emotion-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 20px 12px;
    text-align: center;
    cursor: default;
    transition: all 0.25s ease;
    position: relative;
    overflow: hidden;
  }

  .emotion-card::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at 50% 0%, var(--ec, rgba(124,58,237,0.12)), transparent 70%);
    opacity: 0;
    transition: opacity 0.25s;
  }

  .emotion-card:hover { transform: translateY(-4px); border-color: rgba(124,58,237,0.5); }
  .emotion-card:hover::before { opacity: 1; }

  .emotion-emoji { font-size: 2.2rem; display: block; margin-bottom: 8px; }

  .emotion-name {
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    color: var(--muted);
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }

  .emotion-bar {
    margin-top: 10px;
    height: 3px;
    background: var(--border);
    border-radius: 2px;
    overflow: hidden;
  }

  .emotion-fill {
    height: 100%;
    border-radius: 2px;
    background: linear-gradient(to right, var(--accent), var(--accent2));
    animation: growBar 1s ease both;
    transform-origin: left;
  }

  @keyframes growBar {
    from { transform: scaleX(0); }
    to { transform: scaleX(1); }
  }

  /* ── TECH TABLE ── */
  .tech-table {
    width: 100%;
    border-collapse: collapse;
    border-radius: 14px;
    overflow: hidden;
    border: 1px solid var(--border);
  }

  .tech-table th {
    background: rgba(124,58,237,0.12);
    padding: 13px 20px;
    text-align: left;
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--accent);
    border-bottom: 1px solid var(--border);
  }

  .tech-table td {
    padding: 13px 20px;
    border-bottom: 1px solid rgba(30,30,46,0.5);
    font-size: 0.92rem;
  }

  .tech-table tr:last-child td { border-bottom: none; }

  .tech-table tr:nth-child(odd) td { background: rgba(22,22,31,0.5); }

  .tech-table tr:hover td { background: rgba(124,58,237,0.05); }

  .tech-badge {
    display: inline-block;
    padding: 3px 9px;
    border-radius: 6px;
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    background: rgba(6,182,212,0.1);
    color: var(--accent2);
    border: 1px solid rgba(6,182,212,0.25);
  }

  /* ── ARCHITECTURE ── */
  .arch-flow {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0;
  }

  .arch-step {
    display: flex;
    align-items: center;
    gap: 16px;
    width: 100%;
    max-width: 500px;
  }

  .arch-box {
    flex: 1;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 16px 20px;
    display: flex;
    align-items: center;
    gap: 14px;
    transition: all 0.2s;
  }

  .arch-box:hover {
    border-color: var(--accent);
    background: rgba(124,58,237,0.06);
    transform: scale(1.02);
  }

  .arch-num {
    width: 28px; height: 28px;
    border-radius: 8px;
    background: rgba(124,58,237,0.2);
    color: #a78bfa;
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
  }

  .arch-info { flex: 1; }

  .arch-name {
    font-size: 0.9rem;
    font-weight: 700;
    color: var(--text);
  }

  .arch-detail {
    font-size: 0.78rem;
    color: var(--muted);
    margin-top: 2px;
    font-family: 'Space Mono', monospace;
  }

  .arch-arrow {
    text-align: center;
    color: var(--accent);
    font-size: 1.1rem;
    padding: 6px 0;
    opacity: 0.6;
  }

  /* ── CODE BLOCK ── */
  .code-block {
    background: #0d0d14;
    border: 1px solid var(--border);
    border-radius: 14px;
    overflow: hidden;
  }

  .code-header {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 12px 16px;
    background: rgba(255,255,255,0.02);
    border-bottom: 1px solid var(--border);
  }

  .code-dot {
    width: 10px; height: 10px;
    border-radius: 50%;
  }

  .code-dot.red { background: #ef4444; }
  .code-dot.yellow { background: #f59e0b; }
  .code-dot.green { background: #10b981; }

  .code-filename {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    color: var(--muted);
    margin-left: 4px;
  }

  pre {
    padding: 20px;
    font-family: 'Space Mono', monospace;
    font-size: 0.8rem;
    line-height: 1.7;
    color: #c4b5fd;
    overflow-x: auto;
    white-space: pre;
  }

  .kw { color: #f472b6; }
  .fn { color: #34d399; }
  .str { color: #fbbf24; }
  .cm { color: #475569; }
  .num { color: #f59e0b; }

  /* ── FEATURE CARDS ── */
  .feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 12px;
  }

  .feature-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 20px;
    transition: all 0.2s;
    position: relative;
    overflow: hidden;
  }

  .feature-card::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(to right, var(--accent), var(--accent2));
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.3s ease;
  }

  .feature-card:hover { border-color: rgba(124,58,237,0.4); transform: translateY(-3px); }
  .feature-card:hover::after { transform: scaleX(1); }

  .feature-icon { font-size: 1.6rem; margin-bottom: 10px; }

  .feature-title {
    font-size: 0.88rem;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 6px;
  }

  .feature-desc {
    font-size: 0.78rem;
    color: var(--muted);
    line-height: 1.5;
  }

  /* ── ACCURACY ── */
  .accuracy-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 28px;
    display: flex;
    align-items: center;
    gap: 28px;
    flex-wrap: wrap;
  }

  .accuracy-circle {
    width: 110px; height: 110px;
    flex-shrink: 0;
    position: relative;
  }

  .accuracy-circle svg { width: 100%; height: 100%; transform: rotate(-90deg); }

  .accuracy-circle .bg { fill: none; stroke: var(--border); stroke-width: 8; }
  .accuracy-circle .fg {
    fill: none;
    stroke: url(#grad);
    stroke-width: 8;
    stroke-linecap: round;
    stroke-dasharray: 283;
    stroke-dashoffset: 141; /* 50% */
    transition: stroke-dashoffset 1.5s ease;
  }

  .accuracy-label {
    position: absolute;
    inset: 0;
    display: flex; align-items: center; justify-content: center;
    flex-direction: column;
  }

  .accuracy-pct {
    font-size: 1.4rem;
    font-weight: 800;
    color: var(--text);
    letter-spacing: -0.03em;
  }

  .accuracy-sub {
    font-family: 'Space Mono', monospace;
    font-size: 9px;
    color: var(--muted);
    text-transform: uppercase;
  }

  .accuracy-info { flex: 1; min-width: 200px; }

  .accuracy-info h3 {
    font-size: 1rem;
    font-weight: 700;
    margin-bottom: 8px;
  }

  .accuracy-info p {
    font-size: 0.85rem;
    color: var(--muted);
    line-height: 1.6;
  }

  .metric-row {
    display: flex;
    gap: 12px;
    margin-top: 14px;
    flex-wrap: wrap;
  }

  .metric-pill {
    display: flex;
    align-items: center;
    gap: 6px;
    background: rgba(16,185,129,0.1);
    border: 1px solid rgba(16,185,129,0.25);
    border-radius: 100px;
    padding: 4px 12px;
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    color: var(--green);
  }

  /* ── PREREQ ── */
  .prereq-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(170px, 1fr));
    gap: 10px;
  }

  .prereq-item {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 14px 16px;
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 0.88rem;
    font-weight: 600;
    transition: all 0.2s;
  }

  .prereq-item:hover {
    border-color: rgba(6,182,212,0.4);
    color: var(--accent2);
  }

  .prereq-dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    background: var(--accent2);
    flex-shrink: 0;
  }

  /* ── FOLDER TREE ── */
  .tree {
    background: #0d0d14;
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 20px 24px;
    font-family: 'Space Mono', monospace;
    font-size: 0.8rem;
    line-height: 1.9;
    color: var(--muted);
  }

  .tree .folder { color: var(--accent3); }
  .tree .file { color: var(--accent2); }
  .tree .root { color: var(--text); font-weight: 700; }

  /* ── LICENSE / FOOTER ── */
  .license-card {
    background: rgba(239,68,68,0.05);
    border: 1px solid rgba(239,68,68,0.2);
    border-radius: 14px;
    padding: 20px 24px;
    display: flex;
    align-items: center;
    gap: 14px;
  }

  .license-icon { font-size: 1.8rem; }

  .license-text h4 {
    font-size: 0.95rem;
    font-weight: 700;
    margin-bottom: 4px;
  }

  .license-text p {
    font-size: 0.82rem;
    color: var(--muted);
  }

  footer {
    margin-top: 64px;
    text-align: center;
    padding-bottom: 32px;
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    color: var(--muted);
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }

  /* ── ANIMATIONS ── */
  @keyframes fadeDown {
    from { opacity: 0; transform: translateY(-16px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  .section { animation: fadeUp 0.5s ease both; }
</style>
</head>
<body>
<div class="container">

  <!-- HERO -->
  <div class="hero">
    <div class="hero-glow"></div>
    <div class="badge"><span class="badge-dot"></span> Deep Learning · Computer Vision</div>
    <h1>
      <span class="line1">AI Facial Emotion</span>
      <span class="line2">Recognition System</span>
    </h1>
    <p class="hero-desc">
      A real-time deep learning system that detects and classifies human facial emotions using CNN trained on the FER-2013 dataset, powered by OpenCV for live webcam inference.
    </p>
    <div class="stats-row">
      <div class="stat">
        <span class="stat-num">7</span>
        <span class="stat-label">Emotions</span>
      </div>
      <div class="stat">
        <span class="stat-num">48<span>px</span></span>
        <span class="stat-label">Input Size</span>
      </div>
      <div class="stat">
        <span class="stat-num">~50<span>%</span></span>
        <span class="stat-label">Val. Accuracy</span>
      </div>
      <div class="stat">
        <span class="stat-num">RT</span>
        <span class="stat-label">Inference</span>
      </div>
    </div>
  </div>

  <!-- FEATURES -->
  <div class="section">
    <div class="section-header">
      <div class="section-icon" style="background:rgba(124,58,237,0.15);">⭐</div>
      <div class="section-title">Key Features</div>
      <div class="section-line"></div>
    </div>
    <div class="feature-grid">
      <div class="feature-card">
        <div class="feature-icon">🎥</div>
        <div class="feature-title">Real-Time Detection</div>
        <div class="feature-desc">Live webcam feed processed frame-by-frame for instant emotion output.</div>
      </div>
      <div class="feature-card">
        <div class="feature-icon">🧠</div>
        <div class="feature-title">CNN Architecture</div>
        <div class="feature-desc">Deep convolutional layers automatically extract facial features hierarchically.</div>
      </div>
      <div class="feature-card">
        <div class="feature-icon">⚡</div>
        <div class="feature-title">Lightweight</div>
        <div class="feature-desc">Optimised model that runs smoothly on standard consumer hardware.</div>
      </div>
      <div class="feature-card">
        <div class="feature-icon">🎯</div>
        <div class="feature-title">7 Emotion Classes</div>
        <div class="feature-desc">Covers the full Ekman set plus Disgust and Neutral for broad coverage.</div>
      </div>
      <div class="feature-card">
        <div class="feature-icon">🖥️</div>
        <div class="feature-title">Normal Webcam</div>
        <div class="feature-desc">No special hardware required — any USB or built-in camera works.</div>
      </div>
      <div class="feature-card">
        <div class="feature-icon">🔧</div>
        <div class="feature-title">Easy Setup</div>
        <div class="feature-desc">Simple pip install and a single command to start inference.</div>
      </div>
    </div>
  </div>

  <!-- EMOTIONS -->
  <div class="section">
    <div class="section-header">
      <div class="section-icon" style="background:rgba(6,182,212,0.15);">😃</div>
      <div class="section-title">Emotions Detected</div>
      <div class="section-line"></div>
    </div>
    <div class="emotion-grid">
      <div class="emotion-card">
        <span class="emotion-emoji">😊</span>
        <span class="emotion-name">Happy</span>
        <div class="emotion-bar"><div class="emotion-fill" style="width:78%"></div></div>
      </div>
      <div class="emotion-card">
        <span class="emotion-emoji">😔</span>
        <span class="emotion-name">Sad</span>
        <div class="emotion-bar"><div class="emotion-fill" style="width:62%"></div></div>
      </div>
      <div class="emotion-card">
        <span class="emotion-emoji">😠</span>
        <span class="emotion-name">Angry</span>
        <div class="emotion-bar"><div class="emotion-fill" style="width:55%"></div></div>
      </div>
      <div class="emotion-card">
        <span class="emotion-emoji">😨</span>
        <span class="emotion-name">Fear</span>
        <div class="emotion-bar"><div class="emotion-fill" style="width:45%"></div></div>
      </div>
      <div class="emotion-card">
        <span class="emotion-emoji">😮</span>
        <span class="emotion-name">Surprise</span>
        <div class="emotion-bar"><div class="emotion-fill" style="width:50%"></div></div>
      </div>
      <div class="emotion-card">
        <span class="emotion-emoji">🤢</span>
        <span class="emotion-name">Disgust</span>
        <div class="emotion-bar"><div class="emotion-fill" style="width:38%"></div></div>
      </div>
      <div class="emotion-card">
        <span class="emotion-emoji">😐</span>
        <span class="emotion-name">Neutral</span>
        <div class="emotion-bar"><div class="emotion-fill" style="width:70%"></div></div>
      </div>
    </div>
  </div>

  <!-- TECH STACK -->
  <div class="section">
    <div class="section-header">
      <div class="section-icon" style="background:rgba(245,158,11,0.15);">🧠</div>
      <div class="section-title">Technologies Used</div>
      <div class="section-line"></div>
    </div>
    <table class="tech-table">
      <thead>
        <tr>
          <th>Technology</th>
          <th>Version / Role</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Python</strong></td>
          <td><span class="tech-badge">3.8+</span></td>
          <td>Core programming language for all scripts</td>
        </tr>
        <tr>
          <td><strong>TensorFlow & Keras</strong></td>
          <td><span class="tech-badge">2.x</span></td>
          <td>Model building, training, and inference</td>
        </tr>
        <tr>
          <td><strong>CNN</strong></td>
          <td><span class="tech-badge">Custom</span></td>
          <td>Automatic feature extraction from face images</td>
        </tr>
        <tr>
          <td><strong>OpenCV</strong></td>
          <td><span class="tech-badge">4.x</span></td>
          <td>Face detection (Haar Cascade) & webcam I/O</td>
        </tr>
        <tr>
          <td><strong>NumPy</strong></td>
          <td><span class="tech-badge">1.21+</span></td>
          <td>Image array processing and normalisation</td>
        </tr>
        <tr>
          <td><strong>FER-2013</strong></td>
          <td><span class="tech-badge">Dataset</span></td>
          <td>35,887 labelled 48×48 grayscale face images</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- ARCHITECTURE -->
  <div class="section">
    <div class="section-header">
      <div class="section-icon" style="background:rgba(236,72,153,0.15);">⚙️</div>
      <div class="section-title">System Architecture</div>
      <div class="section-line"></div>
    </div>
    <div class="arch-flow">
      <div class="arch-step">
        <div class="arch-box">
          <div class="arch-num">01</div>
          <div class="arch-info">
            <div class="arch-name">📷 Webcam Input</div>
            <div class="arch-detail">cv2.VideoCapture · RGB frames</div>
          </div>
        </div>
      </div>
      <div class="arch-arrow">↓</div>
      <div class="arch-step">
        <div class="arch-box">
          <div class="arch-num">02</div>
          <div class="arch-info">
            <div class="arch-name">🔍 Face Detection</div>
            <div class="arch-detail">Haar Cascade · bounding box</div>
          </div>
        </div>
      </div>
      <div class="arch-arrow">↓</div>
      <div class="arch-step">
        <div class="arch-box">
          <div class="arch-num">03</div>
          <div class="arch-info">
            <div class="arch-name">🖼️ Preprocessing</div>
            <div class="arch-detail">Grayscale · 48×48 resize · /255</div>
          </div>
        </div>
      </div>
      <div class="arch-arrow">↓</div>
      <div class="arch-step">
        <div class="arch-box">
          <div class="arch-num">04</div>
          <div class="arch-info">
            <div class="arch-name">🧠 CNN Inference</div>
            <div class="arch-detail">Conv→Pool→Dense → softmax(7)</div>
          </div>
        </div>
      </div>
      <div class="arch-arrow">↓</div>
      <div class="arch-step">
        <div class="arch-box">
          <div class="arch-num">05</div>
          <div class="arch-info">
            <div class="arch-name">🏷️ Label Overlay</div>
            <div class="arch-detail">cv2.putText · real-time display</div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- MODEL ACCURACY -->
  <div class="section">
    <div class="section-header">
      <div class="section-icon" style="background:rgba(16,185,129,0.15);">📊</div>
      <div class="section-title">Model Performance</div>
      <div class="section-line"></div>
    </div>
    <div class="accuracy-card">
      <div class="accuracy-circle">
        <svg viewBox="0 0 100 100">
          <defs>
            <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" style="stop-color:#7c3aed"/>
              <stop offset="100%" style="stop-color:#06b6d4"/>
            </linearGradient>
          </defs>
          <circle class="bg" cx="50" cy="50" r="45"/>
          <circle class="fg" cx="50" cy="50" r="45"/>
        </svg>
        <div class="accuracy-label">
          <span class="accuracy-pct">~50%</span>
          <span class="accuracy-sub">Val. Acc</span>
        </div>
      </div>
      <div class="accuracy-info">
        <h3>Validation Accuracy</h3>
        <p>
          ~50% accuracy on FER-2013 is a solid baseline — the dataset is notoriously challenging due to label noise, small image size (48×48), and high inter-class ambiguity. State-of-the-art models reach ~73%.
        </p>
        <div class="metric-row">
          <div class="metric-pill">✓ Adam Optimizer</div>
          <div class="metric-pill">✓ Categorical Crossentropy</div>
          <div class="metric-pill">✓ Dropout Regularisation</div>
        </div>
      </div>
    </div>
  </div>

  <!-- INSTALLATION -->
  <div class="section">
    <div class="section-header">
      <div class="section-icon" style="background:rgba(245,158,11,0.15);">🛠️</div>
      <div class="section-title">Installation & Setup</div>
      <div class="section-line"></div>
    </div>
    <div class="code-block">
      <div class="code-header">
        <div class="code-dot red"></div>
        <div class="code-dot yellow"></div>
        <div class="code-dot green"></div>
        <span class="code-filename">terminal</span>
      </div>
      <pre><span class="cm"># 1. Clone the repository</span>
<span class="fn">git</span> clone https://github.com/your-username/emotion-recognition.git
<span class="fn">cd</span> emotion-recognition

<span class="cm"># 2. Create virtual environment</span>
<span class="fn">python</span> -m venv venv
<span class="fn">source</span> venv/bin/activate  <span class="cm"># Windows: venv\Scripts\activate</span>

<span class="cm"># 3. Install dependencies</span>
<span class="fn">pip</span> install -r requirements.txt

<span class="cm"># 4. Train the model (optional — pretrained weights included)</span>
<span class="fn">python</span> train_emotion_model.py

<span class="cm"># 5. Run real-time detection</span>
<span class="fn">python</span> detect_emotion.py</pre>
    </div>
  </div>

  <!-- REQUIREMENTS -->
  <div class="section">
    <div class="section-header">
      <div class="section-icon" style="background:rgba(6,182,212,0.15);">📦</div>
      <div class="section-title">Prerequisites</div>
      <div class="section-line"></div>
    </div>
    <div class="prereq-grid">
      <div class="prereq-item"><div class="prereq-dot"></div>Python 3.8+</div>
      <div class="prereq-item"><div class="prereq-dot"></div>TensorFlow 2.x</div>
      <div class="prereq-item"><div class="prereq-dot"></div>OpenCV 4.x</div>
      <div class="prereq-item"><div class="prereq-dot"></div>NumPy 1.21+</div>
      <div class="prereq-item"><div class="prereq-dot"></div>Matplotlib</div>
      <div class="prereq-item"><div class="prereq-dot"></div>FER-2013 Dataset</div>
      <div class="prereq-item"><div class="prereq-dot"></div>Webcam / USB Cam</div>
      <div class="prereq-item"><div class="prereq-dot"></div>8 GB RAM min</div>
    </div>
  </div>

  <!-- PROJECT STRUCTURE -->
  <div class="section">
    <div class="section-header">
      <div class="section-icon" style="background:rgba(245,158,11,0.15);">📂</div>
      <div class="section-title">Project Structure</div>
      <div class="section-line"></div>
    </div>
    <div class="tree">
<span class="root">emotion-recognition/</span>
├── <span class="folder">data/</span>
│   └── <span class="folder">fer2013/</span>
│       ├── <span class="folder">train/</span>  <span style="color:#475569">← angry/ happy/ sad/ ...</span>
│       └── <span class="folder">test/</span>   <span style="color:#475569">← angry/ happy/ sad/ ...</span>
├── <span class="folder">models/</span>
│   └── <span class="file">emotion_model.h5</span>    <span style="color:#475569">← trained weights</span>
├── <span class="file">train_emotion_model.py</span> <span style="color:#475569">← CNN training script</span>
├── <span class="file">detect_emotion.py</span>     <span style="color:#475569">← real-time inference</span>
├── <span class="file">requirements.txt</span>
└── <span class="file">README.md</span>
    </div>
  </div>

  <!-- LICENSE -->
  <div class="section">
    <div class="section-header">
      <div class="section-icon" style="background:rgba(239,68,68,0.15);">📜</div>
      <div class="section-title">License</div>
      <div class="section-line"></div>
    </div>
    <div class="license-card">
      <div class="license-icon">⚖️</div>
      <div class="license-text">
        <h4>Academic & Educational Use Only</h4>
        <p>This project is intended for learning and research purposes. Commercial use, redistribution, or production deployment requires explicit permission from the author.</p>
      </div>
    </div>
  </div>

  <footer>
    AI-Based Real-Time Facial Emotion Recognition · Built with TensorFlow + OpenCV · FER-2013 Dataset
  </footer>
</div>
</body>
</html>
