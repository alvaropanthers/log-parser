class Log:
    def __init__(self, user, ip):
        self.users = [user]
        self.ip = ip

    def print(self):
        print(f"ip: {self.ip};")
        print("users attempted:")
        for item in self.users:
            print(item)
        print("\n")
        
    def __str__(self):
        return f"user: {self.users[0].user} ip: {self.ip} port: {self.users[0].port}"

class User:
    def __init__(self, user, port, date, validuser):
        self.user = user
        self.port = port
        self.date = date
        self.validuser = validuser

    def print(self):
        return f"user: {self.user} port: {self.port}"

    def __str__(self):
        return f"(Invalid user: {str(self.validuser)}), {self.date.month} {self.date.day} {self.date.time}; {self.user}, (port: {self.port})"

class Date:
    def __init__(self, month, day, time):
        self.month = month
        self.day = day
        self.time = time

class AuthLog:
    def __init__(self, filepath):
        self.filepath = filepath
        self.FAILED_LOC = 5
        self.IP_LOC = 12
        self.USERNAME_LOC = 10
        self.PORT_LOC = 14
        self.INVALID_LOC = 8
        self.FOR_LOC = 7
        self.VALID_USER_ADJUST = 2

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
                retval = self.call_back(line.strip().split(' '), records)
                if retval:
                    records.append(retval)

        return records

    def call_back(self, line, data):
        lineLen = len(line)
        if (0 <= lineLen < 14) or line[self.FAILED_LOC] != 'Failed':
            return None

        ip = username = port =  ''
        validuser = False

        if line[self.INVALID_LOC] == 'invalid':
            ip = line[self.IP_LOC]
            username = line[self.USERNAME_LOC]
            port = line[self.PORT_LOC]
            validuser = False 
        else:  # line[FOR_LOC] == 'for'
            ip = line[self.IP_LOC - self.VALID_USER_ADJUST]
            username = line[self.USERNAME_LOC - self.VALID_USER_ADJUST]
            port = line[self.PORT_LOC - self.VALID_USER_ADJUST]
            validuser = True 
                
        for i in range(len(data)):
            if data[i].ip == ip:
                data[i].users.append(User(username, port, Date(month = line[0], day = line[1], time = line[2]), validuser))
                return None

        return Log(User(username, port, Date(month = line[0], day = line[1], time = line[2]), validuser), ip)

