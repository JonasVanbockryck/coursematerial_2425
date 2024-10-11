# write your code here

def close_enough(x, y):
    close = False
    difference_num = x - y

    if x == y:
        close = True
    elif -0.1 <= difference_num <= 0.1:
        close = True
    
    return close