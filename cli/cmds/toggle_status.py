from cli.cmds.abs_command import AbsCommand


class ToggleStatus(AbsCommand):
    name = "ToggleStatus"

    def execute(self):
        task_id = input('Task id?\n')
        try:
            task_id = int(task_id)
            task = self.dashboard.get_task(task_id)
        except ValueError as err:
            print(f'Incorrect value {task_id}')
        except IndexError as err:
            print(f'No task with this id, {task_id}')
        else:
            task.toggle_status()
