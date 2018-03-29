import sqlite3


class UserModel:

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('./db/datashop.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM user WHERE username=?;'
        result = cursor.execute(query, (name,))
        rows = result.fetchall()
        if rows:
            for row in rows:
                user = UserModel(row[0], row[1], row[2])
            connection.close()
            return user


    @classmethod
    def find_by_id(cls, id):
        connection = sqlite3.connect('./db/datashop.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM user WHERE id=?'
        result = cursor.execute(query, (id,))
        rows = result.fetchall()
        if rows:
            for row in rows:
                user = UserModel(row[0], row[1], row[2])
            connection.close()
            return user

    @classmethod
    def insert_into_table(cls, username, password):
        connection = sqlite3.connect('./db/datashop.db')
        cursor = connection.cursor()
        query = 'INSERT INTO user VALUES(NULL, ?, ?)'
        cursor.execute(query, (username, password))
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
        'password': self.password}
