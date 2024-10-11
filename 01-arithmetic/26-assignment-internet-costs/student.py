# write your code here
# this probably wasn't the intended solution. too bad
from math import ceil

def internet_costs(duration_in_seconds, cost_per_block):
    # one block is 360 seconds long. even a single second over that 360 seconds is another block, so round up. 
    block_amounts = ceil(duration_in_seconds/360)
    total_cost = cost_per_block * block_amounts

    return total_cost