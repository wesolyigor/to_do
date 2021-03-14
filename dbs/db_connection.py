import os
import sqlite3

from singleton.singleton import Singleton


class DbConnection(Singleton):

    def __init__(self):
        db_path = os.environ.get("DB_PATH")
        db_name = os.environ.get("DB_NAME")
        db_root = os.environ.get("ROOT_DIR")
        db_path = os.path.join(db_root, db_path, db_name)
        self._db = sqlite3.connect(db_path)

    @property
    def db(self) -> object:
        return self._db
