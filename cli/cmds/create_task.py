from cli.cmds.abs_command import AbsCommand
from dbs.db_connection import DbConnection


class CreateTask(AbsCommand):
    name = 'CreateTask'

    def execute(self):
        """
        przekazuje task name
        :return:
        """
        task_name = input('Provide task name, please \n')

        db = DbConnection().db
        c = db.cursor()
        query = f"INSERT INTO tasks (name, status, dashboard_id) VALUES (?, ?, ?)"
        c.execute(query, (task_name, 0, 0))
        # przygotowuje zapytanie sql
        db.commit()
        # wywołuje zapytanie, ale nie musi to być commit
        c.execute(f"SELECT * FROM tasks ORDER BY id DESC LIMIT 0, 1")
        t = c.fetchone()

        new_task = self.Task(t)
        self.dashboard.add_task(new_task)
