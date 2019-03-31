class User:
    def __init__(self, user, port, date):
        self.user = user
        self.port = port
        self.date = date

    def print(self):
        return f"user: {self.user} port: {self.port}"

    def __str__(self):
        return f"{self.date.month} {self.date.day} {self.date.time}; {self.user}, (port: {self.port})"