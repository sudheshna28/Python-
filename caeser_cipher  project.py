## encryption and decryption
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def encryption(plain_text,shift_key):
    cipher_text=" "
    for char in plain_text:##hello
        if char in alphabet:
            position=alphabet.index(char) ##7
            new_position=(position+shift_key)%26
            cipher_text+=alphabet[new_position]
        else:
            cipher_text+=char
    print("Here's is the text after encryption:",cipher_text)
def decryption(cipher_text,shift_key):
    plain_text=""
    for char in cipher_text: ##khoor
        if char in alphabet:
            position=alphabet.index(char) ##10
            new_position=(position-shift_key)%26
##        if new_position<0:
##            new_position+=26
            plain_text+=alphabet[new_position]
        else:
            plain_text+=char
    print("Here's is the text after encryption:",plain_text)
    
wanna_end=False
while not wanna_end:
    what_to_do=input("Type  'encrypt' for encryption, type 'decrypt' for decryption:\n")
    text=input("type your message:\n")
    shift=int(input("enter shift key:\n"))
    if what_to_do=="encrypt":
        encryption(plain_text=text,shift_key=shift)
    elif what_to_do=="decrypt":
        decryption(cipher_text=text,shift_key=shift)
    play_again=input("enter 'yes' to continue,type 'no' to exit:")
    if play_again=='no':
        wanna_end=True
        print("Have a nice day! Byee..")
