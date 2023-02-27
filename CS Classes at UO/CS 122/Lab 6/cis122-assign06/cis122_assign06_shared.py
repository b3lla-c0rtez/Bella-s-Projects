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

    
