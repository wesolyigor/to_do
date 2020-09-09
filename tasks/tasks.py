from tasks.abs_tasks import AbsTasks


class Tasks(AbsTasks):
    def add_task(self, task):
        self._tasks.append(task)

    def get_task(self, idx):
        return list(filter(lambda t: t.id == idx, self._tasks))[0]

    def update_task(self, idx, new_task):
        old_task = list(filter(lambda t: t.id == idx, self._tasks))[0]
        new_task.id = old_task.id
        list_id = self._tasks.index(old_task)
        self._tasks[list_id] = new_task

    def delete_task(self, idx):
        task_to_remove = list(filter(lambda t: t.id == idx, self._tasks))
        self._tasks.remove(task_to_remove[0])

    def __repr__(self):
        return f'class Task()'
