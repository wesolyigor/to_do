from cli.cmds.abs_command import AbsCommand


class DeleteTask(AbsCommand):
    name = "DeleteTask"

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
            decision_input = input('are you sure man? Write "yes": ')
            if decision_input == str('yes'):
                self.dashboard.delete_task(task_id)
                print(f'I deleted task number {task_id}')
            else:
                print('Sorry, i can not delete it.')
