import random
import string


def get_password_length():
    while True:
        length = int(input("Enter the length of the password: "))
        if length > 0:
            return length
        else:
            print("password length must be greater than 0.")


def generate_password(length):
    password = ""
    characters = (
        string.ascii_lowercase
        + string.ascii_uppercase
        + string.digits
        + string.punctuation
    )

    for i in range(length):
        password += random.choice(characters)

    # shuffle password: converting string to list:
    password_list = list(password)
    # shuffling the list:
    random.shuffle(password_list)
    password = "".join(password_list)

    return password


def main():
    print("=" * 40)
    print("Python's Password Generator")
    print("=" * 40)
    print()
    print("Generate your own password using python's password generator!")

    password_length = get_password_length()
    password = generate_password(password_length)
    print("Your password is: ", password)


if __name__ == "__main__":
    main()
