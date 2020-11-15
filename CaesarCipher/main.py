import art

def caesar(text, shift, direction):
    toPrint = ""
    if direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
        
            newPosition = position + shift
            newLetter = alphabet[newPosition]
            toPrint += newLetter
        else:
            toPrint += char
    
    print(f"The {direction}d text is {toPrint}.")

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', \
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

toContinue = True
while toContinue:


    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 25
    

    caesar(text, shift, direction)

    decision = input("Type 'yes' if you want to go again. Otherwise, type 'no'\n")
    if decision == "no":
        toContinue = False
        print("Goodbye!")





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
# if direction == "encode":
#     encrypt(text, shift)

# elif direction == "decode":
#     decrypt(text, shift)