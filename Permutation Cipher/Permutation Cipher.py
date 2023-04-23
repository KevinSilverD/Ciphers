import textwrap

def encrypt(n,key):
    plain=open('PlainText.txt','r')
    cipher=open('CipherText.txt','w')
    text=plain.read()
    splittext=textwrap.wrap(text,n)
    key=str(key)
    result=''
    if not len(key)==n:
        print('The length of key should be equal to the length of blocks')
    elif len(text)%n!=0:
        print('The number of letter of the plaintext should be divisible by the length of blocks')
    else:
        for i in splittext:
            for j in key:
                result+=i[int(j)-1]
    cipher.write(result)

def decrypt(n,key):
    cipher=open('CipherText.txt','r')
    decrypt=open('DecryptedText.txt','w')
    text=cipher.read()
    splittext=textwrap.wrap(text,n)
    key=str(key)
    inversekey=list(key)
    x=0

    for i in key:
        inversekey[int(i)-1]=str(x)
        x+=1
    inversekey=''.join(inversekey)

    result=''
    if not len(key)==n:
        print('The length of key should be equal to the length of blocks')
    elif len(text)%n!=0:
        print('The number of letter of the plaintext should be divisible by the length of blocks')
    else:
        for i in splittext:
            for j in inversekey:
                result+=i[int(j)]
    decrypt.write(result)

encrypt(3,312)
decrypt(3,312)

