from datetime import datetime

from task.abc_task import ABSTask


class OneTask(ABSTask):

    def __init__(self, name, uuid):
        self._id = uuid
        self._name = name
        self._status = True
        self._created = datetime.now()
        self._deadline = datetime.strptime()
