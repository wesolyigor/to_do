import os
import sqlite3

from preflight_check_db.abc_builder import AbsBuilder
from preflight_check_db.db_init import db_init
from enviroment.env import save_env


class DbBuilder(AbsBuilder):

    def __init__(self):
        db_root = os.environ.get("ROOT_DIR")
        db_path = os.environ.get("DB_PATH")
        db_name = os.environ.get("DB_NAME")

        try:
            self._db_path = os.path.join(db_root, db_path, db_name)
        except TypeError:
            raise ValueError('App configuration is incorrect')

        self._db = None

    @property
    def db_path(self):
        return self._db_path

    @db_path.setter
    def db_path(self, new_value):
        self._db_path = new_value

    @property
    def db(self):
        return self._db

    def check_db_exist(self):
        return os.path.exists(self.db_path)

    def connect_to_db(self):
        self._db = sqlite3.connect(self.db_path)

    def check_db_is_correct(self):
        query_dashboard = f"SELECT id, name, created FROM dashboard LIMIT 1"
        query_tasks = f"SELECT id, name, status, created, dashboard_id FROM tasks LIMIT 1"

        try:
            self.db.execute(query_dashboard)
            self.db.execute(query_tasks)
            return True

        except sqlite3.OperationalError:
            return False

    # TODO - move to cli

    def get_user_path(self):

        user_answer = input("Hello my friend! Do you want to create new db?[Y/N]\n")

        if user_answer.lower() == "y":
            user_path = input("put the db path inside app please\n")

            root = os.environ.get('ROOT_DIR')
            try:
                abs_path = os.path.join(root, user_path)
            except TypeError:
                raise ValueError("Invalid db path")
            # TODO - zrobić try na OSError
            os.makedirs(abs_path, exist_ok=True)
            os.environ["DB_PATH"] = user_path
            # TODO needs to pass as an argument
            save_env('DB_PATH', user_path) # zapisujemy ją fizycznie na dysku
            self.db_path = os.path.join(abs_path, os.environ.get("DB_NAME"))
        else:
            raise ValueError('App configuration is incorrect')

    @staticmethod
    # TODO needs to pass an arguments
    def create_new_db():
        db_init()
        # TODO ask about sample data
