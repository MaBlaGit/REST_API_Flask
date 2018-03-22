import sqlite3


class UserModel:

    def __init__(self, id, username, user_email):
        self.id = id
        self.username = username
        self.user_email = user_email

    @classmethod
    def find_by_name(cls, name):
        users = list()
        connection = sqlite3.connect('./db/datashop.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM user WHERE username=?;'
        result = cursor.execute(query, (name,))
        rows = result.fetchall()
        if rows:
            for row in rows:
                users.append(UserModel(row[0], row[1], row[2]))
            return users
        connection.close()

    @classmethod
    def insert_into_table(cls, username, user_email ):
        connection = sqlite3.connect('./db/datashop.db')
        cursor = connection.cursor()
        query = 'INSERT INTO user VALUES(NULL, ?, ?)'
        cursor.execute(query, (username, user_email))
        connection.commit()
        connection.close()

    @classmethod
    def find_all(cls):
        users = list()
        connection = sqlite3.connect('./db/datashop.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM user;'
        result = cursor.execute(query)
        rows = result.fetchall()
        if rows:
            for row in rows:
                users.append(UserModel(row[0], row[1], row[2]))
            return users
        connection.close()

    def json(self):
        return {'id': self.id,
        'username': self.username,
        'user_email': self.user_email}
