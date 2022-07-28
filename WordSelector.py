
###
# Class owning the set of hints and restricted words given in the course of playing one game of Wordle

intMax = 0x7fffffff

class WordData:

    Mask = [0, 0, 0, 0, 0]
    Freq = [0] * 26

    def __init__(self, word):
        index = 0
        while index < 5:
            self.Mask[index] |= 1 << (word[index] - ord('a'))
            self.Freq[word[index] - ord('a')] += 1
            index += 1


class WordSelector:

    remains = set()
    CanDo = [intMax, intMax, intMax, intMax, intMax]
    WillDo = [0, 0, 0, 0, 0]
    Freq = [[False, 5]] * 26

    def __init__(self, valids):
        self.remains = valids

    def Check(self, word):


    def AddWords (self, valids):
        for word in valids:
            if word is 

    ###
    # Updates the internal state of the checker with a new hint
    def update(self, hint):
        index = 0
        while index < 5:
            
            index += 1
        
    ###
    # Returns the best word out of the  remaining
    def best(self):

###
# WordChecker test code
if __name__ == "__main__":
    # creates a test WordChecker object and run through its methods
    wordChecker = WordChecker()
    wordChecker.update("some hint")
    print(wordChecker.check("some word"))
    print(wordChecker)
'''