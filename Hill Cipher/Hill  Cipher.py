import math
import string
import numpy as np
from sympy import Matrix


def issquare(key):
    key_length = len(key)
    if 2 <= key_length == int(math.sqrt(key_length)) ** 2:
        return True
    else:
        return False


def keymatrix(key, alphabet):
    k = list(key)
    dim = int(math.sqrt(len(k)))
    for (i, character) in enumerate(k):
        k[i] = alphabet[character]

    return np.reshape(k, (dim, dim))

def textmatrix(text, dim, alphabet):
    matrix = list(text)
    remainder = len(text) % dim
    for (i, character) in enumerate(matrix):
        matrix[i] = alphabet[character]
    if remainder != 0:
        for i in range(dim - remainder):
            matrix.append(25)
    return np.reshape(matrix, (int(len(matrix) / dim), dim)).transpose()

def matrixtotext(matrix, order, alphabet):
    if order == 't':
        text_array = np.ravel(matrix, order='F')
    else:
        text_array = np.ravel(matrix)
    text = ""
    for i in range(len(text_array)):
        text = text + alphabet[text_array[i]]
    return text


def encrypt(key):
    alphabet = {}
    for character in string.ascii_uppercase:
        alphabet[character] = string.ascii_uppercase.index(character)

    reverse_alphabet = {}
    for i, value in alphabet.items():
        reverse_alphabet[value] = i

    if issquare(key)==True:
        key=keymatrix(key,alphabet)
    else:
        raise Exception("key should be a square")
    
    plaintext=open('PlainText.txt','r')
    text=plaintext.read()
    text=text.replace(" ", "")
    text=text.upper()
    text=textmatrix(text, key.shape[0], alphabet)
    Ciphertext=open('CipherText.txt','w')

    dim = key.shape[0]
    m_grams = text.shape[1]
    cipher = np.zeros((dim, m_grams)).astype(int)
    for i in range(m_grams):
        cipher[:, i] = np.reshape(np.dot(key, text[:, i]) % len(alphabet), dim)
    Ciphertext.write(matrixtotext(cipher,'t',reverse_alphabet))

def inverse(matrix, alphabet):
    alphabet_len = len(alphabet)
    if math.gcd(int(round(np.linalg.det(matrix))), alphabet_len) == 1:
        matrix = Matrix(matrix)
        return np.matrix(matrix.inv_mod(alphabet_len))
    else:
        return None


def decrypt(key):
    alphabet = {}
    for character in string.ascii_uppercase:
        alphabet[character] = string.ascii_uppercase.index(character)

    reverse_alphabet = {}
    for i, value in alphabet.items():
        reverse_alphabet[value] = i

    if issquare(key)==True:
        key=keymatrix(key,alphabet)
        key=inverse(key,alphabet)
    else:
        raise Exception("key should be a square")
    
    if key is None:
        raise Exception("matrix of the key is not invertable")
    
    ciphertext=open('CipherText.txt','r')
    cipher=ciphertext.read()
    cipher=textmatrix(cipher, key.shape[0], alphabet)
    decrypted=open('DecryptedText.txt','w')

    dim = key.shape[0]
    m_grams = cipher.shape[1]
    decyptrext = np.zeros((dim, m_grams)).astype(int)
    for i in range(m_grams):
        decyptrext[:, i] = np.reshape(np.dot(key, cipher[:, i]) % len(alphabet), dim)
    decrypted.write(matrixtotext(decyptrext,'t',reverse_alphabet))


def bruteforce(dim):
    alphabet = {}
    for character in string.ascii_uppercase:
        alphabet[character] = string.ascii_uppercase.index(character)

    reverse_alphabet = {}
    for i, value in alphabet.items():
        reverse_alphabet[value] = i

    plaintext=open('PlainText.txt','r')
    plain=plaintext.read()
    plain=plain.replace(" ", "")
    plain=plain.upper()
    ciphertext=open('CipherText.txt','r')
    cipher=ciphertext.read()
    brute=open('BruteForce.txt','w')

    if len(plain) / dim >= dim:
        p = textmatrix(plain, dim, alphabet)
        p = p[:, 0:dim]
    pinverse = inverse(p, alphabet)

    if pinverse is None:
        raise Exception("matrix of the plaintext is not invertable")
    
    c = textmatrix(cipher, dim, alphabet)
    c = c[:, 0:dim]

    dim = c.shape[0]
    m_grams = pinverse.shape[1]
    key = np.zeros((dim, m_grams)).astype(int)
    for i in range(m_grams):
        key[:, i] = np.reshape(np.dot(c, pinverse[:, i]) % len(alphabet), dim)
    brute.write(matrixtotext(key,'k',reverse_alphabet))


encrypt('STARLESSZ')
decrypt('STARLESSZ')
bruteforce(3) #Needs plaintext and the corresponding ciphertext to get the key, also 3 is the squareroot of the key should be changed if bruteforce fails