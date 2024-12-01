def election_winner(votes):
    # if votes is empty, return none
    if not votes:
        return None

    frequency_dict = dict()

    for item in votes:
        # if the item is in our dictionary,  increase that elements count by 1
        if item in frequency_dict:
            frequency_dict[item] += 1
        # otherwise, set it to one in our dictionary
        else:
            frequency_dict[item] = 1
    
    # gets the one, highest value in our dictionary
    max_value = max(frequency_dict, key = frequency_dict.get)

    return max_value
