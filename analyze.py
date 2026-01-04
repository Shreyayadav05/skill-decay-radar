import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()

# Baseline (restricted)
c.execute("""
SELECT AVG(duration), AVG(correct)
FROM responses
WHERE ai_used = 0
""")
baseline = c.fetchone()

# Assisted
c.execute("""
SELECT AVG(duration), AVG(correct)
FROM responses
WHERE ai_used = 1
""")
assisted = c.fetchone()

conn.close()

print("BASELINE (Restricted mode)")
print("Average Time:", baseline[0])
print("Accuracy:", baseline[1])

print("\nASSISTED mode")
print("Average Time:", assisted[0])
print("Accuracy:", assisted[1])
