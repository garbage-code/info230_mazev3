import csv

key = False

def config_parser():
    global upkey
    global downkey
    global leftkey
    global rightkey
    global moves_conf
    global map_1
    global map_2
    global map_3
    global moves
    fp = open("config.txt")
    lines = fp.readlines()
    upkey = lines[1]
    downkey = lines[2]
    leftkey = lines[3]
    rightkey = lines[4]
    moves_conf = lines[7]
    map_1 = lines[9]
    map_2 = lines[10]
    map_3 = lines[11]
    first_digit = moves_conf[8]
    second_digit = moves_conf[9]
    third_digit = moves_conf[10]
    if len(moves_conf) == 10:
        moves = int(first_digit + second_digit + third_digit)
    elif len(moves_conf) == 9:
        moves = int(first_digit + second_digit)
    elif len(moves_conf) == 8:
        moves = int(first_digit)
    else:
        print("lying-dormant cyber pathogen")


def startup():
    ans = True
    while ans:
        print("""
        WELCOME TO THE GAUNTLET!
        
        1. START THE GAME!
        2. MESS WITH THE SETTINGS!
        3. QUIT THE GAME!
        \n
        """)
        ans = input("\nSELECT 1, 2, OR 3: ")
        if ans == "1":
            print("\nYOU HAVE SELECTED THE GAME! GOOD LUCK!")
            game(grid)
        if ans == "2":
            print("\nYOU OPTED TO MESS WITH THE SETTINGS! C'MON MAN! CHILL! THE SETTINGS ARE FINE!")
            config_edit()
        if ans == "3":
            print("LAME MAN, LAME!")
            break
        
def config_edit():
    setting_to_change = True
    while setting_to_change:
        print("""
        WELCOME TO THE SETTINGS MENU!
        WHAT DO YOU WANT TO CHANGE?
        
        1. KEY MAPPINGS!
        2. NUMBER OF MOVES!
        3. MAZE LOCATIONS!
        4. BACK!
        """)
        setting_to_change = input("SELECT 1, 2, OR 3: ")
        if setting_to_change == "1":
            print("YOU ARE CHANGING KEY MAPPINGS!")
            keymap_edit()
        if setting_to_change == "2":
            print("YOU ARE CHANGING THE NUMBER OF ALLOWED MOVES!")
            new_moves = input("How many allowed moves should there be?: ")
            replace_line("config.txt", 7, "moves = " + new_moves)
        if setting_to_change == "3":
            print("YOU ARE CHANGING THE LOCATIONS OF THE FILES!")
            file_edit()
        if setting_to_change == "4":
            print("YOU ARE GOING BACK TO THE MAIN MENU!")
            break

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()
    
def keymap_edit():
    keymap = True
    while keymap:
        print("""
        WELCOME TO THE SETTINGS MENU!
        WHAT DO YOU WANT TO CHANGE?
        
        1. YOU WANNA CHANGE THE UP KEY? BE MY GUEST!
        2. YOU WANNA CHANGE THE DOWN KEY? BE MY GUEST!
        3. YOU WANNA CHANGE THE LEFT KEY? BE MY GUEST!
        4. YOU WANNA CHANGE THE RIGHT KEY? BE MY GUEST!
        5. WASD PRESET!
        6. NUMPAD PRESET!
        7. GO BACK!
        """)
        keymap = input("SELECT 1, 2, 3, 4, 5, OR 6!: ")
        if keymap == "1":
            new_upkey = input("TYPE IN THE KEY YOU WANT TO USE FOR UP!: ")
            replace_line("config.txt", 1, 'up = "' + new_upkey + '"')
            print("UP KEY IS NOW " + new_upkey + "!")
        if keymap == "2":
            new_upkey = input("TYPE IN THE KEY YOU WANT TO USE FOR DOWN!: ")
            replace_line("config.txt", 2, 'down = "' + new_upkey + '"')
            print("DOWN KEY IS NOW " + new_upkey + "!")
        if keymap == "3":
            new_upkey = input("TYPE IN THE KEY YOU WANT TO USE FOR LEFT!: ")
            replace_line("config.txt", 3, 'left = "' + new_upkey + '"')
            print("LEFT KEY IS NOW " + new_upkey + "!")
        if keymap == "4":
            new_upkey = input("TYPE IN THE KEY YOU WANT TO USE FOR RIGHT!: ")
            replace_line("config.txt", 4, 'right = "' + new_upkey + '"')
            print("RIGHT KEY IS NOW " + new_upkey + "!")
        if keymap == "5":
            print("GOOD CHOICE! YOUR CONTROLS ARE NOW ALL WASD!")
            replace_line("config.txt", 1, 'up = "w"')
            replace_line("config.txt", 2, 'down = "a"')
            replace_line("config.txt", 3, 'left = "s"')
            replace_line("config.txt", 4, 'right = "d"')
        if keymap == "6":
            print("WHAT ARE YOU, A CASUAL? YOUR CONTROLS ARE NOW THE NUMPAD.")
            replace_line("config.txt", 1, 'up = "8"')
            replace_line("config.txt", 2, 'down = "2"')
            replace_line("config.txt", 3, 'left = "4"')
            replace_line("config.txt", 4, 'right = "6"')
        if keymap == "7":
            break

