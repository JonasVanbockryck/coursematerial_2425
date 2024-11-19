# write your code here

def thanos(queue_size, target_size):
    i = queue_size
    snaps_needed = 0

    # while I is greater than the target size, halve I and then add an extra 1 to the count.
    # if you do greater than or equals then he'll do an extra snap, which we don't want
    while i > target_size:
        i = (i / 2)
        snaps_needed = snaps_needed + 1
    
    return (snaps_needed)
