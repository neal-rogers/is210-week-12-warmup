#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """Class object docstring.

    """

    def __init__(self, logfilename):
        """Constructor.

        args(str): Accepts filename as parameter.

        """
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """Docstring.
        """
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """Docstring.
        """
        handled = []

        try:
            fhandler = open(self.logfilename, 'a')
        except IOError:
            self.log('Log file not found.', time.time())
        for index, entry in enumerate(self.msgs):
            fhandler.write(str(entry) + '\n')
            handled.append(index)

        for index in handled[::-1]:
            del self.msgs[index]

        fhandler.close()
