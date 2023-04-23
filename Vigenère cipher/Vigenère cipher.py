import itertools
import string

def encrypt(key):
    key = key.lower()
    plaintext=open('PlainText.txt','r')
    plain=plaintext.read()
    plain=plain.lower()
    ecryptedtext=open('CipherText.txt','w')

    keyiter = itertools.cycle(map(ord, key))
    Encrypted=(chr(ord('a') + ((next(keyiter) - ord('a') + ord(letter) - ord('a')) + 0) % 26) if letter in string.ascii_lowercase else letter for letter in plain)
    Encrypted="".join(Encrypted)

    ecryptedtext.write(Encrypted)

def decrypt(key):
    keyinverse =(chr(ord('a') +(26 - (ord(k) - ord('a'))) % 26) for k in key)
    keyinverse="".join(keyinverse)
    ciphertext=open('CipherText.txt','r')
    cipher=ciphertext.read()
    decryptedtext=open('DecryptedText.txt','w')

    keyiter = itertools.cycle(map(ord, keyinverse))
    Decrypted=(chr(ord('a') + ((next(keyiter) - ord('a') + ord(letter) - ord('a')) + 0) % 26) if letter in string.ascii_lowercase else letter for letter in cipher)
    Decrypted="".join(Decrypted)

    decryptedtext.write(Decrypted)



frequency = (0.0749, 0.0129, 0.0354, 0.0362, 0.1400, 0.0218, 0.0174, 0.0422, 0.0665, 0.0027, 0.0047, 0.0357, 0.0339,
             0.0674, 0.0737, 0.0243, 0.0026, 0.0614, 0.0695, 0.0985, 0.0300, 0.0116, 0.0169, 0.0028, 0.0164, 0.0004)

def brutetest(text,key):
    keyinverse =(chr(ord('a') +(26 - (ord(k) - ord('a'))) % 26) for k in key)
    keyinverse="".join(keyinverse)
    keyiter = itertools.cycle(map(ord, keyinverse))
    Decrypted=(chr(ord('a') + ((next(keyiter) - ord('a') + ord(letter) - ord('a')) + 0) % 26) if letter in string.ascii_lowercase else letter for letter in text)
    Decrypted="".join(Decrypted)
    return Decrypted


def comparefrequence(text):
    if not text:
        return None
    text = [t for t in text.lower() if t in string.ascii_lowercase]
    freq = [0] * 26
    total = float(len(text))
    for l in text:
        freq[ord(l) - ord('a')] += 1
    return sum(abs(f / total - E) for f, E in zip(freq, frequency))


def bruteforce():
    ciphertext=open('CipherText.txt','r')
    cipher=ciphertext.read()
    bruteforce=open('BruteForce.txt','w')
    bestkeys = []
    keyminsize = 1 # increase if you know the key has more that one letter
    keymaxsize = 20 # increase if it fails to find key

    textletters = [c for c in cipher.lower() if c in string.ascii_lowercase]

    for keylength in range(keyminsize, keymaxsize):
        key = [None] * keylength
        for keyindex in range(keylength):
            letters = "".join(itertools.islice(textletters, keyindex, None, keylength))
            shifts = []
            for keychr in string.ascii_lowercase:
                shifts.append((comparefrequence(brutetest(letters,keychr)), keychr))
            key[keyindex] = min(shifts, key=lambda x: x[0])[1]
        bestkeys.append("".join(key))
    bestkeys.sort(key=lambda key: comparefrequence((brutetest(cipher,key))))
    bruteforce.write(str(bestkeys[:1]))# increase this if failed to get key


encrypt('kingcrimson')
decrypt('kingcrismon')
bruteforce() #if it failed to find the right key increase the integer on line 75 "bestkeys[:integer]" the default is 1

