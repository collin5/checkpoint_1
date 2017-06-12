# @Author: collins
# @Date:   2017-06-09T12:14:44+03:00
# @Last modified by:   collins
# @Last modified time: 2017-06-12T12:48:49+03:00

from const import *
from office import Office
from living_space import LivingSpace
from modules.security.validation.Validate import *


class Amity(list):

    def __init__(self):
        super(Amity, self).__init__()

        self.rooms = []  # rooms in Amity
        self.people = []  # people in Amity

    def create_room(self, *args):

        # map for room types with respective instances
        instance = {
            "office": Office,
            "living": LivingSpace
        }

        for label in args[1:]:
            # create room with room name according to map value
            self.rooms.append(instance[args[0].lower()].with_name(label))

        # return the type instance for validity check
        return instance[args[0].lower].with_name(None)

    @check_empty_rooms  # check if rooms are empty since we are randomly allocating on adding person
    def add_person(self, name, type, accomodation=False):
        instance = {
            "fellow": Fellow,
            "staff": Staff
        }

    @staticmethod
    @validate_allocation
    def allocated_room(person, room):
        # set person attribute according to room instance
        attr = person.allocated_office is isinstance(room, Office) else person.allocated_livingroom

        if(room.people.append(person)):
            with (attr=room):
                return True

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
