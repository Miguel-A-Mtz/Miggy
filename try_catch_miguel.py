# Miguel Martinez
# Lab 20: Using Try-catch BLocks with Objects

class Error_Class:

    def __init__(self):
        print(f'The Error_Class constructor has been called.')

    def catch_zero(self):
        try:
            my_math = 20 / 0
        except ZeroDivisionError as zde:
            print(f'Error is {zde}')
        return

    def catch_file_not_found(self):
        try:
            with open('this_file.txt', 'r') as thisfile:
                print(f"{thisfile.read()}")
        except FileNotFoundError as fnfe:
            print(f'The Error is: {fnfe}')
        return

    def catch_import_error(self):
        try:
            import zebra
        except ModuleNotFoundError as mnfe:
            print(f'\tThe error is {mnfe}')
        return


def main_menu():
    print(f'\n\t1) Try Math Error')
    print(f'\t2) Try File Error')
    print(f'\t3) Try Import Error')
    print(f'\t4) Exit')
    return


def main():
    print(f'Welcome to Lab 20 Using Try-Except Error Handling')
    this_object = Error_Class()
    user_select = -1
    main_menu()
    try:
        user_select = int(input(f'\tPlease select an option: '))
    except ValueError as ve:
        pass
    while user_select != 4:
        if user_select == 1:
            this_object.catch_zero()
        elif user_select == 2:
            this_object.catch_file_not_found()
        elif user_select == 3:
            this_object.catch_import_error()
        elif user_select == 4:
            break
        else:
            print(f'\tInvalid Selection')
        main_menu()
        try:
            user_select = int(input(f"\tPlease select an option: "))
        except ValueError as ve:
            pass

    return


main()

