from _thread import start_new_thread as newThread
from app import database

DataBase = database.DataBase
import secrets

class Chat:
    def __init__(self):
        self.users = {}
        self.online = True
        self.chatlog = []
        self.database = DataBase("user_credentials")

    def loginUser(self, username, userHash):
        if not self.check_user(username, userHash):
            return ""
        else:
            secret = secrets.token_hex(20)
            self.users[username + str(secret)] = self.database.getUser(username)
            print("Creating secret!")
            return username + str(secret)

    def getLog(self):
        return self.chatlog

    def addMessage(self, message):
        self.chatlog.append(message)

    def check_user(self, username, userHash):
        return self.database.validateUser(username, userHash)

    def exists(self, secret):
        try:
            x=self.users[secret]
            return True
        except KeyError:
            return False

    def get(self, secret):
        return self.users[secret]