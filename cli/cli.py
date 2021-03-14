import emoji
from colored import fg, bg, attr

from cli.cmds.null_command import NoCommand


class Cli:
    def __init__(self, cmds):
        self.cmds = cmds

    def run(self):
        print(emoji.emojize('%s%s WITAJ W APLIKACJI TODO! :fire: :fire: :fire: %s') % (
            fg('white'), bg('dark_red_1'), attr('reset')))
        while True:
            self.get_user_command()

    def get_commands(self):

        commands = self.cmds
        c_name = {cls.name: cls for cls in
                  commands}
        c_index = {str(idx + 1): cls for idx, cls in enumerate(commands)}
        c_name.update(c_index)  # by python 3.9
        # return {**c_name, **c_index}  # ** for dict union, by python 3.8
        return c_name  # by python 3.9

    def parse_command(self, cmd):

        commands = self.get_commands()
        command = commands.setdefault(cmd,
                                      NoCommand)  # setdefault zwraca wartość z klucza podanego w pierwszym parametrze, a jak nie to defaultowy
        return command(cmd)

    def get_user_command(self):
        for idx, cmd in enumerate({k: v for k, v in self.get_commands().items() if
                                   not k.isdigit()}.values()):
            print(f'%s%s {idx + 1}. {cmd.name} %s' % (fg('white'), bg('black'), attr('bold')))
        user_command = input(
            "%s%s \N{eyes} Choose command \N{eyes} %s \n" % (fg('white'), bg('dark_red_1'), attr('reset')))
        command = self.parse_command(
            user_command)
        command.execute()

