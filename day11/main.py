#!/usr/bin/python

def check_occupied_in_view(matrix_a, start_row, start_col, step_row, step_col) :
    max_row = len(matrix_a)
    max_col = len(matrix_a[start_row])
    move_row = step_row
    move_col = step_col
    while 0 <= start_row+move_row < max_row and 0 <= start_col+move_col < max_col :
        if matrix_a[start_row+move_row][start_col+move_col] == "L" :
            return 0
        elif matrix_a[start_row+move_row][start_col+move_col] == "#" :
            return 1
        else :
            move_row += step_row
            move_col += step_col
    return 0

def check_occupied_adjacent(matrix_a, start_row, start_col, step_row, step_col) :
    max_row = len(matrix_a)
    max_col = len(matrix_a[start_row])
    if 0 <= start_row+step_row < max_row and 0 <= start_col+step_col < max_col :
        if matrix_a[start_row+step_row][start_col+step_col] == "L" :
            return 0
        elif matrix_a[start_row+step_row][start_col+step_col] == "#" :
            return 1
    return 0


def change_seat_in_view(matrix_a) :
    matrix_b = []
    nbr_of_row = len(matrix_a)
    for row in range(nbr_of_row):
        nbr_of_col = len(matrix_a[row])
        matrix_b.append('')
        for col in range(nbr_of_col):
            if matrix_a[row][col] == '.':
                matrix_b[row] += '.'  # If floor, stay floor
            else:
                nbr_of_occupied_around = 0
                for step_row, step_col in [(-1, -1), (-1, 0), (-1, +1), (0, -1), (0, +1), (+1, -1), (+1, 0), (+1, +1)] :
                    nbr_of_occupied_around += check_occupied_in_view(matrix_a, row, col, step_row, step_col)
                    #nbr_of_occupied_around += check_occupied_adjacent(matrix_a, row, col, step_row, step_col)

                if matrix_a[row][col] == 'L' and nbr_of_occupied_around == 0:
                    matrix_b[row] += '#'
                elif matrix_a[row][col] == '#' and nbr_of_occupied_around >= 5:
                    matrix_b[row] += 'L'
                else:
                    matrix_b[row] += matrix_a[row][col]
    return matrix_b


def check_seat_occupied(matrix_a) :
    occupied_seat = 0
    for row in matrix_a :
        for col in range(len(row)) :
            if row[col] == '#' :
                occupied_seat += 1
    return occupied_seat


def change_seat_adjacent(matrix_a) :
    # If a seat is empty(L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    # If a seat is occupied(#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    # Otherwise, the seat's state does not change.
    matrix_b = []
    nbr_of_row = len(matrix_a)
    for row in range(nbr_of_row) :
        nbr_of_col = len(matrix_a[row])
        matrix_b.append('')
        for col in range(nbr_of_col) :
            if matrix_a[row][col] == '.' :
                matrix_b[row] += '.'  # If floor, stay floor
            else :
                row_to_check_start = row - 1 if row - 1 > 0 else 0
                row_to_check_end = row + 2 if row + 2 <= nbr_of_row else nbr_of_row
                col_to_check_start = col - 1 if col - 1 > 0 else 0
                col_to_check_end = col + 2 if col + 2 <= nbr_of_col else nbr_of_col
                nbr_of_occupied_around = 0
                for rowCheck in range(row_to_check_start, row_to_check_end) :
                    for colCheck in range(col_to_check_start, col_to_check_end) :
                        if not (rowCheck == row and colCheck == col) :
                            nbr_of_occupied_around += 1 if matrix_a[rowCheck][colCheck] == '#' else 0
                if matrix_a[row][col] == 'L' and nbr_of_occupied_around == 0 :
                    matrix_b[row] += '#'
                elif matrix_a[row][col] == '#' and nbr_of_occupied_around >= 4 :
                    matrix_b[row] += 'L'
                else :
                    matrix_b[row] += matrix_a[row][col]
    return matrix_b


if __name__ == "__main__" :
    with open("input") as a :
        data = a.read().split("\n")
    a.close()

    # part one
    matrixA = list(data)
    step = 0
    while True :
        matrixB = change_seat_adjacent(matrixA)
        #matrixB = change_seat_in_view(matrixA)
        if matrixA == matrixB :
            print("step : {}".format(step))
            print("occupied seats : {}".format(check_seat_occupied(matrixA)))
            break
        else :
            matrixA = matrixB
            step += 1

    # part two
    matrixA = list(data)
    step = 0
    while True :
        matrixB = change_seat_in_view(matrixA)
        if matrixA == matrixB :
            print("step : {}".format(step))
            print("occupied seats : {}".format(check_seat_occupied(matrixA)))
            break
        else :
            matrixA = matrixB
            step += 1
