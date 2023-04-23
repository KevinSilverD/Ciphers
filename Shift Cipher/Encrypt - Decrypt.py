def encrypt(key):
    plain=open('PlainText.txt','r')
    cipher=open('CipherText.txt','w')
    message = plain.read()
    message=message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha:
            letter_index = (alpha.find(letter) + key) % len(alpha)
            result = result + alpha[letter_index]
        else:
            result = result + letter
    cipher.write(result)

def decrypt(key):
    cipher=open('CipherText.txt','r')
    decrypted=open('DecryptedText.txt','w')
    message = cipher.read()
    message=message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha:
            letter_index = (alpha.find(letter) - key) % len(alpha)
            result = result + alpha[letter_index]
        else:
            result = result + letter
    decrypted.write(result)


encrypt(3)
decrypt(3)