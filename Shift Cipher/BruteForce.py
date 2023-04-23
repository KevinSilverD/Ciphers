def bruteforce():
    ciphertext=open('CipherText.txt','r')
    brute=open('BruteForce.txt','w')
    cipher=ciphertext.read()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key=0
    while key<=26:
        result=''
        for letter in cipher:
            if letter in alpha:
                letter_index = (alpha.find(letter) - key) % len(alpha)
                result = result + alpha[letter_index]
            else:
                result = result + letter
        brute.write(result + '\n')
        key+=1
    
    
bruteforce()