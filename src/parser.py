from modules.log import Log
from modules.user import User
from modules.date import Date

MONTH_SPACE_INDEX = 0
DAY_SPACE_INDEX = 1
TIME_SPACE_INDEX = 2

def parse_file(file):
    found = []
    for line in file:
        start = whsp_count =  0
        ip = user = port = day = month = time = prevline = '' 
        contains = invalid_user = False

        for index, char in enumerate(line):
            currentline = line[start:index]
            if  currentline == 'Failed':
                contains = True

            if char == ' ':
                if not month and whsp_count == MONTH_SPACE_INDEX:
                    month = currentline
                elif not day and whsp_count == DAY_SPACE_INDEX:
                    day = currentline
                elif not time and whsp_count == TIME_SPACE_INDEX:
                    time = currentline
                
                if contains and not user and (prevline == 'user' or (prevline == 'for' and currentline != 'invalid')):
                    if prevline == 'for':
                        invalid_user = False
                    else:
                        invalid_user = True
                    user = currentline
                elif contains  and not ip and prevline == 'from':
                    ip = currentline
                elif contains and not port and prevline == 'port':
                    port = currentline

                prevline = currentline
                start = index + 1
                whsp_count += 1
                
        if user and ip and port and month and day and time:
            encounter = False
            if len(found) > 0:
                for item in found:
                    if item.ip == ip:
                        item.users.append(User(user, port, Date(month, day, time), invalid_user))
                        encounter = True

            if not encounter:
                found.append(Log(User(user, port, Date(month, day, time), invalid_user), ip))

    return found