def find_duplicates(xs):
    seen = set()
    duplicates = set()

    for item in xs:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)