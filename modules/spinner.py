#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: modules/spinner.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 29.06.2017
# Last Modified: 29.06.201

import itertools
import sys
import time


class Spinner(object):
   
    @staticmethod
    def show(msg = None):
        spinner = itertools.cycle(['-', '/', '|', '\\'])

        for i in range(1):
            sys.stdout.write(next(spinner))
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write('\b')
