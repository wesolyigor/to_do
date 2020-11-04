import os
import sqlite3

from singleton.singleton import Singleton


class DbConnection(Singleton):

    def __init__(self):
        """
        jeżeli nie podam ścieżki do bazy to trafi do defaulotwych
        """

        db_path = os.environ.get("DB_PATH")
        db_name = os.environ.get("DB_NAME")
        db_root = os.environ.get("ROOT_DIR")
        db_path = os.path.join(db_root, db_path, db_name) #ścieżka do bazy z którą się połączymy
        print(db_root, db_path, db_name)

        self._db = sqlite3.connect(db_path) #singleton użyty

    @property
    def db(self) -> object:
        return self._db
    # dzięki getter dostajemy db
