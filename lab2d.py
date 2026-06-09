#!/usr/bin/env python3
# Author: Christian Staffiere
# Author ID: cstaffiere
# Date Created: 2024/06/17
# lab2d. Takes name & age as arguments and returns a usage msg if anything other than 2 arguments are given.

import sys

if len(sys.argv) != 3:
    print ("Usage: " + sys.argv[0] + " name age")
    sys.exit(0)

name = sys.argv[1]
age = sys.argv[2]

print('Hi ' + name + ', you are ' + str(age) + ' years old.')