from random import *

grid = [ #0  #1  #2  #3  #4  #5  #6
        [" "," "," "," "," "," "," "], #0
        [" "," "," "," "," "," "," "], #1
        [" "," "," "," "," "," "," "], #2
        [" "," "," "," "," "," "," "], #3
        [" "," "," "," "," "," "," "], #4
        [" "," "," "," "," "," "," "], #5
        [" "," "," "," "," "," "," "]] #6

row1 = 6
row2 = 6
row3 = 6
row4 = 6
row5 = 6
row6 = 6
row7 = 6
win1 = False
win2 = False
win = False

def printGrid():
    i = 1
    print ("1   2   3   4   5   6   7")
    while i < 7:
    
        print ("--+---+---+---+---+---+--")
        print(" | ".join(map(str, grid[i])))
        i += 1
    print ("--+---+---+---+---+---+--")

def rowAvailable():
    if row1 <= 0:
        turn1= int(input("Player 1 Select a Column (1,2,3,4,5,6,7): "))

##def FirstPlay():
##    first = randint (0,1)
##    if first == 1:
##def turn (first):
##    if first == #working on who goes first

def checkWinX():
    global win1
    global win2
##Row 1 Ver 
    if grid[6][0] == 'X' and grid[5][0] == 'X' and grid[4][0] == 'X' and grid[3][0] == 'X':
        win1 = True
        win = True
    if grid[5][0] == 'X' and grid[4][0] == 'X' and grid[3][0] == 'X' and grid[2][0] == 'X':
        win1 = True
        win = True
    if grid[4][0] == 'X' and grid[3][0] == 'X' and grid[2][0] == 'X' and grid[1][0] == 'X':
        win1 = True
        win = True
##Row 2 Ver
    if grid[6][1] == 'X' and grid[5][1] == 'X' and grid[4][1] == 'X' and grid[3][1] == 'X':
        win1 = True
        win = True
    if grid[5][0] == 'X' and grid[4][1] == 'X' and grid[3][1] == 'X' and grid[2][1] == 'X':
        win1 = True
        win = True
    if grid[4][0] == 'X' and grid[3][1] == 'X' and grid[2][1] == 'X' and grid[1][1] == 'X':
        win1 = True
        win = True
##Row 3 Ver
    if grid[6][2] == 'X' and grid[5][2] == 'X' and grid[4][2] == 'X' and grid[3][2] == 'X':
        win1 = True
        win = True
    if grid[5][2] == 'X' and grid[4][2] == 'X' and grid[3][2] == 'X' and grid[2][2] == 'X':
        win1 = True
        win = True
    if grid[4][2] == 'X' and grid[3][2] == 'X' and grid[2][2] == 'X' and grid[1][2] == 'X':
        win1 = True
        win = True
##Row 4 Ver
    if grid[6][3] == 'X' and grid[5][3] == 'X' and grid[4][3] == 'X' and grid[3][3] == 'X':
        win1 = True
        win = True
    if grid[5][3] == 'X' and grid[4][3] == 'X' and grid[3][3] == 'X' and grid[2][3] == 'X':
        win1 = True
        win = True
    if grid[4][3] == 'X' and grid[3][3] == 'X' and grid[2][3] == 'X' and grid[1][3] == 'X':
        win1 = True
        win = True
##Row 5 Ver
    if grid[6][4] == 'X' and grid[5][4] == 'X' and grid[4][4] == 'X' and grid[3][4] == 'X':
        win1 = True
        win = True
    if grid[5][4] == 'X' and grid[4][4] == 'X' and grid[3][4] == 'X' and grid[2][4] == 'X':
        win1 = True
        win = True
    if grid[4][4] == 'X' and grid[3][4] == 'X' and grid[2][4] == 'X' and grid[1][4] == 'X':
        win1 = True
        win = True
