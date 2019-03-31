class Log:
    def __init__(self, user, ip, invalid_user):
        self.users = [user]
        self.ip = ip
        self.invalid_user = invalid_user

    def print(self):
        print(f"ip: {self.ip}; valid user: {str(self.invalid_user)};")
        print("users attempted:")
        for item in self.users:
            print(item)
        print("\n")
        
    def __str__(self):
        return f"user: {self.users[0].user} ip: {self.ip} port: {self.users[0].port} valid user: {str(self.invalid_user)}"