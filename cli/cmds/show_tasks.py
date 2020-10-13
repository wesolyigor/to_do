from cli.cmds.abs_command import AbsCommand


class ShowTasks(AbsCommand):
    name = 'ShowTasks'

    def execute(self):
        for task in self.dashboard:
            print(task)

