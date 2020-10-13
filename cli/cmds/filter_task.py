from datetime import datetime

from cli.cmds.abs_command import AbsCommand
from task.task import Task


class FilterTask(AbsCommand):
    name = 'FilterTask'

    def execute(self):
        date_from = input('Provide start date dd.mm.')
        date_to = input('Provide end date dd.mm.')

        year = datetime.now().year
# TODO validate and support None value
        date_start = datetime.strptime(f"{date_from}.{year}", "%d.%m.%Y")
        date_end = datetime.strptime(f"{date_to}.{year}", "%d.%m.%Y")

        # time_delta_start = datetime.now() - date_start
        # time_delta_end = datetime.now() - date_end

        for task in self.dashboard:
            if date_start < task.created < date_end:
                print(task)
