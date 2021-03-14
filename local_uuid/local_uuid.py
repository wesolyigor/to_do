from collections import Iterator

from singleton.singleton import Singleton


class UUID(Singleton, Iterator):
    _idx: int = 0

    def __init__(self, start=None):
        if start is not None:
            self._idx = start

    def __iter__(self):
        return self

    def __next__(self):
        result: int = self._idx
        self._idx += 1
        return result
