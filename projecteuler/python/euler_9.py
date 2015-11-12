#!/usr/bin/env python3

__author__ = "Asher Minden-Webb"
__title__ = "Project Euler Problem 9: Special Pythagorean Triplet"
__date_created__ = "2014/09/24"

'''
URL: https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''


import math

def pythagorean_triplet(n: int) -> (int, int, int):
    cap1 = n - 2
    for a in range(1, cap1):
        cap2 = n - a - 1
        for b in range(1, cap2):
            c = math.sqrt(a ** 2 + b ** 2)
            if int(c) == c and a + b + c == n:
                return a, b, int(c)
    print("No such triplet")    
    return None, None, None

a, b, c = pythagorean_triplet(1000)
print("%d x %d x %d = %d" %(a, b, c, a * b * c))