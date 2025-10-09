def valid_column(column_focus, row_focus, list):

    for j in range(0, row_focus+1):
        if j == column_focus:
            if list[column_focus][j] != 1:
                return False
        elif list[column_focus][j] != 0:
            return False
        
    return True
    # return true / false based off if the column given is valid

def decimal_count(n1, n2):
    str1 = str(n1 / n2).split('.')
    str2 = str(n2 / n1).split('.')

    return min(int(str1[1]), int(str2[1]))

def RREF(list):

    column_focus = 0
    row_focus = len(list[column_focus]) - 1

    while True:
        # check if the matrix is in RREF

        print("in da while loop")
        if column_focus == len(list) - 1 and valid_column(column_focus, row_focus, list):
            print("That shi consistent")
            break
            
        elif list[column_focus][row_focus] != 0:
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
            curr_decimal_count = 1001 # abitrary large number so the first number is chosen (if not 0) to avoid div by 0

            # keep track of the row to apply operations
            row = 0

            for j in range(0, len(list[column_focus])):

                if j == row_focus or list[column_focus][j] == 0:
                    print('skipping, row focus matching with current loop idx: ',{j==row_focus},' the current idx is ',j,' and row focus = ',row_focus)
                    continue
                
                temp = decimal_count(current, list[column_focus][j])
                print('the smallest decimal count between ',current,' and ',list[column_focus][j],' is ',temp)
                
                if temp <= curr_decimal_count:
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
                print('found operation to be applied, the row to apply the operation to is row ',j,', with the number ',divisor)

            # update column focus if needed
            if valid_column(column_focus, row_focus, list):
                column_focus += 1
                row_focus = len(list[column_focus]) - 1
        
        row_focus -= 1
        
        

