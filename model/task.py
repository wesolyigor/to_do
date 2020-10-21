import inspect

from model import Model


class Tasks(Model):
    name = ''
    status = ''
    dashboard_id = ''


task = Tasks(name='ala')

print(Tasks.query(name='dupa'))


# Tasks.add(task)
#
# task2 = Tasks(status=0)
# Tasks.update(task2, 22, 1)
#
# task3 = Tasks()
# Tasks.delete(task3, 33)
# for member in inspect.getmembers(task):
#     print(member)
#
# for name in dir(task):
#     if not inspect.getattr_static(task, name) and not name.startswith('__'):
#         name = str(name)
