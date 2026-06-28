import random
import string


def get_password_length():
    length = int(input("Enter the length of the password: "))
    return length


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
