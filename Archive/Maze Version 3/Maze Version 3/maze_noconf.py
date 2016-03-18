import csv

key = False

moves = 300

def playerinput1():
    move = input("Please Enter Move (4, 5, 6, or 8):   ")
    if int(move) == 8 or int(move) == 5  or int(move) == 4 or int(move) == 6 or int(move) == 1:
        return move
    else:
        print ("Please Enter Valid Input")
        
def playerinput():
    move = input("Please Enter Move (w, a, s, or d):   ")
    if str(move) == 'w' or str(move) == 's'  or str(move) == 'a' or str(move) == 'd':
        if str(move) == 'w':
            move = str(8)
        if str(move) == 's':
            move = str(5)
        if str(move) == 'a':
            move = str(4)
        if str(move) == 'd':
            move = str(6)
        return move
    else:
        print ("Please Enter Valid Input")
        
currentlevel = ""
        
def newmaze(level):
    global currentlevel
    maze = []
    itr =open(level)
    for line in itr:
        string=line.strip()
        maze.append(string.split(' '))
    currentlevel = level
    return maze

grids = ["level1.txt", "level2.txt", "level3.txt"] 

grid = newmaze(grids[0])

def start(a):
    if a == 'S':
        return True
    else:
        return False
        
def haskey(a):
    global key
    if a == "K":
        key = True 
        
def changekey(boolean):
    global key
    key = boolean
        
def door(a):
    if a == "D":
        if key == True:
            return False
        else: 
            return True
    else:
        return False


def drawgrid(grid):
    print("\n"*100)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[0] == x and grid[1] == y:
                print('P', end=" ")
            elif abs(x-position(0, 0)[0])>1 or abs(y-position(0, 0)[1])>1:
                print('0', end=' ')
            else:
                print (grid[y][x], end=' ')
        print()

def positionx(x, y):
    if x== len(grid[1]) - 1:
        return False
    if grid[y][x+1]=='P':
        return (x+1, y)
    else:
        return positionx(x+1, y)
        
def positiony(x, y):
    if y== len(grid) - 1:
        return False
    elif grid[y+1][x]=='P':
        return (x, y+1)
    else:
        return positiony(x, y+1)


def position(x, y):
    if grid[y][x]=='P':
        return (x, y)
    elif positionx(x, y):
        return positionx(x, y)
    elif positiony(x, y):
        return positiony(x, y)
    elif grid[y+1][x]=='P':
        return (x, y+1)
    elif grid[y][x+1]=='P':
        return (x+1, y)
    else:
        return position(x+1, y+1)
        
def iswall(a):
    if a == "H":
        return True
    else: 
        return False
        
def iswin(a):
    if a == "F":
        return True
    else: 
        return False
        
        
def game(board1):
    global currentlevel
    global moves
    global grid
    x = 1
    y = 1
    board = board1
    drawgrid(board)
    key = ""
    while moves > 0:
        key = playerinput()
        if key == "8": 
            haskey(board[y - 1][x])
            if door(board[y - 1][x]) or iswall(board[y - 1][x]):
                print("Dishonor to your family") 
            else:
                board[y - 1][x] = "P"
                board[y][x] = "_"
                y = y - 1
                drawgrid(board)
                if iswin(board[y][x]):
                    print("You Win")
                    break
        elif key == "4": 
            haskey(board[y][x - 1])
            if door(board[y][x - 1]) or iswall(board[y][x - 1]):
                print("Dishonor to your family")
            elif currentlevel == 'level2.txt' and start(board[y][x - 1]):
                x = 9
                y = 11
                grid = newmaze(grids[0])
                board = grid
                board[y][x] = "P"
                board[1][1] = "_"
                changekey(True)
                drawgrid(board)
            elif currentlevel == 'level3.txt' and start(board[y][x - 1]):
                x = 8
                y = 11
                grid = newmaze(grids[1])
                board = grid
                board[y][x] = "P"
                board[1][1] = "_"
                changekey(True)
                drawgrid(board)
            else:
                board[y][x - 1] = "P"
                board[y][x] = "_"
                x = x - 1
                drawgrid(board)
                if iswin(board[y][x]):
                    print("You Win")
                    break
        elif key == "5": 
            haskey(board[y + 1][x])
            if  door(board[y + 1][x]) or iswall(board[y + 1][x]):
                print("Dishonor to your family") 
            else:
                board[y + 1][x] = "P"
                board[y][x] = "_"
                y = y + 1
                drawgrid(board)
                if iswin(board[y][x]):
                    print("You Win")
                    break
        elif key == "6": #Only checks win for input of 6
            haskey(board[y][x + 1])
            if door(board[y][x + 1]) or iswall(board[y][x + 1]):
                print("Dishonor to your family")
            elif iswin(board[y][x + 1]):
                if currentlevel == 'level3.txt':
                    board[y][x + 1] = "P"
                    board[y][x] = "_"
                    drawgrid(board)
                    print("You Win")
                    break
                elif currentlevel == 'level1.txt':
                    x = 1
                    y = 1
                    grid = newmaze(grids[1])
                    board = grid
                    drawgrid(board)
                    print("You Have Reached Level 2")
                    changekey(False)
                elif currentlevel == 'level2.txt':
                    x = 1
                    y = 1
                    grid = newmaze(grids[2])
                    board = grid
                    drawgrid(board)
                    print("You Have Reached Level 3")
                    changekey(False)
            else:
                board[y][x + 1] = "P"
                board[y][x] = "_"
                x = x + 1
                drawgrid(board)
        moves = moves - 1
        print(" ")
        print("You Have " + str(moves) + " Remaining Moves")
    if moves == 0:
        print("You Have Run Out Of Moves")
    

    
#game(grid)






