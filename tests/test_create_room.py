# @Author: collins
# @Date:   2017-06-10T13:27:37+03:00
# @Last modified by:   collins
# @Last modified time: 2017-06-10T16:51:17+03:00


from unittest import TestCase
from modules.amity import Amity
from modules.office import Office
from modules.living_space import LivingSpace
from constants import *


class TestCreateRoom(TestCase):

    def setUp():
        self.amity = Amity()

    def test_create_room_succesfully():
        initial_room_count = len(self.amity.rooms)
        self.amity.create_room("Mombasa")
        new_room_count = len(self.amity.rooms)

        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_create_rooms_successfully():
        initial_room_count = len(self.amity.rooms)
        self.amity.create_room("Mombasa", "Lagos")
        new_room_count = len(self.amity.rooms)

        self.assertEqual(new_room_count - initial_room_count, 2)

    def test_create_rooms_successfully_2():
        initial_room_count = len(self.amity.rooms)
        self.amity.create_room("Kampala", "Lagos", "NewYork", "Nairobi")
        new_room_count = len(self.amity.rooms)

        self.assertEqual(new_room_count - initial_room_count, 4)

    def test_default_room_office():
        # Room type must be office if type not specified
        self.amity.rooms[:] = []  # first remove all rooms from Amity
        self.amity.create_room("MaleWing")

        self.assertTrue(isinstance(amity.rooms[0], Office))

    def test_create_room_with_type_office():
        self.amity.rooms[:] = []
        self.amity.create_room("Office", "Lagos")

        self.assertTrue(isinstance(amity.rooms[0], Office))

    def test_create_room_with_type_livingspace():
        self.amity.rooms[:] = []
        self.amity.create_room("Living", "Catherines")

        self.assertTrue(isinstance(amity.rooms[0], LivingSpace))

    def test_create_rooms_multiple_types():
        self.amity.rooms[:] = []
        self.amity.create_room("Office", "Dojo")
        self.amity.create_room("Living", "Catherines")

        self.assertTrue(self.amity.rooms[0], Office)
        self.assertTrue(self.amity.rooms[1], LivingSpace)
