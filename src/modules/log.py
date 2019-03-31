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