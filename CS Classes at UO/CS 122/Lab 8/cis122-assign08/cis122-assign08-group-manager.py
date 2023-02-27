''' 
CIS 122 Fall 2020 Assignment 8
Author: Isabella Cortez
Credit: Jasmine Wallin and Lauren Mathews and Tori Walters
Description: Creates a dictionary that creates a group, lists the groups, adds data to to the group, and lists the data from the group
'''

d = {}
group = []

def create_group(d):
    '''
    description: has someone create a group when the user inputs the command
    args
        d (dictionary/string) = d is a dictionary where the inputs are being stored
    Returns:
        none
    '''
    print("** Create new group ** \n")

    while True:
        print()
        # prompt user for group name
        group_name = input("Enter group name (empty to cancel): ")

        # if nothing is entered function will break
        if group_name == "":
            break
        # if the name is in d already, it has already be entered
        elif group_name in d:
            print("Error, this name has already been entered")
        else:
            # dictionary
            temp = {}
            # list
            keys = []
            while True:
                # prompt user for field name
                field_name = input("Enter field name (empty to stop): ")
                if field_name == "":
                    break
                else:
                    keys.append(field_name)
                    
            temp['_keys_'] = keys
            temp['_data_'] = []
            d[group_name] = temp
        
def list_groups(d):
    '''
    description: shows the list of groups
    args
        d (dictionary/string) = d is a dictionary where the inputs are being stored
    Returns:
        none
    '''
    # prints out a list of groups with their properties
    print("** List of groups **")
    # counter = 0
    #range(len(group)
    
    for group_name in sorted(d):
        keys = ""
        for key in d[group_name]['_keys_']:
            if len(keys) > 0:
                keys += ", "
            keys += key
        print(group_name, ":" , str(len(d[group_name]['_keys_'])), "properties (" + keys + ")")

def add_group_data(d):
    '''
    description: adds the data of the different field names to the dictionary and lists
    args
        d (dictionary/string) = d is a dictionary where the inputs are being stored
    Returns:
        none
    '''
    print("** Add group data **")
    list_groups(d)

    while True:
        print()
        # prompts user for group to add data to
        group_name = input("Enter group (empty to cancel): ")
        # counter = 0
        
        # if there is no input, exit
        if group_name == "":
            break
        # if group name is not in dictionary, error message
        elif group_name not in d:
            print("Group name does not exist")
            list_groups(d)
        else:
            #d[input_group]['_data_'].append({})
            temp_dict = {}
            #['Title', "Artits"]
            for keys in d[group_name]['_keys_']:
                value = input("Enter "+keys+": ")
                temp_dict[keys] = value
            d[group_name]['_data_'].append(temp_dict)
        
def list_group_data(d):
    '''
    description: lists the data from each group 
    args
        d (dictionary/string) = d is a dictionary where the inputs are being stored
    Returns:
        none
    '''
    list_groups(d)

    while True:
        # prompt user for group name and this function will list the data from the group
        print()
        group_name = input("Enter group name (empty to cancel): ")

        # if nothing is entered, break
        if group_name == "":
            break
        # if group is not in the dictionary, error message
        elif group_name not in d:
            print("Error, group does not exist")
        else:
            for i in range(len(d[group_name]['_data_'])):
                group_data = ""
                for key in d[group_name]['_keys_']:
                    if len(group_data) > 0:
                        group_data += ", "
                    group_data += key
                    group_data += " = "
                    group_data += d[group_name]['_data_'][i][key]
                print(i, group_data)

print(">> Welcome to Group Manager <<")
print("This program creates groups with dynamic properties \n")
while True:
    input_command = str(input("Command (empty or X to quit, ? for help): ").strip().upper())
    # if user types ? show this list
    if input_command == "?":
        print("?: list commands")
        print("C: Create a new group")
        print("G: List groups")
        print("A: Add data to a group")
        print("L: list data for a group")
        print("X: Exit\n")
        
    # if user types C or c, create group
    elif input_command == "C":
        create_group(d)
        print()
    # if user types a or A, add data to groups function
    elif input_command == "A":
        add_group_data(d)
        print()
    # if user types g or G, show the groups
    elif input_command == "G":
        list_groups(d)
        print()
    # if user types l, show the data from the groups
    elif input_command == "L":
        list_group_data(d)
        print()
    # if user types in x or it is blank, exit the program
    elif input_command == "X": 
        print("Goodbye!")
        break
    else:
        print("Goodbye!")
        break
        

            



        
