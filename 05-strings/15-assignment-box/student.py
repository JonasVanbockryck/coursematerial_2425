# write your code here
# So, let's conceptualize it. Top line should be the same length as the bottom line and the first and last characters are a +.
# middle line should be a "|" then a space, then the line, then a space, then a "|"
# bottom line same as before

def box(string):
    length_string = len(string)

    line_one = "+" + ("-" * (length_string + 2)) + "+"
    line_two = "| " + string + " |"

    final_result = line_one + "\n" + line_two + "\n" + line_one

    return final_result