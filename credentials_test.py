import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    def setUp(self):

        self.new_credentials = Credentials("Ian","12345")

    def tearDown(self):

         Credentials.credentials_list=[]

    def test_init(self):
        self.assertEqual(self.new_credentials.user_name,"Ian")
        self.assertEqual(self.new_credentials.password,"12345")

    def test_keep_credentials(self):

        self.new_credentials.keep_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)


if __name__ == '__main__':
   unittest.main()
