import sys
sys.path.append('../..')
from models import store
import unittest


class StoreModelTests(unittest.TestCase):

    def setUp(self):
        self.store_model = store.StoreModel(1, 'car', 2599.99)

    def test_store_model_params(self):
        self.assertEqual(1, self.store_model.id)
        self.assertEqual('car', self.store_model.product)
        self.assertEqual(2599.99, self.store_model.price)

    def test_json_return(self):
        output = {'price': 2599.99, 'product': 'car', 'id': 1}
        self.assertEqual(output, self.store_model.json())

if __name__ == '__main__':
    unittest.main(verbosity=2)
