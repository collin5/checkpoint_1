# @Author: collins
# @Date:   2017-06-09T12:15:11+03:00
# @Last modified by:   collins
# @Last modified time: 2017-06-12T12:14:50+03:00

from .person import Person


class Staff(Person):

    def __init__(self, name, accomodation=False):
        super(Staff, self).__init__(name, accomodation)
        # No rooms allocated to fellow on instantiation
        self.allocated_office =  None

    @classmethod
    def with_name(ctx, name, accomodation=False):
        return Staff(name, accomodation)

    def __str__(self):
        return 'Staff'
