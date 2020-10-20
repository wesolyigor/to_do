from sqlite3 import OperationalError

from dbs.db_init import db_init


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
    except OperationalError:
        db_init()