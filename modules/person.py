# @Author: collins
# @Date:   2017-06-09T12:15:11+03:00
# @Last modified by:   collins
# @Last modified time: 2017-06-09T13:15:37+03:00


class Person(object):

    def __init__(self, person_name, accomodation):
        super(Person, self).__init()

        self.id = 0  # sets initial person id to 0
        self.first_name, self.last_name = person_name.split(' ')
        self.accomodation = accomodation

    @classmethod
    def create_from_name(ctx, person_name):
        return ctx(person_name, 'N')

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
