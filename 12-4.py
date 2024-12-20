data = open('data/12-4.txt', 'r').read().strip().split('\n')

## part 1 ##

def check_valid_xmas(r1, c1, r2, c2, r3, c3):
    return data[r1][c1] == 'M' and data[r2][c2] == 'A' and data[r3][c3] == 'S'

def find_xmas(x_row, x_col):
    count = 0
    ## case 1
    upper_indices = list(range(x_row-3, x_row))
    lower_indices = list(range(x_row+1, x_row+4))

    left_indices = list(range(x_col-3, x_col))
    right_indices = list(range(x_col+1, x_col+4))

    upper_valid = all(map(lambda x : x >= 0, upper_indices))
    lower_valid = all(map(lambda x : x <= len(data) - 1, lower_indices))

    left_valid = all(map(lambda x : x >= 0, left_indices))
    right_valid = all(map(lambda x : x <= len(data[0]) - 1, right_indices))

    if upper_valid:
        ut, uo, uz = upper_indices
        if left_valid:
            lt, lo, lz = left_indices
            count += check_valid_xmas(uz, lz, uo, lo, ut, lt)
        
        count += check_valid_xmas(uz, x_col, uo, x_col, ut, x_col)

        if right_valid:
            rz, ro, rt = right_indices
            count += check_valid_xmas(uz, rz, uo, ro, ut, rt)
    
    if left_valid:
        lt, lo, lz = left_indices
        count += check_valid_xmas(x_row, lz, x_row, lo, x_row, lt)

    if right_valid:
        rz, ro, rt = right_indices
        count += check_valid_xmas(x_row, rz, x_row, ro, x_row, rt)

    if lower_valid:
        lwz, lwo, lwt = lower_indices
        if left_valid:
            lt, lo, lz = left_indices
            count += check_valid_xmas(lwz, lz, lwo, lo, lwt, lt)
        
        count += check_valid_xmas(lwz, x_col, lwo, x_col, lwt, x_col)

        if right_valid:
            rz, ro, rt = right_indices
            count += check_valid_xmas(lwz, rz, lwo, ro, lwt, rt)

    return count


xmas_count = 0
for row in range(len(data)):
    for col in range(len(data[0])):
        if data[row][col]=='X' : xmas_count+=find_xmas(row, col)

print(xmas_count)

## part 2 ##
def find_real_xmas(a_row, a_col):
    a_left, a_right = a_col - 1, a_col + 1
    a_bottom, a_top = a_row + 1, a_row - 1

    if a_left >= 0 and a_top >= 0 and a_right <= len(data[0]) - 1 and a_bottom <= len(data) - 1:
        l = [data[a_top][a_left], data[a_top][a_right], data[a_bottom][a_left], data[a_bottom][a_right]]
        
        return ((l[0] == 'S' and l[1] == 'S' and l[2] == 'M' and l[3] == 'M') or
                (l[0] == 'S' and l[1] == 'M' and l[2] == 'S' and l[3] == 'M') or
                (l[0] == 'M' and l[1] == 'M' and l[2] == 'S' and l[3] == 'S') or
                (l[0] == 'M' and l[1] == 'S' and l[2] == 'M' and l[3] == 'S'))

    return False

real_xmas_count = 0
for row in range(len(data)):
    for col in range(len(data[0])):
        if data[row][col]=='A' : real_xmas_count+=find_real_xmas(row, col)

print(real_xmas_count)