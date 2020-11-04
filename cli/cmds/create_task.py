from cli.cmds.abs_command import AbsCommand
from dbs.db_connection import DbConnection


class CreateTask(AbsCommand):
    name = 'Create Task'

    def execute(self):
        """
        przekazuje task name
        :return:
        """
        task_name = input('Provide task name, please \n')

        db = DbConnection().db
        # tworzymy połączenie z bazą danych, uchwyt do bazy
        c = db.cursor()
        # pobieramy kursor
        query = f"INSERT INTO tasks (name, status, dashboard_id) VALUES (?, ?, ?)"
        c.execute(query, (task_name, 0, 0))  # nie zrobiliśmy obsługi do bazy z innym dashboardem niż pierwszy
        # przygotowuje zapytanie sql
        db.commit()
        # wywołuje zapytanie, ale nie musi to być commit
        c.execute(f"SELECT * FROM tasks ORDER BY id DESC LIMIT 0, 1")
        # wykorzystujemy autoinkrementacje id
        t = c.fetchone()
        # pobieramy jeden task

        new_task = self.Task(t)
        # przypisujemy wywołanie klasy task z parametrem T

        self.dashboard.add_task(new_task)
        # przypisujemy nowy task do dashboardu