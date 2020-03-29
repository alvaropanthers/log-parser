from datetime import datetime

_MONTHNUMBER = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Agu': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
_MONTHNAMES = [None, "Jan", "Feb", "Mar", "Apr", "May", "Jun",
                     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
class Log:
    def __init__(self, user, ip):
        self.users = [user]
        self.ip = ip

    def addUser(self, user):
        self.users.append(user)

    def print(self):
        print(f"ip: {self.ip};")
        print("users attempted:")
        for item in self.users:
            print(item)
        print("\n")
        
    def __str__(self):
        return f"user: {self.users[0].user} ip: {self.ip} port: {self.users[0].port}"

class User:
    def __init__(self, user, port, datetime, validuser):
        self.user = user
        self.port = port
        self.datetime = datetime
        self.validuser = validuser

    def print(self):
        return f"user: {self.user} port: {self.port}"

    def __str__(self):
        return f"(Valid user: {str(self.validuser)}), {self.datetime.ctime()} ; {self.user}, port: {self.port}"

class AuthLog:
    def __init__(self, filepath):
        self.filepath = filepath
        self._FAILED_LOC = 5
        self._IP_LOC = 12
        self._USERNAME_LOC = 10
        self._PORT_LOC = 14
        self._INVALID_LOC = 8
        self._FOR_LOC = 7
        self._VALID_USER_ADJUST = 2

    def print_log(self):
        records = self.parse_file()
        if records:
            for record in records:
                record.print()
        else:
            print("No data loaded")

    def print_raw_log(self):
        pass

    def parse_file(self):
        with open(self.filepath, 'r') as file:
            records = []
            for line in file:
                record = self.createRecord(line.strip().split(' '), records)
                if record:
                    records.append(record)

        return records

    def createRecord(self, line, data):
        if (0 <= len(line) < 14) or line[self._FAILED_LOC] != 'Failed':
            return None

        invalid = line[self._INVALID_LOC] == 'invalid'
        adjust = 0 if invalid else self._VALID_USER_ADJUST
        ip = line[self._IP_LOC - adjust]
        username = line[self._USERNAME_LOC - adjust]
        port = line[self._PORT_LOC - adjust]

        time = [ int(item.lstrip('0')) for item in line[2].split(':') ]
        today = datetime.now().replace(month=_MONTHNUMBER[line[0]], day=int(line[1].lstrip('0')), hour=time[0], minute=time[1], second=time[2])
        user = User(username, port, today, not invalid)
                
        for i in range(len(data)):
            if data[i].ip == ip:
                data[i].addUser(user)
                return None

        return Log(user, ip)
