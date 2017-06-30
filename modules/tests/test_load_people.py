#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: test_load_people.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 30.06.2017
# Last Modified: 30.06.2017

from unittest import TestCase
from modules.amity import Amity
import os

class LoadPeopleTestCase(TestCase):

    def setUp(self):
        self.amity = Amity()

    def test_load_people_successfully(self):
        self.amity.create_room(['office nania'])
        buffer_str = "COLLINS A FELLOW"
        #first write str to file
        with open("test_file_load_people.txt", 'w') as f:
            f.write(buffer_str)

        #now load from file
        res = self.amity.load_people("test_file_load_people.txt")
        self.assertTrue(res)
        os.system("rm test_file_load_people.txt")

    def test_load_people_successfully_2(self):
        self.amity.create_room(['office ruby'])
        initial_people_count = len(self.amity.rooms[0].people)

        buffer_str = "JOSEPH A FELLOW"
        with open("test_file_load_people.txt", 'w') as f:
            f.write(buffer_str)

        self.amity.load_people("test_file_load_people.txt")
        self.assertEqual(len(self.amity.rooms[0].people) - initial_people_count, 1)
        os.system("rm test_file_load_people.txt")


    def test_load_people_invalid_file_name(self):
        self.amity.create_room(['office ruby'])
        err = self.amity.load_people("lwlwlwllwl.txt")
        self.assertEqual(err.lower(), "file path lwlwlwllwl.txt doesn't exist, please try again")


