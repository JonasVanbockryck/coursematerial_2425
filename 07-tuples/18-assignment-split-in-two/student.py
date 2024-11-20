# write your code here

def split_in_two(xs):
    split_two = len(xs) // 2

    x = xs[:split_two]
    y = xs[split_two:]

    return (x, y)