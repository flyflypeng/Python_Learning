#!/usr/bin/env python
# _*_ coding: utf-8 -*-

import hello
import sys
import fileinput
import time

# hello.test()

# print sys.modules

# fileinput module example test
# for line in fileinput.input(backup=True):
#     line = line.rstrip()
#     num = fileinput.lineno()
#     print '%-40s # %2d' % (line,num)

# time module example test
print time.time()
print time.asctime()