##Row 6 Ver
    if grid[6][5] == 'X' and grid[5][5] == 'X' and grid[4][5] == 'X' and grid[3][5] == 'X':
        win1 = True
        win = True
    if grid[5][5] == 'X' and grid[4][5] == 'X' and grid[3][5] == 'X' and grid[2][5] == 'X':
        win1 = True
        win = True
    if grid[4][5] == 'X' and grid[3][5] == 'X' and grid[2][5] == 'X' and grid[1][5] == 'X':
        win1 = True
        win = True
##Row 7 Ver
    if grid[6][6] == 'X' and grid[5][6] == 'X' and grid[4][6] == 'X' and grid[3][6] == 'X':
        win1 = True
        win = True
    if grid[5][6] == 'X' and grid[4][6] == 'X' and grid[3][6] == 'X' and grid[2][6] == 'X':
        win1 = True
        win = True
    if grid[4][6] == 'X' and grid[3][6] == 'X' and grid[2][6] == 'X' and grid[1][6] == 'X':
        win1 = True
        win = True
        
##Row 1 Hor 
    if grid[6][0] == 'X' and grid[6][1] == 'X' and grid[6][2] == 'X' and grid[6][3] == 'X':
        win1 = True
        win = True
    if grid[6][1] == 'X' and grid[6][2] == 'X' and grid[6][3] == 'X' and grid[6][4] == 'X':
        win1 = True
        win = True
    if grid[6][2] == 'X' and grid[6][3] == 'X' and grid[6][4] == 'X' and grid[6][5] == 'X':
        win1 = True
        win = True
    if grid[6][3] == 'X' and grid[6][4] == 'X' and grid[6][5] == 'X' and grid[6][6] == 'X':
        win1 = True
        win = True
##Row 2 Hor
    if grid[5][0] == 'X' and grid[5][1] == 'X' and grid[5][2] == 'X' and grid[5][3] == 'X':
        win1 = True
        win = True
    if grid[5][1] == 'X' and grid[5][2] == 'X' and grid[5][3] == 'X' and grid[5][4] == 'X':
        win1 = True
        win = True
    if grid[5][2] == 'X' and grid[5][3] == 'X' and grid[5][4] == 'X' and grid[5][5] == 'X':
        win1 = True
        win = True
    if grid[5][3] == 'X' and grid[5][4] == 'X' and grid[5][5] == 'X' and grid[5][6] == 'X':
        win1 = True
        win = True
##Row 3 Hor 
    if grid[4][0] == 'X' and grid[4][1] == 'X' and grid[4][2] == 'X' and grid[4][3] == 'X':
        win1 = True
        win = True
    if grid[4][1] == 'X' and grid[4][2] == 'X' and grid[4][3] == 'X' and grid[4][4] == 'X':
        win1 = True
        win = True
    if grid[4][2] == 'X' and grid[4][3] == 'X' and grid[4][4] == 'X' and grid[4][5] == 'X':
        win1 = True
        win = True
    if grid[4][3] == 'X' and grid[4][4] == 'X' and grid[4][5] == 'X' and grid[4][6] == 'X':
        win1 = True
        win = True
##Row 4 Hor
    if grid[3][0] == 'X' and grid[3][1] == 'X' and grid[3][2] == 'X' and grid[3][3] == 'X':
        win1 = True
        win = True
    if grid[3][1] == 'X' and grid[3][2] == 'X' and grid[3][3] == 'X' and grid[3][4] == 'X':
        win1 = True
        win = True
    if grid[3][2] == 'X' and grid[3][3] == 'X' and grid[3][4] == 'X' and grid[3][5] == 'X':
        win1 = True
        win = True
    if grid[3][3] == 'X' and grid[3][4] == 'X' and grid[3][5] == 'X' and grid[3][6] == 'X':
        win1 = True
        win = True
