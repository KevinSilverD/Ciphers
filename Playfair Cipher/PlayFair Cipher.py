
def createtable(key):
    key=key.replace(" ", "")
    key=key.upper()
    result=list()

    for i in key: #storing key
        if i not in result:
            if i=='J':
                result.append('I')
            else:
                result.append(i)
    flag=0
    for i in range(65,91): #storing other character
        if chr(i) not in result:
            if i==73 and chr(74) not in result:
                result.append("I")
                flag=1
            elif flag==0 and i==73 or i==74:
                pass    
            else:
                result.append(chr(i))
    k=0
    table=[[0 for i in range(5)] for j in range(5)]
    for i in range(0,5):
        for j in range(0,5):
            table[i][j]=result[k]
            k+=1
    return table

def locindex(table,x):
    loc=list()
    if x=='J':
        x='I'
    for i ,j in enumerate(table):
        for k,l in enumerate(j):
            if x==l:
                loc.append(i)
                loc.append(k)
                return loc
            
def encrypt(Key):
    Plaintext=open('PlainText.txt','r')
    Plain=Plaintext.read()
    Plain=Plain.upper()
    Plain=Plain.replace(" ", "")
    ciphertext=open('CipherText.txt','a')
    table=createtable(Key)             
    i=0
    for s in range(0,len(Plain)+1,2):
        if s<len(Plain)-1:
            if Plain[s]==Plain[s+1]:
                Plain=Plain[:s+1]+'X'+Plain[s+1:]
    if len(Plain)%2!=0:
        Plain=Plain[:]+'X'
    while i<len(Plain):
        loc=list()
        loc=locindex(table,Plain[i])
        loc1=list()
        loc1=locindex(table,Plain[i+1])
        if loc[1]==loc1[1]:
            ciphertext.write("{}{}".format(table[(loc[0]+1)%5][loc[1]],table[(loc1[0]+1)%5][loc1[1]]))
            ciphertext.write(' ')
        elif loc[0]==loc1[0]:
            ciphertext.write("{}{}".format(table[loc[0]][(loc[1]+1)%5],table[loc1[0]][(loc1[1]+1)%5]))
            ciphertext.write(' ')
        else:
            ciphertext.write("{}{}".format(table[loc[0]][loc1[1]],table[loc1[0]][loc[1]]))
            ciphertext.write(' ')
        i=i+2

def decrypt(Key):
    ciphertext=open('CipherText.txt','r')
    cipher=ciphertext.read()
    cipher=cipher.upper()
    cipher=cipher.replace(" ", "")
    decrypted=open('DecryptedText.txt','a')
    table=createtable(Key)
    i=0
    while i<len(cipher):
        loc=list()
        loc=locindex(table,cipher[i])
        loc1=list()
        loc1=locindex(table,cipher[i+1])
        if loc[1]==loc1[1]:
            decrypted.write("{}{}".format(table[(loc[0]-1)%5][loc[1]],table[(loc1[0]-1)%5][loc1[1]]))
        elif loc[0]==loc1[0]:
            decrypted.write("{}{}".format(table[loc[0]][(loc[1]-1)%5],table[loc1[0]][(loc1[1]-1)%5])) 
        else:
            decrypted.write("{}{}".format(table[loc[0]][loc1[1]],table[loc1[0]][loc[1]])) 
        i=i+2        

decrypt('Monarchy')