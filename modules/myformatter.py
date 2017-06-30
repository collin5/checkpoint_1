#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: myformatter.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 28.06.2017
# Last Modified: 28.06.2017


class MyFormatter(object):

    @staticmethod
    def room_format(room_assoc):
        res = ""
        if len(room_assoc) > 0:
            for room in room_assoc:
                res += "\n\n"+room.name.upper()+"\n-------------------------------------\n"

                people_str = ""
                if len(room.people) > 0:
                    for person in room.people:
                        people_str += ", [ID - {} ] {} ".format(person.id, person.full_name.upper())
                else:
                    people_str = " \tEMPTY"

                res += people_str[1:] #strip off first comma

        else:
            res = "NO ROOMS FOUND IN AMITY"
        return res

