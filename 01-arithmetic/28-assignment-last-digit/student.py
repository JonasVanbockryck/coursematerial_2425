# write your code here

def last_digit(n):
    # this just rounds down our N.
    rounded_n = round(n)
        
    final_result = min(rounded_n % 10, 9)

    return final_result

