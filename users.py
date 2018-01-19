class User:

    users_list = []

    def __init__(self,user_name,password):

        self.user_name = user_name
        self.password = password

    def create_users(self):

        User.users_list.append(self)

    def save_users(self):

        User.users_list.append(self)
