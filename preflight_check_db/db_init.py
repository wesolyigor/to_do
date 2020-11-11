import inspect
import os
import sqlite3
from sqlite3.dbapi2 import Connection, Cursor

from dbs.db_connection import DbConnection
from enviroment.env import load_envs
from model_adapter.task import Task

load_envs()


def db_init():
    # db_name = 'todo.db'
    # db_path: str = os.path.join(os.path.dirname(__file__), '..', db_name)
    db_path = os.environ.get("DB_PATH")
    db_name = os.environ.get('DB_NAME')
    db_root = os.environ.get('ROOT_DIR')
    db_path = os.path.join(db_root, db_path, db_name)

    print('ten konkretny', db_path)

    # dbpath prowadzi do roota aplikacji
    conn = DbConnection().db
    # połączenie z bazą - żebyśmy mogli z nią rozmawiać
    c = conn.cursor()

    c.execute('DROP TABLE IF EXISTS dashboard')  # nazwy tabeli

    c.execute('''CREATE TABLE dashboard(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                created TEXT default (datetime('now', 'localtime'))
            )''')

    for cls in [Task]:
        table_name = cls.__name__
        c.execute('DROP TABLE IF EXISTS task')

        cols_list = [name for name in inspect.getmembers(cls) if
                     inspect.getattr_static(cls, name[0]) and not name[0].startswith('__') and isinstance(name[1], str)]

        # cols_list = [('FOREIGN_KEY', attr[1]) if attr[0] == 'foreign_key' else attr for attr in cols_list]

        query = f"CREATE TABLE {table_name.lower()} (id INTEGER PRIMARY KEY AUTOINCREMENT,{''.join([f' {name} {val},' for name, val in cols_list])[:-1]})"

        print(query)
        c.execute(query)

        conn.commit()
        conn.close()

        print('DB initialized')

    # kursor żebyśmy mogli coś z tym zrobić

        # c.execute('DROP TABLE IF EXISTS task')  # nazwy tabeli

        # c.execute('''CREATE TABLE task(
        #     id INTEGER PRIMARY KEY AUTOINCREMENT,
        #     name TEXT,
        #     status INTEGER,
        #     created TEXT default (datetime('now', 'localtime')),
        #     dashboard_id INTEGER,
        #     FOREIGN KEY (dashboard_id) REFERENCES dashboard (id)
        #
        # )''')
        #


# w terminalu, gdy chcemy odpalić ten plik wpisujemy: python db_init.py
# dzięki temu kod będzie można też wywołać terminala, a przy imporcie się nie wywoła
if __name__ == '__main__':
    db_init()
