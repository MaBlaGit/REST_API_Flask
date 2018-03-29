import sqlite3
from models.user import UserModel
from models.store import StoreModel


class PurchaseHistoryModel:

    db_path = './db/datashop.db'

    def __init__(self, id, product, user_id, product_id):
        self.id = id
        self.product = product
        self.user_id = user_id
        self.product_id = product_id

    @classmethod
    def find_products_related_with_user_name(cls, name):

        products_history_list = list()

        user = UserModel.find_by_name(name)
        if not user:
            return {'message': 'Cannot find user in database!'}
        else:
            connection = sqlite3.connect(cls.db_path)
            cursor = connection.cursor()
            query = 'SELECT * FROM purchase_history WHERE user_id=?;'
            result = cursor.execute(query, (user.id,))
            rows = result.fetchall()
            if rows:
                for row in rows:
                    products = PurchaseHistoryModel(row[0], row[1], row[2], row[3])
                    products_history_list.append(products)
                connection.close()
                return products_history_list

    def json(self):
        return {
            'user': self.user_id,
            'product id': self.id,
            'product name': self.product,
            'product store number': self.product_id
        }
