import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("database.db")
c = conn.cursor()

c.execute("SELECT id, duration, correct, ai_used FROM responses")
rows = c.fetchall()
conn.close()

ids = [r[0] for r in rows]
durations = [r[1] for r in rows]
accuracy = [r[2] for r in rows]
ai_used = ["Assisted" if r[3] == 1 else "Restricted" for r in rows]

plt.figure()
plt.plot(ids, durations)
plt.xlabel("Attempt")
plt.ylabel("Time (seconds)")
plt.title("Thinking Time Over Attempts")
plt.show()

plt.figure()
plt.plot(ids, accuracy)
plt.xlabel("Attempt")
plt.ylabel("Correctness (0/1)")
plt.title("Accuracy Over Attempts")
plt.show()
