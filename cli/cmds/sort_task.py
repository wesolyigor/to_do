from cli.cmds.abs_command import AbsCommand


class SortTasks(AbsCommand):
    name = 'SortTasks'

    def execute(self):
        choose_options = [(1, 'name'), (2, 'status'), (3, 'created')]
        text_options = "\n".join(f"{key}.{opt}" for key, opt in choose_options)

        sort_by = int(input(f'Choose by:\n{text_options}')) - 1

        for task in sorted(self.dashboard, key=lambda x: getattr(x, choose_options[sort_by][1])):
            print(task)
