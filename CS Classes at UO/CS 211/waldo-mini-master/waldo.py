"""
Name: Isabella Cortez

Project: Where's Waldo

Credits: Quinn Rainen, Catherine Raj, Jayden Ben

Description: This is a little exercise in the logic of "for all" and "there exists".
"For all" and "There exists", in rows and columns of a matrix
"""

Waldo = "W"
Other = "."

def all_row_exists_waldo(waldo_matrix) -> bool:
    row_length = len(waldo_matrix)
    counter = 0
    for rows in waldo_matrix:
        if Waldo in rows:
            counter += 1
    if counter == row_length:
        return True
    else:
        return False

def all_col_exists_waldo(waldo_matrix) -> bool:
    row_length = len(waldo_matrix)
    if row_length == 0:
        return True
    col_length = len(waldo_matrix[0])
    if col_length == 0:
        return True
    for cols in range(col_length):
        counter = 0
        for rows in range(row_length):
          if Waldo in waldo_matrix[rows][cols]:
              counter += 1
        if counter == 0:
            return False
    return True

def all_row_all_waldo(waldo_matrix) -> bool:
    if len(waldo_matrix) == 0:
        return True
    for rows in waldo_matrix:
        for objects in rows:
            if Waldo not in objects:
                return False
    return True

def all_col_all_waldo(waldo_matrix) -> bool:
    if len(waldo_matrix) == 0:
        return True
    for cols in waldo_matrix:
        for objects in cols:
            if Waldo not in objects:
                return False
    return True

def exists_row_all_waldo(waldo_matrix) -> bool:
    if len(waldo_matrix) == 0:
        return False
    else:
        if len(waldo_matrix[0]) == 0:
            return True
        else:
            pass
    for rows in waldo_matrix:
        for object in rows:
            if all(object == Waldo for object in rows):
                return True
            else:
                pass
    return False

def exists_col_all_waldo(waldo_matrix) -> bool:
    counter = 0
    if len(waldo_matrix) == 0:
        return False
    else:
        if len(waldo_matrix[0]) == 0:
            return False
        else:
            pass
    for col in waldo_matrix[0]:
        if col is Waldo:
            the_index = waldo_matrix[0].index(Waldo)
            counter += the_index
    i = len(waldo_matrix) - 2
    while i > 0:
        if waldo_matrix[i][counter] == waldo_matrix[1 + i][counter]:
            i -= 1
            pass
        else:
            return False
    return True

def exists_row_exists_waldo(waldo_matrix) -> bool:
    if len(waldo_matrix) == 0:
        return False
    for rows in waldo_matrix:
        for object in rows:
            if object == Waldo:
                return True
            else:
                pass
    return False

def exists_col_exists_waldo(waldo_matrix) -> bool:
    if len(waldo_matrix) == 0:
        return False
    for cols in waldo_matrix:
        for object in cols:
            if object == Waldo:
                return True
            else:
                pass
    return False
