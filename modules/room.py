# @Author: collins
# @Date:   2017-06-09T12:16:10+03:00
# @Last modified by:   collins
# @Last modified time: 2017-06-10T18:06:56+03:00
from abc import ABCMeta


class Room(list):
    __metaclass__ = ABCMeta

    def __init__(self, name, capacity, people=[]):
        super(Room, self).__init__()
        self.name, self.capacity, self.people = name, capacity, people

