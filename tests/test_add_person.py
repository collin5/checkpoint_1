# @Author: collins
# @Date:   2017-06-10T19:03:16+03:00
# @Last modified by:   collins
# @Last modified time: 2017-06-10T19:57:32+03:00


from unittest import TestCase
from modules.amity import Amity
from modules.fellow import Fellow
from modules.staff import Staff


class TestAddPerson(TestCase):

    def setUp():
        self.amity = Amity()
        self.amity.create_room('office', 'Mombasa')
        self.amity.create_room('living', 'Catherines')

    def test_add_person_successfully():
        # clear all people in the room
        initial_people_count = len(self.amity.people)
        self.add_person("Collins Abitekaniza", "Fellow")
        self.assertEqual(len(self.amity.people) - initial_people_count, 1)

    def test_add_more_people_successfully():
        initial_people_count = len(self.amity.people)
        self.add_person("Mbithe Nzomo", "Fellow")
        self.add_person("John A", "Fellow")
        self.assertEqual(len(self.amity.people) - initial_people_count, 2)

    def test_add_people_different_types():
        initial_people_count = len(self.amity.people)
        self.add_person("Collins Abitekaniza", 'Fellow')
        self.add_person("Josh A", "Staff")
        self.assertEqual(len(self.amity.people) - initial_people_count, 2)

    def test_person_type():
        person_1 = self.amity.add_person("Mukiibi David", "Fellow")
        person_2 = self.amity.add_person("Bill TheLizard", "Staff")

        self.assertTrue(isinstance(person_1, Fellow))
        self.assertTrue(isinstance(person_2, Staff))

    def test_person_type_ignorecasing():
        person_1 = self.add_person("John Skeet", "Fellow")
        person_2 = self.add_person("Collins Abitekaniza", "fEllOw")
        person_3 = self.add_person("Josh A", "sTAFF")
        person_4 = self.add_person("Mahad A", "fElloW")

        self.assertTrue(isinstance(person_1, Fellow))
        self.assertTrue(isinstance(person_2, Fellow))
        self.assertTrue(isinstance(person_3, Staff))
        self.assertTrue(isinstance(person_4, Fellow))
