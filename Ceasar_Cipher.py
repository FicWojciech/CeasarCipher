from art import logo
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
]


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ''
    if cipher_direction == 'decode':
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction + 'd'} text is '{end_text}'.")



print(logo)

while True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    if direction == 'encode' or direction == 'decode':
        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
        print("Type 'yes' if you want to go again. Otherwise type 'no'.")
        one_more = input().lower()
        if one_more == 'no':
            print("Goodbye.")
            break


# def encrypt(plain_text, shift_amount):
#     cipher_text = ''
#     for char in plain_text:
#         position = alphabet.index(char)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is '{cipher_text}'.")
#
#
# def decrypt(cipher_text, shift_amount):
#
#         decrypted_text = ''
#         for char in cipher_text:
#             position = alphabet.index(char)
#             new_position = position - shift_amount
#             letter = alphabet[new_position]
#             decrypted_text += letter
#         print(f"The decoded text is '{decrypted_text}'.")
