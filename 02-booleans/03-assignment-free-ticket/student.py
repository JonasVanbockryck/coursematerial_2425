# write your code here

def free_ticket(age):
    gets_ticket = False
    if age < 12:
        gets_ticket = True
    elif age >= 65:
        gets_ticket = True
    
    return gets_ticket