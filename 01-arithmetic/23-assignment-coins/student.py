# write your code here

def coins (amount):
    c5 = amount // 5
    amount_after_1 = amount - (5 * c5)

    c2 = amount_after_1 // 2
    amount_after_2 = amount_after_1 - (2 * c2) #made a typo here and lost 20 minutes. I love my life

    c1 = amount_after_2

    final_count = c5 + c2 + c1
    return final_count
