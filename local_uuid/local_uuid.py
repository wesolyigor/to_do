from collections import Iterator

from local_uuid.singleton import Singleton


# # todo implement using clousure
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

#
# def uuid():
#     counter = 0
#
#     def inner(idx=None):
#         nonlocal counter
#         if idx is not None:
#             counter = idx
#         result = counter
#         counter += 1
#         return result
#
#     return inner
