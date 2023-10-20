from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(direction, text, shift):
    ec_txt = []
    dc_txt = []
    for i in range(len(text)):
        letter = text[i]
        for j in range(0, 26):
            if alphabet[j] == letter:
                if direction == 'encode':
                    t = j+shift
                    if t > 25:
                        j = j-26
                        lett = alphabet[j+shift]
                    else:
                        lett = alphabet[j+shift]
                    ec_txt.append(lett)
                elif direction == 'decode':
                    t = j-shift
                    if t<0:
                        j = j+26
                        lett = alphabet[j-shift]
                    else:
                        lett = alphabet[j-shift]
                    dc_txt.append(lett)
    if direction == 'decode':
        print(f"The Secret message is revealed! The decoded message delivered for you is {''.join(dc_txt)}")
    elif direction == 'encode':
        print(f"The secret is safe guarded! And the new encrypted text is {''.join(ec_txt)}")

game = 'yes'

while game == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message(For your kind request write your text without spaces):\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 26:
        shift = shift % 26
    caeser(direction, text, shift)

game = input("Were you impressed by my work! If you were then type 'yes' to continue or type 'no'? ").lower()



