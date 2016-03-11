import csv

key = False

def playerinput():
    move = input("Please Enter Move (4, 5, 6, or 8):   ")
    if int(move) == 8 or int(move) == 5  or int(move) == 4 or int(move) == 6 or int(move) == 1:
        return move
    else:
        print ("Please Enter Valid Input")

thing = open('level2.txt', 'r')
grid = thing.readlines()



def haskey(a):
    global key
    if a == "K":
        key = True 
        
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
    if x==11:
        return False
    if grid[y][x+1]=='P':
        return (x+1, y)
    else:
        return positionx(x+1, y)
        
def positiony(x, y):
    if y==11:
        return False
    if grid[y+1][x]=='P':
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
    x = 1
    y = 1
    moves = 75
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
                board[y][x + 1] = "P"
                board[y][x] = "_"
                drawgrid(board)
                print("You Win")
                break
            else:
                board[y][x + 1] = "P"
                board[y][x] = "_"
                x = x + 1
                drawgrid(board)
        moves = moves - 1
        print(" ")
        print("You Have " + str(moves) + " Remaining Moves")
    print("You Have Run Out Of Moves")
    
game(grid)



