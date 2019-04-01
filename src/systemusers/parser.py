def break_string(string, delimiter):
    items = []
    start = 0
    for index, char in enumerate(string):
        if char == delimiter or index == (len(string) - 1):
            items.append(string[start:index])
            start = index + 1
    
    return items

def parse_file(file, delimiter):
    found = []
    for line in file:
        found.append(break_string(line, delimiter))

    return found

def parse(path, delimiter):
    with open(path, 'r') as f:
        items = parse_file(f, delimiter)

    return items