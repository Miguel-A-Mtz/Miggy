# Miguel Martinez
# CIS 135 Summer Python Programming
# Script 16: "File Append"
# MIT Open Source License (License.html)

def line_counter(file_name):
    """
    This function counts the number of lines
    :param file_name:
    :return
    """
    counter_file = open(file_name, 'r')
    counter_lines = len(counter_file.readlines())
    counter_file.close()
    return counter_lines


def append_file(file_name, the_count):
    """
    This function writes a single line of text to a file
    :param file_name:
    :param the_count:
    :return:
    """
    write_file = open(file_name, 'a')
    write_file.write(f'\ndata_file.data had {the_count} lines of data, and now it has {the_count + 1}')
    write_file.close()
    return

def confirm_append(file_name):
    """
    This function prints the data from the file
    :param file_name:
    :return:
    """
    read_file = open(file_name, 'r')
    print(read_file.read())
    read_file.close()
    return

def append_to_ten(file_name):
    """
    Inside append_to_ten use a loop and call other functions
    (i.e., append_file) until file_name contains the string
    "data_file.data had 9 lines of data, and now it has 10".
    Once file_name contains that string, call confirm_append
    to print the contents of the file to the screen, and exit
    the function.
    :param file_name:
    :return:
    """
    counter = line_counter(file_name)
    while counter <= 9:
        append_file(file_name, counter)
        counter = line_counter(file_name)
    confirm_append(file_name)
    return

def main():
    print("\nWelcome to lab 16 Append")

    file_name = "data_file.data"
    append_to_ten(file_name)

main()
