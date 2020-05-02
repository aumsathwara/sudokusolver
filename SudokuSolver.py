#BOARD is array of 9x9 sudoku
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
#This Function represnts BOARD into Tabular Form
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            #To present visible division in Tabular Form
            print("- - - - - - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")
#This function is to find "0"(s) in Sudoku 
def find_empty(bo):
    #To find "0"(s) in vertical coulomn (Whole sets of 9 arrays)
    for i in range(len(bo)):
        #To find "0"(s) in horizontal row (Inside those 9 arryas)
        for j in range(len(bo[0])):
            #board[coulomn][row] == 0
            if bo[i][j] == 0:
                return (i,j)
    return None
#This function is used to check wether the solution enterred is correct or not
def valid(bo, num , pos ):

    #Check Row
    for i in range(len(bo[0])):
        #To check if the number entered is not in the same row     
        #board[pos[0]][i], pos[0] represents left most Row of Sudoku.
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    #Check Column
    for i in range(len(bo)):
        #To check if the number entered is not in the same column     
        #board[i][pos[0]], pos[0] represents left most column of Sudoku.
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    #Check Box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y *3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False


    return True
#This function is used to find Solution by using function empty and valid...
def solve(bo):
    find = find_empty(bo)
    #If value is not empty...
    if not find:
        #To end loop
        return True
    else:
        #To check again
        row, col = find

    #To check possible answers from 1 to 9
    for i in range(1,10):
        #Calling valid function with Board,num=i(1 to 9), and pos =(row, coulmn)
        if valid(bo, i, (row, col)):
            bo[row][col] = i
        #Solution Generator
            if solve(bo):
                return True
        #Backtracking,Making value of previous entered incorrect value back to 0 
            bo[row][col] = 0

    return False
print_board(board)
print("_________________________________")
solve(board)
print("_________________________________")
print_board(board)
