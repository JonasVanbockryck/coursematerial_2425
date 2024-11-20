# write your code here

def increase_version(version, breaking_change, new_features):
    num1, num2, num3 = version

    if breaking_change == True:
        num1 += 1
        num2 = 0
        num3 = 0
    elif new_features == True:
        num2 += 1
        num3 = 0
    else:
        num3 += 1
    
    return (num1, num2, num3)

def is_more_recent(v1, v2):
    return v1 > v2

def is_older(v1, v2):
    return v1 < v2