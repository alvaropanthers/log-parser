class User:
    def __init__(self, username, password, uid, gid, gecos, hmdir, logshell):
        self.username = username
        self.password = password
        self.uid = uid
        self.gid = gid
        self.gecos = gecos
        self.hmdir = hmdir
        self.logshell = logshell

    def __str__(self):
        return f'username: {self.username} password: {self.password} uid: {self.uid} gid: {self.gid} gecos: {self.gecos} hmdir: {self.hmdir} logshell: {self.logshell}'