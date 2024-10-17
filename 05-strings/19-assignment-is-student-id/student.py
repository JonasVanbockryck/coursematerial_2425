# write your code here
# A student id must count exactly eight characters.
# The first character must be an r or an s. Both upper and lowercase are acceptable.
# The remaining seven characters must all be digits.

def is_student_id(string):
    is_8_char = False
    first_char_is_r_or_s = False
    is_digit = False
    final_result = False

    # Check 1. If the length of the string is equal to 8, then true.
    if len(string) == 8:
        is_8_char = True
    
    # If the first number in our string has "r" or "s" then return true.
    # lower() is used to turn them lowercase to not be case sensitive.
    # in is used to calculate and see if r or s are in the first number of the string.
    if string[0].lower() in ['r', 's']:
        first_char_is_r_or_s = True 

    # if the rest of the string (1 and greater) is a digit, return true
    # slicing is used here to slice off everything after 1
    if string[1:].isdigit():
        is_digit = True
    
    # if all the wellness checks returned true, then the final result means "yeperinyo everything's fine here"
    if is_8_char == True and first_char_is_r_or_s == True and is_digit == True:
        final_result = True
    
    return final_result