# write your code here

def is_capitalized(string):
    numba_one_is_capital = False
    rest_numba_is_lower = False

    if len(string) == 0:
        return False
    
    if string[0] == string[0].upper():
        numba_one_is_capital = True
    if string[1:] == string[1:].lower():
        rest_numba_is_lower = True
    
    if numba_one_is_capital == True and rest_numba_is_lower == True:
        return True
    else:
        return False