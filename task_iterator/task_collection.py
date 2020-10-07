from collections import Iterator


class TaskCollection(Iterator):
    _task_collections = []
    _counter = 0
    _task_id = 0

   def add_task(self, task):
        self

   def __iter__(self):
       self._counter = 0
       return self

   def __next__(self):
       if self._counter < self._task_id:
           