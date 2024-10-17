# write your code here
# let's go in steps.
# step 1: remove the () from the string.
# step 2, find the location of the ","

def parse_position_x(string):
    where_comma = (string).find(",")

    x_pos = string[1:where_comma]

    return float(x_pos)

def parse_position_y(string):
    where_comma = (string).find(",")
    where_end = (string).find(")")

    y_pos = float(string[where_comma+1:where_end])

    return y_pos
