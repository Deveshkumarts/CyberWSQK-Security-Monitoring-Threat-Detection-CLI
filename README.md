# 🛡️ CyberWSQK

A Terminal-Based Cybersecurity Monitoring and Analysis Toolkit built using Python.

CyberWSQK provides real-time system monitoring, SSH monitoring, port analysis, log analysis, threat intelligence, website security scanning, dashboard reporting, and security event management through a simple command-line interface.

---

# 🚀 Features

## 🖥️ System Monitoring
Monitor system resources in real time:

- CPU Usage
- Memory Usage
- Disk Usage
- Running Processes

Command:

```bash
cyberwsqk monitor
```

---

## 🌐 Port Monitoring

Scan and identify open ports on the host system.

Features:

- Open Port Detection
- Network Service Visibility

Command:

```bash
cyberwsqk ports
```

---

## 🔐 SSH Security Monitoring

Analyze SSH authentication logs.

Features:

- Failed Login Detection
- Successful Login Detection
- Invalid User Detection
- Brute Force Activity Identification

Command:

```bash
cyberwsqk ssh
```

---

## 📊 Log Analysis

Analyze security logs and identify suspicious activities.

Features:

- Failed Login Statistics
- Invalid User Statistics
- Suspicious IP Detection
- Security Event Analysis

Command:

```bash
cyberwsqk logs
```

---

## 🧠 Threat Intelligence

Check logs against known malicious indicators.

Features:

- Suspicious IP Identification
- Threat Correlation
- Intelligence-Based Analysis

Command:

```bash
cyberwsqk intel
```

---

## 🌍 Web Security Scanner

Perform security assessment of websites.

Features:

### Security Header Analysis

Checks for:

- Content-Security-Policy
- Strict-Transport-Security
- X-Frame-Options
- X-Content-Type-Options
- Referrer-Policy
- Permissions-Policy

### SSL/TLS Analysis

Checks:

- TLS Version
- Certificate Expiry Information

### HTTP Method Analysis

Detects:

- GET
- POST
- PUT
- DELETE
- OPTIONS
- HEAD

### Technology Stack Detection

Identifies:

- Web Servers
- Frameworks
- Technologies

### Security Score Generation

Generates a score out of 100 based on security posture.

Command:

```bash
cyberwsqk webscan https://example.com
```

---

## 📋 Dashboard

Displays complete security overview.

Features:

- System Status
- Network Status
- Security Status
- Event Statistics

Command:

```bash
cyberwsqk dashboard
```

---

## 🗄️ Security Event Storage

Stores detected security events using SQLite.

Features:

- Persistent Event Storage
- Event Tracking
- Event History

Command:

```bash
cyberwsqk events
```

---

## 📄 Security Reports

Generate security reports.

Features:

- Text-Based Reports
- Event Summaries
- Audit Records

Command:

```bash
cyberwsqk report
```

---

# 🏗️ Project Structure

```text
CyberWSQK/
│
├── config/
│
├── database/
│   └── cyberwsqk.db
│
├── logs/
│
├── reports/
│
├── modules/
│   ├── monitor.py
│   ├── ports.py
│   ├── ssh_monitor.py
│   ├── log_analyzer.py
│   ├── threat_intel.py
│   ├── dashboard.py
│   ├── web_scanner.py
│   ├── database.py
│   └── report.py
│
├── cyberwsqk.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone <repository-url>
cd CyberWSQK
```

---

## Create Virtual Environment

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

# ▶️ Running CyberWSQK

Run directly:

```bash
python3 cyberwsqk.py --help
```

---

# 🔧 Create Global Command

Create executable:

```bash
sudo nano /usr/local/bin/cyberwsqk
```

Paste:

```bash
#!/bin/bash

source /mnt/d/Projects/CyberWSQK/venv/bin/activate
python3 /mnt/d/Projects/CyberWSQK/cyberwsqk.py "$@"
```

Make executable:

```bash
sudo chmod +x /usr/local/bin/cyberwsqk
```

Verify:

```bash
which cyberwsqk
```

Expected:

```bash
/usr/local/bin/cyberwsqk
```

---

# 💻 Usage Examples

System Monitoring

```bash
cyberwsqk monitor
```

Port Monitoring

```bash
cyberwsqk ports
```

SSH Monitoring

```bash
cyberwsqk ssh
```

Log Analysis

```bash
cyberwsqk logs
```

Threat Intelligence

```bash
cyberwsqk intel
```

Dashboard

```bash
cyberwsqk dashboard
```

Stored Events

```bash
cyberwsqk events
```

Generate Report

```bash
cyberwsqk report
```

Web Security Scan

```bash
cyberwsqk webscan https://google.com
```

---

# 🔒 Technologies Used

- Python 3
- Typer CLI
- SQLite3
- Requests
- BeautifulSoup4
- SSL
- Socket Programming
- Linux System Utilities
- WSL (Windows Subsystem for Linux)

---

# 🎯 Intended Use Cases

- Cybersecurity Learning
- Security Monitoring
- Security Auditing
- Log Analysis
- Threat Detection
- Website Security Assessment
- Academic Projects
- Cybersecurity Demonstrations

---

# 👨‍💻 Author

**Devesh Kumar TS**

B.E CSE (Cyber Security)  
Chennai Institute of Technology (CIT'28)

---

# 📜 License

This project is intended for educational and research purposes only.

Use responsibly and only on systems you own or are authorized to test.