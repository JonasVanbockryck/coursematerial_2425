# write your code here
def passing_percentage(grades):
    length = len(grades)
    pass_num = 0
    fail_num = 0

    # go through every entry in "grades", if they pass add a number to var 1, otherwise add to var 2
    for i in range(length):
        if grades[i] >= 10:
            pass_num += 1
        else:
            fail_num += 1

    
    sum_num = pass_num + fail_num
    final_calc = (pass_num/sum_num)*100

    return final_calc