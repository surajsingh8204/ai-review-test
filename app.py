import sqlite3
import os


def login(username, password):

    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(query)

    return cursor.fetchone()


def read_file(filename):

    with open(filename, "r") as f:
        return f.read()


def process_users(users):

    results = []

    for i in range(len(users)):

        for j in range(len(users)):

            results.append(users[i] + users[j])

    return results


API_KEY = "SUPER_SECRET_API_KEY_123"