def remove_empty_lines(source, destination):
    with open (source, 'r') as file:
        input_lines = file.readlines()

    new_lines = []
    
    # making a new space is done at the end of your sentence and is just a "\n" at the end of it. then readlines makes a new "string" in the list
    # a white space line is a line with only "\n" inside of it. 
    for lines in input_lines:
        if lines == "\n":
            # removes all spaces and "\n"
            lines.strip()
        else:
            new_lines.append(lines)
    
    with open (destination, 'w') as file:
        file.writelines(new_lines)