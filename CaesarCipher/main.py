import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', \
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# def encrypt(text, shift):
#     cipheredText = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         newPosition = position+shift
#         newLetter = alphabet[newPosition]
#         cipheredText += newLetter
#     print(f"The encoded text is {cipheredText}")


# def decrypt(cipher, shift):
#     plainText = ""
#     for letter in cipher:
#         position = alphabet.index(letter)
#         newPosition = position - shift
#         plainText += alphabet[newPosition]
#     print(f"The decoded message is {plainText}")


def caesar(text, shift, direction):
    toPrint = ""
    for letter in text:
        position = alphabet.index(letter)
        if direction == "decode":
            shift *= -1
        newPosition = position + shift
        newLetter = alphabet[newPosition]
        toPrint += newLetter
    print(f"The {direction}d text is {toPrint}.")


# if direction == "encode":
#     encrypt(text, shift)

# elif direction == "decode":
#     decrypt(text, shift)

caesar(text, shift, direction)