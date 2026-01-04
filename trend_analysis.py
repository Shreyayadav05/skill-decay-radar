import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()

# Get all restricted attempts in order
c.execute("""
SELECT duration, correct
FROM responses
WHERE ai_used = 0
ORDER BY id
""")

restricted = c.fetchall()

conn.close()

print("Restricted Mode Trend (Baseline Over Time)")
print("----------------------------------------")

for i, row in enumerate(restricted, start=1):
    print(f"Attempt {i}: Time={round(row[0],2)} sec, Correct={row[1]}")
