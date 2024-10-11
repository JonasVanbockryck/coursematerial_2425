# write your code here
# modulo is a function that divides number 1 by number 2 and then sees what the rest is.
# therefore, if there is no "rest" (aka we get a 0), then it's divisible perfectly
# if module has a remainder then it's not divisble and we get a false!

def is_divisible(a, b):
    yep_its_divisible = False
    if a % b == 0:
        yep_its_divisible = True
    
    return yep_its_divisible
