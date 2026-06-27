def get_length():
    pass_length = int(input("Enter the lenght for the password: "))
    return pass_length


def main():
    print("=" * 30)
    print("Python password generator")
    print("=" * 30)

    print("Generate strong and secure passwords!")


password_length = get_length()
print("Password length: ", password_length)

if __name__ == "__main__":
    main()
