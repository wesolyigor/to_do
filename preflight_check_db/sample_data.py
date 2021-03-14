import os
import sqlite3

from enviroment.env import load_envs

load_envs()


def sample_data():
    db_path = os.environ.get("DB_PATH")
    db_name = os.environ.get('DB_NAME')
    db_root = os.environ.get('ROOT_DIR')
    db_path = os.path.join(db_root, db_path, db_name)

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute("INSERT INTO dashboard (name) VALUES ('main')")
    tasks = [
        ('Kebab', 0, 0),
        ('Burger', 0, 0),
        ('Pizza', 0, 0),
        ('Alkohol', 0, 0)
    ]
    print(tasks)
    c.executemany("INSERT INTO task (name, status, dashboard_id) VALUES (?, ?, ?)", tasks)

    conn.commit()
    conn.close()

    print('Sample data ')


if __name__ == '__main__':
    sample_data()
