import sys
from parser import parse
from user import User

DEFAULT_FILE_PATH = "/etc/passwd"

if len(sys.argv) > 1:
    DEFAULT_FILE_PATH = sys.argv[1]

def call_back(buff):
    return User(buff[0], buff[1], buff[2], buff[3], buff[4], buff[5], buff[6])

objs = parse(DEFAULT_FILE_PATH, ':', call_back)

for user in objs:
    print(user)

print(f"{len(objs)} objects found")