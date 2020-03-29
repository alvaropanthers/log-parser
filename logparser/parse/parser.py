def parse(path, call_back):
    with open(path, 'r') as file:
        records = []
        for line in file:
            retval = call_back(line.split(' '), records)
            if retval:
                records.append(retval)
    
    return records
    