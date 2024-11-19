def remove_backspaces(string):
    change = [('/')]

    for char, change in string:
        if char in string:
            string = string.replace(char, change)
    
    return string