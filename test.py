print("niv amelhe")


# Algo to solve rubix cube

# 1. Create a 3x3x3 matrix
# 2. Create a function to rotate the matrix
# 3. Create a function to rotate the matrix in a specific direction
# 4. Create a function to rotate the matrix in a specific direction and a specific number of times
# 5. Create a function to rotate the matrix in a specific direction and a specific number of times and a specific layer
# 6. Create a function to rotate the matrix in a specific direction and a specific number of times and a specific layer and a specific row
# 7. Create a function to rotate the matrix in a specific direction and a specific number of times and a specific layer and a specific row and a specific column

def create_matrix():
    matrix = []
    for i in range(3):
        row = []
        for j in range(3):
            column = []
            for k in range(3):
                column.append(0)
            row.append(column)
        matrix.append(row)
    return matrix

def rotate_matrix(matrix):
    new_matrix = create_matrix()
    for i in range(3):
        for j in range(3):
            for k in range(3):
                new_matrix[i][j][k] = matrix[k][j][i]
    return new_matrix


def rotate_matrix_in_direction(matrix, direction):
    