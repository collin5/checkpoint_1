# @Author: collins
# @Date:   2017-06-09T12:16:21+03:00
# @Last modified by:   collins
# @Last modified time: 2017-06-09T13:14:24+03:00


from person import Person


class Staff(Person):

    def __init__(self, person_name):
        super(Person, self).__init__(person_name)

        self.allocated_office = None  # Person initially allocated to no office
