#!/usr/bin/python

if __name__ == "__main__" :
    with open("input") as a :
        data = a.read()
        data = data.split("\n")
        a.close()
    #print(data)
    #print(type(data))

    cycle = len(data[0])

    allMoveR = [1, 3, 5, 7, 1] # move right
    allMoveD = [1, 1, 1, 1, 2] # move down

    multiTree = 1

    for moveR, moveD in zip(allMoveR, allMoveD) :
        currentPos = 0
        tree = 0
        snow = 0
        for slice in range(moveD, len(data), moveD) :
            currentPos = (currentPos+moveR)%cycle
            if data[slice][currentPos] == '#' : tree += 1
            elif data[slice][currentPos] == '.' : snow += 1
            else :
                print("Ooops : {}".format(data[slice][currentPos]))
                break
        print("tree : {}".format(tree))
        print("snow : {}".format(snow))
        multiTree *= tree
    print(multiTree)
