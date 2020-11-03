from abc import ABC, abstractmethod


class AbsBuilder(ABC):

    @abstractmethod
    def check_db_exist(self):
        pass

    @abstractmethod
    def connect_to_db(self):
        pass

    @abstractmethod
    def check_db_is_correct(self):
        pass

    @property
    @abstractmethod
    def db_path(self):
        pass

    @db_path.setter
    @abstractmethod
    def db_path(self, new_value):
        pass
