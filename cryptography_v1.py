def encode(message, key):
    encoded = ''
    for char in message:
        if char.isalpha():  # if letter
            code = ord(char)
            code += key
            if code > ord('z'):
                code -= 26
            encodedChar = chr(code)
            encoded += encodedChar
        # if space, full stop or number
        elif char in {' ', '.', } or char.isnumeric():
            encoded += char
    return encoded


def decode(message, key):
    decoded = ''
    for char in message:
        if char.isalpha():  # if letter
            code = ord(char)
            code -= key
            if code < ord('a'):
                code += 26
            decodedChar = chr(code)
            decoded += decodedChar
        # if space, full stop or number
        elif char in {' ', '.'} or char.isnumeric():
            decoded += char
    return decoded


print('Welcome to Cryptography Inc.\nCaesar cipher...\n')
# Ask the user what function to perform
menu = '(d) Decode\n(e) Encode\n\n(x) Exit\n\nChoice> '
response = input(menu)
response = response.lower()
while response not in {'e', 'd', 'x'}:
    response = input(menu)
if response == 'e':  # Encode
    message = input('Enter the message to be encoded\n> ')
    message = message.lower()
    key = input('Enter the numeric key\n> ')
    key = int(key)
    encoded = encode(message, key)
    print(encoded)
elif response == 'd':  # Decode
    message = input('Enter the message to be decoded\n> ')
    message = message.lower()
    key = input('Enter the numeric key\n> ')
    key = int(key)
    decoded = decode(message, key)
    print(decoded)

input('\nPress enter to exit')