def file_edit():
    filelocation = True
    while filelocation:
        print("""
        HERE YOU CAN CHANGE WHERE THE LEVELS ARE!
        
        1. CHANGE LEVEL 1!
        2. CHANGE LEVEL 2!
        3. CHANGE LEVEL 3!
        4. GO BACK!
        """)
        filelocation = input("SELECT 1, 2, 3, OR 4!")
        if filelocation == "1":
            new_level1 = input("TYPE IN THE NAME OF THE FILE YOU WANT TO BE LEVEL 1!: ")
            replace_line("config.txt", 10, "map_1 = " + new_level1 + '"')
            print("Level 1 is now at " + new_level1 + ".")
        if filelocation == "2":
            new_level2 = input("TYPE IN THE NAME OF THE FILE YOU WANT TO BE LEVEL 2!: ")
            replace_line("config.txt", 11, "map_2 = " + new_level2 + '"')
            print("Level 2 is now at " + new_level2 + ".")
        if filelocation == "3":
            new_level3 = input("TYPE IN THE NAME OF THE FILE YOU WANT TO BE LEVEL 3!: ")
            replace_line("config.txt", 12, "map_3 = " + new_level3 + '"')
            print("Level 3 is now at " + new_level3 + ".")
        if filelocation == "4":
            break


#def playerinput1():
#    move = input("Please Enter Move (4, 5, 6, or 8):   ")
#    if int(move) == 8 or int(move) == 5  or int(move) == 4 or int(move) == 6 or int(move) == 1:
#        return move
#    else:
#        print ("Please Enter Valid Input")
        
def playerinput():
    move = input("Move, bro: ")
    fp = open("config.txt")
    lines = fp.readlines()
    upkey = lines[1]
    downkey = lines[2]
    leftkey = lines[3]
    rightkey = lines[4]
    upkey = upkey[6]
    downkey = downkey[8]
    leftkey = leftkey[8]
    rightkey = rightkey[9]
    if str(move) == upkey or str(move) == downkey  or str(move) == leftkey or str(move) == rightkey:
        if str(move) == upkey:
            move = str(8)
        if str(move) == downkey:
            move = str(5)
        if str(move) == leftkey:
            move = str(4)
        if str(move) == rightkey:
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

tricorder = open("config.txt")
lines = tricorder.readlines()
map_1 = lines[10]
map_2 = lines[11]
map_3 = lines[12]
map_1 = map_1[8:]
map_2 = map_2[8:]
map_3 = map_3[8:]
map_1 = map_1.rstrip('\n')
map_2 = map_2.rstrip('\n')
map_3 = map_3.rstrip('\n')
grids = [map_1, map_2, map_3]

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
    porta_parser = open("config.txt")
    lines = porta_parser.readlines()
    moves_conf = lines[7]
    digits = moves_conf[7:]
    moves = int(digits)
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
            elif currentlevel == map_2 and start(board[y][x - 1]):
                x = 9
                y = 11
                grid = newmaze(grids[0])
                board = grid
                board[y][x] = "P"
                board[1][1] = "_"
                changekey(True)
                drawgrid(board)
            elif currentlevel == map_3 and start(board[y][x - 1]):
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
                if currentlevel == map_3:
                    board[y][x + 1] = "P"
                    board[y][x] = "_"
                    drawgrid(board)
                    print("You Win")
                    break
                elif currentlevel == map_1:
                    x = 1
                    y = 1
                    grid = newmaze(grids[1])
                    board = grid
                    drawgrid(board)
                    print("You Have Reached Level 2")
                    changekey(False)
                elif currentlevel == map_2:
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
    
startup()







