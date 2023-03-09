
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


def main():
    password = input("type password")
    print(encoder(password))


if __name__ == '__main__':
    main()