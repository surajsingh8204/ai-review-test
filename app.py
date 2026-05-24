import sqlite3

def login(username, password):

    query = f"SELECT * FROM users WHERE username='{username}'"

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(query)

    return cursor.fetchone()