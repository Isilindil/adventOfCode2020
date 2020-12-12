#!/usr/bin/python

def parse_instruction(instruction_list, index_max) :
    accumulator = 0
    current_index = 0
    while 1 :
        try : ins, value = instruction_list[current_index].split()
        except AttributeError : return ['loop', accumulator]
        except IndexError : return ['OK', accumulator]
        else :
            if ins == "acc" :
                instruction_list[current_index] = None
                accumulator += int(value)
                current_index += 1
            elif ins == "jmp" :
                instruction_list[current_index] = None
                current_index += int(value)
            elif ins == "nop" :
                instruction_list[current_index] = None
                current_index += 1
            else :
                break


if __name__ == "__main__" :
    with open("input") as a :
        data = a.read().split("\n")
    a.close()

    # Part Two
    last_modif = -1
    out = 'loop'
    while out == 'loop' :
        modif_data = list(data)
        if None in modif_data :
            ins, value = instruction_list[current_index].split()
            break
        for i in range(last_modif+1, len(modif_data)) :
            ins, value = modif_data[i].split()
            if ins == 'jmp' :
                modif_data[i] = modif_data[i].replace('jmp', 'nop')
                last_modif = i
                break
            elif ins == 'nop':
                modif_data[i] = modif_data[i].replace('nop', 'jmp')
                last_modif = i
                break
        else : break
        out, accumulator = parse_instruction(modif_data, len(data))
    print(out, " - ", accumulator)

    # Part One
    print(parse_instruction(data, len(data))[1])
