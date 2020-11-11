import inspect

from enviroment.env import load_envs
from model_adapter import Model

load_envs()


class Task(Model):
    name = 'TEXT'
    status = 'INTEGER'
    created = 'TEXT default (datetime("now", "localtime"))'
    dashboard_id = 'INTEGER'
    foreign_key = '(dashboard_id) REFERENCES dashboard (id)'


task = Task(name='veneo33', status=1, dahsboard_id=0)
Task.add(task)

Task.update(task, 50, 0)
# print(Task.query())

# Task.add(task)
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
