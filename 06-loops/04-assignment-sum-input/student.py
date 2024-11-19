# write your code here

def sum_input():
    i = int(input("Enter integer: "))
    stored_numba = 0

    while i != 0:
        stored_numba = stored_numba + i
        i = int(input("Enter integer: "))
    
    print ("The sum equals " + str(stored_numba) + ".")

