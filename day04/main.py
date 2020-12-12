#!/usr/bin/python

import re

def check_byr(val) :
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if len(val) != 4 : return 0
    if 1920 <= int(val) <= 2002 : return 1
    return 0
def check_iyr(val) :
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    if len(val) != 4 : return 0
    if 2010 <= int(val) <= 2020 : return 1
    return 0
def check_eyr(val) :
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if len(val) != 4 : return 0
    if 2020 <= int(val) <= 2030 : return 1
    return 0
def check_hgt(val) :
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    cm_re = re.compile(r"\d+cm$")
    in_re = re.compile(r"\d+in$")
    return 0
def check_hcl(val) :
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    hcl_re = re.compile(r"^#(\d|[a-f]){6}$")
    if hcl_re.search(val) : return 1
    return 0
def check_ecl(val) :
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    if val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] : return 1
    return 0
def check_pid(val) :
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    pid_re = re.compile(r"^\d{9}$")
    if pid_re.search(val) : return 1
    return 0

#cid (Country ID) - ignored, missing or not.

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

    func_dic = {'byr' : check_byr,
                'iyr' : check_iyr,
                'eyr' : check_eyr,
                'hgt' : check_hgt,
                'hcl' : check_hcl,
                'ecl' : check_ecl,
                'pid' : check_pid }

    validPassport = 0

    # Part two
    for val in data :
        if not val : # new passport
            if 0 not in allField.values() : validPassport += 1
            for k in allField.keys() : allField[k] = 0

        else : # reading passport
            sp = val.split()
            for kv in sp :
                k,v = kv.split(':')
                try: allField[k] += func_dic[k](v)
                except KeyError: pass

    else : # last passport
        print(allField)
        if 0 not in allField.values(): validPassport += 1
        for k in allField.keys(): allField[k] = 0

    print(validPassport)

    exit()

    # Part one
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
