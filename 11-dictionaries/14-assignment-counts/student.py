def counts(xs):
    # create a new dictionary
    frequency_dict = {}

    # iterates through every item in xs
    for item in xs:
        # if the item is in our dictionary,  increase that elements count by 1
        if item in frequency_dict:
            frequency_dict[item] += 1
        # otherwise, set it to one in our dictionary
        else:
            frequency_dict[item] = 1
            
    return frequency_dict