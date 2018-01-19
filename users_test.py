import unittest
from users import User

class TestUser(unittest.TestCase):

    def setUp(self):

        self.new_users = User("Ian","12345")

    def tearDown(self):
        User.users_list = []

    def test_init(self):

        self.assertEqual(self.new_users.user_name,"Ian")
        self.assertEqual(self.new_users.password,"12345")


    def test_create_users(self):

        self.new_users.create_users()
        self.assertEqual(len(User.users_list),1)

    def test_save_users(self):

        self.new_users.save_users()
        self.assertEqual(len(User.users_list),1)








if __name__ == '__main__':
   unittest.main()
