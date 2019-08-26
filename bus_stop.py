"""
There is a bus moving in the city, and it takes and drop some people in each bus stop.
You are provided with a list (or array) of integer arrays (or tuples).
Each integer array has two items which represent number of people get into bus
(The first item) and number of people get off the bus (The second item) in a bus stop.

Your task is to return number of people who are still in the bus after the last bus station
(after the last array). Even though it is the last bus stop, the bus is not empty and some
people are still in the bus, and they are probably sleeping there :D

The number of people in the bus is always >= 0. So the return integer can't be negative.

The second value in the first integer array is 0, since the bus is empty in the first bus stop.
"""


def number(bus_stops):
    return sum((x - y for x, y in bus_stops))


def number_v2(bus_stops):
    inside = out = 0
    for stop in bus_stops:
        inside += stop[0]
        out += stop[1]
    return inside - out