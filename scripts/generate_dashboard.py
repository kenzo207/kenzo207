import os
import random
from datetime import datetime

def generate_hud():
    # Colors
    BG_COLOR = "#0D1117"
    ACCENT_COLOR = "#00FFC8" # Cyber Neon
    TEXT_COLOR = "#E6EDF3"
    DIM_COLOR = "#30363D"
    
    # Fake stats for the proof of concept (will be replaced by API calls)
    commits = 1337
    prs = 42
    stars = 120
    uptime = "99.9%"
    
    # SVG Template
    svg = f"""
    <svg width="800" height="400" xmlns="http://www.w3.org/2000/svg">
        <style>
            .header {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 24px; fill: {ACCENT_COLOR}; font-weight: bold; }}
            .stat-label {{ font-family: monospace; font-size: 14px; fill: {DIM_COLOR}; }}
            .stat-value {{ font-family: monospace; font-size: 20px; fill: {TEXT_COLOR}; font-weight: bold; }}
            .grid-line {{ stroke: {DIM_COLOR}; stroke-width: 0.5; opacity: 0.2; }}
            .box {{ fill: none; stroke: {ACCENT_COLOR}; stroke-width: 1; opacity: 0.5; }}
        </style>
        
        <!-- Background -->
        <rect width="100%" height="100%" fill="{BG_COLOR}" />
        
        <!-- Grid Background -->
        {generate_grid(800, 400)}
        
        <!-- Main Frame -->
        <rect x="10" y="10" width="780" height="380" class="box" rx="10" />
        <path d="M 20 20 L 50 20 L 60 30" stroke="{ACCENT_COLOR}" fill="none" />
        
        <!-- Header -->
        <text x="40" y="60" class="header">SYSTEM // KENZO.HOUNKPE</text>
        <text x="40" y="85" class="stat-label">STATUS: ONLINE | ROLE: SYSTEM & SECURITY ENGINEER</text>
        
        <!-- Stats Module 1 -->
        <rect x="40" y="120" width="200" height="100" fill="#161b22" rx="5" />
        <text x="60" y="150" class="stat-label">TOTAL_COMMITS</text>
        <text x="60" y="180" class="stat-value">{commits}</text>
        
        <!-- Stats Module 2 -->
        <rect x="260" y="120" width="200" height="100" fill="#161b22" rx="5" />
        <text x="280" y="150" class="stat-label">PULL_REQUESTS</text>
        <text x="280" y="180" class="stat-value">{prs}</text>
        
        <!-- Stats Module 3 -->
        <rect x="480" y="120" width="200" height="100" fill="#161b22" rx="5" />
        <text x="500" y="150" class="stat-label">STARS_EARNED</text>
        <text x="500" y="180" class="stat-value">{stars}</text>

        <!-- Dynamic Graph Area (Visual Only) -->
        <rect x="40" y="250" width="720" height="100" fill="#161b22" rx="5" />
        <text x="60" y="280" class="stat-label">ACTIVITY_METRICS_LOG</text>
        
        <!-- Simulated Graph Bars -->
        {generate_bars(40, 250)}
        
        <!-- Footer -->
        <text x="40" y="380" font-family="monospace" font-size="10" fill="{DIM_COLOR}">GENERATED: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} // END_OF_LINE</text>
    </svg>
    """
    
    # Ensure directory exists
    os.makedirs("generated", exist_ok=True)
    
    with open("generated/dashboard.svg", "w") as f:
        f.write(svg)

def generate_grid(width, height):
    lines = ""
    for x in range(0, width, 40):
        lines += f'<line x1="{x}" y1="0" x2="{x}" y2="{height}" class="grid-line" />'
    for y in range(0, height, 40):
        lines += f'<line x1="0" y1="{y}" x2="{width}" y2="{y}" class="grid-line" />'
    return lines

def generate_bars(base_x, base_y):
    bars = ""
    for i in range(30):
        height = random.randint(10, 60)
        x = base_x + 20 + (i * 22)
        y = base_y + 90 - height
        color = "#00FFC8" if i % 2 == 0 else "#238636"
        bars += f'<rect x="{x}" y="{y}" width="15" height="{height}" fill="{color}" opacity="0.7" />'
    return bars

if __name__ == "__main__":
    generate_hud()
