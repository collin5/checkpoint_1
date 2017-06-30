#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: test_print_room.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 30.06.2017
# Last Modified: 30.06.2017

from unittest import TestCase
from modules.amity import Amity


class PrintRoomTestCase(TestCase):

    def setUp(self):
        self.amity = Amity()

    def test_print_room_successfully(self):
        self.amity.create_room(["office Ruby"])
        self.amity.add_person("collins", "a", 'fellow')
        out = self.amity.print_room("Ruby")
        self.assertTrue("collins" in out.lower())

    def test_print_empty_room_with_message_successfully(self):
        self.amity.create_room(["office ruby"])
        out = self.amity.print_room("ruby")
        self.assertTrue("empty" in out.lower())
