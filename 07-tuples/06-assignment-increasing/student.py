# write your code here

def increasing(sn):
    length_sn = len(sn)

    for i in range(length_sn - 1):
        if sn[i] > sn[i+1]:
            return False
    
    return True