#!/usr/bin/python3
from map import rooms
from player import *
from items import *
from gameparser import *



def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_pen, item_handbook])
    'a pen, a student handbook'

    >>> list_of_items([item_id])
    'id card'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_money, item_handbook, item_laptop])
    'money, a student handbook, laptop'

    """
    item_list = []
    item_string = ""
    for key in items:
        item_list.append(key["name"])
    for item in item_list:
        item_string = item_string + item + ", "
    counter = len(item_string)-2
    item_string = item_string[0:counter]
    return item_string



def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:

    >>> print_room_items(rooms["Reception"])
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room_items(rooms["Office"])
    There is a pen here.
    <BLANKLINE>

    >>> print_room_items(rooms["Admins"])

    (no output)

    Note: <BLANKLINE> here means that doctest should expect a blank line.

    """
    
    item = room["items"]
    if len(item) !=0:
        string_items = list_of_items(item)
        print("There is " + string_items + " here.\n")

def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_inventory_items(inventory)
    You have id card, laptop, money.
    <BLANKLINE>

    """
    print("You have " + list_of_items(items) + ".\n")


def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:

    >>> print_room(rooms["Office"])
    <BLANKLINE>
    THE GENERAL OFFICE
    <BLANKLINE>
    You are standing next to the cashier's till at
    30-36 Newport Road. The cashier looks at you with hope
    in their eyes. If you go west you can return to the
    Queen's Buildings.
    <BLANKLINE>
    There is a pen here.
    <BLANKLINE>

    >>> print_room(rooms["Reception"])
    <BLANKLINE>
    RECEPTION
    <BLANKLINE>
    You are in a maze of twisty little passages, all alike.
    Next to you is the School of Computer Science and
    Informatics reception. The receptionist, Matt Strangis,
    seems to be playing an old school text-based adventure
    game on his computer. There are corridors leading to the
    south and east. The exit is to the west.
    <BLANKLINE>
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room(rooms["Admins"])
    <BLANKLINE>
    MJ AND SIMON'S ROOM
    <BLANKLINE>
    You are leaning agains the door of the systems managers'
    room. Inside you notice Matt "MJ" John and Simon Jones. They
    ignore you. To the north is the reception.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()
    print_room_items(room)
    
    #
    # COMPLETE ME!
    #

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
    "MJ and Simon's room"
    >>> exit_leads_to(rooms["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(rooms["Tutor"]["exits"], "west")
    'Reception'
    """
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
    >>> print_exit("south", "MJ and Simon's room")
    GO SOUTH to MJ and Simon's room.
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to MJ and Simon's room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    for take_item in room_items:
        print("TAKE " + take_item["id"].upper() + " to take " + take_item["name"] + ".")

    for drop_item in inv_items:
        print("DROP " + drop_item["id"].upper() + " to drop " + drop_item["name"] + ".")

    if current_room["name"] == "The Bar":
        print("TALK TURING to Talk to Alan Turing")
    if current_room["name"] == "The Cinema":
        print("TALK ZUCC to Talk to The Strange Man")
    if current_room["name"] == "The Lab":
        print("CODE to code for the rest of the Day")
    

    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits


def execute_go(direction):
    global current_room
    exits = current_room["exits"]
    if is_valid_exit(exits,direction) == True:
        current_room = move(exits,direction)
    else:
        print("You cannot go there")


def execute_take(item_id):
    global current_room
    global inventory
    global Energy
    global vouchercheck
    presence_check = False
    items = current_room["items"]
    for check_items in items:

        
        if item_id == "laptop":
            presence_check = True
            for item in inventory:
                if item["id"] == "voucher":
                    vouchercheck = True
                    break
            if vouchercheck == True:
                print("\n\nThey Graciously Accept The Voucher And Give You A New Laptop!\n")
                inventory.remove(item_voucher)
                inventory.append(check_items)
                current_room["items"].remove(check_items)
                presence_check = True
                Energy = Energy - 5
                break
            elif vouchercheck == False:
                print("\n\nYou Do Not Have The Voucher Yet!\n\n")
                break

               
        if check_items["id"] == item_id:
            if item_id == "bluebear":
                print("\nThis Tastes Similar To A Drink That Gives You Wings\n")
                Energy = Energy + 20
                current_room["items"].remove(check_items)
                if Energy > 30:
                    Energy = 30
                break
            if item_id == "food":
                print("\nMmmm.... Tesco 20p Ramen Flavour\n")
                Energy = Energy + 10
                current_room["items"].remove(check_items)
                if Energy > 30:
                    Energy = 30
                break
            if item_id == "water":
                print("\nAm I The Only One That Thinks Water Doesn't Taste Nice?\n")
                Energy = Energy + 5
                current_room["items"].remove(check_items)
                if Energy > 30:
                    Energy = 30

                break
            item_key = check_items
            inventory.append(item_key)
            current_room["items"].remove(item_key)
            presence_check = True
            Energy = Energy - 5
            break 
    if presence_check == False:
        print("\n\nThat Item Does Not Exist")
    

