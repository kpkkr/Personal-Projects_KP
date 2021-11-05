def solver(bo):
    find = find_void(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if validity(bo, i, (row, col)):
            bo[row][col] = i

            if solver(bo):
                return True

            bo[row][col] = 0

    return False

def validity(bo, num, pos):
    # check row
    for i in range(len(bo)):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # check box
    xbox = pos[1] // 3
    ybox = pos[0] // 3
    for i in range(ybox*3, ybox*3 + 3):
        for j in range(xbox*3, xbox*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def print_puzzle(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - ')

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print('|' , end = '')

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + ' ', end = '')  

def find_void(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    
    return None
