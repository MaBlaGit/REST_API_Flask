import requests
import unittest
import json
import os
from database import create_database


class StoreEndpointTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if os.path.exists('../../db/datashop.db'):
            os.system('rm ../../db/datashop.db')
        create_database('../../db/datashop.db')
        cls.uri = 'http://127.0.0.1:5000'

    def test_products_status_code(cls):
        cls.uri += '/products'
        uri_request = requests.get(cls.uri)
        cls.assertEqual(200, uri_request.status_code)

    def test_products_response_check(cls):
        cls.uri += '/products'
        uri_request = requests.get(cls.uri).content
        content_decode = json.loads(uri_request.decode('utf-8'))
        counter = 1
        for product in content_decode.get('products'):
            cls.assertEqual('car_{}'.format(counter), product.get('product'))
            counter+=1

    @classmethod
    def tearDownClass(cls):
        os.system('rm ../../db/datashop.db')

if __name__ == '__main__':
    unittest.main(verbosity=2)
