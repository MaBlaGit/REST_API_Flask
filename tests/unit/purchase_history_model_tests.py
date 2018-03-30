import sys
sys.path.append('../..')
from models import purchase_history
import unittest


class PurchaseHistoryModelTests(unittest.TestCase):

    def setUp(self):
        self.purchase_history = purchase_history.PurchaseHistoryModel(6, 'TestProduct', 8, 20)

    def test_purchase_history_params(self):
        self.assertEqual(6, self.purchase_history.id)
        self.assertEqual('TestProduct', self.purchase_history.product)
        self.assertEqual(8, self.purchase_history.user_id)
        self.assertEqual(20, self.purchase_history.product_id)

    def test_json_return(self):
        output = {
            'user': self.purchase_history.user_id,
            'product history id': self.purchase_history.id,
            'product name': self.purchase_history.product,
            'product store number': self.purchase_history.product_id
        }

        self.assertEqual(output, self.purchase_history.json())

if __name__ == '__main__':
    unittest.main()
