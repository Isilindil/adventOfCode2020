#!/usr/bin/python

def create_sub_chain(data) :
    all_sub_chain = []
    start = 0
    for i in range(len(data) -1) :
        diff = data[i + 1] - data[i]
        if diff == 3:
            all_sub_chain.append(data[start:i+1])
            start = i+1
    return all_sub_chain

def is_this_a_working_solution(adapters_chain) :
    for i in range(len(adapters_chain)-1) :
        diff = adapters_chain[i+1] - adapters_chain[i]
        if diff > 3 : return False
    else : return True

def test_all_solution(adapters_chain) :
    working_alt_chain = []
    for i in range(1, len(adapters_chain)-1) :
        new_chain = list(adapters_chain)
        new_chain.pop(i)
        if is_this_a_working_solution(new_chain) : working_alt_chain.append(new_chain)
    return working_alt_chain

if __name__ == "__main__" :
    with open("input") as a :
        data = a.read().split("\n")
    a.close()
    data = [int(a) for a in data]
    data.sort()

    data.append(data[-1]+3)
    data.insert(0, 0)

    # part one
    diff = {1 : 0, 3 : 0}
    for i in range(len(data)-1) :
        diff[data[i+1] - data[i]] += 1
    print(diff[1]*diff[3])

    # part two
    all_sub_chain = create_sub_chain(data)
    all_sub_chain.append([172])

    all_working_chain = {}
    for chain in all_sub_chain :
        key_chain = "".join([str(a) for a in chain])
        all_working_chain[key_chain] = {0 : [chain]}
        if len(chain) > 2 :
            for i in range(1, len(chain)) :
                all_working_chain[key_chain][i] = []
                for sub_chain in all_working_chain[key_chain][i - 1]:
                    all_working_chain[key_chain][i] += test_all_solution(sub_chain)
                if len(all_working_chain[key_chain][i]) == 0: break

    all_sub_total = []
    for key_chain in all_working_chain.keys() :
        subTotal = 0
        for i in all_working_chain[key_chain].keys() :
            to_set = set([str(a) for a in all_working_chain[key_chain][i]])
            subTotal += len(to_set)
        all_sub_total.append(subTotal)

    total_chain = 1
    for i in all_sub_total :
        #print(i)
        total_chain *= i
    print(total_chain)
