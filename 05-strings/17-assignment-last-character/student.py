# write your code here

def last_character(string):
    # index counts from 0, but length counts from 1. this gets us the index number
    index_numba = (len(string)) - 1

    # our result is None by default. this is to account for a blank response.
    final_result = None

    # if our index number is exactly 0, result is 0. otherwise, result is index number.
    if index_numba == 0:
        final_result = string[0]
    elif index_numba >= 1:
        final_result = string[index_numba]
    
    return final_result