# This is the sample example
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# To change a specific element:
matrix[1][2] = 10  # Changes the element in the second row, third column
print(matrix)

# To change a subarray (row):
matrix[0] = [10, 11, 12]  # Replaces the entire first row
print(matrix)

# To change specific elements in a subarray:
matrix[2][0:2] = [20, 21]  # Changes the first two elements of the third row
print(matrix)
