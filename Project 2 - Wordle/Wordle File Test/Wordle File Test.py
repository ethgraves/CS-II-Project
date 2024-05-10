username_test = ''

def read_file(file):
#     file_reader = file.readlines()
#     for line in file_reader:
#         print(line)
    print(1)
    print(username_test)
    print(2)


def check_username(username):
    try:
        file = open(username + '.txt', 'r')
    except FileNotFoundError:
        file = open(username + '.txt', 'a')
    return file

def main():
    username = input('Input username: ')
    file = check_username(username)
    username_test = username + '.txt'
    read_file(file)

if __name__ == '__main__':
    main()