def execute_drop(item_id):
    global inventory
    global current_room
    global Energy
    
    presence_check = False
    for item in inventory:
        if item_id == "hideokojima":
            print("\nYou are not Konami")
            presence_check = True
            break
            
        if item["id"] == item_id:
            inventory.remove(item)
            presence_check = True
            current_room["items"].append(item)
            Energy = Energy - 1
            break
        
    if presence_check == False:
        print("This Item Does Not Exist")

def execute_talk_turing():
    global Talk_Once_Check_Turing
    global turing_counter
    global current_room
    global Energy
    if current_room["name"] == "The Bar":
        Energy = Energy - 5
        if Talk_Once_Check_Turing == False:
            print("\n\n\nYou walk over to Alan Turing, he seems too sober to code,\nHe says to come back to him with:\n-The appropriate equipment to Code,\n-The Correct Software to Code Online\n-A drink\nThen maybe he will help you")
            Talk_Once_Check_Turing = True
        else:
            print("\n\n\nYou walk over to Alan Turing, he seems too sober to code,\nHe asks you if you have the items he needs to code\n\n")
            for item in inventory:
                if item["id"] == "laptop":
                    print("You Hand Over The Laptop")
                    turing_counter = turing_counter + 1
                    inventory.remove(item)
                if item["id"] == "github":
                    print("You Hand Over The GitHub Software")
                    turing_counter = turing_counter + 1
                    inventory.remove(item)
                if item["id"] == "nicoffee":
                    print("You Hand Over The Northern Irish Coffee, Knowing After 2 Sips, He'll Be Blind")
                    turing_counter = turing_counter + 1
                    inventory.remove(item)
        
            if turing_counter == 0:
                print("\nYou Hand Over Nothing, and Bid Him Adieu\n\n")

            if turing_counter == 3:
                print("\n\nHe Begrudgingly Accepts The Items And Says He'll Get To Work\n\n")
                print("\n\n-----------------------------\n------- Two Days Pass -------\n-----------------------------\n\n")
                print("\n\nHe Hands You The Completed Code,\nAnd You Submit It and Gain Full Marks For The Assessment,\nThe Guilt Burning inside of you")
                victory()
    else:
        print("\n\nYou Look Around But Can't Seem To Find Him\n")

    
def execute_talk_zucc():
    global Talk_Once_Check_Zucc
    global current_room
    global Energy
    if current_room["name"] == "The Cinema":
        Energy = Energy - 5
        if Talk_Once_Check_Zucc == True:
            print("\n\nThe Zucc Man Himself begins to work on your code at an almost machine like speed and precision, and within the hour has finished\n'Its TOO GOOD' says Zucc and he runs out with what little code you have left\nYou Get A Letter In The Mail The Next Day Saying You're Being Sued\n'F**K Sake Zuccerberg, first Facebook, now this?'")
            lose()
        if Talk_Once_Check_Zucc == False:
            print("\n\n\nYou walk over to the strange man,\nhe seems to mechanically turn around and gives you a creepy smile,\nHe says he will complete your code for free, and that he is very intelligent\n*Almost Like A Robot*\n")
            Talk_Once_Check_Zucc = True
    else:
        print("\nYou Can Not See The Meme Man Himself")

def execute_command(command):

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    elif command[0] == "talk":
        if command[1] == "turing":
            execute_talk_turing()
        elif command[1] == "zucc":
            execute_talk_zucc()
        else:
            print("Talk To Whom?")
            
    elif command[0] == "code":
        if current_room["name"] == "The Lab":
            coding()
        else:
            print("You Can Not Code Here")
    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    global Energy
    # Next room to go to
    Energy = Energy - 1
    return rooms[exits[direction]]

def teamcheck(inventory):
    global Team_Member
    for item in inventory:
        if item["id"] == "hideokojima":
            print("\n\n\nHideo Kojima: As Long As I Have Nothing To Do With Konami Anymore, I'm Fine With Helping You Guys Out!")
            inventory.remove(item)
            Team_Member = Team_Member + 1
            break
        elif item["id"] == "profoak":
            print("\n\n\nProfessor Oak: I Don't Know Much About 'Python', Is It Like A Pikachu? (He Can't Code But Keeps You Entertained And Focused)")
            Team_Member = Team_Member + 1
            inventory.remove(item)
            break
        elif item["id"] == "thebae":
            print("\n\n\nJing Wu: I'm Happy To Help You Out As Long As This Game Doesn't Have A God Damn Kirill Reference In The Game!")
            Team_Member = Team_Member + 1
            inventory.remove(item)
            break
        elif item["id"] == "pythonguy":
            print("\n\n\nGuido van Rossum: I am The Creator Of Python!!! Wait You Just Want To Know The Average Airspeed Velocity Of A Swallow?")
            Team_Member = Team_Member + 1
            inventory.remove(item)
            break


    
