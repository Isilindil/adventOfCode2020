#!/usr/bin/python

if __name__ == "__main__":
    with open("input") as a:
        data = a.read().split(",")
    a.close()

    for i, e in enumerate(data):
        data[i] = int(e)
        print(e, " - ", i+1)

    number_turn = {}
    # turn_number = {}
    for i, e in enumerate(data):
        number_turn[int(e)] = [i]
        # turn_number[i] = int(e)

    number_already_shout = data[:-1]
    for turn in range(6, 2020): # Part One
    # for turn in range(6, 30000000): # Part Two
        if data[-1] not in number_already_shout:
            num_to_shout = 0
            number_already_shout.append(data[-1])
            data.append(num_to_shout)
            number_turn[num_to_shout].append(turn)
        else:
            num_to_shout = number_turn[data[-1]][-1] - number_turn[data[-1]][-2]
            data.append(num_to_shout)
            try:
                number_turn[num_to_shout].append(turn)
            except:
                number_turn[num_to_shout] = [turn]
        print(num_to_shout, " - ", len(data))
