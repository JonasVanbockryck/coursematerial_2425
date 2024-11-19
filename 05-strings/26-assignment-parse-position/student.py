# write your code here
# let's go in steps.
# step 1: remove the () from the string.
# step 2, find the location of the ","

def parse_position_x(string):
    # finds coma location
    where_comma = (string).find(",")

    # x pos is after the (), so we go from after the first string and cut off the coma and everything after
    x_pos = string[1:where_comma]

    # returns float not string
    return float(x_pos)

def parse_position_y(string):
    where_comma = (string).find(",")
    where_end = (string).find(")")

    # this selects our y from everywhere after the comma and cuts off the ending brackets and everything after dat.
    # then makes it float not string
    y_pos = float(string[where_comma+1:where_end])

    return y_pos
