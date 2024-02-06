

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [2, 4, 6],
    [8, 10, 12],
    [14, 16, 18]
]

sum_matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for row in range(len(matrix1)):
    for col in range(len(matrix1[row])):
        sum_matrix[row][col] = matrix1[row][col] + matrix2[row][col]

for sum in sum_matrix:
    print(sum)