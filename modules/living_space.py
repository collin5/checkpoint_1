# @Author: collins
# @Date:   2017-06-09T12:15:22+03:00
# @Last modified by:   collins
# @Last modified time: 2017-06-10T18:44:24+03:00

from .room import Room


class LivingSpace(Room):

    def __init__(self, room_name, people=[]):
        super(LivingSpace, self).__init__(room_name, 4, people)

    @classmethod
    def with_name(ctx, name):
        """Creates living room instance with provided name """
        return ctx(name)

    def __str__(self):
        return 'Living space'
