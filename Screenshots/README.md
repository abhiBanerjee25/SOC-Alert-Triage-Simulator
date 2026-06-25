🛡️ SOC Alert Triage Simulator

A lightweight Security Operations Center (SOC) simulation platform built using Flask that processes system logs, detects suspicious activity using rule-based logic, and visualizes security incidents through a web dashboard.

🚀 Features
🔍 Real-time log parsing system
⚠️ Rule-based threat detection engine
🧠 Incident classification (HIGH / MEDIUM / CRITICAL)
📊 Web-based SOC dashboard
📁 Modular architecture (Parser + Rules + UI)
🔄 Easy to extend with new detection rules

⚙️ Tech Stack
Python 3
Flask
HTML5
CSS3
Jinja2 Templates

![Dashboard](Screenshots/dashboard.png)
![Project-Structure](Screenshots/project-structure.png)

SOC-Alert-Simulator/
│
├── app.py
├── analyzer.py
├── rules.py
├── logs.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── screenshots/
    ├── dashboard.png
    └── incidents.png

Detection Logic
Brute Force Attack
Trigger: 3+ failed logins from same target
Severity: HIGH
Port Scan Activity
Trigger: 2+ scan events
Severity: MEDIUM
Malware Detection
Trigger: direct detection event
Severity: CRITICAL

🧠 Future Improvements
🔴 Real-time log streaming (WebSocket support)
📡 SIEM-style dashboard enhancements
🤖 ML-based anomaly detection
📊 Incident severity analytics dashboard
🔐 User authentication system
🧾 MITRE ATT&CK mapping integration
