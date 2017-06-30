# @Author: collins
# @Date:   2017-06-10T13:27:37+03:00
# @Last modified by:   collins
# @Last modified time: 2017-06-10T16:51:17+03:00


import os
os.sys.path.append('.')
from unittest import TestCase
from modules.amity import Amity
from modules.office import Office
from modules.living_space import LivingSpace
from modules.middleware.const import *


class TestCreateRoom(TestCase):

    def setUp(self):
        self.amity = Amity()

    def test_create_room_succesfully(self):
        initial_room_count = len(self.amity.rooms)
        self.amity.create_room(["office Mombasa"])
        new_room_count = len(self.amity.rooms)

        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_create_rooms_successfully(self):
        initial_room_count = len(self.amity.rooms)
        self.amity.create_room(["office Mombasa Lagos"])
        new_room_count = len(self.amity.rooms)

        self.assertEqual(new_room_count - initial_room_count, 2)

    def test_create_rooms_successfully_2(self):
        initial_room_count = len(self.amity.rooms)
        self.amity.create_room(["office Kampala Lagos NewYork Nairobi"])
        new_room_count = len(self.amity.rooms)

        self.assertEqual(new_room_count - initial_room_count, 4)


    def test_create_room_with_type_office(self):
        self.amity.rooms[:] = []
        self.amity.create_room(["Office Lagos"])

        self.assertTrue(isinstance(self.amity.rooms[0], Office))

    def test_create_room_with_type_livingspace(self):
        self.amity.rooms[:] = []
        self.amity.create_room(["Living Catherines"])

        self.assertTrue(isinstance(self.amity.rooms[0], LivingSpace))

    def test_create_rooms_multiple_types(self):
        self.amity.rooms[:] = []
        self.amity.create_room(["Office Dojo"])
        self.amity.create_room(["Living Catherines"])

        self.assertTrue(isinstance(self.amity.rooms[0], Office))
        self.assertTrue(isinstance(self.amity.rooms[1], LivingSpace))


    def test_create_room_invalid_type(self):
        err = self.amity.create_room(["lorem ipsum"])
        self.assertEqual(err.lower(), "room of type lorem doesn\'t exist")

    def test_create_room_duplicate(self):
        self.amity.rooms[:] = []
        self.amity.create_room(["office ipsum"])
        err = self.amity.create_room(["office ipsum"])
        self.assertEqual(len(self.amity.rooms), 1)
