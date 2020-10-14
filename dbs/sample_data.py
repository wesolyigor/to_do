import os
import sqlite3

db_name = 'todo.db'

db_path = os.path.join(os.path.dirname(__file__), '..', db_name)
# dbpath prowadzi do roota aplikacji
conn = sqlite3.connect(db_path)
c = conn.cursor()

c.execute("INSERT INTO dashboard (name) VALUES ('main')")

tasks = [
    ('Kebab', 0, 0),
    ('Burger', 0, 0),
    ('Pizza', 0, 0),
    ('Alkohol', 0, 0)
]

c.executemany("INSERT INTO tasks (name, status, dashboard_id) VALUES (?, ?, ?)", tasks)

conn.commit()
conn.close()

print('Sample data ')