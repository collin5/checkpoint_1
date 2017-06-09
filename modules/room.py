# @Author: collins
# @Date:   2017-06-09T12:16:10+03:00
# @Last modified by:   collins
# @Last modified time: 2017-06-09T13:10:06+03:00


class Room(list):

    def __init__(room_name, capacity, people=[]):
        super(Room, self).__init__()
        self.room_name, self.capacity, self.people = room_name, capacity, people

    def add_people(*args):
        pass
