# write your code 

# write your code here
# I can just use my cold here.

def cake4(eggs, flour, butter, sugar, eggs_per_cake, flour_per_cake, butter_per_cake, sugar_per_cake):
    n_eggs = eggs/eggs_per_cake
    n_flour = flour/flour_per_cake
    n_butter = butter/butter_per_cake
    n_sugar = sugar/sugar_per_cake
    n_cakes =  (min(n_eggs, n_flour, n_butter, n_sugar))

    return n_cakes
        