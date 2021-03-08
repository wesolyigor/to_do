import emoji
from colored import fg, bg, attr

from cli.cmds.null_command import NoCommand


class Cli:
    def __init__(self, cmds):
        """
        przypisanie pola klasy, cmds jest parametrem, który przekazujemy w wywołaniu obiektu klasy CLI, nniezbędny
        :param cmds:
        """
        self.cmds = cmds

    def run(self):
        """

        :return: jest while dzięki czemu jest to pętla nieskończona, żeby program się nigdy nie wyłączał. uruchamia me
        todę get_user command
        """
        print(emoji.emojize('%s%s WITAJ W APLIKACJI TODO! :fire: :fire: :fire: %s') % (
            fg('white'), bg('dark_red_1'), attr('reset')))
        while True:
            self.get_user_command()

    def get_commands(self):
        """
        mamy polę przypisane do __init__,
        commands jest tuplą klas,
        operator ** łączy ze sobą 2 słowniki

        :return: operator ** łączy ze sobą 2 słowniki, nazwą jest nazwa lub index klasy, a wartością jest wywołanie
        klasy

        """
        commands = self.cmds
        c_name = {cls.name: cls for cls in
                  commands}  # wartość pola statycznego każdej klasy jest kluczem, a cls.name to jest pole statyczne klasy, a value to deklaracja klasy
        c_index = {str(idx + 1): cls for idx, cls in enumerate(commands)}
        c_name.update(c_index)  # według pythona 3.9
        # return {**c_name, **c_index}  # te gwiazdki służą do łąćzenia słowników w jeden, według pythona 3.8
        return c_name  # według pythona 3.9

    def parse_command(self, cmd):
        """

        :param cmd: klasa
        :return: wynik wywołania klasy, obiekt
        """
        commands = self.get_commands()
        command = commands.setdefault(cmd,
                                      NoCommand)  # setdefault zwraca wartość z klucza podanego w pierwszym parametrze, a jak nie to defaultowy
        return command(cmd)

    def get_user_command(self):
        for idx, cmd in enumerate({k: v for k, v in self.get_commands().items() if
                                   not k.isdigit()}.values()):  # dosłuchać 19:07. RObimy to po to, żeby się ładnie wyświetlało dla użytkownika
            print(f'%s%s {idx + 1}. {cmd.name} %s' % (fg('white'), bg('black'), attr('bold')))
        user_command = input(
            "%s%s \N{eyes} Choose command \N{eyes} %s \n" % (fg('white'), bg('dark_red_1'), attr('reset')))
        # print('%s%s Hello World !!! %s' % (fg('white'), bg('black'), attr('reset')))
        command = self.parse_command(
            user_command)  # wywołujemy medotę parse.. z przekazanym inputem od usera, user command jest obiektem klasy
        command.execute()

