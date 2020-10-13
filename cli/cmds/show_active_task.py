from cli.cmds.abs_command import AbsCommand


class ShowActiveTask(AbsCommand):
    name = 'ShowActiveTask'

    def execute(self):
        for task in self.dashboard:
            if not task.status:
                print(task)
