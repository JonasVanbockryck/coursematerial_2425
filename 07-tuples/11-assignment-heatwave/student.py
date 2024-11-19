# write your code here

def heatwave(temperatures):
    length = len(temperatures)
    count_25 = 0
    count_30 = 0

    for i in range(length):
        if temperatures[i] >= 25:
            count_25 += 1
            if temperatures[i] >= 30:
                count_30 += 1

        else:
            count_25 = 0
            count_30 = 0
        if count_25 >= 5 and count_30 >= 3:
            return True
        
    return False 