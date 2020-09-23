from cli.cmds.create_task import CreateTask
from cli.cmds.null_command import NoCommand


class Cli:
    def __init__(self, cmds):
        self.cmds = cmds

    def run(self):
        while True:
            self.get_user_command()

    def get_commands(self):
        commands = self.cmds
        c_name = {cls.name: cls for cls in commands}
        c_index = {str(idx+1): cls for idx, cls in enumerate(commands)}
        return {**c_name, **c_index}

    def parse_command(self, cmd):
        commands = self.get_commands()
        command = commands.setdefault(cmd, NoCommand)
        return command(cmd)

    def get_user_command(self):
        for idx, cmd in enumerate(self.get_commands().values()):
            print(f'{idx + 1}. {cmd.name}')
        user_command = input('Choose command \n')
        command = self.parse_command(user_command)
        command.execute()
