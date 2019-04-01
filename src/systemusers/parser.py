def break_string(string, delimiter):
    items = []
    start = 0
    for index, char in enumerate(string):
        if char == delimiter or index == (len(string) - 1):
            items.append(string[start:index])
            start = index + 1
    
    return items

def parse_file(file, delimiter, call_back):
    found = []
    for line in file:
        sttr = break_string(line, delimiter)
        found.append(call_back(sttr))

    return found

def parse(path, delimiter, call_back):
    with open(path, 'r') as f:
        items = parse_file(f, delimiter, call_back)

    return items