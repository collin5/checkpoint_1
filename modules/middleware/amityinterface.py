# @Author: collins
# @Date:   2017-06-09T16:03:31+03:00
# @Last modified by:   collins
# @Last modified time: 2017-06-18T09:41:55+03:00

from modules.amity import Amity
from modules.middleware.const import Action


amity = Amity()  # Create amity interface


class AmityInterface(object):

    def __init__(self, action, *args, **kwargs):
        super(AmityInterface, self).__init__()

    def __call__(func, action, *args, **kwargs):
        # map actions with corresponding functions

        msg = None

        if action is Action.CREATE_ROOM:
            msg = amity.create_room(*args)

        if action is Action.ADD_PERSON:
            msg = amity.add_person(*args)

        # std out if message retuned by action
        if isinstance(msg, str):
            print(msg)
