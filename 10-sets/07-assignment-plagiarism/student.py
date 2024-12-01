def plagiarism(s1, s2):
    # Split the strings into lines and convert them to sets
    lines1 = set(s1.splitlines())
    lines2 = set(s2.splitlines())
    
    # Find the intersection of the two sets
    common_lines = lines1.intersection(lines2)
    
    # Return the number of unique common lines
    return len(common_lines)
        