##Row 5 Hor 
    if grid[2][0] == 'X' and grid[2][1] == 'X' and grid[2][2] == 'X' and grid[2][3] == 'X':
        win1 = True
        win = True
    if grid[2][1] == 'X' and grid[2][2] == 'X' and grid[2][3] == 'X' and grid[2][4] == 'X':
        win1 = True
        win = True
    if grid[2][2] == 'X' and grid[2][3] == 'X' and grid[2][4] == 'X' and grid[2][5] == 'X':
        win1 = True
        win = True
    if grid[2][3] == 'X' and grid[2][4] == 'X' and grid[2][5] == 'X' and grid[2][6] == 'X':
        win1 = True
        win = True
##Row 6 Hor
    if grid[1][0] == 'X' and grid[1][1] == 'X' and grid[1][2] == 'X' and grid[1][3] == 'X':
        win1 = True
        win = True
    if grid[1][1] == 'X' and grid[1][2] == 'X' and grid[1][3] == 'X' and grid[1][4] == 'X':
        win1 = True
        win = True
    if grid[1][2] == 'X' and grid[1][3] == 'X' and grid[1][4] == 'X' and grid[1][5] == 'X':
        win1 = True
        win = True
    if grid[1][3] == 'X' and grid[1][4] == 'X' and grid[1][5] == 'X' and grid[1][6] == 'X':
        win1 = True

    ##Row 1 Dia
    if grid[6][0] == 'X' and grid[5][1] == 'X' and grid[4][2] == 'X' and grid[3][3] == 'X':
        win1 = True
        win = True
    if grid[5][0] == 'X' and grid[4][1] == 'X' and grid[3][2] == 'X' and grid[2][3] == 'X':
        win1 = True
        win = True
    if grid[4][0] == 'X' and grid[3][1] == 'X' and grid[2][2] == 'X' and grid[1][3] == 'X':
        win1 = True
        win = True
    if grid[3][0] == 'X' and grid[4][1] == 'X' and grid[5][2] == 'X' and grid[6][3] == 'X':
        win1 = True
        win = True
    if grid[2][0] == 'X' and grid[3][1] == 'X' and grid[4][2] == 'X' and grid[5][3] == 'X':
        win1 = True
        win = True
    if grid[1][0] == 'X' and grid[2][1] == 'X' and grid[3][2] == 'X' and grid[4][3] == 'X':
        win1 = True
        win = True
##Row 2 Dia
    if grid[6][1] == 'X' and grid[5][2] == 'X' and grid[4][3] == 'X' and grid[3][4] == 'X':
        win1 = True
        win = True
    if grid[5][1] == 'X' and grid[4][2] == 'X' and grid[3][3] == 'X' and grid[2][4] == 'X':
        win1 = True
        win = True
    if grid[4][1] == 'X' and grid[3][2] == 'X' and grid[2][3] == 'X' and grid[1][4] == 'X':
        win1 = True
        win = True
    if grid[3][1] == 'X' and grid[4][2] == 'X' and grid[5][3] == 'X' and grid[6][4] == 'X':
        win1 = True
        win = True
    if grid[2][1] == 'X' and grid[3][2] == 'X' and grid[4][3] == 'X' and grid[5][4] == 'X':
        win1 = True
        win = True
    if grid[1][1] == 'X' and grid[2][2] == 'X' and grid[3][3] == 'X' and grid[4][4] == 'X':
        win1 = True
        win = True
##Row 3 Dia
    if grid[6][2] == 'X' and grid[5][3] == 'X' and grid[4][4] == 'X' and grid[3][5] == 'X':
        win1 = True
        win = True
    if grid[5][2] == 'X' and grid[4][3] == 'X' and grid[3][4] == 'X' and grid[2][5] == 'X':
        win1 = True
        win = True
    if grid[4][2] == 'X' and grid[3][3] == 'X' and grid[2][4] == 'X' and grid[1][5] == 'X':
        win1 = True
        win = True
    if grid[3][2] == 'X' and grid[4][3] == 'X' and grid[5][4] == 'X' and grid[6][5] == 'X':
        win1 = True
        win = True
    if grid[2][2] == 'X' and grid[3][3] == 'X' and grid[4][4] == 'X' and grid[5][5] == 'X':
        win1 = True
        win = True
    if grid[1][2] == 'X' and grid[2][3] == 'X' and grid[3][4] == 'X' and grid[4][5] == 'X':
        win1 = True
        win = True
