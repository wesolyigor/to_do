import os
import sqlite3

from dbs.dbs_schema_validator import schema_validator
from singleton.singleton import Singleton


class DbConnection(Singleton):

    def __init__(self):
        """
        jeżeli nie podam ścieżki do bazy to trafi do defaulotwych
        """

        db_path = os.environ.get("DB_PATH")
        db_name = os.environ.get("DB_NAME")
        db_root = os.environ.get("ROOT_DIR")
        print(db_root)
        db_path = os.path.join(db_root, db_path, db_name)

        self._db = sqlite3.connect(db_path)
        schema_validator(self._db)

    @property
    def db(self) -> object:
        return self._db
    # dzięki getter dostajemy db
