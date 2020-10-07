from abc import ABC, abstractmethod


class ABSTask(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def created(self):
        pass

    @property
    @abstractmethod
    def status(self):
        pass

    @abstractmethod
    def toggle_status(self):
        pass

    @abstractmethod
    def deadline(self):
        pass

