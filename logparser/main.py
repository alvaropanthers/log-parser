import sys
import argparse
from authlog import AuthLog

if __name__ == '__main__':
    parse = argparse.ArgumentParser(description="Parse Authlog file")
    parse.add_argument('--path', help="Path to Auth.log", default="auth.log")
    args = parse.parse_args()
    authLog = AuthLog(args.path)
    authLog.print_log()
    