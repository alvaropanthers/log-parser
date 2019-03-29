import sys
from parser import get_data

file_path = "/var/log/auth.log"

if len(sys.argv) > 1:
    file_path = sys.argv[1]

with open(file_path, 'r') as f:
    objs = get_data(f)

for obj in objs:
    obj.print()

print(f"{len(objs)} objects found")
