import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE users (username TEXT, password TEXT)")
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('admin', 'admin123'))

conn.commit()
conn.close()
print("✅ Database created with default user.")
