import sys
from authlog.auth import parse_file

DEFAULT_FILE_PATH = "/var/log/auth.log"

if len(sys.argv) > 1:
    DEFAULT_FILE_PATH = sys.argv[1]

data = parse_file(DEFAULT_FILE_PATH)

if data:
    for item in data:
        item.print()
else:
    print("No data loaded")