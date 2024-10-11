# write your code here

def drop_last_digit(n):
    # this just finds us the last digit of our "n" number
    last_digit = n % 10

    # this grabs our N and removes the previous amount of the last number, then divided by 10 to fully remove our last digit.
    final_result = (n - last_digit) // 10

    return final_result