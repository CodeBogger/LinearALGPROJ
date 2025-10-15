import math
from functools import reduce

def valid_column(current_col, row, aug_matrix):
    # sometimes, columns may not take the form of a perfect RREF, merely check if a column has a valid pivot pos in echelon form
    for j in range(row+1):
        # check whether there are nonzeros below the diaganol position
        if j > current_col and aug_matrix[current_col][j] != 0:
            return False
    # return true / false based off if the column given is valid

def valid_pivot_pos(current_col, row, aug_matrix):
    # check if the current position is a valid pivot position
    for j in range(row+1):
        # check whether there are nonzeros below the diaganol position
        if j > current_col and aug_matrix[current_col][j] != 0:
            return False
    # check if there are any nonzeros to the left of the current position in the same row
    for j in range(current_col):
        if aug_matrix[j][row] != 0:
            return False
        
    return True

def valid_row(row_focus, list):
    # check if each ele is a nonzero or not, if it is, its considered valid
    for i in range(0, len(list)-1):
        if list[i][row_focus] != 0:
            return True
    # if all elements before the last ele is zero, then the system make be consistent with inf sol
    return list[len(list)-1][row_focus] == 0

def swap_leading_one_to_diagonal(aug_matrix, current_col):
    # If possible, swap a row with a leading 1 to the current diagonal position
    # Swap the leading zero rows towards the bottom of the matrix
    if current_col < len(aug_matrix[current_col]) and aug_matrix[current_col][current_col] != 1:
        for i in range(current_col+1, len(aug_matrix)):
            if aug_matrix[i][current_col] == 1:
                aug_matrix[i], aug_matrix[current_col] = aug_matrix[current_col], aug_matrix[i]
                break

def row_ify(aug_matrix, row):
    # since the augmented matrix is in column form, convert it to row form for easier manipulation
    temp = []
    for i in range(len(aug_matrix)):
        temp.append(aug_matrix[i][row])
    return temp

def swap_rows(aug_matrix, row1, row2):
    # swap two rows in the augmented matrix
    for i in range(len(aug_matrix)):
        temp = aug_matrix[i][row1]
        aug_matrix[i][row1] = aug_matrix[i][row2]
        aug_matrix[i][row2] = temp     

def RREF(aug_matrix):

    current_col = 0
    count = 0

    while current_col < len(aug_matrix)-1:
        
        count += 1
        # objective: find the best operation to apply in the current state of the matrix
        
        # 1. Check if a row could be simplified by a scalar for simplier operations, disregard if the row contains a diagnol leading 1
        for j in range(0, len(aug_matrix[current_col])):
            if j < len(aug_matrix) and aug_matrix[j][j] != 1:
                row = row_ify(aug_matrix, j)

                gcd = reduce(math.gcd, [int(abs(num)) for num in row if num != 0])
                gcd *= -1 if aug_matrix[j][j] < 0 else 1

                if gcd != 0 and gcd != 1:
                    for k in range(len(aug_matrix)):
                        aug_matrix[k][j] /= gcd
                
        # each index in the list represents the amount of nonzero elements below its column position
        nonzero_count_list = []
        nonzero_count_list.append(0)

        # initialize the nonzero count
        count = 1 if aug_matrix[current_col][len(aug_matrix[current_col])-1] != 0 else 0

        # we would not want to swap a row with a leading 1 in the diagonal position but also want to zeroify the rows above the diagnol position
        for j in range(len(aug_matrix[current_col])-2, -1, -1):
            nonzero_count_list.insert(0, count)
            count += 1 if aug_matrix[current_col][j] != 0 else 0
        
        for j in range(0, len(aug_matrix[current_col])):
            if nonzero_count_list[j] > 0 and (j == current_col and aug_matrix[current_col][j] == 0 or j != current_col) and aug_matrix[current_col][j] == 0:
                # we are on a position that needs to be zeroified
                # we will swap the rows with each other, adjusting the nonzero count list and count accordingly
                swap_position = -1

                # find a nonzero row position to swap with bottom up
                for k in range(len(aug_matrix)-1, j, -1):
                    if aug_matrix[k][j] != 0:
                        swap_position = k
                        break

                swap_rows(aug_matrix, swap_position, j)
                
                # adjust the nonzero count list
                for j in range(j, swap_position):
                    nonzero_count_list[j] -= 1

        
        # actual RREF operations
        # find a suitable operation to get the matrix closer to RREF
        
        
        current_col += 1
    
