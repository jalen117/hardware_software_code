
def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary


def binary_to_decimal(binary):
    decimal = 0
    power = 0
    while binary > 0:
        decimal += (binary % 10) * (2 ** power)
        binary = binary // 10
        power += 1
    return decimal


def main():
        print ("Hello there!!, ")
        print("Let's start to convert Decimal to Binary and Binary to Decimal")
        print("Let's go try it out")
        while True:
            print("\nPlease select an option")
            print("A. Convert Decimal to Binary")
            print("B. Convert Binary to Decimal")
            print("C. Quit")
            choice = input("Enter your Choice (A, B, or C):")

            if choice == 'A':
                try:
                    decimal = int(input("Enter a decimal number: "))
                    binary = decimal_to_binary(decimal)
                    print("Decimal {} to Binary: {}".format(decimal, binary))
                except ValueError:
                    print("Invalid input! Please enter a valid decimal number.")
            elif choice == 'B':
                try:
                    binary = input("Enter a binary number: ")
                    decimal = binary_to_decimal(int(binary))
                    print("Binary {} to Decimal: {}".format(binary, decimal))
                except ValueError:
                    print("Invalid input! Please enter a valid binary number.")
            elif choice == 'C':
                print("Thank you for using the Decimal to Binary and Binary to Decimal Converter. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option (A, B, or C).")

if __name__ == "__main__":
    main()
