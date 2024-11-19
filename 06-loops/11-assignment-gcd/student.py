def gcd(x, y):
    # turns x and y into their absolute value, as gcd doesn't care about negative/positive.
    x, y = abs(x), abs(y)

    # while y is not equal to 0, x is equal to y, and y is equal to x modulo y.
    # when y becomes 0, x becomes the GCD
    while y != 0:
        x, y = y, x % y
    
    return x