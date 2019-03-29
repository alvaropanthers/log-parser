class User:
    def __init__(self, user, port):
        self.user = user
        self.port = port

    def print(self):
        return f"user: {self.user} port: {self.port}"

    def __str__(self):
        return f"{self.user}, (port: {self.port})"

class Log:
    def __init__(self, user, ip, invalid_user):
        self.users = [user]
        self.ip = ip
        self.invalid_user = invalid_user

    def print(self):
        print(f"ip: {self.ip}; valid user: {str(self.invalid_user)};")
        print("users:")
        for item in self.users:
            print(item)
        print("\n")
        
    def __str__(self):
        return f"user: {self.users[0].user} ip: {self.ip} port: {self.users[0].port} valid user: {str(self.invalid_user)}"

def get_data(file):
    found = []
    for line in file:
        start = index = 0
        prev_line = ''
        ip = '' 
        user = '' 
        port = ''
        contains = False
        invalid_user = False

        for index, char in enumerate(line):
            if line[start:index] == 'Failed':
                contains = True
            
            if line[start:index] == 'invalid':
                invalid_user = True

            if char == ' ':
                if contains and (prev_line == 'user' or prev_line == 'for'):
                    user = line[start:index] 
                elif contains  and not ip and prev_line == 'from':
                    ip = line[start:index]
                elif contains and not port and prev_line == 'port':
                    port = line[start:index]
                prev_line = line[start:index]
                start = index + 1
                
        if user and ip and port:
            encounter = False
            if len(found) > 0:
                for item in found:
                    if item.ip == ip:
                        if user and port:
                            item.users.append(User(user, port))
                            encounter = True
            if not encounter and user and port and ip and invalid_user:
                found.append(Log(User(user, port), ip, invalid_user))

    return found