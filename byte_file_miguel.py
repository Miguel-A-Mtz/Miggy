# Miguel Martinez
# CIS 135 Summer Python Programming
# Lab 17: "File Byte Stream"
# MIT Open Source License (License.html)

def write_bytes(file_name, string_data):
    # write_by = open(file_name, 'wb')
    with open(file_name, "wb") as write_by:
        write_by.write(bytes(string_data, encoding='utfg'))
    return

def print_bytes(file_name):
    with open(file_name, "rb") as reader_byte:
        print(reader_byte.read())
    return

def print_strings(file_name):
    with open(file_name, "rb") as reader_string:
        print(reader_string.read().decode("utf-8"))
    return

def main():
    print(f'Welcome to lab 17 using bytes')

    file_name = "bytes_file.bytes"
    the_data = input(f'Please enter a word or phrase: ')
    write_bytes(file_name, the_data)
    print_bytes(file_name)
    print_strings(file_name)

    return

main()
