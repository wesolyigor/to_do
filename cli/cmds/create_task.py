from colored import fg, attr, bg

from cli.cmds.abs_command import AbsCommand
from model_adapter.task import Task as TaskModel


class CreateTask(AbsCommand):
    name = 'Create Task'

    def execute(self):
        task_name = input('Provide task name, please \n')

        task = TaskModel(name=task_name, status=1, dashboard_id=1)
        TaskModel.add(task)

        task_from_db = TaskModel.query(name=task_name)

        new_task = self.Task(task_from_db[0])
        self.dashboard.add_task(new_task)






