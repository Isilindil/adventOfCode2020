#!/usr/bin/python

def is_bus_at_terminus(bus, time):
    if time % bus == 0:
        return 1
    return 0


if __name__ == "__main__":
    with open("input") as a:
        early_timestamp = int(a.readline().strip("\n"))
        all_buses = a.readline().strip("\n").split(",")
        all_buses = [int(x) for x in all_buses if x != 'x']
    a.close()
    print(early_timestamp)
    print(all_buses)

    timestamp = 0
    bus_not_found = 1
    bus_at_sea = 0
    while bus_not_found:
        timestamp += 1
        for i, e in enumerate(all_buses):
            print(timestamp)
            if is_bus_at_terminus(e, timestamp):
                print(e)
                if timestamp >= early_timestamp:
                    bus_not_found = 0
                    bus_at_sea = e

    waiting = timestamp - early_timestamp
    print(waiting)
    print(bus_at_sea*waiting)
