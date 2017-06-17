# @Author: collins
# @Date:   2017-06-09T12:15:11+03:00
# @Last modified by:   collins
# @Last modified time: 2017-06-12T12:14:50+03:00

from .person import Person


class Fellow(Person):

    def __init__(self, name, accomodation=False):

        # No rooms allocated to fellow on instantiation
        self.allocated_office, self.allocated_livingroom = None, None

    @classmethod
    def with_name(ctx, name, accomodation=False):
        return Fellow(name, accomodation)
