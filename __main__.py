from enviroment.env import load_envs
from preflight_check_db import Director, DbBuilder

load_envs()
db_builder = Director(DbBuilder())
db_builder.connect_or_create()

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

app = Cli(commands)  # tworzymy obiekt app klasy CLI
app.run()  # wywołujemy metodę run obiektu app


print('*' * 20)

