# @Author: collins
# @Date:   2017-06-09T12:14:44+03:00
# @Last modified by:   collins
# @Last modified time: 2017-06-09T14:53:07+03:00

from enum import Enum


class RoomType(Enum):
    OFFICE = 0
    LIVING = 1


class PersonType(Enum):
    STAFF = 0
    FELLOW = 1


class Amity(list):

    def __init__(self):
        super(Dojo, self).__init__()

    def create_room(self, *args):
        return 'Ok'

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
