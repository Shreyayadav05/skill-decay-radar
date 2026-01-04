from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os
import time
import random

app = Flask(__name__)

app.secret_key = "skill-decay-secret"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")

QUESTIONS = [
    {
        "text": "All A are B. Some B are C. No C are D. Which statement is necessarily true?",
        "answer": "no a are d",
        "hint": "If something is C, it cannot be D."
    },
    {
        "text": "All roses are flowers. Some flowers fade quickly. Can some roses fade quickly?",
        "answer": "yes",
        "hint": "Roses are flowers."
    },
    {
        "text": "All engineers are logical. Some logical people are creative. Are some engineers creative?",
        "answer": "cannot be determined",
        "hint": "No guaranteed overlap."
    }
]

@app.route("/", methods=["GET", "POST"])
def home():
    mode = request.args.get("mode", "restricted")
    question = random.choice(QUESTIONS)

    if request.method == "POST":
        user = request.form["user"]
        session["user"] = user
        answer = request.form["answer"]
        justification = request.form["justification"]
        correct_answer = request.form["correct_answer"]
        question_text = request.form["question"]

        start_time = float(request.form["start_time"])
        duration = time.time() - start_time

        correct = 1 if answer.strip().lower() == correct_answer else 0
        ai_used = 1 if mode == "assisted" else 0

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("""
        INSERT INTO responses 
        (user, question, answer, justification, duration, correct, ai_used)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (user, question_text, answer, justification, duration, correct, ai_used))
        conn.commit()
        conn.close()

        return redirect(url_for("profile"))



    return render_template("index.html", question=question, mode=mode)

@app.route("/dashboard")
def dashboard():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT duration, ai_used FROM responses")
    rows = c.fetchall()
    conn.close()
    return render_template("dashboard.html", rows=rows)

@app.route("/profile")
def profile():
    user = session.get("user")

    if not user:
        return "<h3>No user found. Please submit an answer first.</h3><a href='/'>Go Back</a>"

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "SELECT question, answer, correct, ai_used, duration FROM responses WHERE user=?",
        (user,)
    )
    rows = c.fetchall()
    conn.close()

    return render_template("profile.html", user=user, rows=rows)



if __name__ == "__main__":
    app.run(debug=True)
