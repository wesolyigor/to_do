from task.task import Task
from tasks.tasks import Tasks

dashboard = Tasks()
for i in range(10):
    dashboard.add_task(Task(f'kebab {i}'))

for t in dashboard:
    print(t)
