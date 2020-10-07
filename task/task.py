from datetime import datetime
from time import strptime

from dbs.db_connection import DbConnection
from task.abc_task import ABSTask


class Task(ABSTask):

    def __init__(self, db_task):
        self._id = db_task[0]
        self._name = db_task[1]
        self._status = db_task[2]
        time_delta = datetime.now() - datetime.strptime(db_task[3], "%Y-%m-%d %H:%M:%S")
        m, s = divmod(time_delta.seconds, 60)
        h, m = divmod(m, 60)
        # TODO do sprawdzenia divmod
        self._created = f"{time_delta.days} days, {h:d}h:{m:02d}m"

    @property
    def id(self):
        return self._id

    @property
    def due_time(self):
        return datetime.now() - self.created

    # TODO block change id
    @id.setter
    def id(self, new_val):
        self._id = new_val

    @property
    def name(self):
        return self._name

    @property
    def created(self):
        return self._created

    @property
    def status(self):
        return self._status

    def toggle_status(self):
        self._status = 0 if self._status else 1

        db = DbConnection().db
        c = db.cursor()
        query = f"UPDATE tasks SET status = {self._status} WHERE id = {self._id}"
        c.execute(query)
        db.commit()

    def deadline(self):
        return self._deadline

    def __repr__(self):
        return f'class Task(id:{self.id} name: {self.name}, status: {"Done" if self.status else "Active"}, created: {self._created}))'

    __str__ = __repr__
