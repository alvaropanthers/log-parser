import sys
from parser import parse_file

DEFAULT_FILE_PATH = "/var/log/auth.log"

if len(sys.argv) > 1:
    DEFAULT_FILE_PATH = sys.argv[1]

with open(DEFAULT_FILE_PATH, 'r') as f:
    objs = parse_file(f)

for obj in objs:
    obj.print()

print(f"{len(objs)} objects found")
