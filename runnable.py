# @Author: collins
# @Date:   2017-06-09T11:36:19+03:00
# @Last modified by:   collins
# @Last modified time: 2017-06-09T12:55:29+03:00


from cmd import Cmd

version = 0
str_launch = """"
Type \'help\' for instructions
"""


class Console(Cmd):
    def __init__(self):
        super(Console, self).__init__()

    def do_create_room(self, args):
        """create_room  <room_name> ... """
        pass

    def do_version(self, args):
        """Show the version of the program"""
        print("Version {} ".format(str(version)))

    def do_quit(self, args):
        """Quits the program"""
        raise SystemExit


if __name__ == '__main__':
    console = Console()
    console.prompt = " Amity $ "
    console.cmdloop(str_launch)
