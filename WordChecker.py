###
# https://github.com/Ioaxx/ioa_code.git 
# Class owning the set of hints given in the course
# of playing one game of Wordle
class WordChecker:
    
    # Class constructor:
    def __init__(self):
        #print(f"TODO: WordChecker is initialized")
        self.dictionar = {}
        self.hint_word = ""
        for l in range(ord('A'), ord('Z')+1):
            self.dictionar[chr(l)] = "unknown" 

    ###
    # Updates the internal state of the checker with a new hint
    def update(self, hint):
        print(f"TODO: WordChecker adding the hint: '{hint}'.")
        '''
        dictionar pe litere, adaugam culoare si pozitii,
        primim ca parametru "hint " cu tilda plusuri si minusuri si tilda
        '''
        #+c-h~a-i-r
        hint_word=list(hint)
        for i in range (0,10,2):
            if self.dictionar[hint_word[i+1]] == "unknown": #or dictionar[self.hint_word[i+1]=="yellow" and dictionar[hint_word[i]]=="+"]:
                self.dictionar.pop(hint_word[i+1])
                #dictionar[hint_word[i+1]]={}#SET
            if hint_word[i]=="+":
                self.dictionar[hint_word[i+1]] = ["green", ((i+1)//2)+1]
            elif hint_word[i]=="-":
                self.dictionar[hint_word[i+1]] = ["grey", ((i+1)//2)+1]
            elif hint_word[i]=="~":
                if hint_word[i+1] not in self.dictionar.keys():
                    self.dictionar[hint_word[i+1]] = []
                self.dictionar[hint_word[i+1]] += ["yellow", ((i+1)//2)+1]
    
     ###
     # Checks whether a given word matches all known hints
    def check(self, word, dictionar):
        for l in word:
            if "green" not in self.dictionar[l]:
                return False
        #filter bazza de date pt litere grey
        f= open("stats\\words.txt")
        dictionar_cuvinte = {}
        lines = f.readlines()
        for line in lines:      #Tinder de cuvinte
            cuv = line.split()
            for i in range(1) :
                dictionar_cuvinte[cuv[0]]=cuv[1]
        for cuv in dictionar_cuvinte.keys():        #not good   TO BE DONE
            for lit in dictionar.keys():
                if "grey" in lit and  lit in cuv:
                    return False
                for i in range(10):
                    if lit is "yellow"  and cuv[dictionar.index("yellow")+1] ==lit:
                        return False
        return True    
        
        
        ###
        # Returns a string representation of the entire object
    def __str__(self):
        return f"TODO: WordChecker internal state."

###
# WordChecker test code
if __name__ == "__main__":
    # creates a test WordChecker object and run through its methods
    wordChecker = WordChecker()
    wordChecker.update("~S~T-A-I-R")
    wordChecker.update("~T~S-A-I-R")
    print(wordChecker.check("TSAIR"))
    print(wordChecker)