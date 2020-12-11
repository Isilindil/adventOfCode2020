#!/usr/bin/python

if __name__ == "__main__" :
    with open("input") as a :
        data = a.readlines()
        a.close()

    for i in range(len(data)) :
        a = int(data[i])
        for j in range(i,len(data)) :
            b = int(data[j])
            if a+b == 2020 :
                print("{}+{}=2020".format(a, b))
                print("{}*{}={}".format(a, b, a*b))

