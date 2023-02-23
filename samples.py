import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")

username1, password1 = "daniel123", hashlib.sha256("danielpassword".encode()).hexdigest()
username2, password2 = "john", hashlib.sha256("johncenainvis".encode()).hexdigest()
username3, password3 = "striker999", hashlib.sha256("Striker999".encode()).hexdigest()
username4, password4 = "iloveyeeting", hashlib.sha256("mekdiKFC123".encode()).hexdigest()
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))

conn.commit()