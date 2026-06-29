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

    while True:
        # Keeps repeating the following code block until

        # ask for password length:
        password_length = get_password_length()

        # generate password for the specified length:
        password = generate_password(password_length)

        # Display the generated password:
        print("Your password is: ", password)

        # Ask the user if thay want another password and store the user's choice
        choice = input("Do you want to generate another password? (y/n): ")

        # the user enters a letter
        # if the user's letter is in uppercase convert it to lowercase -> compare the lowercased letter to "y" (which is meant for yes) -> if that letter == "y" -> continue
        if choice.lower() == "y":
            continue
        else:
            # if the user types "n" (which is meant for no) -> break the loop
            print("Thank you for using python's password generator!")
            break


if __name__ == "__main__":
    main()

# output:
# Enter the length of the password: 6
# Your password is:  8yX29<
# Do you want to generate another password? (y/n): y
# Enter the length of the password: 8
# Your password is:  2k\pv!BW
# Do you want to generate another password? (y/n): n
# Thank you for using python's password generator!
