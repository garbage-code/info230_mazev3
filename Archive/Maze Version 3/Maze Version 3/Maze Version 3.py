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
            break
            #game(grid)
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
            replace_line("config.txt", 1, "moves_num = " + new_moves)
        if setting_to_change == "3":
            print("YOU ARE CHANGING THE LOCATIONS OF THE FILES!")
            #file_edit()
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
            replace_line("config.txt", 2, 'down = "' + new_upkey + "'")
            print("DOWN KEY IS NOW " + new_upkey + "!")
        if keymap == "3":
            new_upkey = input("TYPE IN THE KEY YOU WANT TO USE FOR LEFT!: ")
            replace_line("config.txt", 3, 'left = "' + new_upkey + "'")
            print("LEFT KEY IS NOW " + new_upkey + "!")
        if keymap == "4":
            new_upkey = input("TYPE IN THE KEY YOU WANT TO USE FOR RIGHT!: ")
            replace_line("config.txt", 4, 'right = "' + new_upkey + "'")
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

startup()
            
    
