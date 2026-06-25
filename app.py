from flask import Flask, render_template
from analyzer import parse_logs
from rules import detect_incident

app = Flask(__name__)

@app.route("/")
def dashboard():
    logs = parse_logs()
    incidents = detect_incident(logs)

    return render_template("index.html", incidents=incidents)

if __name__ == "__main__":
    app.run(debug=True)

