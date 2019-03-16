from _thread import start_new_thread as newThread
from app import database

DataBase = database.DataBase
import secrets

class Chat:
    def __init__(self):
        self.users = {}
        self.online = True

        self.database = DataBase("user_credentials")

    def loginUser(self, username, userHash):
        if not self.check_user(username, userHash):
            return ""
        else:
            self.users[secrets] = self.database.getUser(username)
            return username + srt(secrets.token_hex(20))

    def check_user(self, username, userHash):
        return self.database.validateUser(username, userHash)

    def exists(self, secret):
        self.users[secret]

    def get(self, username):
        return self.database.getUser(username)