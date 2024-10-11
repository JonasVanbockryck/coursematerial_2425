# write your code here

def is_valid_month(month): 
    valid = False
    if 1 <= month <= 12:
        valid = True
    
    return valid

def is_leap_year(year):
    leap_year = False

    # If the year is divisable by 4 AND ISN'T divisable by 100 it's a leap year.
    # If a year is divisible by 100 it's a leap year.
    # by the way the language the assignent uses to explain this is dogshit.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap_year = True

    return leap_year

def has_30_days(month):
    has_30 = False

    if month == 4 or month == 6 or month == 9 or month == 11:
        has_30 = True
    
    return has_30

# this is my worst code yet and I want to kill myself.
def has_31_days(month):
    has_31 = False

    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        has_31 = True
    
    return has_31

# Asked ChatGPT why this shit broke. turned out I forgot to.
# give the function to check for a leap year.... the year.
def has_28_days(month, year):
    final_result = False

    if month == 2:
        final_result = True
    if is_leap_year(year) == True and month == 2:
        final_result = False
    
    return final_result

def has_29_days(month, year):
    final_result = False

    if is_leap_year(year) == True and month == 2:
        final_result = True
    
    return final_result

# now time to write the bigboy function.

def is_valid_date(day, month, year):
    final_result = False

    # If this month has 30 days and less than or equal to 30 days, it's valid.
    # Repeat this for all other possible combo's.
    if has_30_days(month) == True and day <= 30:
        final_result = True
    elif has_31_days(month) == True and day <= 31:
        final_result = True
    elif has_28_days(month, year) == True and day <= 28:
        final_result = True
    elif has_29_days(month, year) == True and day <= 29:
        final_result = True
    
    return final_result