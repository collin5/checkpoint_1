# @Author: collins
# @Date:   2017-06-09T12:14:44+03:00
# @Last modified by:   collins
# @Last modified time: 2017-06-18T09:42:31+03:00

from .middleware.const import *
from .office import Office
from .living_space import LivingSpace
from .validation.decorators import Validate
from .fellow import Fellow
from .staff import Staff
import random

class Amity(list):

    def __init__(self):
        super(Amity, self).__init__()

        self.rooms = []  # rooms in Amity

    def create_room(self, *args):
        args = args[0][0].split()  # get arguments

        # map for room types with respective instances
        instance = {
                "office": Office,
                "living": LivingSpace
                }

        if args[0].lower() not in instance:
            return 'Room of type {} doesn\'t exist'.format(args[0].lower())

        for label in args[1:]:
            # create room with room name according to map value
            self.rooms.append(instance[args[0].lower()].with_name(label))
            print("{} {} successfully created".format(self.rooms[len(self.rooms) - 1], label))

        # return the type instance for validity check
        return instance[args[0]].with_name(None)

    @Validate.check_empty_offices 
    def add_person(self, fname, lname, type, accomodation):
        name = "{} {}".format(fname, lname)
        instance = {
            "fellow": Fellow,
            "staff": Staff
            }

        if type.lower() not in instance:
            return 'Person of type {} doesn\'t exist'.format(type)

        # first create person
        new_person = instance[type].with_name(name)

        # Get empty offices
        empty_offices = list(filter(lambda office: isinstance(office, Office) 
            and (len(office.people) < office.capacity), self.rooms))

        # Get empty living rooms
        empty_living_rooms = list(filter(lambda room: isinstance(
            room, LivingSpace) and (len(room.people) < room.capacity), self.rooms))

        # Allocate random office first
        if(len(empty_offices) < 1):
            return "No empty offices found in Amity"
        else:
            # Randomly allocate office
            print(self.allocate_room(new_person, random.choice(empty_offices)))

        # Then living room with choice
        if(accomodation):
            if isinstance(new_person, Fellow):
                if len(empty_living_rooms) < 1:
                    return "No empty living rooms to allocate this fellow"
                else:
                    # Randomly allocate living space
                    print(self.allocate_room(new_person, random.choice(empty_living_rooms)))
            else:
                return "No living room for non fellows"

    @staticmethod
    @Validate.validate_allocation
    def allocate_room(person, room):
        # set person attribute according to room instance
        attr = person.allocated_office if isinstance(room, Office) else person.allocated_livingroom
        room.people.append(person)
        return "{} {} successfully allocated to {} {}".format(person, person.full_name, room, room.name)

    def reallocate_person(self, id, new_room):
        # get people with specified id
        person_assoc = filter(lambda obj: obj.id is id, self.people)
        person = person_assoc[0]  # person is the first object

        next_room_assoc = filter(lambda obj: obj.name is new_room, self.rooms)

        # Return if room not found
        if(len(next_room_assoc) < 1):
            allocate_room(person, next_room_assoc[0])
        else:
            return "Room not found"

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
