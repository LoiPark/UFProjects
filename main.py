def print_menu():
    print("Menu")
    print("-" * 13)
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encoder(password):
    encoded = ''
    for i in password:
        encoded += str((int(i) + 3) % 10)

    return encoded


def decoder(password):
    decoded = ''
    for i in password:
        decoded += str((int(i) - 3) % 10)

    return decoded


def main():
    while True:
        print_menu()
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded = encoder(password)
            print("Your password has been encoded and stored!\n")

        if option == 2:
            decoded = decoder(encoded)
            print(f"The encoded password is {encoded}, and the original password is {decoded}.\n")

        if option == 3:
            break


if __name__ == "__main__":
    main()
