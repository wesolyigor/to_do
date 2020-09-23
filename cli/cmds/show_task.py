from cli.cmds.abs_command import AbsCommand


class ShowTask(AbsCommand):
    name = 'ShowTask'

    def execute(self):
        for task in self.dashboard:
            print(task)
