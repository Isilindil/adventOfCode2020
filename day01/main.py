#!/usr/bin/python

def part_one(a, b) :
    if a+b == 2020 :
        print("{}+{}=2020".format(a, b))
        print("{}*{}={}".format(a, b, a*b))

def part_two(a, b, c) :
    if a+b+c == 2020 :
        print("{}+{}+{}=2020".format(a, b, c))
        print("{}*{}*{}={}".format(a, b, c, a*b*c))

if __name__ == "__main__" :
    with open("input") as a :
        data = a.readlines()
        a.close()

    maxVal = len(data)
    for i in range(maxVal) :
        a = int(data[i])
        for j in range(i, maxVal) :
            b = int(data[j])
            part_one(a, b)
            for k in range(j, maxVal) :
                c = int(data[k])
                part_two(a, b, c)


