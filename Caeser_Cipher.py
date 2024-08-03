letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

def encrypt_decrypt(text, mode, key):
    result = ''
    if mode == 'd':
        key = -key

    for letter in text:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                result += letter
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters
                elif new_index < 0:
                    new_index += num_letters
                result += letters[new_index]
    return result


print()
print('*** CAESAR CIPHER ***')
print()

print('Encrypt or Decrypt')
# check if entered character are e or d
while True:
    user_input = input('e/d: ').lower()
    if user_input == 'e' or user_input == 'd':
        break
    else:
        print("Invalid input!: Please enter only 'e' or 'd'.")
print(user_input)

if user_input == 'e':
    print("ENCRYPTION MODE")
    print()
    while True:
        try:
            key = int(input('Enter the key (1 through 26): '))
            if 1 <= key <= 26:
                break
            else:
                print("Error: Please enter a number between 1 and 26.")
        except ValueError:
            print("Error: Please enter a valid number.")
    text = input('Enter the text to encrypt: ')
    ciphertext = encrypt_decrypt(text, user_input, key)
    print(f'CIPTERTEXT: {ciphertext}')

elif user_input == 'd':
    print("DECRYPTION MODE")
    print()
    while True:
        try:
            key = int(input('Enter the key (1 through 26): '))
            if 1 <= key <= 26:
                break
            else:
                print("Error: Please enter a number between 1 and 26.")
        except ValueError:
            print("Error: Please enter a valid number.")
    text = input("enter the text to decrypt: ")
    plaintext = encrypt_decrypt(text, user_input, key)
    print(f'PLAINTEXT: {plaintext}')     