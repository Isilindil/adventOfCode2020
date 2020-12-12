#!/usr/bin/python

def calc_sum_max_min(l) :
    up = l[0]
    down = l[0]
    for i in l :
        up = max(up, i)
        down = min(down, i)
    return up+down

def find_sum(subLength, data, result) :
    start = 0
    while 1 :
        sub_data = data[start:subLength+start]
        if sum(sub_data) == result :
            print(sub_data)
            return calc_sum_max_min(sub_data)
        else :
            start += 1
            if start >= len(data) - subLength : break
    return 0


if __name__ == "__main__" :
    with open("input") as a :
        data = a.read().split("\n")
    a.close()
    data = [int(a) for a in data]

    # Part one
    start = 0
    end = 25

    while 1 :
        sub_data = data[start:end]
        nbr = data[end]
        flag = 0

        for i in range(len(sub_data)) :
            for j in range(i+1, len(sub_data)) :
                if nbr == sub_data[i] + sub_data[j] : flag = nbr
        if not flag : break

        start += 1
        end += 1
    print(nbr)

    # Part two
    for sub_len in range(2, len(data)) :
        result = find_sum(sub_len, data, nbr)
        if result : break
    print(result)
