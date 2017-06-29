# @Author: collins
# @Date:   2017-06-12T11:28:26+03:00
# @Last modified by:   collins
# @Last modified time: 2017-06-12T15:55:39+03:00

from modules.fellow import Fellow
from modules.staff import Staff
from modules.office import Office

class Validate(object):

    def __init__(self):
        super(Validate, self).__init__()

    @staticmethod
    def validate_allocation(func):
        def verify(*args, **kwargs):
            person, room = args[0], args[1]
             #first only staff are allowed to be allocated living space
            if isinstance(person, Fellow) and isinstance(person, Staff):
                return "Staff cannot be allocated living room"
            else:
                #then check if room is empty
                if len(room.people) == room.capacity:
                    return "This rooom is probably full"
                #pass other wise

            return func(*args, **kwargs)

        return verify

    @staticmethod
    def check_empty_offices(func):
        # Verify if there are any empty offices before creating person, else pass
        def verify(*args, **kwargs):
            ctx, type = args[0], args[1]

            empty_offices = list(filter(lambda room: isinstance(room, Office)
                and (len(room.people) < room.capacity), ctx.rooms))
            if len(empty_offices) < 1:
                return "There are no empty offices in Amity"
            else:
                return func(*args, **kwargs)

        return verify


