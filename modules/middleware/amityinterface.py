# @Author: collins
# @Date:   2017-06-09T16:03:31+03:00
# @Last modified by:   collins
# @Last modified time: 2017-06-09T18:54:09+03:00

from modules.amity import Amity
from modules.middleware.const import *


amity = Amity()

class AmityInterface(object):

    def __init__(self, action, *args, **kwargs):
        super(AmityInterface, self).__init__()
        amity = Amity()

    def __call__(func, action, *args, **kwargs):
        # map actions with corresponding functions
        func = {
                Action.CREATE_ROOM : amity.create_room(*args),
            }

        #finally make action call
        func[action]
