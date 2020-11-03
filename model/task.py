import inspect

from enviroment.env import load_envs
from model import Model

load_envs()
class Tasks(Model):
    name = ''
    status = ''
    dashboard_id = ''


task = Tasks(name='ala')
task.add(task)
task.update(task, 3, status=1)
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
