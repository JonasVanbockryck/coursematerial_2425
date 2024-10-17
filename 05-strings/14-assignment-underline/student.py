# write your code here

def underline(string):
    length_string = len(string)
    second_line = "-" * length_string
    final_string = string + "\n" + second_line

    return final_string