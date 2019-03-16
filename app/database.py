import pymysql

class DataBase:
    def __init__(self, dbName):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.numbers = "1234567890"
        self.server = pymysql.connect(host="localhost", user="root", password="", db=dbName)

    def validateUser(self, username, givenHash):
        if not self.isValid(username, givenHash):
            return False
        try:
            with self.server.cursor() as cursor:
                query = "SELECT hash FROM users WHERE username = %s"
                cursor.execute(query, (str(username)))
                respond = cursor.fetchone()[0]
            print(respond + " =? " + givenHash)
            if respond == givenHash:
                return True
            else:
                return False
        except TypeError:
            return False
    def getUser(self, username):
        if not self.isUsernameValid(username):
            return {}
        try:
            with self.server.cursor() as cursor:
                query = "SELECT id, username FROM users WHERE username = %s"
                cursor.execute(query, (str(username)))
                respond = cursor.fetchone()
            print(respond)
            # ("id", "username")
            return {
                "id": respond[0],
                "username": respond[1]
            }
        except TypeError:
            return {}
    def addUser(self, username, givenHash):
        if not self.isValid(username, givenHash):
            return False
        try:
            with self.server.cursor() as cursor:
                query = "INSERT INTO users (username, hash) VALUES (%s, %s)"
                cursor.execute(query, (str(username), str(givenHash)))
            self.server.commit()
            return True
        except Exception as e:
            print("Error while adding a user error occurred: ", e)
            return False

    def isValid(self, username, givenHash):
        return self.isUsernameValid(username) and self.isHashValid(givenHash)

    def isUsernameValid(self, username):
        if not isinstance(username, str):
            return False
        acceptedCharacters = self.alphabet + self.alphabet.upper() + self.numbers
        temp = username
        for character in acceptedCharacters:
            temp = temp.replace(character, "")
        return temp == ""

    def isHashValid(self, givenHash):
        if not isinstance(givenHash, str):
            return False
        acceptedCharacters = self.alphabet + self.alphabet.upper() + self.numbers
        temp = givenHash
        for character in acceptedCharacters:
            temp = temp.replace(character, "")
        return temp == ""