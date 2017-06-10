# @Author: collins
# @Date:   2017-06-09T12:15:22+03:00
# @Last modified by:   collins
# @Last modified time: 2017-06-10T18:44:24+03:00

from room import Room

MAX_PERSONS = 4  # Living space only allows a maximum of 4 people


class LivingSpace(Room):

    def __init__(self, room_name, people=[]):
        super(LivingSpace, self).__init__(room_name, MAX_PERSONS, people)

    @classmethod
    def with_name(ctx, name):
        return ctx(name)
