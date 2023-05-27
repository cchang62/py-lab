# import module

# print(methodB())

import sys
print(sys.path)

# from . import moduleY
from pkg1 import moduleY as m
print("m: %s"%m.methodB())

import pkg1.moduleY as m1
print("m1: %s"%m1.methodC())


while True:
    a=1
