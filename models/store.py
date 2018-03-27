import sqlite3


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
