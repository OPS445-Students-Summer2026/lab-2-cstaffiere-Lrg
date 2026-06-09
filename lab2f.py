#!/usr/bin/env python3
# Author: Christian Staffiere
# Author ID: cstaffiere
# Date Created: 2024/06/17
# Counts down from value specified in timer as argument until it reaches 0. Exits with "blast off!"
import sys

timer = int(sys.argv[1])

while timer > 0:
    print(timer)
    timer = timer -1

print("blast off!")