d = {}
group = []
field = []
def create_group(d):
    print("** Create new group ** \n")

    while True:
        group_name = str(input("Enter group name (empty to cancel): "))
        
        if group_name == "":
            break
        elif group_name in group:
            print("Error, this name has already been entered")
        while True:
            field_name = input("Enter field name (empty to stop): ")
            
            if field_name == "":
                field.append(field_name)
                break
            else:
                field.append(field_name)
                print()
                
    group.append(group_name)

print(">> Welcome to Group Manager <<")
print("This program creates groups with dynamic properties \n")
while True:
    input_command = str((input("Command (empty or X to quit, ? for help): ").strip()).upper())
    if input_command == "?":
        print("?: list commands")
        print("C: Create a new group")
        print("G: List groups")
        print("A: Add data to a group")
        print("L: list data for a group")
        print("X: Exit\n")
        
    elif input_command == "C":
        create_group(d)
        print()
    elif input_command == "A":
        add_group_data(d)
        print()
    elif input_command == "G":
        list_group(d)
        print()
    elif input_command == "L":
        list_group_data(d)
        print()
    elif input_command == "X":  
        print("Goodbye!")
        break
    elif input_command == "":
        print("Goodbye!")
        break
    else:
        print("Must be one of the commands")
        break
