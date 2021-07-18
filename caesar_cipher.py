import string
from time import sleep

# abcdefghijklmnopqrstuvwxyz
alphabets = string.ascii_letters

# function that encrypts the message
def encrypt():

    text_to_encrypt = input("Enter the text you want to ENCRYPT:")
    print()
    key = int(input("Enter the encryption key: "))
    
    encrypted_message = ""

    for letter in text_to_encrypt:
        if letter in alphabets:
            position = alphabets.index(letter)

            # FORMULA 
            # E_n(x)=(x+n)mod 26  (Encryption Phase with shift n)
            new_position = (position + key) % 26
            encrypted_character = alphabets[new_position]
            encrypted_message += encrypted_character
        else:
            encrypted_message += letter

    print(encrypted_message) 


# function that decrypts the message
def decrypt():

    encrypted_message = input("Enter the text you want to DECRYPT:").strip()
    print()
    key = int(input("Enter the decrypt KEY:"))

    decrypted_message = "" 

    for letter in encrypted_message:
        if letter in alphabets:
            # find the index numbers of the letter in the entered string
            position = alphabets.index(letter)

            # FORMULA
            # D_n(x)=(x-n)mod\ 26    (Decryption Phase with shift n)

            # finds the original position of the letter to decrypt in from alphabets
            new_position = (position - key) % 26
            decrypted_character = alphabets[new_position]

            # adds the decrypted letter to the string
            decrypted_message += decrypted_character
        else:
           decrypted_message += letter 

    print(decrypted_message)


encrypt()
decrypt()