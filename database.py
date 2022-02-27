import sqlite3
from datetime import datetime

con = sqlite3.connect("password_db")
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Records
             (ID INTEGER PRIMARY KEY, PLATFORM, NAME, PASSWORD, LOGGED_ON)''')


def create_entry(platform, name, password):
    con = sqlite3.connect("password_db")
    cur = con.cursor()
    cur.execute(f"INSERT INTO Records VALUES (null,'{platform}','{name}', '{password}' ,'{datetime.now().date()}' )")
    con.commit()
    con.close()


def delete_entry(id_no):
    con = sqlite3.connect("password_db")
    cur = con.cursor()
    cur.execute("DELETE FROM Records WHERE ID = " + str(id_no))
    con.commit()
    con.close()


def show_records():
    con = sqlite3.connect("password_db")
    cur = con.cursor()
    entries = ""
    for row in cur.execute("SELECT * FROM Records"):
        entries += str(row) + "\n"
    con.close()
    return entries


def update(id_no, platform, name, password, date):
    con = sqlite3.connect("password_db")
    cur = con.cursor()
    cur.execute(f"""UPDATE Records SET
         NAME='{name}',PASSWORD='{password}',PLATFORM ='{platform}', LOGGED_ON='{date}' WHERE ID='{id_no}'""")
    con.commit()
    con.close()


def fetch_length():
    con = sqlite3.connect("password_db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Records")
    entries = cur.fetchall()
    records_len = len(entries)
    con.close()
    return records_len


def fetch_one(id_no):
    con = sqlite3.connect("password_db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Records WHERE ID = " + id_no)
    entry = cur.fetchall()
    con.close()
    return entry


def fetch_all():
    con = sqlite3.connect("password_db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Records")
    entries = cur.fetchall()
    con.close()
    return entries
