def invest(amount, rate, goal):
    i = amount
    year_count = 0

    while i < goal:
        i = i * (1 + rate / 100)
        year_count = year_count + 1
    
    return year_count