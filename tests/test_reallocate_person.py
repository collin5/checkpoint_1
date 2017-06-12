# @Author: collins
# @Date:   2017-06-12T17:25:10+03:00
# @Last modified by:   collins
# @Last modified time: 2017-06-12T17:48:48+03:00


from unittest import TestCase
from modules.amity import Amity


class TestReallocatePerson(TestCase):

    def setUp():
        self.amity = Amity()

    def reallocate_person_office_successfully():
        self.amity.create_room("office", "Ruby")

        # Person will be automatically allocated on instantiation
        self.add_person("Mbithe Nzomo", "fellow")
        person = self.amity.rooms[0].people[0]

        # Now let's reallocate
        self.amity.create_room("office", "Blue")
        self.amity.reallocate_person(person.id, self.amity.rooms[0], self.amity.rooms[1])

        self.assertEqual(person.allocated_office.name, "Blue")

    def rallocate_person_living_room_successfully():
        # office needed for every person in amity
        self.amity.create_room("office", "Purple")

        self.amity.create_room("living", "Catherines")

        # This will give fellow living room
        self.add_person("Collins Abitekaniza", "fellow", True)
        fellow = self.amity.rooms[1].people[0]

        # Now reallocate fellow
        self.amity.create_room("living", "Kyampala")
        self.amity.reallocate_person(person.id, self.amity.room[1], self.amity.rooms[2])

        self.assertTrue(person.allocated_livingroom, "Kyampala")
