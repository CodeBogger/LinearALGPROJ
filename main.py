import logic
import random

test = []
col_size = random.randint(3,6)

for i in range(4):
    col = []
    for j in range(col_size):
        col.append(random.randint(0,9))
    test.append(col)

logic.RREF(test)
print(test)