def coding():
    global Coding
    global Team_Member
    global Energy
    global inventory

    for item in inventory:
        if item["id"] == "notes":
            inventory.remove(item)
            print("\n\nThe Notes You Found Helped You Make The Code More Efficient\nAllowing You To Finish The Code Quicker\n")
            Coding = Coding + 15
    if Energy < 5:
        Energy = 5
    amount = Energy // 5
    if Team_Member == 0:
        Coding = Coding + amount*1
    elif Team_Member == 1:
        Coding = Coding + amount*2
    elif Team_Member == 2:
        Coding = Coding + amount*5
    elif Team_Member == 3:
        Coding = Coding + amount*10
    elif Team_Member == 4:
        Coding = Coding + amount*20

    Energy = 0
        

def lose():
    print("""
 __     __           _                    _ _ _ _      __
 \ \   / /          | |                  | | | | |  _ / /
  \ \_/ /__  _   _  | |     ___  ___  ___| | | | | (_) | 
   \   / _ \| | | | | |    / _ \/ __|/ _ \ | | | |   | | 
    | | (_) | |_| | | |___| (_) \__ \  __/_|_|_|_|  _| | 
    |_|\___/ \__,_| |______\___/|___/\___(_|_|_|_) (_) | 
                                                      \_\
                                                         """)
    quit()

def victory():
    print("-------------------------------------------------\nYou Managed To Complete The Code On Time!\nYou Decide To Alpha Test The Game And Boot It Up,\nYou Are Met With The Screen 'Error 404: Game Is Missing'")
    print("""

 __     __          __          ___       _ _ _ _     _____  
 \ \   / /          \ \        / (_)     | | | | |  _|  __ \ 
  \ \_/ /__  _   _   \ \  /\  / / _ _ __ | | | | | (_) |  | |
   \   / _ \| | | |   \ \/  \/ / | | '_ \| | | | |   | |  | |
    | | (_) | |_| |    \  /\  /  | | | | |_|_|_|_|  _| |__| |
    |_|\___/ \__,_|     \/  \/   |_|_| |_(_|_|_|_) (_)_____/ 
                                                            """)
    quit()

    
# This is the entry point of our program
def main():
    global Day
    global Start_Day
    global Energy
    global Team_Member
    global current_room
    global Coding
    # Main game loop
    while True:
        teamcheck(inventory)
        if Coding >= 100:
            victory()
        if Energy <= 0:
            print("\n\n------------------------------\n----- The Next Day Dawns -----\n------------------------------\n\n")
            Start_Day = Start_Day + 1
            if Start_Day == Day:
                lose()
            current_room = rooms["Home"]
            Energy = 30
        # Display game status (room description, inventory etc.)
        print("\n-------------------------------------------------------------------------------")
        print_room(current_room)
        print_inventory_items(inventory)
        print("Game Coding Done: " + str(Coding) +"%")
        print("Team Member Count: " + str(Team_Member))

        print(str(Energy) + "/30 Energy Remaining\nDay: " + str(Start_Day) + " of 5\n")


        
        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    print("""
  ______                       _  _    ___  _  _        _____                        _____       __  __ _         _             
 |  ____|                     | || |  / _ \| || |  _   / ____|                      |_   _|     |  \/  (_)       (_)            
 | |__   _ __ _ __ ___  _ __  | || |_| | | | || |_(_) | |  __  __ _ _ __ ___   ___    | |  ___  | \  / |_ ___ ___ _ _ __   __ _ 
 |  __| | '__| '__/ _ \| '__| |__   _| | | |__   _|   | | |_ |/ _` | '_ ` _ \ / _ \   | | / __| | |\/| | / __/ __| | '_ \ / _` |
 | |____| |  | | | (_) | |       | | | |_| |  | |  _  | |__| | (_| | | | | | |  __/  _| |_\__ \ | |  | | \__ \__ \ | | | | (_| |
 |______|_|  |_|  \___/|_|       |_|  \___/   |_| (_)  \_____|\__,_|_| |_| |_|\___| |_____|___/ |_|  |_|_|___/___/_|_| |_|\__, |
                                                                                                                           __/ |
                                                                                                                          |___/
                                                                                                                          """)
    fake_input = input("\n\n\nPlease Enter Your Name To Begin The Game:\n>")

    print("\n\n-------------------------------------------------------------------------------\n\nIt Is Day 1 Of The Final Deadline for Your Group Project,\nAnd None Of The Team Have Done Anything,\nBetter Find Some Experts\n\n")
    main()

