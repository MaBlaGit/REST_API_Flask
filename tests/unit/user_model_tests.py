import sys
sys.path.append("../..")
from models import user
import unittest


class UserModelTests(unittest.TestCase):

    def setUp(self):
        self.user_model = user.UserModel(1, 'Test', 'test@test.com')

    def test_user_model_params(self):
        self.assertEqual(1, self.user_model.id)
        self.assertEqual('Test', self.user_model.username)
        self.assertEqual('test@test.com', self.user_model.user_email)

    def test_json_return(self):
        json_output = {'username': 'Test', 'id': 1,
                       'user_email': 'test@test.com'}
        self.assertEqual(json_output, self.user_model.json())

if __name__ == '__main__':
    unittest.main(verbosity=2)
