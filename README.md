# 🛡️ Cyber AI – Web Vulnerability Scanner & Phishing Simulation Platform

Cyber AI is an AI-powered cybersecurity toolkit that includes:
- An advanced **Web Vulnerability Scanner** capable of detecting SQLi, LFI, Command Injection, and missing security headers.
- A **Phishing Simulation Platform** to demonstrate social engineering risks.
- A lightweight **AI Pentest Assistant** to interactively help with Capture the Flag (CTF) challenges.

> Developed by **ABHIJEET | abhijeetAI203**

---

## 🚀 Features

### 🔍 Vulnerability Scanner (`scanner_ai_ultimate.py`)
- Full website crawling
- AI-assisted detection of:
  - SQL Injection (SQLi)
  - Local File Inclusion (LFI)
  - Command Injection
  - Missing security headers
  - Exposed admin panels
- AI Pentest Assistant (OpenAI GPT-4)

### 🤖 Quick AI Scanner (`scanner_ai.py`)
- Single-page form scanner
- AI-generated payloads
- Detects common vulnerability signs
- Rich terminal reporting

### 🎣 Phishing Simulator (`phishing_ai.py`)
- AI-generated phishing email template
- AI-generated login page
- SQLite logging of email, IP, timestamp, and user-agent
- Ethical use only — for training or demo purposes

---

## 🧠 Requirements
```
pip install openai requests beautifulsoup4 flask rich colorama
```

## Setup
```
git clone https://github.com/abhijeetAI203/cyber__AI.git
cd cyber_AI
pip install -r requirements.txt
```

## Tools
- Python, Flask
- BeautifulSoup, Requests
- Rich (terminal styling), Colorama
- openai
