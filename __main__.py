from local_uuid import UUID
from task import task
from task.task import Task
from tasks.tasks import Tasks

lc_uuid = UUID()

dashboard = Tasks()
for i in range(10):
    dashboard.add_task(Task(f'kebab {i}', lc_uuid))

for t in dashboard:
    print(t)

print('*' * 20)

dashboard.delete_task(7)
dashboard.delete_task(2)
print(dashboard.get_task(8))
dashboard.add_task(Task('cokolwiek', lc_uuid))
dashboard.update_task(9, Task('costam', lc_uuid))
dashboard.get_task(9).toggle_status()
print(dashboard.get_task(9).due_time)

print('*' * 20)

for t in dashboard:
    print(t)

# TODO prepare 5 commands using command pattern