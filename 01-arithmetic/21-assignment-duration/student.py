# write your code here

# duration here is duration in seconds. 
def hours(duration):
    n_time_in_hours = duration//3600
    return n_time_in_hours

def minutes(duration):
    h = hours(duration)
    leftover = duration - (3600 * h)
    n_time_in_minutes = leftover//60
    return n_time_in_minutes


def seconds(duration):
    h = hours(duration)
    m = minutes(duration)
    remove_hours = duration - (3600 * h)
    remove_minutes = remove_hours - (60 * m)

    return remove_minutes
    
