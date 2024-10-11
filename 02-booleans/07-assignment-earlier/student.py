# write your code here

def earlier(h1, m1, h2, m2):
    earlier_time = False
    converted_time_1 = (h1 * 60) + m1
    converted_time_2 = (h2 * 60) + m2

    if converted_time_1 < converted_time_2:
        earlier_time = True
    
    return earlier_time