##Row 4 Dia
    if grid[6][3] == 'X' and grid[5][4] == 'X' and grid[4][5] == 'X' and grid[3][6] == 'X':
        win1 = True
        win = True
    if grid[5][3] == 'X' and grid[4][4] == 'X' and grid[3][5] == 'X' and grid[2][6] == 'X':
        win1 = True
        win = True
    if grid[4][3] == 'X' and grid[3][4] == 'X' and grid[2][5] == 'X' and grid[1][6] == 'X':
        win1 = True
        win = True
    if grid[3][3] == 'X' and grid[4][4] == 'X' and grid[5][5] == 'X' and grid[6][6] == 'X':
        win1 = True
        win = True
    if grid[2][3] == 'X' and grid[3][4] == 'X' and grid[4][5] == 'X' and grid[5][6] == 'X':
        win1 = True
        win = True
    if grid[1][3] == 'X' and grid[2][4] == 'X' and grid[3][5] == 'X' and grid[4][6] == 'X':
        win1 = True
        win = True
        
def checkWinO():
    global win2
##Row 1 Ver 
    if grid[6][0] == 'O' and grid[5][0] == 'O' and grid[4][0] == 'O' and grid[3][0] == 'O':
        win2 = True
        win = True
    if grid[5][0] == 'O' and grid[4][0] == 'O' and grid[3][0] == 'O' and grid[2][0] == 'O':
        win2 = True
        win = True
    if grid[4][0] == 'O' and grid[3][0] == 'O' and grid[2][0] == 'O' and grid[1][0] == 'O':
        win2 = True
        win = True
##Row 2 Ver
    if grid[6][1] == 'O' and grid[5][1] == 'O' and grid[4][1] == 'O' and grid[3][1] == 'O':
        win2 = True
        win = True
    if grid[5][0] == 'O' and grid[4][1] == 'O' and grid[3][1] == 'O' and grid[2][1] == 'O':
        win2 = True
        win = True
    if grid[4][0] == 'O' and grid[3][1] == 'O' and grid[2][1] == 'O' and grid[1][1] == 'O':
        win2 = True
        win = True
##Row 3 Ver
    if grid[6][2] == 'O' and grid[5][2] == 'O' and grid[4][2] == 'O' and grid[3][2] == 'O':
        win2 = True
        win = True
    if grid[5][2] == 'O' and grid[4][2] == 'O' and grid[3][2] == 'O' and grid[2][2] == 'O':
        win2 = True
        win = True
    if grid[4][2] == 'O' and grid[3][2] == 'O' and grid[2][2] == 'O' and grid[1][2] == 'O':
        win2 = True
        win = True
##Row 4 Ver
    if grid[6][3] == 'O' and grid[5][3] == 'O' and grid[4][3] == 'O' and grid[3][3] == 'O':
        win2 = True
        win = True
    if grid[5][3] == 'O' and grid[4][3] == 'O' and grid[3][3] == 'O' and grid[2][3] == 'O':
        win2 = True
        win = True
    if grid[4][3] == 'O' and grid[3][3] == 'O' and grid[2][3] == 'O' and grid[1][3] == 'O':
        win2 = True
        win = True
##Row 5 Ver
    if grid[6][4] == 'O' and grid[5][4] == 'O' and grid[4][4] == 'O' and grid[3][4] == 'O':
        win2 = True
        win = True
    if grid[5][4] == 'O' and grid[4][4] == 'O' and grid[3][4] == 'O' and grid[2][4] == 'O':
        win2 = True
        win = True
    if grid[4][4] == 'O' and grid[3][4] == 'O' and grid[2][4] == 'O' and grid[1][4] == 'O':
        win2 = True
        win = True
