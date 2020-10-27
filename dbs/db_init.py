import os
import sqlite3
from sqlite3.dbapi2 import Connection, Cursor


def db_init():
    # db_name = 'todo.db'
    # db_path: str = os.path.join(os.path.dirname(__file__), '..', db_name)
    db_path = os.environ.get("DB_PATH")
    db_name = os.environ.get('DB_NAME')
    db_root = os.environ.get('ROOT_DIR')
    db_path = os.path.join(db_root, db_path, db_name)

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


# w terminalu, gdy chcemy odpalić ten plik wpisujemy: python db_init.py
# dzięki temu kod będzie można też wywołać terminala, a przy imporcie się nie wywoła
if __name__ == '__main__':
    db_init()
