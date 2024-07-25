# Miguel Martinez
# CIS 135 Summer Python Programming
# Lab 15: "File Write"
# MIT Open Source License (License.html)

def create_file(file_name):
    new_file = open(file_name, 'x')
    new_file.close()
    return

def write_data(file_name):
    write_file = open(file_name, 'w')
    write_file.write(f"Step to file management:")
    write_file.write(f'\n\t#1: Create or open a file.')
    write_file.write(f'\n\t#2: Write or read data the file.')
    write_file.write(f'\n\t#3: Close the file connection or handle.')
    write_file.close()
    return

def print_data(file_name):
    read_file = open(file_name, 'r')
    print(read_file.read())
    read_file.close()
    return

def main():
    print("\nWelcome to lab 15 Creating Files")

    file_name = "data_file.data"
    # create_file(file_name)
    write_data(file_name)
    print_data(file_name)
    return

main()
