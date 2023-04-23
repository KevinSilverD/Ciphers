import random

def makekey():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    key = list(alpha)
    random.shuffle(key)
    key = "".join(key)
    generatedkey=open('key.txt','w')
    generatedkey.write(key)

def encrypt():
    alpha = "abcdefghijklmnopqrstuvwxyz"

    key=open('key.txt','r').read()
    plaintext = open('PlainText.txt','r')
    plain=plaintext.read().lower()
    encryptedtext=open('CipherText.txt','w')

    substitution = str.maketrans(alpha, key)
    encrypted=plain.translate(substitution)

    encryptedtext.write(encrypted)

def decrypt():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    key=open('key.txt','r').read()
    ciphertext=open('CipherText.txt','r')
    cipher=ciphertext.read()
    decryptedtext=open('DecryptedText.txt','w')

    substitution = str.maketrans(key, alpha)
    decrypted=cipher.translate(substitution)

    decryptedtext.write(decrypted)

makekey() #makes new key, remove this if you want to use a specific key
encrypt()
decrypt()