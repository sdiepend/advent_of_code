N, E, S, W = (-1, 0), (0, 1), (1, 0), (0,-1)
turn_left = {S: E, E: N, N: W, W: S}

def spiral(width, height):
    if width < 1 or height < 1:
        print('Invalid matrix size, smaller than 1')
    x, y = height // 2, width // 2 #Start in the center
    dx, dy = S
    matrix = [[None] * width for _ in range(height)]
    matrix[x][y] = 1
    while True:
        next_dx, next_dy = turn_left[dx, dy]
        next_x, next_y = x + next_dx, y + next_dy
        if (0 <= next_x < height and 0 <= next_y < width and matrix[next_x][next_y] is None):
            x, y = next_x, next_y
            dx, dy = next_dx, next_dy
        else:
            x, y = x + dx, y + dy
            if not (0 <= x < height and 0 <= y < width):
                return matrix

        matrix[x][y] = check_none(matrix, x - 1, y) + check_none(matrix, x, y - 1)\
        + check_none(matrix, x + 1, y) + check_none(matrix, x, y + 1)\
        + check_none(matrix, x - 1, y - 1) + check_none(matrix, x + 1, y + 1)\
        + check_none(matrix, x - 1, y + 1) + check_none(matrix, x + 1, y - 1)

        if matrix[x][y] > 325489:
            print(matrix[x][y])

def check_none(matrix, x, y):
    if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] is not None :
        return matrix[x][y]
    else:
        return 0


def print_matrix(matrix):
    for row in matrix:
        print(row)
    
print_matrix(spiral(9,9))
