def remove_duplicate_lines(source, destination):
    with open(source, 'r') as file:
        lines = file.readlines()
    
    # Ensure we always write the last line
    new_lines = []

    for i in range(len(lines) - 1):
        if lines[i] != lines[i + 1]:
            new_lines.append(lines[i])
    
    # Always include the last line
    if lines:
        new_lines.append(lines[-1])
    
    with open(destination, 'w') as file:
        file.writelines(new_lines)