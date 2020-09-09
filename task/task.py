from datetime import datetime

from task.abc_task import ABSTask


class Task(ABSTask):

    def __init__(self, name, uuid):
        self._id = next(uuid)
        self._name = name
        self._status = True
        self._created = datetime.now()

    @property
    def id(self):
        return self._id

    @property
    def due_time(self):
        return datetime.now() - self.created

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
        self._status = False if self._status else True

    def __repr__(self):
        return f'class Task(id:{self.id} name: {self.name}, status: {self.status}, created: {self.created})'

    __str__ = __repr__
