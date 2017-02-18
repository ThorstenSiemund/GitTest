#!/usr/bin/env python


def blah(addition=None):
    return 'Blah ' + addition


name = 'Frodo'
age = 30
my_string = f"He said his name is {name} and he is {age} years old."

age += 10

print(my_string)  # random comment

name != 'Frieda'  # this is wrong

print(blah('blah'))
