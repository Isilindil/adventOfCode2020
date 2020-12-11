#!/usr/bin/python

def checkpwd_step_one(min, max, neededLetters, pwd) :
    cpt = 0
    for l in pwd :
        if l == neededLetters : cpt += 1
    if min <= cpt <= max :
        #print("{} {} - {}".format(min, max, cpt))
        return 1
    else : return 0

def checkpwd_step_two(pos1, pos2, neededLetters, pwd) :
    if pwd[pos1 - 1] == neededLetters and pwd[pos2 - 1] == neededLetters : return 0
    elif pwd[pos1 - 1] == neededLetters or pwd[pos2 - 1] == neededLetters : return 1
    else : return 0

if __name__ == "__main__" :
    with open("input") as a :
        data = a.readlines()
        a.close()

    validPWD_one = 0
    validPWD_two = 0

    for i in data :
        sp = i.split()

        val1, val2 = sp[0].split("-")
        val1, val2 = int(val1), int(val2)
        neededLetters = sp[1].replace(":", "")
        pwd = sp[2]

        validPWD_one += checkpwd_step_one(val1, val2, neededLetters, pwd)
        validPWD_two += checkpwd_step_two(val1, val2, neededLetters, pwd)

    print(validPWD_one)
    print(validPWD_two)
