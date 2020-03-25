# Board initialisation
board = [[1, 0, 6, 0, 0, 2, 3, 0, 0],
         [0, 5, 0, 0, 0, 6, 0, 9, 1],
         [0, 0, 9, 5, 0, 1, 4, 6, 2],
         [0, 3, 7, 9, 0, 5, 0, 0, 0],
         [5, 8, 1, 0, 2, 7, 9, 0, 0],
         [0, 0, 0, 4, 0, 8, 1, 5, 7],
         [0, 0, 0, 2, 6, 0, 5, 4, 0],
         [0, 0, 4, 1, 5, 0, 6, 0, 9],
         [9, 0, 0, 8, 7, 4, 2, 1, 0]]

""" Main solve function  """


def solve(board):
    empty = find_empty(board)
    if len(empty) == 0:
        return True

    for j in range(1, len(board) + 1):

        if is_Valid(empty[0], j) == -1:
            continue
        board[empty[0][1]][empty[0][0]] = j

        if solve(board):
            return True
        board[empty[0][1]][empty[0][0]] = 0

    return False


"""                                 """

"""     Constraint check function   """


def is_Valid(position, val):
    check = 0
    for i in range(0, 9):

        if val == board[position[1]][i]:
            check = -1
        if val == board[i][position[0]]:
            check = -1
        if checkSquare(val, position[0], position[1]) == -1:
            check = -1

    return check


# specialised function to check the 3x3 square constraint
def checkSquare(val, x, y):
    origin_x = x - (x % 3)
    origin_y = y - (y % 3)
    x = 0
    y = 0
    for i in range(3):
        x = origin_x + i
        for j in range(3):
            y = origin_y + j
            if board[y][x] == val:
                return -1
    return 1


"""                                                             """

"""     Function to find all the empty spaces on the board      """


def find_empty(b):
    empty = []
    x = 0
    y = 0

    for i in b:
        x = 0

        for j in i:
            if j == 0:
                empty.append([x, y])
            x += 1

        y += 1

    return empty


"""     Main     """
solve(board)

# Print a formated version of the board once it's finished
for i in range(0, len(board)):
    print(board[i])
