#!/usr/bin/python

a = 0
b = 0
c = 0

def descriminant():

    return ((b * b) - (4 * a * b))

a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))

print("( " + str(b * b) + " +/- " + str(descriminant()) + " )/( " + str(a * 2) + " )")

