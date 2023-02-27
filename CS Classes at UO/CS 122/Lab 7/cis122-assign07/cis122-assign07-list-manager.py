''' 
CIS 122 Fall 2020 Assignment 7
Author: Isabella Cortez
Credit: Jasmine Wallin
Description: Create list that can add, delete, list, and clear items in it
'''

label_spacing = 5
num_spacing = 5

adora = ["Add" , "Delete" , "List" , "Clear"]
description = ["Add to list", "Delete information" , "List information" , "Clear list"]

variable_list = []

left = True
right = True

def cmd_help():
    print("*** Available commads ***")
    for command in adora:
        command_num = adora.index(command)
        print(pad_right(command, (10 - get_max_list_item_size(command))) + description[command_num])
    print("Empty to exit")

def cmd_add(t):
    while True:
        add = input("Enter information (empty to stop): " ).strip()
        if add == "":
            break
        else:
            variable_list.append(add)
            print ("Added, item count = " , str(len(variable_list)))
        return variable_list
        
def cmd_delete(t):
    while True:
        for item in variable_list:
            command_num = variable_list.index(item)
            print(pad_right(str(command_num), 2) + str(item))
        print()
        delete = input("Enter number to delete (empty to stop): ").strip()
        if delete == "":
            break
        elif delete.isdigit() == False:
            print("Must be digit")
            print()
        else:
            delete = int(delete)
            if (len(variable_list) - 1) < delete:
                print("Invalid input")
                print()
            elif len(variable_list) >= delete:
                if len(variable_list) > 0:
                    del variable_list[delete]
                elif len(variable_list) == 0:
                    print("All items deleted")
                    break
                
def cmd_list(t):
    print("List contains " , str(len(variable_list)) , "item(s)")
    for item in variable_list:
        print(item)

def cmd_clear(t):
    print(str(len(variable_list)), " item(s) removed, list empty")
    variable_list.clear()
    
def get_max_list_item_size(t):
    max_size = len(t)
    return max_size

def pad_string(data, size, direction = 'left', character = " "):
    '''
    Description: takes data to see if it is bigger than size and returns the direction
    Args:
        data = the number (average, count, comments, total)
        size = the amount of empty space
        direction = the place where the word or number is going
        character = the space that is timed by size
    Return:
        returns the direction if it is left and the direction if it is right
    '''
    
    data = str(data)
    if len(data) > size:
        return data
    elif direction == 'left':
        return character*(size-len(data))+ data
    else:
        return data + character * (size-len(data))
    
def pad_left(data, size, character = " "):
    '''
    Description: returns the left direction
    Args:
        data = the number (average, count, comments, total)
        size = the amount of empty space
        character = the space that is timed by size
    Return:
        returns the direction if it is left 
    '''
    
    return pad_string(data, size, direction = 'left', character = " ")
    
def pad_right(data, size, character = " "):
    '''
    Description: returns the right directin
    Args:
        data = the number (average, count, comments, total)
        size = the amount of empty space
        character = the space that is timed by size
    Return:
        returns the direction if it is right
    '''
    
    return pad_string(data, size, direction = 'right', character = " ")

while True:
    input_command = str(input("Enter a command (? for help): ").strip())

    if input_command == '':
        print("Goodbye!")
        break
    elif input_command == "?":
        cmd_help()
        print()
    elif input_command == "add":
        cmd_add(variable_list)
        print()
    elif input_command == "delete":
        cmd_delete(variable_list)
        print()
    elif input_command == "list":
        cmd_list(variable_list)
        print()
    elif input_command == "clear":
        cmd_clear(variable_list)
        print()
    else:
        print("Unknown command")
        print()

print("hi")
