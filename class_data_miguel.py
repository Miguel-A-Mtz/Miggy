# Miguel Martinez
# Lab 19: User_Data


class User_Data:
    # Member Data Section
    user_name = ""
    user_role = ""
    user_id = -1

    def __init__(self):
        print(f'The User_Data constructor has been called.')

    def set_user_name(self, new_name):
        self.user_name = new_name
        return

    def set_user_role(self, new_role):
        self.user_role = new_role
        return

    def set_user_id(self, new_id):
        self.user_id = new_id

    def get_user_name(self):
        return self.user_name

    def get_user_role(self):
        return self.user_role

    def get_user_id(self):
        return self.user_id

    def show_user(self):
        print(f"User: {self.user_name}, Role: {self.user_role}), ID: {self.user_id}")
        return


def main():
    print()
    user_one = User_Data()
    user_one.set_user_name("roho")
    user_one.set_user_role("admin")
    user_one.set_user_id(11)
    print(f'\tuser one name: {user_one.get_user_name()}')
    print(f'\tuser one role: {user_one.get_user_role()}')
    print(f'\tuser one id: {user_one.get_user_id()}')

    return


main()
