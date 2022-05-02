# Cryptography
 Caesar Cipher

def CaesarCipher():
    # Ask the user what function to perform
    menu = '(d) Decode\n(e) Encode\n(b) Break The Code\n\n(h) Help\n(x) Exit\n\nChoice> '
    response = input(menu)
    response = response.lower()
    while response not in {'e', 'd', 'b', 'h', 'x'}:
        response = input(menu)
        response = response.lower()
    if response == 'e':
        message = input('Enter the message to be encoded\n> ')
        message = message.lower()
        # Ensures the key is always a integer
        key = input('Enter the numeric key\n> ')
        key = convertToInt(key)
        encoded = encode(message, key)
        print(encoded+'\n')
        CaesarCipher()
    elif response == 'd':
        message = input('Enter the message to be decoded\n> ')
        message = message.lower()
        key = input('Enter the numeric key\n> ')
        # Ensures the key is always a integer
        key = convertToInt(key)
        decoded = decode(message, key)
        print(decoded+'\n')
        CaesarCipher()
    elif response == 'b':
        message = input('Enter the message to be decoded\n> ')
        message = message.lower()
        breakTheCode(message)
        CaesarCipher()
    elif response == 'h':
        print('\nWelcome to Cryptography Inc.')
        print(textwrap.fill('This program helps you to encode, decode and break caesar cipher codes! Simply select an option from the above list by typing the letter next to the option and then pressing enter. By following the instructions provided, you should have no trouble. If you need further assistance, please contact me at: malachi.haskew@education.nsw.gov.au.', 80))
        print('\n')
        CaesarCipher()
