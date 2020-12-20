#!/usr/bin/python

def is_bus_at_terminus(bus, time):
    if time % bus == 0:
        return 1
    return 0


def part_one(early_timestamp, all_buses):
    timestamp = 0
    bus_not_found = 1
    bus_at_sea = 0
    while bus_not_found:
        timestamp += 1
        for i, e in enumerate(all_buses):
            # print(timestamp)
            if is_bus_at_terminus(e, timestamp):
                # print(e)
                if timestamp >= early_timestamp:
                    bus_not_found = 0
                    bus_at_sea = e

    waiting = timestamp - early_timestamp
    # print(waiting)
    print("Answer Part One: ", bus_at_sea*waiting)


if __name__ == "__main__":
    with open("input") as a:
        early_timestamp = int(a.readline().strip("\n"))
        all_buses = a.readline().strip("\n").split(",")
        all_buses_p1 = [int(x) for x in all_buses if x != 'x']
    a.close()
    # print(early_timestamp)
    # print(all_buses)

    # part_one(early_timestamp, all_buses_p1)

    # part_two
    all_diff = []
    for i, e in enumerate(all_buses):
        if e != 'x':
            all_diff.append((int(e), i))

    # for id, offset in all_diff:
    #    print(f"(ts + {offset}) % {id} = 0")

    # all_diff = [(7, 0), (13, 1), (59, 4), (31, 6), (19, 7)]

    add = all_diff[0][0]
    ts = 0
    for i in range(2, len(all_diff)+1):
        while True:
            ts += add
            for id, offset in all_diff[:i]:
                if (ts + offset) % id != 0:
                    break
            else :
                add *= all_diff[i-1][0]
                print(ts, "\t", add)
                break