##Row 6 Ver
    if grid[6][5] == 'O' and grid[5][5] == 'O' and grid[4][5] == 'O' and grid[3][5] == 'O':
        win2 = True
        win = True
    if grid[5][5] == 'O' and grid[4][5] == 'O' and grid[3][5] == 'O' and grid[2][5] == 'O':
        win2 = True
        win = True
    if grid[4][5] == 'O' and grid[3][5] == 'O' and grid[2][5] == 'O' and grid[1][5] == 'O':
        win2 = True
        win = True
##Row 7 Ver
    if grid[6][6] == 'O' and grid[5][6] == 'O' and grid[4][6] == 'O' and grid[3][6] == 'O':
        win2 = True
        win = True
    if grid[5][6] == 'O' and grid[4][6] == 'O' and grid[3][6] == 'O' and grid[2][6] == 'O':
        win2 = True
        win = True
    if grid[4][6] == 'O' and grid[3][6] == 'O' and grid[2][6] == 'O' and grid[1][6] == 'O':
        win2 = True
        win = True
        
##Row 1 Hor 
    if grid[6][0] == 'O' and grid[6][1] == 'O' and grid[6][2] == 'O' and grid[6][3] == 'O':
        win2 = True
        win = True
    if grid[6][1] == 'O' and grid[6][2] == 'O' and grid[6][3] == 'O' and grid[6][4] == 'O':
        win2 = True
        win = True
    if grid[6][2] == 'O' and grid[6][3] == 'O' and grid[6][4] == 'O' and grid[6][5] == 'O':
        win2 = True
        win = True
    if grid[6][3] == 'O' and grid[6][4] == 'O' and grid[6][5] == 'O' and grid[6][6] == 'O':
        win2 = True
        win = True
##Row 2 Hor
    if grid[5][0] == 'O' and grid[5][1] == 'O' and grid[5][2] == 'O' and grid[5][3] == 'O':
        win2 = True
        win = True
    if grid[5][1] == 'O' and grid[5][2] == 'O' and grid[5][3] == 'O' and grid[5][4] == 'O':
        win2 = True
        win = True
    if grid[5][2] == 'O' and grid[5][3] == 'O' and grid[5][4] == 'O' and grid[5][5] == 'O':
        win2 = True
        win = True
    if grid[5][3] == 'O' and grid[5][4] == 'O' and grid[5][5] == 'O' and grid[5][6] == 'O':
        win2 = True
        win = True
##Row 3 Hor 
    if grid[4][0] == 'O' and grid[4][1] == 'O' and grid[4][2] == 'O' and grid[4][3] == 'O':
        win2 = True
        win = True
    if grid[4][1] == 'O' and grid[4][2] == 'O' and grid[4][3] == 'O' and grid[4][4] == 'O':
        win2 = True
        win = True
    if grid[4][2] == 'O' and grid[4][3] == 'O' and grid[4][4] == 'O' and grid[4][5] == 'O':
        win2 = True
        win = True
    if grid[4][3] == 'O' and grid[4][4] == 'O' and grid[4][5] == 'O' and grid[4][6] == 'O':
        win2 = True
        win = True
##Row 4 Hor
    if grid[3][0] == 'O' and grid[3][1] == 'O' and grid[3][2] == 'O' and grid[3][3] == 'O':
        win2 = True
        win = True
    if grid[3][1] == 'O' and grid[3][2] == 'O' and grid[3][3] == 'O' and grid[3][4] == 'O':
        win2 = True
        win = True
    if grid[3][2] == 'O' and grid[3][3] == 'O' and grid[3][4] == 'O' and grid[3][5] == 'O':
        win2 = True
        win = True
    if grid[3][3] == 'O' and grid[3][4] == 'O' and grid[3][5] == 'O' and grid[3][6] == 'O':
        win2 = True
        win = True
