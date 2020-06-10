SIZE = 9
SUB_SIZE = 3
sudoku = [9*[0]]
p = 1
while p != 9:
    sudoku.append (9*[0])
    p += 1

def printSudoku():
    for x in sudoku:
        print("-------------------------------------")
        for y in x:
            print("|", y,end = " ")
        print("| ")
    print("-------------------------------------")
#-------
row = int(input("Enter the row \n"))
while row > 8 or row < 0:
    row = int(input("Enter a valid row number(between 0-8) \n"))
    
col = int(input("Enter the column \n"))
while col > 8 or col < 0:
    col = int(input("Enter a valid column number(between 0-8) \n"))
    
val = int(input("Enter the value \n"))
while val > 9 or val < 1:
    val = int(input("Enter a valid value(between 1-9) \n"))
    
sudoku[row][col] = val

while row != -1:
    row = int(input("Enter the row \n"))
    while row > 8 or row < -1:
        row = int(input("Enter a valid row number(between 0-8) \n"))
    col = int(input("Enter the column \n"))
    while col > 8 or col < 0:
        col = int(input("Enter a valid column number(between 0-8) \n"))   
    val = int(input("Enter the value \n"))
    while val > 9 or val < 0:
        val = int(input("Enter a valid value(between 1-9) \n"))
        
    sudoku[row][col] = val
    
printSudoku()

def isAvailable(row, col, num):
    
    rowStart = int(int(row/3) * 3);
    colStart = int(int(col/3) * 3);
    i = 0
    while(i<9):
        if (sudoku[row][i] == num):
            return False
        if (sudoku[i][col] == num):
            return False
        if (sudoku[int(rowStart + (i%3))][int(colStart + (i/3))] == num):
            return False
        
        i = i+1
    return True;
#--------------------

def fillSudoku(row, col):

    if(row<9 and col<9):
        
        if(sudoku[row][col] != 0):
            
            if((col+1)<9):
                return fillSudoku(row, col+1)
            elif((row+1)<9):
                return fillSudoku(row+1, 0)
            else:
                return True
        else:
            i = 0
            while(i<9):
                if(isAvailable(row, col, i+1)):
                    sudoku[row][col] = i+1
                    if((col+1)<9):
                        if(fillSudoku(row, col +1)):
                            return True
                        else :
                            sudoku[row][col] = 0
                    elif((row+1)<9):
                        if(fillSudoku(row+1, 0)):
                            return True;
                        else:
                            sudoku[row][col] = 0
                    else :
                        return True;
                i = i+1
        return False;
    else:
        return True;
#-------------------
        
if (fillSudoku(0, 0)) : 
    print ("\n\nSolution is \n")
    printSudoku()

else :
    print("\n\nNO SOLUTION\n\n")
