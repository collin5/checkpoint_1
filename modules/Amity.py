# @Author: collins
# @Date:   2017-06-09T12:14:44+03:00
# @Last modified by:   collins
# @Last modified time: 2017-06-10T18:54:13+03:00

from const import *
from office import Office
from living_space import LivingSpace


class Amity(list):

    def __init__(self):
        super(Amity, self).__init__()

        self.rooms = []  # rooms in Amity
        self.people = []  # people in Amity

    def create_room(self, *args):

        # map for room types with instance
        map = {
            "office": Office,
            "living": LivingSpace
        }

        for label in args[1:]:
            # create room with room name according to map value
            self.rooms.append(map[args[0].lower()].with_name(label))

        return True

    def add_person(self, person_name, type, accomodation=False):
        pass

    def reallocate_person(self, id, room_name):
        pass

    def load_people(self, file_path=False):
        pass

    def print_allocation(self, output_path=False):
        pass

    def print_unallocated(self, output_path=False):
        pass

    def print_room(self, room_name):
        pass

    def sate_state(self, db=False):
        pass

    def load_state(self, db=False):
        pass


if __name__ == '__main__':
    amity = Amity()
    amity.create_room("office", "lagos", "demo", "Catherines")
    for x in amity.rooms:
        print(x.name)
