

MINIMUM_PASSWORD_LENGTH = 4


def version_1():
    """Request password with valid length"""
    password = input("Enter password of at least {} characters: ".format(MINIMUM_PASSWORD_LENGTH))
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        password = input("Enter password of at least {} characters: ".format(MINIMUM_PASSWORD_LENGTH))
    print('*' * len(password))


def main():
    password = get_password()
    print_asterisk(password)


def print_asterisk(password):
    print('*' * len(password))


def get_password():
    password = input("Enter password of at least {} characters: ".format(MINIMUM_PASSWORD_LENGTH))
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print("The provided password is too short")
        password = input("Enter password of at least {} characters: ".format(MINIMUM_PASSWORD_LENGTH))
    return password


main()
