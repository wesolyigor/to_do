from datetime import datetime

from cli.cmds.abs_command import AbsCommand
from cli.cmds.null_command import NoCommand
from task.task import Task


class FilterTask(AbsCommand):
    name = 'FilterTask'

    def execute(self):

        year = datetime.now().year
        valid_from = False
        valid_to = False

        while not valid_from:
            date_from = input('Provide start date dd.mm.')
            try:
                date_start = datetime.strptime(f"{date_from}.{year}", "%d.%m.%Y")
                print("It's correct! \N{pile of poo} ")
                valid_from = True
            except ValueError:
                print('Incorrect date. \N{pile of poo} Check your value.')

        while not valid_to:
            date_to = input('Provide end date dd.mm.')
            try:
                date_end = datetime.strptime(f"{date_to}.{year}", "%d.%m.%Y")
                valid_to = True
            except ValueError:
                print(f'Incorrect date. \N{pile of poo} Check your value.')

        if date_start > date_end:
            print("Date start must be earlier than date of end!")
            return

        for task in self.dashboard:
            if date_start < task.created < date_end:
                print(task)
