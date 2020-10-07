import os
import sqlite3

from singleton.singleton import Singleton


class DbConnection(Singleton):

    def __init__(self, db_path=None):
        """
        jeżeli nie podam ścieżki do bazy to trafi do defaulotwych
        # TODO move db path to enviroment variables
        :param db_path:
        """
        if db_path is None:
            db_path = os.path.join(os.path.dirname(__file__), '..', 'todo.db')

        self._db = sqlite3.connect(db_path)

    @property
    def db(self):
        return self._db
