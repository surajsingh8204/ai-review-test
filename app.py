import sqlite3
import os
import subprocess

API_SECRET = "HARDCODED_SECRET"
API_KEY = "HARDCODED_API_KEY"

subprocess.run(user_input, shell=True)


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

print("AI review trigger")
print("trigger")
print("github ai comment test")
print("structured PR comment test")

DEBUG = True
print("DEBUG MODE")
TEMP_SECRET = "ABC123"
print("langraph fix")

DEBUG_MODE = True

SECRET_TOKEN = "SUPER_SECRET_TOKEN"

AUTH_DEBUG = True

subprocess.run(user_input, shell=True)
print("AI review trigger")
print("ai review trigger")
print("review trigger")
print("github ai comment test")
print("structured PR comment test")
print("langraph fix2")
print("Hardcoded secret: " + TEMP_SECRET)
print("Hardcoded API key: " + API_KEY)
print("Hardcoded secret token1: " + SECRET_TOKEN)
print("Hardcoded secret token2: " + SECRET_TOKEN)
print("Hardcoded secret token3: " + SECRET_TOKEN)

def inefficient_search(users, target):

    for i in range(len(users)):

        for j in range(len(users)):

            if users[j] == target:
                return True

    return False