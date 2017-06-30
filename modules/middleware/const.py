# @Author: collins
# @Date:   2017-06-09T16:20:04+03:00
# @Last modified by:   collins
# @Last modified time: 2017-06-10T13:22:01+03:00


class Enum(set):
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError


# all actions amity can perform
Action = Enum([
    'CREATE_ROOM', 'ADD_PERSON',
    'REALLOCATE_PERSON', 'LOAD_PEOPLE',
    'PRINT_ALLOCATIONS', 'PRINT_UNALLOCATED',
    'PRINT_ROOM', 'SAVE_STATE',
    'LOAD_STATE'
])


RoomType = Enum([
    'LIVING', 'OFFICE'
])

PersonType = Enum([
    'STAFF', 'FELLOW'
])
