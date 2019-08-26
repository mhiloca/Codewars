def number(bus_stops):
    return sum((x - y for x, y in bus_stops))

def number(bus_stops):
    inside = out = 0
    for stop in bus_stops:
        inside += stop[0]
        out += stop[1]
    return inside - out