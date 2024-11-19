# write your code here
def all_different(xs):
    aiy = len(xs)
    if aiy <= 1:
        return True

    # start our outer loop I, checking through every single entry into our tupple
    for i in range(aiy):
        # then our loop J starts after outer loop I, going through every other entry in I.
        for j in range (i + 1, aiy):
            # then it checks our outer loop I against everything else in our tuple.
            if xs[i] == xs[j]:
                return False
    
    return True