##Row 5 Hor 
    if grid[2][0] == 'O' and grid[2][1] == 'O' and grid[2][2] == 'O' and grid[2][3] == 'O':
        win2 = True
        win = True
    if grid[2][1] == 'O' and grid[2][2] == 'O' and grid[2][3] == 'O' and grid[2][4] == 'O':
        win2 = True
        win = True
    if grid[2][2] == 'O' and grid[2][3] == 'O' and grid[2][4] == 'O' and grid[2][5] == 'O':
        win2 = True
        win = True
    if grid[2][3] == 'O' and grid[2][4] == 'O' and grid[2][5] == 'O' and grid[2][6] == 'O':
        win2 = True
        win = True
##Row 6 Hor
    if grid[1][0] == 'O' and grid[1][1] == 'O' and grid[1][2] == 'O' and grid[1][3] == 'O':
        win2 = True
        win = True
    if grid[1][1] == 'O' and grid[1][2] == 'O' and grid[1][3] == 'O' and grid[1][4] == 'O':
        win2 = True
        win = True
    if grid[1][2] == 'O' and grid[1][3] == 'O' and grid[1][4] == 'O' and grid[1][5] == 'O':
        win2 = True
        win = True
    if grid[1][3] == 'O' and grid[1][4] == 'O' and grid[1][5] == 'O' and grid[1][6] == 'O':
        win2 = True
        win = True

##Row 1 Dia
    if grid[6][0] == 'O' and grid[5][1] == 'O' and grid[4][2] == 'O' and grid[3][3] == 'O':
        win2 = True
        win = True
    if grid[5][0] == 'O' and grid[4][1] == 'O' and grid[3][2] == 'O' and grid[2][3] == 'O':
        win2 = True
        win = True
    if grid[4][0] == 'O' and grid[3][1] == 'O' and grid[2][2] == 'O' and grid[1][3] == 'O':
        win2 = True
        win = True
    if grid[3][0] == 'O' and grid[4][1] == 'O' and grid[5][2] == 'O' and grid[6][3] == 'O':
        win2 = True
        win = True
    if grid[2][0] == 'O' and grid[3][1] == 'O' and grid[4][2] == 'O' and grid[5][3] == 'O':
        win2 = True
        win = True
    if grid[1][0] == 'O' and grid[2][1] == 'O' and grid[3][2] == 'O' and grid[4][3] == 'O':
        win2 = True
        win = True
##Row 2 Dia
    if grid[6][1] == 'O' and grid[5][2] == 'O' and grid[4][3] == 'O' and grid[3][4] == 'O':
        win2 = True
        win = True
    if grid[5][1] == 'O' and grid[4][2] == 'O' and grid[3][3] == 'O' and grid[2][4] == 'O':
        win2 = True
        win = True
    if grid[4][1] == 'O' and grid[3][2] == 'O' and grid[2][3] == 'O' and grid[1][4] == 'O':
        win2 = True
        win = True
    if grid[3][1] == 'O' and grid[4][2] == 'O' and grid[5][3] == 'O' and grid[6][4] == 'O':
        win2 = True
        win = True
    if grid[2][1] == 'O' and grid[3][2] == 'O' and grid[4][3] == 'O' and grid[5][4] == 'O':
        win2 = True
        win = True
    if grid[1][1] == 'O' and grid[2][2] == 'O' and grid[3][3] == 'O' and grid[4][4] == 'O':
        win2 = True
        win = True
##Row 3 Dia
    if grid[6][2] == 'O' and grid[5][3] == 'O' and grid[4][4] == 'O' and grid[3][5] == 'O':
        win2 = True
        win = True
    if grid[5][2] == 'O' and grid[4][3] == 'O' and grid[3][4] == 'O' and grid[2][5] == 'O':
        win2 = True
        win = True
    if grid[4][2] == 'O' and grid[3][3] == 'O' and grid[2][4] == 'O' and grid[1][5] == 'O':
        win2 = True
        win = True
    if grid[3][2] == 'O' and grid[4][3] == 'O' and grid[5][4] == 'O' and grid[6][5] == 'O':
        win2 = True
        win = True
    if grid[2][2] == 'O' and grid[3][3] == 'O' and grid[4][4] == 'O' and grid[5][5] == 'O':
        win2 = True
        win = True
    if grid[1][2] == 'O' and grid[2][3] == 'O' and grid[3][4] == 'O' and grid[4][5] == 'O':
        win2 = True
        win = True
