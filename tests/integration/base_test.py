import os
import sys
sys.path.append('../')
from system.database import create_database
import unittest

class BaseTest(unittest.TestCase):

    def setUp(self):
        if os.path.exists('./db/datashop.db'):
            os.system('rm ./db/datashop.db')
        create_database('./db/datashop.db')

    def tearDown(self):
        os.system('rm ./db/datashop.db')
