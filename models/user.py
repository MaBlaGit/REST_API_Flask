import sqlite3


class UserModel:

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @classmethod
    def find_by_name(cls, name, db_path='./db/datashop.db'):
        connection = sqlite3.connect(db_path)
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
    def find_by_id(cls, id, db_path='./db/datashop.db'):
        connection = sqlite3.connect(db_path)
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
    def insert_into_table(cls, username, password, db_path='./db/datashop.db'):
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        query = 'INSERT INTO user VALUES(NULL, ?, ?)'
        cursor.execute(query, (username, password))
        connection.commit()
        connection.close()

    @classmethod
    def find_all(cls, db_path='./db/datashop.db'):
        users = list()
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        query = 'SELECT * FROM user;'
        result = cursor.execute(query)
        rows = result.fetchall()
        if rows:
            for row in rows:
                users.append(UserModel(row[0], row[1], row[2]))
            return users
        connection.close()

    @classmethod
    def delete_user(self, name, db_path='./db/datashop.db'):
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        user_id_query_for_purchase_his = 'SELECT id FROM user WHERE username=?;'
        user_id = cursor.execute(user_id_query_for_purchase_his, (name,))
        result_user_id = str(user_id.fetchone()[0])

        purchase_history_deletion = 'DELETE FROM purchase_history WHERE user_id=?;'
        delete_user_history = cursor.execute(purchase_history_deletion, (result_user_id))

        user_to_delete = 'DELETE FROM user WHERE username=?;'
        delete_user = cursor.execute(user_to_delete, (name,))
        connection.commit()
        connection.close()

    def json(self):
        return {'id': self.id,
        'username': self.username,
        'password': self.password}
