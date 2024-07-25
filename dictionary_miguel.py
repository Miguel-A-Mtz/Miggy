# Miguel Martinez
# Introduction to programming with python
# Script 14: "Dictionary Values"
# MIT Open Source License (see License.html)

def main():
    print("\nWelcome to Lab 14 Dictionary Values")

    # simple_dictionary = dict()
    admin_dict = {'username': 'admin', 'password': 'x\\zm/s.y', 'strength': 'strong'}
    manager_dict = {'username': 'manager', 'password': 'xr,ly.zn', 'strength': 'strong'}
    editor_dict = {'username': 'editor', 'password': 'xrytnz', 'strength': 'fair'}
    creator_dict = {'username': 'creator', 'password': 'xyzzts', 'strength': 'fair'}
    guest_dict = {'username': 'guest', 'password': 'xrs', 'strength': 'weak'}
    visitor_dict = {'username': 'visitor', 'password': 'lxm', 'strength': 'weak'}

    user_access = {admin_dict, manager_dict, editor_dict, creator_dict, guest_dict, visitor_dict}

    print(f' all user_access dictionary values {user_access}')

    print(f'\neach user_access values: {user_access}')
    for each, value in enumerate(user_access):
        print(f'\t{user_access}')

    print(f'\neach user_access values: {user_access}')
    for each, value in enumerate(user_access):
        print(f'\t{value["username"]}, passkey strength is: {value["strength"]}')

    print(f'\nWhich users have strong passwords:')
    for each, value in enumerate(user_access):
        if value['strength'] == 'strong':
            print(f'\tusername is: {value["username"]} is strong')

    return

main()
