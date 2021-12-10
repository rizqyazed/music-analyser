import sqlite3

conn = sqlite3.connect("database.db")

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS user_logins(
        username text,
        password text
        )""")
print("Database Loaded!")


# c.execute("DELETE FROM user_logins")


# c.execute("SELECT * FROM user_logins")
# c.fetchall()
# print(c.fetchall())
conn.commit()
# conn.close()
