from random import randint

class TextGenerator:

    def __init__(self, textParser):
        self.d = {}
        arr = textParser.getArr()
        for i in range(len(arr)-1):
            self.add(arr[i], arr[i+1])
        if arr[-1] not in self.d:
            self.add(arr[-1], arr[0])

    def add(self, currWord, nextWord):
        if currWord not in self.d:
            self.d[currWord] = []
        self.d[currWord].append(nextWord)

    def generateSentence(self, numWords):
        index = randint(0, len(self.d.keys())-1)
        currWord = self.d.keys()[index]
        result = [currWord]
        for i in range(numWords-1):
            index = randint(0, len(self.d[currWord])-1)
            nextWord = self.d[currWord][index]
            result.append(nextWord)
            currWord = nextWord
        return ' '.join(result).capitalize()
