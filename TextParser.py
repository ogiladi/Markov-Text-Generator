import re
LETTERS = re.compile(ur'[^a-z]')

class TextParser:

    def __init__(self, fileName):
        f = open(fileName, 'rb')
        lines = f.readlines()
        f.close()
        self.arr = []
        self.setArr(lines)

    def cleanWord(self, word):
        word = word.lower().decode('utf8')
        # toRemove = ["'", '"', ':', '.', ',', ':', ';', '?', '!', '(', ')', '-']
        while len(word) > 0 and not word[0].isalpha():
            word = word[1:]
        while len(word) > 0 and not word[-1].isalpha():
            word = word[:-1]
        return word.encode('utf8')

    def setArr(self, lines):
        for line in lines:
            for word in line.split():
                word = word
                cleanWord = self.cleanWord(word)
                if len(cleanWord) > 0:
                    self.arr.append(cleanWord)
    def getArr(self):
        return self.arr
