#!/usr/bin/python

#byr (Birth Year)
#iyr (Issue Year)
#eyr (Expiration Year)
#hgt (Height)
#hcl (Hair Color)
#ecl (Eye Color)
#pid (Passport ID)
#cid (Country ID) # Optionnal

if __name__ == "__main__" :
    with open("input") as a :
        data = a.read().split("\n")
        a.close()

    allField = {'byr' : 0,
                'iyr' : 0,
                'eyr' : 0,
                'hgt' : 0,
                'hcl' : 0,
                'ecl' : 0,
                'pid' : 0 }

    validPassport = 0

    for val in data :
        if not val : # new passport
            print(allField)
            if 0 not in allField.values() : validPassport += 1
            for k in allField.keys() : allField[k] = 0

        else : # reading passport
            sp = val.split()
            for kv in sp :
                k,v = kv.split(':')
                try : allField[k] += 1
                except KeyError : pass
    else : # last passport
        print(allField)
        if 0 not in allField.values(): validPassport += 1
        for k in allField.keys(): allField[k] = 0

    print(validPassport)
