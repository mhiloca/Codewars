"""
You are given an array (which will have a length of at least 3, but could be very large) containing integers.
The array is either entirely comprised of odd integers or entirely comprised of even integers
except for a single integer N.
Write a method that takes the array as an argument and returns this "outlier" N.
"""


def find_outlier(integers):
    evens = [x for x in integers if x % 2 == 0]
    odds = [y for y in integers if y % 2 != 0]
    if len(evens) == 1:
        return evens[0]
    return odds[0]


print(find_outlier([2, 4, 6, 8, 10, 3]))
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))