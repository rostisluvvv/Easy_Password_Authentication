import getpass


DATABASE: dict[str, str] = {
    'rostisluvvv': '123456789',
    'maria': '112233',
    'mike': '998877',
    'kate': '445566',
}

username = input('Enter Your Username: ')

password = getpass.getpass("Enter Your Password : ")

for u_name in DATABASE.keys():
    if u_name == username:
        while password != DATABASE.get(u_name):
            password = getpass.getpass("WRONG!!! Enter Your Password Again: ")
        break

print('Verified')
