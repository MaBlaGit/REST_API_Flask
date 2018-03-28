import os
import sys
sys.path.append('../')
from system.database import create_database
import unittest


class BaseTest(unittest.TestCase):

    def setUp(self):
        if os.path.exists('./datashop.db'):
            os.system('rm ./datashop.db')
        create_database('./datashop.db')


    def tearDown(self):
        os.system('rm ./datashop.db')
