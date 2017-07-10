# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 28.06.2017
# Last Modified: 28.06.2017

import os
os.sys.path.append('.')
from unittest import TestCase
from modules.amity import Amity


class PrintAllocationsTestCase(TestCase):

    def setUp(self):
        self.amity = Amity()

    def test_print_allocations_successfully(self):
        self.amity.create_room(["office Mombasa"])
        self.amity.add_person('Edwin', 'Kato', 'fellow')
        stdout = self.amity.print_allocations()
        self.assertTrue('edwin' in stdout.lower())

    def test_print_allocations_successfully_2(self):
        self.amity.create_room(['office shell'])
        self.amity.add_person('Dona', 'Mwine', 'fellow')
        self.amity.add_person('Shem', 'O', 'staff')
        stdout = self.amity.print_allocations()
        self.assertTrue('dona' in stdout.lower())
        self.assertTrue('shem' in stdout.lower())

    def test_print_allocations_with_living_room(self):
        self.amity.create_room(['office oculus'])
        self.amity.create_room(['living catherines'])
        self.amity.add_person('collins', 'a', 'fellow', True)

        stdout = self.amity.print_allocations()
        self.assertTrue('catherines' in stdout.lower())
        self.assertTrue('collins' in stdout.lower())


    def test_print_allocations_to_file(self):
        self.amity.create_room(['office ruby'])
        self.amity.add_person('collins', 'a', 'fellow', True)
        msg = self.amity.print_allocations("test_allocations.txt")
        self.assertEqual(msg.lower(),"allocations successfully written to file test_allocations.txt." )

    def tearDown(self):
        if os.path.exists("test_allocations.txt"):
            os.system('rm test_allocations.txt')

