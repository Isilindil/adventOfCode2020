#!/usr/bin/python

if __name__ == "__main__":
    with open("input") as a:
        data = a.read().split(",")
    a.close()

    for i, e in enumerate(data):
        data[i] = int(e)
        # print(e, " - ", i+1)

    number_turn = {}
    for i, e in enumerate(data[:-1]):
        number_turn[int(e)] = int(i)
    print(number_turn)

    last_number_shout = data[-1]
    print(last_number_shout)
    print(len(data)-1)

    # for turn in range(len(data)-1, 2020-1):  # Part One
    for turn in range(len(data)-1, 30000000-1):  # Part Two
        try:
            last_time = number_turn[last_number_shout]
        except KeyError:
            number_turn[last_number_shout] = turn
            last_number_shout = 0
        else:
            number_turn[last_number_shout] = turn
            last_number_shout = turn - last_time

    print(turn+1, " - ", last_number_shout)
