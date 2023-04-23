import math

def inverse(x, m):
    possible_a_inv = [a for a in range(0,26) 
                        if math.gcd(a, 26) == 1]
    for i in possible_a_inv:
        if (x*i)%m == 1:
            return i
    
def encrypt(a, b):
    plaintext=open('PlainText.txt','r')
    plain=plaintext.read()
    plain=plain.lower()
    ciphertext=open('CipherText.txt','w')
    Result=''
    for i in plain:
        if i == ' ':
            Result+=''
        else:
            Result+=chr(((a*(ord(i)-97)+b)%26)+97)
    ciphertext.write(Result)

def decrypt(a, b):
    ciphertext=open('CipherText.txt','r')
    cipher=ciphertext.read()
    decryptedtext=open('DecryptedText.txt','w')
    Result=''
    for i in cipher:
        Result+=chr((( inverse(a, 26)*(ord(i) - 97 - b))% 26) + 97)
    decryptedtext.write(Result)

def bruteforce():
    cipher=open('CipherText.txt','r')
    message = cipher.read()
    decrypted=open('DecryptedText.txt','r')
    reference = decrypted.read()
    bruteforce=open('BruteForce.txt','w')
    possible_a = [a for a in range(0, 26) 
                    if math.gcd(a, 26) == 1]
    for a in possible_a:
        for b in range(0, 26):
            Result=''
            for i in reference:
                if i == ' ':
                    Result+=''
                else:
                    Result+=chr(((a*(ord(i)-97)+b)%26)+97)
            if Result == message:
                bruteforce.write('Key 1: '+ str(a) +'    Key 2: '+ str(b))
encrypt(3,5)
decrypt(3,5)
bruteforce()