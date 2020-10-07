import os
import sqlite3

db_name = 'todo.db'

db_path = os.path.join(os.path.dirname(__file__), '..', db_name)
# dbpath prowadzi do roota aplikacji
conn = sqlite3.connect(db_path)
# połączenie z bazą - żebyśmy mogli z nią rozmawiać
c = conn.cursor()
# kursor żebyśmy mogli coś z tym zrobić


c.execute('DROP TABLE IF EXISTS tasks')
c.execute('DROP TABLE IF EXISTS dashboard')  # nazwy tabeli

c.execute('''CREATE TABLE dashboard(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    created TEXT default (datetime('now', 'localtime'))
)''')

c.execute('''CREATE TABLE tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    status INTEGER,
    created TEXT default (datetime('now', 'localtime')),
    dashboard_id INTEGER, 
    FOREIGN KEY (dashboard_id) REFERENCES dashboard (id)

)''')

conn.commit()
conn.close()

print('DB initialized')
