#!/usr/bin/env python3
# Author = Siddhartha Shrestha Student ID = 160706222

def is_digits(sobj):
    for i in sobj:
        if not i.isdigit():
            return False
    return True

if __name__ == '__main__':
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')