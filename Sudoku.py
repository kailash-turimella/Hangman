"""
Enter the row, column(both starting from 0) and value of boxes that are already filled.
Enter the row as -1 when finished.
"""
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

row = 0
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
    
if (fillSudoku(0, 0)) : 
    print ("\n\nSolution is \n")
    printSudoku()

else :
    print("\n\nNO SOLUTION\n\n")
"""
EXAMPLE:

Python 3.6.8 (v3.6.8:3c6b436a57, Dec 24 2018, 02:04:31) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
Enter the row 
0
Enter the column 
0
Enter the value 
5
Enter the row 
0
Enter the column 
1
Enter the value 
3
Enter the row 
0
Enter the column 
4
Enter the value 
7
Enter the row 
1
Enter the column 
0
Enter the value 
6
Enter the row 
1
Enter the column 
3
Enter the value 
1
Enter the row 
1
Enter the column 
4
Enter the value 
9
Enter the row 
1
Enter the column 
5
Enter the value 
5
Enter the row 
2
Enter the column 
1
Enter the value 
9
Enter the row 
2
Enter the column 
2
Enter the value 
8
Enter the row 
2
Enter the column 
7
Enter the value 
6
Enter the row 
3
Enter the column 
0
Enter the value 
8
Enter the row 
3
Enter the column 
4
Enter the value 
6
Enter the row 
3
Enter the column 
8
Enter the value 
3
Enter the row 
4
Enter the column 
0
Enter the value 
4
Enter the row 
4
Enter the column 
3
Enter the value 
8
Enter the row 
4
Enter the column 
5
Enter the value 
3
Enter the row 
4
Enter the column 
8
Enter the value 
1
Enter the row 
5
Enter the column 
0
Enter the value 
7
Enter the row 
5
Enter the column 
4
Enter the value 
2
Enter the row 
5
Enter the column 
8
Enter the value 
6
Enter the row 
6
Enter the column 
1
Enter the value 
6
Enter the row 
6
Enter the column 
6
Enter the value 
2
Enter the row 
6
Enter the column 
7
Enter the value 
8
Enter the row 
7
Enter the column 
3
Enter the value 
4
Enter the row 
7
Enter the column 
4
Enter the value 
1
Enter the row 
7
Enter the column 
5
Enter the value 
9
Enter the row 
7
Enter the column 
8
Enter the value 
5
Enter the row 
8
Enter the column 
4
Enter the value 
8
Enter the row 
8
Enter the column 
7
Enter the value 
7
Enter the row 
8
Enter the column 
8
Enter the value 
9
Enter the row 
-1
Enter the column 
0
Enter the value 
0
-------------------------------------
| 5 | 3 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 
-------------------------------------
| 6 | 0 | 0 | 1 | 9 | 5 | 0 | 0 | 0 | 
-------------------------------------
| 0 | 9 | 8 | 0 | 0 | 0 | 0 | 6 | 0 | 
-------------------------------------
| 8 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 3 | 
-------------------------------------
| 4 | 0 | 0 | 8 | 0 | 3 | 0 | 0 | 1 | 
-------------------------------------
| 7 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 6 | 
-------------------------------------
| 0 | 6 | 0 | 0 | 0 | 0 | 2 | 8 | 0 | 
-------------------------------------
| 0 | 0 | 0 | 4 | 1 | 9 | 0 | 0 | 5 | 
-------------------------------------
| 0 | 0 | 0 | 0 | 8 | 0 | 0 | 7 | 9 | 
-------------------------------------


Solution is 

-------------------------------------
| 5 | 3 | 4 | 6 | 7 | 8 | 9 | 1 | 2 | 
-------------------------------------
| 6 | 7 | 2 | 1 | 9 | 5 | 3 | 4 | 8 | 
-------------------------------------
| 1 | 9 | 8 | 3 | 4 | 2 | 5 | 6 | 7 | 
-------------------------------------
| 8 | 5 | 9 | 7 | 6 | 1 | 4 | 2 | 3 | 
-------------------------------------
| 4 | 2 | 6 | 8 | 5 | 3 | 7 | 9 | 1 | 
-------------------------------------
| 7 | 1 | 3 | 9 | 2 | 4 | 8 | 5 | 6 | 
-------------------------------------
| 9 | 6 | 1 | 5 | 3 | 7 | 2 | 8 | 4 | 
-------------------------------------
| 2 | 8 | 7 | 4 | 1 | 9 | 6 | 3 | 5 | 
-------------------------------------
| 3 | 4 | 5 | 2 | 8 | 6 | 1 | 7 | 9 | 
-------------------------------------
>>> 
"""
