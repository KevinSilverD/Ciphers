import copy
import re
from itertools import combinations

dictionarynum = 2  # Choose a number between 1 to 7, increase if decryption failed 
maxbadwordrate = 0.06 # Choose a number between 0 to 1, increase if decryption failed 

Alpha = 'abcdefghijklmnopqrstuvwxyz'


class WordList:
    maxwordlength = 8

    def __init__(self):
        self.words = {}
        for i in range(dictionarynum):
            for word in open('Dictionary/' + str(i) + '.txt'):
                word = word.strip()
                wordlen = len(word)
                properties = (wordlen, len(set(word)))

                if wordlen > WordList.maxwordlength:
                    words = self.words.get(properties, [])
                    words.append(word)
                    self.words[properties] = words
                else:
                    words = self.words.get(properties, set([]))
                    for i in range(wordlen + 1):
                        for dotpos in combinations(range(wordlen), i):
                            addword = list(word)
                            for j in dotpos:
                                addword[j] = '.'

                            words.add(''.join(addword))
                    self.words[properties] = words

    def findword(self, template, diffchr):

        properties = (len(template), diffchr)
        if properties not in self.words:
            return False

        words = self.words[properties]

        if properties[0] > WordList.maxwordlength:
            template = re.compile(template)

            for word in words:
                if template.match(word):
                    return True
        else:
            if template in words:
                return True
        return False


class KeyFinder:
    def __init__(self, encword):
        self.maxpoint = int(len(encword) * maxbadwordrate)
        self.wordlist = WordList()
        self.cipherword = encword
        self.diffchr = {}
        self.foundkey = {}
        for cipherword in encword:
            self.diffchr[cipherword] = len(set(cipherword))

    def keypoints(self, key):

        trans = str.maketrans(Alpha, key)
        points = 0

        for cipherword in self.cipherword:
            different_chars = self.diffchr[cipherword]
            translated_word = cipherword.translate(trans)

            if not self.wordlist.findword(translated_word,different_chars):
                points += 1
        return points

    def recursivekey(self, key, possibleletters, level):
        if '.' not in key:
            points = self.keypoints(key)
            self.foundkey[key] = points
            return

        nextpos = -1
        minlen = len(Alpha) + 1

        for pos in range(len(Alpha)):
            if key[pos] == ".":
                for letter in list(possibleletters[pos]):
                    new_key = key[:pos] + letter + key[pos + 1:]

                    if self.keypoints(new_key) > self.maxpoint:
                        possibleletters[pos].remove(letter)
                        if not possibleletters[pos]:
                            return

                if len(possibleletters[pos]) < minlen:
                    minlen = len(possibleletters[pos])
                    nextpos = pos

        while possibleletters[nextpos]:
            letter = possibleletters[nextpos].pop()
            newpossibleletters = copy.deepcopy(possibleletters)
            for pos in range(len(Alpha)):
                newpossibleletters[pos] -= set([letter])
            newpossibleletters[nextpos] = set([letter])
            new_key = key[:nextpos] + letter + key[nextpos + 1:]
            self.recursivekey(new_key, newpossibleletters, level + 1)

    def find(self):
        if not self.foundkey:
            possibleletters = [set(Alpha) for i in range(len(Alpha))]
            self.recursivekey("." * len(Alpha), possibleletters, 1)
        return self.foundkey


def bruteforce():
    ciphertext = open('CipherText.txt','r').read().lower()
    cipherwords = re.findall(r"[a-z']+", ciphertext)

    cipherwords = [word for word in cipherwords
                      if "'" not in word and
                         len(word) <= WordList.maxwordlength
                ]
    cipherwords = cipherwords[:200]

    keys = KeyFinder(cipherwords).find()
    if not keys:
        print('Key not founded, try to increase MAX_BAD_WORDS_RATE')
    bestkey = min(keys, key=keys.get)
    trans = str.maketrans(Alpha, bestkey)
    Decrypted = open('CipherText.txt','r').read().translate(trans)

    bruteforced = open('BruteForce.txt', 'w')
    bruteforced.write(Decrypted)

bruteforce() #Takes a while but it works be paitient