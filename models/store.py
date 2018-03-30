import sqlite3
from models.user import UserModel
from models.purchase_history import PurchaseHistoryModel


class StoreModel:

    def __init__(self, id, product, price):
        self.id = id
        self.product = product
        self.price = price

    @classmethod
    def find_by_product(cls, product):
        products = list()
        connection = sqlite3.connect('./db/datashop.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM store WHERE product=?;'
        result = cursor.execute(query, (product,))
        rows = result.fetchall()
        if rows:
            for row in rows:
                products.append(StoreModel(row[0], row[1], row[2]))
            return products
        connection.close()

    @classmethod
    def find_all_products(cls):
        products = list()
        connection = sqlite3.connect('./db/datashop.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM store;'
        result = cursor.execute(query)
        rows = result.fetchall()
        if rows:
            for row in rows:
                products.append(StoreModel(row[0], row[1], row[2]))
            return products
        connection.close()

    @classmethod
    def add_product(self, product, price):
        connection = sqlite3.connect('./db/datashop.db')
        cursor = connection.cursor()
        query = 'INSERT INTO store VALUES(NULL, ?, ?);'
        result = cursor.execute(query, (product, price,))
        connection.commit()
        connection.close()

    def json(self):
        return {'id': self.id,
        'product': self.product,
        'price': self.price
        }


class ShoppingStore:

    # def __init__(id, product, user_id, product_id):
    #     self.id = id
    #     self.product = product
    #     self.user_id = user_id
    #     self.product_id = product_id

    @classmethod
    def buy_product(cls, username, product):
        user = UserModel.find_by_name(username)
        if user:
            products = StoreModel.find_by_product(product)
            if products:
                connection = sqlite3.connect('./db/datashop.db')
                cusrsor = connection.cursor()
                query = 'INSERT INTO purchase_history VALUES(NULL, ?, ?, ?);'
                result = cusrsor.execute(query, (product, user.id, products[0].id,))
                connection.commit()
                connection.close()
                return {'message': 'Selected product was bought!'}, 200
            else:
                return {'message': 'No product in database!'}, 404
        else:
            return {'message': 'Shopping impossible, no user in database!'}, 404
