from colored import fg, bg, attr

from cli.cmds.abs_command import AbsCommand


class ShowTasks(AbsCommand):
    name = 'ShowTasks'

    def execute(self):
        for task in self.dashboard:
            print(f'%s%s {task} %s' % (fg('black'), bg('blue'), attr('reset')))


