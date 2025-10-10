def valid_column(column_focus, row_focus, list):

    for j in range(0, row_focus+1):
        if j == column_focus:
            if list[column_focus][j] != 1:
                return False
        elif list[column_focus][j] != 0:
            return False
    return True
    # return true / false based off if the column given is valid

def valid_row(row_focus, list):
    for i in range(0, len(list)-1):
        if list[i][row_focus] != 0:
            return True
    return False

def decimal_count(n1, n2):
    str1 = str(n1 / n2).split('.')
    return int(str1[1])

def RREF(list):

    column_focus = 0
    row_focus = len(list[column_focus]) - 1

    while True:
        # check if the matrix is in RREF
        if list[column_focus][row_focus] != 0:

            if column_focus == row_focus:

                print(f'Now dividing everything in row {row_focus+1} by {list[column_focus][row_focus]:.2f} to achieve the diagnol one RREF form.')
                for i in range(0, len(list)):

                    # diagnol position case
                    list[i][row_focus] /= list[column_focus][row_focus]

            else:
                # if possible, simplify a row if they share a common divisor
                for j in range(0, len(list[column_focus])):
                    # each j represents the jth index in each individual array that represents a column vector
                    # loop thru each column vector

                    row = []

                    for i in range(0, len(list)):
                        row.append(list[i][j])
                
                    gcd = max(row)
                    while gcd > 0:
            
                        for num in row:
                            if num % gcd != 0:
                                gcd -= 1
                                break
                        else:
                            for i in range(0, len(list)):
                                # found a gcd that perfectly divides, so apply the operation
                                list[i][j] = int(list[i][j] / gcd)
                            break
                # if gcd turns out to be 0, it means that there is no gcd among the row


            # compute RREF operation, usual multiplication, addition, substracting logic

                current = list[column_focus][row_focus]
                divisor = None

                # gets the decimal space count for either dividing cur / div or visa versa
                curr_decimal_count = -1 # large number so the first number is chosen (if not 0) to avoid div by 0

            # keep track of the row to apply operations
                row = 0

                for j in range(0, len(list[column_focus])):

                    if j == row_focus or list[column_focus][j] == 0:
                        continue
                
                    temp = decimal_count(current, list[column_focus][j])
                
                    if divisor == None or temp <= curr_decimal_count:
                        if temp == curr_decimal_count:
                            if current - list[column_focus][j] > current - divisor:
                                divisor = list[column_focus][j]
                                row = j
                        else:
                            curr_decimal_count = temp
                            divisor = list[column_focus][j]
                            row = j

                # rank based off size in difference and number of decimal places

                # actual operation applied
                if divisor != None:
                    
                    # gets the multiplier of current / divisor to apply standard subtraction row operation multiplier*list[i]["row of where the suitable number was found"]
                    multiplier = current / divisor

                    print(f'R{row_focus+1} -> R{row_focus+1} - {multiplier:.2f}R{row+1}')
                    for i in range(0, len(list)):
                        list[i][row_focus] -= multiplier * list[i][row]
                
            
            # check if the row became inconsistent, determine if its infinite sol or not
            if valid_row(row_focus, list) == False:
                
                if list[len(list)-1][row_focus] == 0:
                    print(f'Infinite solutions for row {row_focus+1}!')
                else:
                    print(f'Inconsistent solution! {list[len(list)-1][row_focus]} != 0!')

                return False
                
            # update column focus if needed
            if valid_column(column_focus, row_focus, list):
                column_focus += 1

                # check if last row is finally traversed over, if so, the system is consistent

                if column_focus == len(list)-1:
                    print('The system is consistent')
                    return True
            
                row_focus = len(list[column_focus])
        row_focus -= 1
    
        
        

