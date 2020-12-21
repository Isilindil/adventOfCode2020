#!/usr/bin/python

import re

if __name__ == "__main__":
    with open("input") as a:
        data = a.read().split("\n")
    a.close()

    digit_re = re.compile(r"\d+")

    # Part One
    mem = {}
    mask = ""
    for l in data:
        k, v = l.split("=")
        k = k.replace(" ", "")
        if k == "mask":
            mask = v.strip()
            # print(mask, " - mask")
        else:
            index = digit_re.search(k).group()
            bin_v = format(int(v), '036b')
            # print(bin_v)
            new_bin_v = ""
            for i in range(36):
                if mask[i] == 'X':
                    new_bin_v += bin_v[i]
                else:
                    new_bin_v += mask[i]
            # print(new_bin_v)
            new_int_v = int(new_bin_v, 2)
            mem[index] = new_int_v
            # print(new_int_v)

    mem_sum = 0
    for k in mem.keys():
        mem_sum += mem[k]
    print("Sum after mask: ", mem_sum)

    # Part Two
    mem = {}
    mask = ""
    for l in data:
        k, v = l.split("=")
        k = k.replace(" ", "")
        if k == "mask":
            mask = v.strip()
        else:
            v = int(v)
            index_int = int(digit_re.search(k).group())
            index_bin = format(index_int, '036b')
            new_index_bin = [""]
            for i in range(36):
                if mask[i] == '0':
                    for j, val in enumerate(new_index_bin):
                        new_index_bin[j] += index_bin[i]
                elif mask[i] == '1':
                    for j, val in enumerate(new_index_bin):
                        new_index_bin[j] += '1'
                elif mask[i] == 'X':
                    new_list = []
                    for val in new_index_bin:
                        new_list.append(val+'0')
                        new_list.append(val+'1')
                    new_index_bin = list(new_list)
                else:
                    exit(f"Error in mask: {mask}")

            for index in new_index_bin:
                mem[int(index, 2)] = v
            # print(new_int_v)

    mem_sum = 0
    for k in mem.keys():
        mem_sum += mem[k]
    print("Sum after mask: ", mem_sum)
