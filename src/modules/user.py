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