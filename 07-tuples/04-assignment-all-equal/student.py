# write your code here

def all_equal(xs):
    aiy = len(xs)
    if aiy <= 1:
        return True

    # we make our range the length of our tuple -1, so that we don't end up comparing the last entry of our list to nothing.
    # we continue looping, only reporting something if our loop fails. 
    # if we find no errors, we return True
    for i in range(aiy - 1):
        if xs[i] != xs[i+1]:
            return False
    
    return True