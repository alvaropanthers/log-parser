import sys
from parser import parse
from date import Date
from log import Log
from user import User

DEFAULT_FILE_PATH = "/var/log/auth.log"

if len(sys.argv) > 1:
    DEFAULT_FILE_PATH = sys.argv[1]

def call_back(line, data):
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

    if username.strip() != '' and port.strip() != '' and ip.strip() != '' and returnNew:
        return Log(User(username, port, Date(month = line[0], day = line[1], time = line[2]), validuser), ip)
    
    return None

objs = parse(DEFAULT_FILE_PATH, ' ', call_back, True)

for obj in objs:
    obj.print()

print(f"{len(objs)} objects found")