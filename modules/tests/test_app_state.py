#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: test_app_state.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 30.06.2017
# Last Modified: 30.06.2017

from unittest import TestCase
from modules.amity import Amity
import os

class AppStateTestCase(TestCase):

    def setUp(self):
        self.amity = Amity()

    def test_save_state_successfully(self):
        self.amity.create_room(['office demo'])
        self.amity.save_state()
        self.assertTrue(os.path.exists("recent.db"))
        # house cleaning
        os.system('rm default_state.db')


    def test_save_state_with_specific_db_name(self):
        self.amity.create_room(['office demo'])
        self.amity.save_state('my_state.db')
        self.assertTrue(os.path.exists("my_state.db"))
        os.system("rm my_state.db")

    def test_load_state(self):
        self.amity.save_state("empty_state.db")
        msg = self.amity.load_state("empty_state.db")
        self.assertEqual(msg.lower(), "state empty_state.db loaded successfully")

    def test_load_state_no_params(self):
        msg = self.amity.load_state()
        self.assertEqual(msg.lower(), "please specify target state, use 'recent.db' to get the recently saved")

    def test_load_state_invalid_path(self):
        msg = self.amity.load_state("lsksksksks.db")
        self.assertEqual(msg.lower(), "target state lsksksksks.db not found, please check spelling")
