import logic
import random

test = [[2, 0, 0, 4], [4, 0, 0, 8], [6, 0, 0, 12], [8, 2, 2, 16]]

"""
col_size = random.randint(3,6)

for i in range(4):
    col = []
    for j in range(col_size):
        col.append(random.randint(0,9))
    test.append(col)

"""
print(test)
logic.RREF(test)
print(test)

