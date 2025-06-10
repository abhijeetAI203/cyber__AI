from flask import Flask, render_template_string, request
import sqlite3
import time
from rich.console import Console
from rich.progress import track
from colorama import init, Fore

init()
console = Console()
app = Flask(__name__)

# Simple SQLite init
def init_db():
    conn = sqlite3.connect("phishing_logs.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT,
        email TEXT,
        timestamp TEXT,
        user_agent TEXT
    )""")
    conn.commit()
    conn.close()

# Simulated GPT-style phishing email generation
def generate_ai_template():
    return """<html>
<body style='font-family:sans-serif;text-align:center;'>
    <h2>Security Alert</h2>
    <p>Dear user,</p>
    <p>We detected unauthorized access to your account.</p>
    <p>Please <a href='/login'>login</a> to verify your identity.</p>
    <hr/>
    <small>This is an automated security alert. Do not reply.</small>
</body>
</html>"""

# AI-generated login page
login_template = """<html>
<head><title>Secure Login</title></head>
<body style='font-family:sans-serif; text-align:center;'>
    <h2>Secure Verification</h2>
    <form method='POST'>
        <input name='email' placeholder='Enter your email' /><br><br>
        <input type='submit' value='Verify' />
    </form>
</body>
</html>"""

@app.route("/")
def index():
    return render_template_string(generate_ai_template())

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        ip = request.remote_addr
        user_agent = request.headers.get("User-Agent")
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        conn = sqlite3.connect("phishing_logs.db")
        c = conn.cursor()
        c.execute("INSERT INTO logs (ip, email, timestamp, user_agent) VALUES (?, ?, ?, ?)",
                  (ip, email, timestamp, user_agent))
        conn.commit()
        conn.close()

        return "<h3>Thank you. Verification complete.</h3>"
    return render_template_string(login_template)

def animated_banner():
    banner = """
█▀▀ █░█ █▀█ █▀█ █▄░█   █▀▄ █░█ █▀▄ █░█
█▄▄ █▄█ █▄█ █▀▄ █░▀█   █▄▀ █▄█ █▄▀ █▄█
   PHISHING SIMULATOR AI | OWNER ABHI
    """
    for line in banner.splitlines():
        print(Fore.MAGENTA + line)
        time.sleep(0.1)

if __name__ == "__main__":
    animated_banner()
    console.print(Fore.YELLOW + "\n[AI] Initializing Ethical Phishing Simulator...")
    for _ in track(range(15), description="⚙️ Preparing environment..."):
        time.sleep(0.05)
    init_db()
    console.print("[green]\nServer running at http://127.0.0.1:5000[/green]")
    app.run(debug=False)
