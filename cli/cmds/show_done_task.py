from cli.cmds.abs_command import AbsCommand


class ShowDoneTask(AbsCommand):
    name = 'ShowDoneTask'

    def execute(self):
        for task in self.dashboard:
            if task.status:
                print(task)
