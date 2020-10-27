import os
from sqlite3 import OperationalError

from dbs.db_init import db_init
from enviroment.env import load_envs, save_env


def get_path():
    answer = input("Do you want to create new db?\n")
    if not answer == "yes":
        exit()
    else:
        path = input("Put the db path please\n")
        root = os.environ.get('ROOT_DIR')
        abs_path = os.path.join(root, path)
        print(os.path.exists(os.path.join(root, path)))
        print(os.path.join(root, path))
        if os.path.exists(abs_path):
            os.environ["DB_PATH"] = path
            save_env('DB_PATH', path)


def schema_validator(db):
    """
    Sprawdza czy istnieje baza, jeżeli nie tworzy ją automatycznie
    :rtype: object
    """
    query_dashboard = f"SELECT id, name, created FROM dashboard LIMIT 1"
    query_tasks = f"SELECT id, name, status, created, dashboard_id FROM tasks LIMIT 1"
    try:
        db.execute(query_dashboard)
        db.execute(query_tasks)
    except OperationalError: # żeby query się nie wywalało i szedł operationalerror
        get_path()
        # load_envs()
        db_init()
