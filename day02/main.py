#!/usr/bin/python

if __name__ == "__main__" :
    with open("input") as a :
        data = a.readlines()
        a.close()
    for i in data :
        print(i)
print("done")
