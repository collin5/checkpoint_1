# @Author: collins
# @Date:   2017-06-09T12:16:21+03:00
# @Last modified by:   collins
# @Last modified time: 2017-06-12T12:17:09+03:00


from .person import Person


class Staff(Person):

    def __init__(self, name):
        super(Person, self).__init__(name)

        self.allocated_office = None  # Person initially allocated to no office

    @classmethod
    def with_name(ctx, name):
        return Staff(name)

    def __str__(self):
        return 'staff'
