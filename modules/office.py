# @Author: collins
# @Date:   2017-06-09T12:15:41+03:00
# @Last modified by:   collins
# @Last modified time: 2017-06-10T18:22:55+03:00


from .room import Room


class Office(Room):

    def __init__(self, name, people=[]):
        super(Office, self).__init__(name, 6, people)

    @classmethod
    def with_name(ctx, name):
        """Creates office instance with provided name """
        return ctx(name)

    def __str__(self):
        return 'Office'
