def count_lines_in_file(path):
    with open(path) as file:
        lines = file.readlines()

    return len(lines)