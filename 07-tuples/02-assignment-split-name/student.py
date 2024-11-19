# write your code here

def split_name(full_name):
    # find space location
    space_location = full_name.index(' ')
    # find the first name up to the space
    name_one = full_name[0:space_location]
    # go after the space, to the rest of the string
    name_two = full_name[space_location + 1:]

    return (name_one, name_two)
