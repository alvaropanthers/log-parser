import sys
from parser import parse
from user import User

DEFAULT_FILE_PATH = "/etc/passwd"

if len(sys.argv) > 1:
    DEFAULT_FILE_PATH = sys.argv[1]

objs = parse(DEFAULT_FILE_PATH, ':')

users = []
for item in objs:
    username = password = uid = gid = gecos = hmdir = logshell = ''
    for index, cuser in enumerate(item):
        if index == 0:
            username = cuser
        elif index == 1:
            password = cuser
        elif index == 2:
            uid = cuser
        elif index == 3:
            gid = cuser
        elif index == 4:
            gecos = cuser
        elif index == 5:
            hmdir = cuser
        elif index == 6:
            logshell = cuser
    users.append(User(username, password, uid, gid, gecos, hmdir, logshell))

for user in users:
    print(user)

print(f"{len(users)} objects found")