##Row 4 Dia
    if grid[6][3] == 'O' and grid[5][4] == 'O' and grid[4][5] == 'O' and grid[3][6] == 'O':
        win2 = True
        win = True
    if grid[5][3] == 'O' and grid[4][4] == 'O' and grid[3][5] == 'O' and grid[2][6] == 'O':
        win2 = True
        win = True
    if grid[4][3] == 'O' and grid[3][4] == 'O' and grid[2][5] == 'O' and grid[1][6] == 'O':
        win2 = True
        win = True
    if grid[3][3] == 'O' and grid[4][4] == 'O' and grid[5][5] == 'O' and grid[6][6] == 'O':
        win2 = True
        win = True
    if grid[2][3] == 'O' and grid[3][4] == 'O' and grid[4][5] == 'O' and grid[5][6] == 'O':
        win2 = True
        win = True
    if grid[1][3] == 'O' and grid[2][4] == 'O' and grid[3][5] == 'O' and grid[4][6] == 'O':
        win2 = True
        win = True
        
                                                       




def CheckASpace1(user):
    global row1
    global row2
    global row3
    global row4
    global row5
    global row6
    global row7
    if grid [row1][0] == "X" or grid [row1] [0] == "O":
        if row1 <= 0 and user == 1:
             print ("When you let go of your chip, it rolls off the chip that occupies that space")
        elif row1 > 0:
            row1 -= 1
        
    if grid [row2][1] == "X" or grid [row2] [1] == "O":
        if row2 <= 0 and user == 2:
             print ("This column is full. Pick again!")
        elif row2 > 0:
            row2 -= 1
        
    if grid [row3][2] == "X" or grid [row3] [2] == "O":
        if row3 <= 0 and user == 3:
            print ("This column is full. Pick again!")
        elif row3 > 0:
            row3 -= 1
        
    if grid [row4][3] == "X" or grid [row4] [3] == "O":
        if row4 <= 0 and user == 4:
             print ("This column is full. Pick again!")
        elif row4 > 0:
            row4 -= 1
        
    if grid [row5][4] == "X" or grid [row5] [4] == "O":
        if row5 <= 0 and user == 5:
             print ("This column is full. Pick again!")
        elif row5 > 0:
            row5 -= 1
        
    if grid [row6][5] == "X" or grid [row6] [5] == "O":
        if row6 <= 0 and user == 6:
             print ("This column is full. Pick again!")
        elif row6 > 0:
            row6 -= 1
        
    if grid [row7][6] == "X" or grid [row7] [6] == "O":
        if row7 <= 0 and user == 7:
             print ("This column is full. Pick again!")
        elif row7 > 0:
            row7 -= 1

def CheckASpace2(user):
    global row1
    global row2
    global row3
    global row4
    global row5
    global row6
    global row7
    if grid [row1][0] == "X" or grid [row1] [0] == "O":
        if row1 <= 0 and user == 1:
             print ("This column is full. Pick again!")
        elif row1 > 0:
            row1 -= 1
        
    if grid [row2][1] == "X" or grid [row2] [1] == "O":
        if row2 <= 0 and user == 2:
             print ("This column is full. Pick again!")
        elif row2 > 0:
            row2 -= 1
        
    if grid [row3][2] == "X" or grid [row3] [2] == "O":
        if row3 <= 0 and user == 3:
             print ("This column is full. Pick again!")
        elif row3 > 0:
            row3 -= 1
        
    if grid [row4][3] == "X" or grid [row4] [3] == "O":
        if row4 <= 0 and user == 4:
             print ("This column is full. Pick again!")
        elif row4 > 0:
            row4 -= 1
        
    if grid [row5][4] == "X" or grid [row5] [4] == "O":
        if row5 <= 0 and user == 5:
             print ("This column is full. Pick again!")
        elif row5 > 0:
            row5 -= 1
        
    if grid [row6][5] == "X" or grid [row6] [5] == "O":
        if row6 <= 0 and user == 6:
             print ("This column is full. Pick again!")
        elif row6 > 0:
            row6 -= 1
        
    if grid [row7][6] == "X" or grid [row7] [6] == "O":
        if row7 <= 0 and user == 7:
             print ("This column is full. Pick again!")
        elif row7 > 0:
            row7 -= 1
        
