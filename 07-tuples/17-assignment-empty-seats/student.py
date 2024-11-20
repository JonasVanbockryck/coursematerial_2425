# write your code here

def empty_seats(used_seats):
    max_seats = max(used_seats)
    len_seats = len(used_seats)
    final_result = max_seats - len_seats

    if len_seats == 0 or max_seats == 0:
        return None
    else:
        return final_result