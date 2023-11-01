def encode(password):
    final = ""
    for i in password:
        if i == "1":
            final = final + '4'
        if i == "2":
            final = final + '5'
        if i == "3":
            final = final + '6'
        if i == "4":
            final = final + '7'
        if i == "5":
            final = final + '8'
        if i == "6":
            final = final + '9'
        if i == "7":
            final = final + '0'
        if i == "8":
            final = final + '1'
        if i == "9":
            final = final + '2'
        if i == "0":
            final = final + '3'
    return final
def main():
    while True:
        print("Menu")
        print('-------------')
        print("1. Encode")
        print('2. Decode')
        print('3. Quit')
        print(" ")
        cho = int(input("Please enter an option: "))
        if cho == 1:
            password = str(input("Please enter your password to encode:"))
            if len(password) == 8:
                encoded_password = encode(password)
                print("Your password has been encoded and stored!")
            else:
                print("Password must be 8 digits!")
        #if cho == 2:
            #
        if cho == 3:
            quit()
main()

