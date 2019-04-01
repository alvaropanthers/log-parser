def break_string(string, delimiter):
    items = []
    start = 0
    for index, char in enumerate(string):
        if char == delimiter or index == (len(string) - 1):
            items.append(string[start:index])
            start = index + 1
    
    return items

def parse_file(file, delimiter, call_back, pdata = False):
    found = []
    for line in file:
        sttr = break_string(line, delimiter)
        if pdata:
            retval = call_back(sttr, found)
        else:
            retval = call_back(sttr)

        if retval:
            found.append(retval)

    return found

def parse(path, delimiter, call_back, pdata = False):
    with open(path, 'r') as f:
        items = parse_file(f, delimiter, call_back, pdata)

    return items