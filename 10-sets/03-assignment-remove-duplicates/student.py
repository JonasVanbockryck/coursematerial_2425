def remove_duplicates(xs):
    # we make an empty set so that we don't get duplicates, and an empty list (so we can preserve duplicates)
    seen = set()
    result = []

    # for every entry into the list "xs", if it's not in our set, add it to our set and to our list. 
    # this creates a list with the same order as "xs", but no duplicates
    for item in xs:
        if item not in seen:
            result.append(item)
            seen.add(item)

    return result