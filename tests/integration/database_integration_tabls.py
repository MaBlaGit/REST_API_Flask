import sys
sys.path.append('../..')
from base_test import BaseTest
from models.user import UserModel
from models.store import StoreModel
import os
os.chdir('../..')
import unittest


class DataBaseIntegrationTests(BaseTest):

    def test_user_model_crud(self):
        self.user_model = UserModel(6, 'TestUser', 't@t.pl')
        self.assertIsNone(self.user_model.find_by_name('TestUser'))
        self.user_model.insert_into_table(self.user_model.username,
                                    self.user_model.user_email)
        self.assertIsNotNone(self.user_model.find_by_name('TestUser'))

    def test_store_model_crud(self):
        self.store_model = StoreModel(6, 'TestProduct', 19.99)
        self.assertIsNone(self.store_model.find_by_product('TestProduct'))
        self.assertIsNotNone(self.store_model.find_by_product('car_1'))


if __name__ == '__main__':
    unittest.main()
