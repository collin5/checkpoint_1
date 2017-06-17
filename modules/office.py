# @Author: collins
# @Date:   2017-06-09T12:15:41+03:00
# @Last modified by:   collins
# @Last modified time: 2017-06-10T18:22:55+03:00


from .room import Room

MAX_PERSONS = 6  # office only allows maximum of 6 people


class Office(Room):

    def __init__(self, name, people=[]):
        super(Office, self).__init__(name, MAX_PERSONS, people)

    @classmethod
    def with_name(ctx, name):
        return ctx(name)
