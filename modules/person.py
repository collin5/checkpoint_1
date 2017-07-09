# @Author: collins
# @Date:   2017-06-09T12:15:11+03:00
# @Last modified by:   collins
# @Last modified time: 2017-06-10T13:20:25+03:00

from modules.middleware.fileiointerface import FileIO
from abc import ABCMeta


class Person:
    __metaclass__ = ABCMeta

    def __init__(self, person_name, accomodation):
        self.id = Person.get_ID()  # get person ID autoincrement
        self.first_name, self.last_name = person_name.split(' ')
        self.accomodation = accomodation

    @classmethod
    def create_from_name(ctx, person_name):
        """Create person object from provided name"""
        return ctx(person_name, 'N')

    @property
    def full_name(self):
        """Return person full name as an attr"""
        return "{} {}".format(self.first_name, self.last_name)

    @staticmethod
    @FileIO.generate_pk_with_file
    def get_ID(*args, **kwargs):
        """Create unique primary key with auto increment for each person object"""
        return args[0]['PK']
