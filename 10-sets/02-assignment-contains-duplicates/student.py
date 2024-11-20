def contains_duplicates(xs):
    # converts xs to a set (which removes all duplicates).
    # if they're not the same length as the list, then there were duplicates.
    setxs = set(xs)

    if len(xs) != len(setxs):
        return True
    else:
        return False