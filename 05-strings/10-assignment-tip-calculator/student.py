# write your code here
def tip_calculator():
    # asks for total price in a string form. then converts to int.
    total_price = int(input("Enter total price: "))
    # asks for tip percentage in string form, then converts to int.
    tip_percentage = input("Enter tip percentage (default=20): ")

    # a check to make sure our percentage defaults to 20% if none is given.
    if tip_percentage == '':
        tip_percentage = 20
    else:
        tip_percentage = int(tip_percentage)

    # Calculates the amount of tip we gotta pay. 
    tip_amount = total_price * (tip_percentage / 100)

    # money. round down
    final_money_price = round(total_price + tip_amount)

    print (f"You have to pay {final_money_price}")

# so that we can make it executable I guess
if __name__ == "__main__":
    tip_calculator()


