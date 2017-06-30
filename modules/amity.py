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
from .myformatter import MyFormatter
import random
from functools import reduce
from .spinner import Spinner
import os
import pickle


class Amity(list):

    def __init__(self):
        super(Amity, self).__init__()

        self.rooms = []  # rooms in Amity
        self.people = []

    def create_room(self, *args):
        Spinner.show()
        args = args[0][0].split()  # get arguments

        # map for room types with respective instances
        instance = {
            "office": Office,
            "living": LivingSpace
        }

        if args[0].lower() not in instance:
            return 'Room of type {} doesn\'t exist'.format(args[0].lower())

        for label in args[1:]:
            # check for duplicates
            similar = list(filter(lambda room: room.name.lower()
                                  == label.lower(), self.rooms))
            if len(similar) > 0:
                print(
                    "\nRoom called {} already exists, please try a different room name".format(label))
            else:
                # create room with room name according to map value
                self.rooms.append(instance[args[0].lower()].with_name(label))
                self.rooms[len(self.rooms) - 1].people = list()

                print("\n{} {} successfully created\n".format(
                    self.rooms[len(self.rooms) - 1], label))

        # return the type instance for validity check
        return instance[args[0].lower()].with_name(None)

    @Validate.check_empty_offices
    def add_person(self, fname=False, lname=False, type=False, accomodation=False):
        # in case of trailing white space, do nothing
        if not fname or not lname or not type:
            return
        Spinner.show()
        name = "{} {}".format(fname, lname)
        instance = {
            "fellow": Fellow,
            "staff": Staff
        }

        if type.lower() not in instance:
            return 'Person of type {} doesn\'t exist'.format(type)

        # first create person
        new_person = instance[type.lower()].with_name(name)
        self.people.append(new_person)

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
            print("{} {} was successfully created".format(
                new_person, new_person.full_name.upper()))
            # Randomly allocate office
            print(self.allocate_room(new_person,
                                     random.choice(empty_offices)) + "\n")

        # Then living room with choice
        if(accomodation):
            if isinstance(new_person, Fellow):
                if len(empty_living_rooms) < 1:
                    return "No empty living rooms to allocate this fellow"
                else:
                    # Randomly allocate living space
                    print("\b" + self.allocate_room(new_person,
                                                    random.choice(empty_living_rooms)))
            else:
                return "No living room for non fellows"

        return new_person

    @Validate.validate_allocation
    def allocate_room(self, person, room):
        # set person attribute according to room instance
        if isinstance(room, Office):
            person.allocated_office = room

        if isinstance(room, LivingSpace):
            person.allocated_livingroom = room

        room.people.append(person)
        return "{} {} successfully allocated to {} {}".format(person, person.full_name.upper(), room, room.name)

    def reallocate_person(self, id, new_room):
        # first reduce all people in all rooms, convert to generator to save memory
        gathering = (reduce(lambda x, y: x.people + y.people, self.rooms))
        # get people with specified id
        id = int(id)
        person_assoc = list(filter(lambda obj: obj.id == id, gathering))
        if len(person_assoc) < 1:
            return "Person with identiifer {} not found".format(id)
        person = person_assoc[0]  # person is the first object
        
        next_room_assoc = list(filter(lambda obj: obj.name.lower() == new_room.lower(), self.rooms))
        next_room = next_room_assoc[0]

        # Return if room not found
        if(len(next_room_assoc) > 0):
            #check if instance and allocate with same type
            if isinstance(next_room_assoc[0], Office):
                prev_room_assoc = list(filter(lambda obj: obj.name == person.allocated_office.name, self.rooms))
                if len(prev_room_assoc) < 1:
                    return "Previous office for {} {} not found".format(person, person.full_name.upper())
                #get index of person in previous room
                index = [i for i, x in enumerate(prev_room_assoc[0].people) if x.id == person.id][0]
                del prev_room_assoc[0].people[index]
                person.allocated_office = None
            else:
                prev_room_assoc = list(filter(lambda obj: obj.name == person.allocated_livingroom.name, self.rooms))
                if len(prev_room_assoc) < 1:
                    return "Previous Living room for {} {} not found".format(person, person.full_name.upper())
                #get index of person in previous room
                index = [i for i, x in enumerate(prev_room_assoc[0].people) if x.id == person.id][0]
                del prev_room_assoc[0].people[index]
                person.allocated_livingroom = None
                
            return (self.allocate_room(person, next_room))
        else:
            return "Room called {} not found".format(new_room)

    def load_people(self, file_path=False):
        Spinner.show()
        if file_path:
            if not os.path.exists(file_path):
                return "File path {} doesn't exist, please try again".format(file_path)
            with open(file_path, 'r') as f:
                rows = f.read().split('\n')
                for row in rows:
                    self.add_person(*row.split(' '))
            return True
        else:
            return "Oops, file path not found !"

    def print_allocations(self, output_path=False):
        Spinner.show()
        # get rooms with people allocated to them
        search = list(filter(lambda room: len(room.people) > 0, self.rooms))
        if len(search) < 1:
            return "No allocations found in Amity"

        # get formatted output of the allocations
        res = MyFormatter.room_format(search)

        # write to file if path is specified
        if output_path:
            with open(output_path, "w") as f:
                f.write(res)
                return "Allocations successfully written to file {}.".format(output_path)
        else:
            return res

    def print_unallocated(self, output_path=False):
        Spinner.show()
        if len(self.rooms) < 1:
            return "No rooms present in Amity yet, please try adding some rooms"

        # first reduce all people in all rooms, convert to generator to save memory
        gathering = (reduce(lambda x, y: x.people + y.people, self.rooms))
        # get all unallocated people first
        search = list(
            filter(lambda person: person.allocated_office is None, gathering))

        if len(search) < 1:
            return "No unallocations found in Amity"

        res = MyFormatter.people_format(search)
        if output_path:
            with open(output_path, "w") as f:
                f.write(res)
                return "Unallocated people successfully written to file {}".format(output_path)
        else:
            return res

    def print_room(self, room_name):
        Spinner.show()
        search = list(filter(lambda room: room.name.lower()
                             == room_name.lower(), self.rooms))
        if len(search) < 1:
            return "Room with name {} not found in amity, please check spelling and try again".format(room_name)
        return MyFormatter.room_format(search)

    def save_state(self, db=False):
        Spinner.show()
        name = db if db else "recent.db"
        with open(name,'wb+') as f:
            f.write(pickle.dumps(self))
        return "State saved successfuly as {}".format(name)

    def load_state(self, db=False):
        Spinner.show()
        if not db:
            return "Please specify target state, use 'recent.db' to get the recently saved"

        if not os.path.exists(db):
            return "Target state {} not found, please check spelling".format(db)
        with open(db,'rb') as f:
            state = pickle.loads(f.read())
            self.rooms = state.rooms
            self.people = state.people
        return "State {} loaded successfully".format(db)

