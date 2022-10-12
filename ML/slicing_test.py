import numpy as np

arr1 = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
[11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
[21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
[31, 32, 33, 34, 35, 36, 37, 38, 39, 40]]

print(arr1)

arr2 = [arr1[0][2:9], arr1[1][2:9]]

print(arr2)

arr3 = []

for i in range(0, 40):
    arr3.append(i+1)

print(arr3)

arr4 = np.zeros((4, 10))

print(arr4)

for i in range(0, 4):
    for j in range(0, 10):
        arr4[i][j] = arr3[i*10 + j]

print(arr4)

arr5 = np.zeros((4, 8))

for i in range(0, 4):
    for j in range(0, 8):
        arr5[i][j] = arr3[i*10 + j + 2]

print(arr5)

arr6 = np.zeros((4, 1))



for i in range(0, 4):        
    arr6[i][0] = arr3[i*10 + 9]


print(arr6)