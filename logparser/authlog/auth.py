from parse.parser import parse
from modules.date import Date
from modules.log import Log
from modules.user import User

def call_back(line, data):
    if len(line) == 0:
        return None

    ip = username = port =  ''
    validuser = False
    returnNew = True

    if len(line) >= 14 and line[5] == 'Failed':
        if line[8] == 'invalid':
            ip = line[12]
            username = line[10]
            port = line[14]
            validuser = False 
        elif line[7] == 'for':
            ip = line[10]
            username = line[8]
            port = line[12]
            validuser = True 
            
        if ip != '':
            for i in range(0, len(data)):
                if data[i].ip == ip:
                    data[i].users.append(User(username, port, Date(month = line[0], day = line[1], time = line[2]), validuser))
                    returnNew = False
                    break

    if username != '' and port != '' and ip != '' and returnNew:
        return Log(User(username, port, Date(month = line[0], day = line[1], time = line[2]), validuser), ip)
    
    return None

def parse_file(fileName):
    return parse(fileName, call_back)