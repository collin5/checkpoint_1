#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: test_print_unallocated.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 30.06.2017
# Last Modified: 30.06.2017

from modules.amity import Amity
from unittest import TestCase

class UnallocatedTestCase(TestCase):
    
    def setUp(self):
        self.amity = Amity()


    def test_print_unallocated_no_rooms(self):
        msg = self.amity.print_unallocated()
        self.assertEqual(msg.lower(), "no rooms present in amity yet, please try adding some rooms")

    def test_print_unallocated_with_no_people_created(self):
        self.amity.create_room(['office ruby'])
        msg = self.amity.print_unallocated()
        self.assertEqual(msg.lower(), "no unallocations found in amity")
