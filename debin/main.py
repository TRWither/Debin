def decimal_to_binary(decimal):
    # convert decimal to binary
    if decimal == 0:
        return '0'
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary

def main():
    while True:
        decimal_number = int(input("Enter a decimal number (Ctrl+Z to quit) : "))
        binary_number = decimal_to_binary(decimal_number)
        print("Converted to binary :", binary_number)

if __name__ == "__main__":
    main()