def dropAChip1 (user):
    if user == 1:
        grid [row1][0] = "X"
    if user == 2:
        grid [row2][1] = "X"
    if user == 3:
        grid [row3][2] = "X"
    if user == 4:
        grid [row4][3] = "X"
    if user == 5:
        grid [row5][4] = "X"
    if user == 6:
        grid [row6][5] = "X"
    if user == 7:
        grid [row7][6] = "X"
    if user > 7:
        print ("You miss the board and your chip rolls off the table. You miss your turn...")
        return

def dropAChip2 (user):
    if user == 1:
        grid [row1][0] = "O"
    if user == 2:
        grid [row2][1] = "O"
    if user == 3:
        grid [row3][2] = "O"
    if user == 4:
        grid [row4][3] = "O"
    if user == 5:
        grid [row5][4] = "O"
    if user == 6:
        grid [row6][5] = "O"
    if user == 7:
        grid [row7][6] = "O"
    if user > 7:
        print ("You miss the board and your chip rolls off the table. You miss your turn...")
        return
var=0
def play():
##    if win == False:
##        var = 0
##    elif win == True:
##        var = 1
##        
##    if var == 0:
##        printGrid()
##        turn1= int(input("\nPlayer 1 Select a Column (1-7): "))
##        dropAChip1(turn1)
##        CheckASpace1(turn1)
##        checkWinX()
##        printGrid ()
##        turn2= int(input("\nPlayer 2 Select a Column (1-7): "))
##        dropAChip2(turn2)
##        CheckASpace2(turn2)
##        checkWinO()
##    elif var == 1:
##        exit()
    while win1 != True or win2 != True:
        if win2 == False:
            printGrid()
            turn1= int(input("\nPlayer 1 Select a Column (1-7): "))
            dropAChip1(turn1)
            CheckASpace1(turn1)
            checkWinX()
        else:
            printGrid()
            print('██████╗     ██████╗     ██╗    ██╗██╗███╗   ██╗███████╗')
            print('██╔══██╗    ╚════██╗    ██║    ██║██║████╗  ██║██╔════╝')
            print('██████╔╝     █████╔╝    ██║ █╗ ██║██║██╔██╗ ██║███████╗')
            print('██╔═══╝     ██╔═══╝     ██║███╗██║██║██║╚██╗██║╚════██║')
            print('██║         ███████╗    ╚███╔███╔╝██║██║ ╚████║███████║')
            print('╚═╝         ╚══════╝     ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚══════╝')
            break
        
        if win1 == False:
            printGrid ()
            turn2= int(input("\nPlayer 2 Select a Column (1-7): "))
            dropAChip2(turn2)
            CheckASpace2(turn2)
            checkWinO()
        else:
            printGrid()
            print("██████╗      ██╗    ██╗    ██╗██╗███╗   ██╗███████╗")
            print("██╔══██╗    ███║    ██║    ██║██║████╗  ██║██╔════╝")
            print("██████╔╝    ╚██║    ██║ █╗ ██║██║██╔██╗ ██║███████╗")
            print("██╔═══╝      ██║    ██║███╗██║██║██║╚██╗██║╚════██║")
            print("██║          ██║    ╚███╔███╔╝██║██║ ╚████║███████║")
            print("╚═╝          ╚═╝     ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚══════╝")
            break       

def main():
    
    play()
    
main()
