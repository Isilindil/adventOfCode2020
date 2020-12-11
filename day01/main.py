#!/usr/bin/python

def part_one(a, b) : # Naive but work
    if a+b == 2020 :
        print("{}+{}=2020".format(a, b))
        print("{}*{}={}".format(a, b, a*b))

def part_two(a, b, c) : # Naive but work
    if a+b+c == 2020 :
        print("{}+{}+{}=2020".format(a, b, c))
        print("{}*{}*{}={}".format(a, b, c, a*b*c))

def detectNumbers(data, howManyToSum, requiredSum) : # try harder
    if howManyToSum == 0 or len(data) == 0 : return 0
    head = data[0]
    tail = data[1:]

    if howManyToSum == 1 and head == requiredSum : return head

    result = head * detectNumbers(tail, howManyToSum-1, requiredSum-head)
    if result != 0 : return result

    return detectNumbers(tail, howManyToSum, requiredSum)

if __name__ == "__main__" :
    with open("input") as a :
        data = a.readlines()
        a.close()

    maxVal = len(data)
    for i in range(maxVal) :
        data[i] = int(data[i])

    howManyToSum = 3
    requiredSum = 2020

    solution = detectNumbers(data, howManyToSum, requiredSum) # try harder
    print(solution)

    # Naive approach
    for i in range(maxVal) :
        a = int(data[i])
        for j in range(i+1, maxVal) :
            b = int(data[j])
            part_one(a, b)
            for k in range(j+1, maxVal) :
                c = int(data[k])
                part_two(a, b, c)
