# @Author: collins
# @Date:   2017-06-09T11:36:19+03:00
# @Last modified by:   collins
# @Last modified time: 2017-06-09T15:34:09+03:00

"""
Usage:
    create_room <room_name>...

Options:
    --version

"""

from cmd import Cmd
from docopt import docopt, DocoptExit
import sys

version = 0
str_launch = """"
Type \'help\' for instructions
"""


class Cli(Cmd):
    def __init__(self):
        super(Cli, self).__init__()

    def with_docopt(func):
        def execute(*args, **kwargs):
            # set args & function name as system arguments for docopt to be able to pick them
            sys.argv = [func.__name__[3:]] + list(args)[1:]

            try:
                doc_Args = docopt(func.__doc__, version=version)

                # Add func name which is previously stripped off
                # Also remove do_ prefix from function name
                doc_Args.update({func.__name__[3:]: True})

            except DocoptExit as e:
                print("Invalid command")
                return
            except SystemExit as e:
                return  # Keep Amity instance in case of System Exit
            finally:
                return

        return execute

    @with_docopt
    def do_create_room(self, args):
        """Usage: create_room <room_name>..."""
        pass

    @with_docopt
    def do_add_person(self, args):
        """Usage: add_person <person_firstname> <person_lastname> <FELLOW_or_STAFF> [<wants_accommodation>] """
        pass

    @with_docopt
    def do_reallocate_person(self, args):
        pass

    @with_docopt
    def do_load_people(self, args):
        pass

    @with_docopt
    def do_print_allocations(self, args):
        pass

    @with_docopt
    def do_print_unallocated(self, args):
        pass

    @with_docopt
    def do_print_room(self, args):
        pass

    @with_docopt
    def do_save_state(self, args):
        pass

    @with_docopt
    def do_load_state(self, args):
        pass

    def do_version(self, args):
        """Show the version of the program"""
        print("Version {} ".format(str(version)))

    def do_quit(self, args):
        """Quits the program"""
        raise SystemExit


if __name__ == '__main__':
    cli = Cli()
    cli.prompt = " Amity $ "
    cli.cmdloop(str_launch)
