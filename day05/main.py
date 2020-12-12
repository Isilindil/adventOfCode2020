#!/usr/bin/python

def seat(coord_code, coord_authorized) :
    if len(coord_authorized) == 1 : return coord_authorized
    code = coord_code[0]
    code_tail = coord_code[1:]
    if code == "F" :
        return seat(code_tail, coord_authorized[:len(coord_authorized)//2])
    elif code == "B" :
        return seat(code_tail, coord_authorized[len(coord_authorized)//2:])
    elif code == "L" :
        return seat(code_tail, coord_authorized[:len(coord_authorized)//2])
    elif code == "R" :
        return seat(code_tail, coord_authorized[len(coord_authorized)//2:])


if __name__ == "__main__" :
    with open("input") as a :
        data = a.read().split("\n")
    a.close()

    row = range(128)
    column = range(8)

    max_seat_ID = 0
    all_seat_ID = []

    for coord in data :
        row_coord = coord[:7]
        col_coord = coord[7:]

        row_val = int(seat(row_coord, row)[0])
        col_val = int(seat(col_coord, column)[0])

        max_seat_ID = max(max_seat_ID, row_val*8+col_val)
        all_seat_ID.append(row_val*8+col_val)

    print("highest seat : {}".format(max_seat_ID))
    all_seat_ID.sort()
    #print(all_seat_ID)

    for s in range(len(all_seat_ID)-1) :
        if all_seat_ID[s+1]-all_seat_ID[s] != 1 :
            print("Your seat : {}".format(all_seat_ID[s+1]-1))
