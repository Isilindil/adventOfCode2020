#!/usr/bin/python

if __name__ == "__main__" :
    with open("input") as a :
        data = a.read().split("\n")
    a.close()

    group_yes = {}
    members_in_group = 0
    total_yes = 0
    total_common_yes = 0

    for l in data :
        if not l : # new group
            total_yes += len(group_yes.keys())
            total_common_yes += list(group_yes.values()).count(members_in_group)
            group_yes = {}
            members_in_group = 0
        else :
            members_in_group += 1
            for i in list(l) :
                try : group_yes[i] += 1
                except KeyError : group_yes[i] = 1
    else : # last group
        total_yes += len(group_yes.keys())
        total_common_yes += list(group_yes.values()).count(members_in_group)
        group_yes = {}
        members_in_group = 0

    print(total_yes)
    print(total_common_yes)
