def reverse_list(l:list):
    """
    DONE: Reverse a list without using any built in functions
    The function should return a sorted list.
    Input l is a list which can contain any type of data.
    """
    return l[::-1]

def solve_sudoku(matrix):
    """
    DONE: Write a programme to solve 9x9 Sudoku board.
    Sudoku is one of the most popular puzzle games of all time. The goal of Sudoku is to fill a 9×9 grid with numbers so that each row, column and 3×3 section contain all of the digits between 1 and 9. As a logic puzzle, Sudoku is also an excellent brain game.
    The input matrix is a 9x9 matrix. You need to write a program to solve it.
    NOTE for matrix demo is like a list included 9 list which there is 9 nums in each. for unknown num use 0 instead.
    """
    def matrix_valid_check(matrix,row,col,num):
        # row check
        for i in range(9):
            if matrix[row][i] == num:
                return False
        # columns check
        for i in range(9):
            if matrix[i][col] == num:
                return False
        # 3*3 check
            temp_row = 3 * (row//3)
            temp_col = 3 * (col//3)
        for i in range(3):
            for j in range(3):
                if matrix[temp_row+i][temp_col+j] == num:
                    return False
        return True
    def traceback(matrix,row,col):
        if col == 9:
            return traceback(matrix,row + 1, 0)
        if row == 9:
            return True
        if matrix[row][col] != 0:
            return traceback (matrix,row,col + 1)
        for num in range(1,10):
            if matrix_valid_check(matrix,row,col,num):
                matrix[row][col] = num
                if traceback(matrix,row,col +1):
                    return True
            matrix[row][col] = 0
        return False
    def display(matrix):
        for i in range(9):
            for j in range(9):
                print(matrix[i][j],end = " ")
            print()
    traceback(matrix,0,0)
    display(matrix)