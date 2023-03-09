# encoder written by travis Shepherd
def encoder(string):
    original_password = string
    encoded_password = ''
    for i in original_password:
        if int(i) in range(7):
            encoded_password_addon = str(int(i) + 3)
            encoded_password += encoded_password_addon
        if int(i) > 6:
            if i == '7':
                encoded_password_addon = '0'
                encoded_password += encoded_password_addon
            elif i == '8':
                encoded_password_addon = '1'
                encoded_password += encoded_password_addon
            elif i == '9':
                encoded_password_addon = '2'
                encoded_password += encoded_password_addon
    return encoded_password


def menu():
    print("""
    Menu  
------------- 
1. Encode  
2. Decode  
3. Quit 
 
Please enter an option:""")


x = 1


def main():
    while x == 1:
        menu()
        user_choice = int(input())
        if user_choice == 1:
            original_password = str(input('Please enter your password to encode:'))
            encoded_password = encoder(original_password)
            print('Your password has been encoded and stored!')




if __name__ == '__main__':
    main()