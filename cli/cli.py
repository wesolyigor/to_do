from cli.cmds.create_task import CreateTask
from cli.cmds.null_command import NoCommand


class Cli:
    def __init__(self, cmds):
        '''
        przypisanie pola klasy, cmds jest parametrem, który przekazujemy w wywołaniu obiektu klasy CLI, nniezbędny
        :param cmds:
        '''
        self.cmds = cmds

    def run(self):
        '''

        :return: jest while dzięki czemu jest to pętla nieskończona, żeby program się nigdy nie wyłączał. uruchamia me
        todę get_user command
        '''
        while True:
            self.get_user_command()

    def get_commands(self):
        '''
        mamy polę przypisane do __init__,
        commands jest tuplą klas,
        operator ** łączy ze sobą 2 słowniki

        :return: operator ** łączy ze sobą 2 słowniki, nazwą jest nazwa lub index klasy, a wartością jest wywołanie
        klasy

        '''
        commands = self.cmds
        c_name = {cls.name: cls for cls in commands}
        c_index = {str(idx + 1): cls for idx, cls in enumerate(commands)}
        return {**c_name, **c_index}

    def parse_command(self, cmd):
        """

        :param cmd: parametr przekazany przez użytkownika
        :return: wynik wywołania klasy, obiekt
        """
        commands = self.get_commands()
        command = commands.setdefault(cmd, NoCommand)
        return command(cmd)

    def get_user_command(self):
        for idx, cmd in enumerate({k: v for k, v in self.get_commands().items() if not k.isdigit()}.values()):
            print(f'{idx + 1}. {cmd.name}')
        user_command = input('Choose command \n')
        command = self.parse_command(user_command)
        command.execute()
