from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3, os, time, random
import google.generativeai as genai

app = Flask(__name__)
app.secret_key = "skill-decay-secret"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
print("GEMINI KEY FOUND:", bool(os.getenv("GEMINI_API_KEY")))
model = genai.GenerativeModel("gemini-pro")

QUESTIONS = [
    {
        "text": "All A are B. Some B are C. No C are D. Which statement is necessarily true?",
        "answer": "no a are d"
    },
    {
        "text": "All roses are flowers. Some flowers fade quickly. Can some roses fade quickly?",
        "answer": "yes"
    },
    {
        "text": "All engineers are logical. Some logical people are creative. Are some engineers creative?",
        "answer": "cannot be determined"
    }
]

@app.route("/", methods=["GET", "POST"])
def home():
    mode = request.args.get("mode", "restricted")
    question = random.choice(QUESTIONS)
    ai_hint = None

    if request.method == "POST":
        user = request.form["user"]
        session["user"] = user

        answer = request.form["answer"].lower().strip()
        justification = request.form["justification"]
        correct_answer = request.form["correct_answer"]

        start_time = float(request.form["start_time"])
        duration = time.time() - start_time

        correct = 1 if answer == correct_answer else 0
        ai_used = 1 if mode == "assisted" else 0

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("""
        INSERT INTO responses (user, question, answer, justification, duration, correct, ai_used)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (user, question["text"], answer, justification, duration, correct, ai_used))
        conn.commit()
        conn.close()

        return redirect(url_for("profile"))

    if mode == "assisted":
        try:
            prompt = f"Give brief reasoning guidance without final answer: {question['text']}"
            ai_hint = model.generate_content(prompt).text
        except:
            ai_hint = "AI unavailable"

    return render_template("index.html", question=question, mode=mode, ai_hint=ai_hint)

@app.route("/profile")
def profile():
    user = session.get("user")
    if not user:
        return redirect(url_for("home"))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
    SELECT question, answer, correct, ai_used, duration
    FROM responses WHERE user=?
    """, (user,))
    rows = c.fetchall()
    conn.close()

    return render_template("profile.html", user=user, rows=rows)

@app.route("/dashboard")
def dashboard():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT duration, correct, ai_used FROM responses")
    rows = c.fetchall()
    conn.close()

    restricted = [r for r in rows if r[2] == 0]

    if len(restricted) >= 2:
        base = restricted[:2]
        post = restricted[2:] if len(restricted) > 2 else restricted[:2]

        baseline_time = sum(r[0] for r in base) / len(base)
        baseline_acc = sum(r[1] for r in base) / len(base)

        post_time = sum(r[0] for r in post) / len(post)
        post_acc = sum(r[1] for r in post) / len(post)

        sds = round((post_time - baseline_time) + (baseline_acc - post_acc) * 10, 2)
    else:
        sds = 0

    return render_template("dashboard.html", sds=sds)

if __name__ == "__main__":
    app.run()

