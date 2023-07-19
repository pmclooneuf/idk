# Patrick McLoone

def encode(password):
    encoded_password = ""

    for num in password:
        encoded_password += str((int(num) + 3) % 10) # adds 3 to each num, mod 10 so nums like 9 wrap around back to 2 not 12

    return encoded_password


def decode(password):
    decoded_password = ""
    for num in password:
        if int(num) < 3:
            decoded_password += str(int(num) + 7)
        else:
            decoded_password += str(int(num) - 3)
    return decoded_password


def main():

    while True:
        print("Menu ")
        print("------------- ")
        print("1. Encode ")
        print("2. Decode ")
        print("3. Quit ")
        print()

        option = int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored! ")

        elif option == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")

        elif option == 3:
            break

if __name__ == '__main__':
    main()
