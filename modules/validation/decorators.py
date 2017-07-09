# @Author: collins
# @Date:   2017-06-12T11:28:26+03:00
# @Last modified by:   collins
# @Last modified time: 2017-06-12T15:55:39+03:00

from modules.fellow import Fellow
from modules.staff import Staff
from modules.office import Office


class Validate:

    @staticmethod
    def validate_allocation(func):
        def verify(*args, **kwargs):
            person, room = args[1], args[2]
            # first only staff are allowed to be allocated living space
            if isinstance(person, Fellow) and isinstance(person, Staff):
                return "Staff cannot be allocated living room"
            else:
                # then check if room is empty
                if len(room.people) == room.capacity:
                    return "This rooom is probably full"
                # pass other wise

            return func(*args, **kwargs)

        return verify
