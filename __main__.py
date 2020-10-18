from cli.cli import Cli
from cli.cmds.create_task import CreateTask
from cli.cmds.filter_task import FilterTask
from cli.cmds.remove_task import DeleteTask
from cli.cmds.show_active_task import ShowActiveTask
from cli.cmds.show_done_task import ShowDoneTask
from cli.cmds.show_tasks import ShowTasks
from cli.cmds.sort_task import SortTasks
from cli.cmds.toggle_status import ToggleStatus

commands = (CreateTask, ShowTasks, ToggleStatus, DeleteTask, ShowActiveTask, ShowDoneTask, FilterTask, SortTasks)

app = Cli(commands)
app.run()

# cammelcase - piszemy clasy, dlatego w tej tupli


# get_user_command()

# def get_commands():
#     _commands_old = (AddTask,)
#     return AddTask
#
#
# command = get_commands()
# command.action()

# for i in range(10):
#     dashboard.add_task(Task(f'kebab {i}', lc_uuid))
#
# for t in dashboard:
#     print(t)
#
# print('*' * 20)

# dashboard.delete_task(7)
# dashboard.delete_task(2)
# print(dashboard.get_task(8))
# dashboard.add_task(Task('cokolwiek', lc_uuid))
# # dashboard.update_task(9, Task('costam', lc_uuid))
# # dashboard.get_task(9).toggle_status()
# print(dashboard.get_task(9).due_time)

print('*' * 20)

# for t in dashboard:
#     print(t)

# # TODO prepare 5 _commands_old using command pattern
