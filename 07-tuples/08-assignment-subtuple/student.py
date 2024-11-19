# write your code here
def subtuple(xs, ys):
    length_ys = len(ys)
    length_xs = len(xs)
    
    if length_ys == 0:
        return True
    
    for i in range(length_xs - length_ys + 1):
        if xs[i:i + length_ys] == ys:
            return True 
    
    return False