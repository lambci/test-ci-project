# -*- coding: utf-8 -*-

"""build script for test repo
"""

from __future__ import print_function


'''
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
LIGHT_PURPLE = '\033[94m'
PURPLE = '\033[95m'
END = '\033[0m'
'''


def red(text):
    return '\033[91m %s\033[00m' % text


print('Hello ' + red('colored') + ' world!')

