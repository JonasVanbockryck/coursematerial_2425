# write your code here
# hmm, idk how to do this one. let's try it by cheating.

# using this library I can just tell it to calculate median for me (aka the median number from a list)
import statistics

# huzzah! I got the actual solution, I think?
# if you wanna find the middle number, just remove the smallest and the biggest number. shrimple
def middle(a, b, c):
    least_num = min(a, b, c)
    biggest_num = max(a, b, c)
    middle_num = ((a + b + c) - least_num) - biggest_num

    return middle_num

def falsemiddle(a, b, c): 
    x = [a, b, c]
    final_result = statistics.median(x) 

    return final_result