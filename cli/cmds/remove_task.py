from cli.cmds.abs_command import AbsCommand


class DeleteTask(AbsCommand):
    name = "DeleteTask"

    def execute(self):
        task_id = input('Task id?\n')
        try:
            task_id = int(task_id)
            task = self.dashboard.get_task(task_id)
            print('are you sure man?')
        except ValueError as err:
            print(f'Incorrect value {task_id}')
        except IndexError as err:
            print(f'No task with this id, {task_id}')
        else:
            self.dashboard.delete_task(task_id)

