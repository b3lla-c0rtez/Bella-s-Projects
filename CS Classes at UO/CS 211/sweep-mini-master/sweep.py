"""
Mini-Project: sweep

Name: Isabella Cortez

Credits: Office Hours

practicing writing a functions, looping, and creating lists
"""

def all_same(l: list) -> bool:
    """determines if items in a list are all the same
        Args:
            l: list of items
        Returns:
            bool: checks if list items are the same
    """
    if len(l) == 0:
        return True
    else:
        new_value = l[0]
        for item in range(len(l)):
            if new_value != l[item]:
                return False
        return True

def dedup(l: list) -> list:
    """returns a list with no duplicate values
        Args:
            l: list of items
        Returns:
            list: list of items with no duplicate items
    """
    if len(l) == 0:
        return []
    else:
        newList = []
        for item in l:
            if item not in newList:
                newList.append(item)
        return newList

def max_run(l: list) -> int:
    """returns the value that appears the most in incremental order
        Args:
            l: list of items
        Returns:
            int: returns the value that appears the most in the list
    """
    if len(l) == 0:
        return 0
    else:
        first_value = l[0]
        long_list = 0
        next_value = 0
        for item in range(len(l)):
            if first_value == l[item]:
                next_value += 1
                if next_value > long_list:
                    long_list = next_value
            else:
                first_value = l[item]
                next_value = 1
        return long_list