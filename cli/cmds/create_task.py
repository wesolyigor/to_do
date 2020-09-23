from cli.cmds.abs_command import AbsCommand


class CreateTask(AbsCommand):
    name = 'CreateTask'

    def execute(self):
        task_name = input('Provide task name, please \n')
        new_task = self.Task(task_name, self.lc_uuid)
        self.dashboard.add_task(new_task)
