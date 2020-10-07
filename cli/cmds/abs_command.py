from abc import ABC, abstractmethod

from tasks.tasks import Tasks
from task.task import Task


class AbsCommand(ABC):
    dashboard = Tasks()
    Task = Task # tu nie ma okrągłych nawiasów, bo chcemy klasę

    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def execute(self):
        pass
