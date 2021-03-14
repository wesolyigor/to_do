from abc import ABC, abstractmethod
from collections import Iterable


class AbsTasks(Iterable, ABC):
    _tasks = []

    @abstractmethod
    def add_task(self, task):
        pass

    @abstractmethod
    def update_task(self, idx, new_task):
        pass

    @abstractmethod
    def get_task(self, idx):
        pass

    @abstractmethod
    def delete_task(self, idx):
        pass

    def __iter__(self):
        return (t for t in self._tasks)

    @abstractmethod
    def __repr__(self):
        pass
