import numpy as np 

arr = np.random.randint(0, 100, (6, 6))
print(arr)

# sum of each col
sumCol = np.sum(arr, axis=0)
print(sumCol)

#max in each row
maxInRow = np.max(arr, axis=1)
print(maxInRow)

#reple val if < 50 wiht -1
rep50 = np.where(arr<50,-1, arr)
print(rep50)