from collections import Iterator

from local_uuid.singleton import Singleton

# todo implement using clousure
class UUID(Singleton, Iterator):
    _idx = 0

    def __init__(self, start=None):
        if start is not None:
            self._idx = start

    def __iter__(self):
        return self

    def __next__(self):
        result = self._idx
        self._idx += 1
        return result

