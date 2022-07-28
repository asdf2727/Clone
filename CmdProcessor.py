from importlib import invalidate_caches
from math import remainder
import os
import requests

from WordChecker import WordChecker
from random import sample

class CmdProcessor:

    # Constructor

    def __init__(self):
        if os.path.isfile("valid-words.txt"):
            print("The file 'valid-words.txt' was found! All ", end = "")
            self.processAdd(["valid-words.txt"])
            self.unsaved = False
        self.processReset(["hints"], True)

    # Info functions

    Hints = []

    def processHelp(self, args = None, forced = False):
        if not args:
            print("Available commands: ?, help, stats, add, remove, save, match, reset")
        elif len(args) == 1:
            FuncName = args[0];
            if FuncName == "quit" or FuncName == "exit":
                print("Exits the program")
            elif FuncName == "?" or FuncName == "help":
                print(FuncName + ": shows available commands.")
                print(FuncName + " [funcion-name]: Shows details about a command.")
            elif FuncName == "stats":
                print("stats database: Shows all the words in the database")
                print("stats hints: Shows all the words in the database")
            elif FuncName == "add":
                print("add [urls... + filepaths... + words...]: Reads web pages, files and words and puts them in the database.")
            elif FuncName == "remove":
                print("remove [urls... + filepaths... + words...]: Reads web pages, files and words and removes them from the database.")
            elif FuncName == "save":
                print("save: Saves the current database in valid-words.txt. If file does not exist, it is created")
            elif FuncName == "match":
                print("match [hinted-word]: Reads the hint and reduces word posibilities.")
                print("match: Output the best word.")
            elif FuncName == "reset":
                print("reset database: Clears the database.")
                print("reset hints: Resets all hints.")
            else:
                print("Command name is not recognized!")
        else:
            print("The 'help' command only accepts zero or one arguments!")

    def processStats(self, args = None, forced = False):
        if len(args) == 1:
            if args[0] == "database":
                for word in self.valids:
                    print(word, end = " ")
                if len(self.valids) == 1:
                    print("\n1 word was found")
                else:
                    print("\n" + str(len(self.valids)) + " words were found")
            elif args[0] == "hints":
                for hint in self.Hints:
                    print(hint)
                if len(self.Hints) == 1:
                    print("1 hint was found")
                else:
                    print(str(len(self.Hints)) + " hints were found")
            else:
                print("The 'stats' command only accepts as argument 'database' or 'hints'!")
        else:
            print("The 'stats' command only accepts one argument!")

    # Database functions

    unsaved = False
    valids = set()

    def isAlpha(self, word):
        for letter in word.lower():
            if 'a' > letter or letter > 'z':
                return False
        return True

    def processExit(self, forced = False):
        if self.unsaved == True and not forced:
            return str(input("You have unsaved changes in the database! Are you sure you want to exit? (Y/n)")) == "Y"
        else:
            return True

    def getWords(self, args = None):
        words = set()
        for source in args:
            if source.startswith("http"):
                words.update(requests.get(source).text.split())
            elif os.path.isfile(source):
                words.update(open(source).read().split())
            else:
                words.add(source)
        ans = set()
        for word in words:
            word = word.upper()
            if len(word) == 6 and not self.isAlpha(word[5]):
                word = word.removesuffix(word[5])
            if len(word) == 5 and self.isAlpha(word):
                ans.add(word.upper())
        return ans

    def processAdd(self, args = None, forced = False):
        news = self.getWords(args)
        added = len(self.valids)
        self.valids = self.valids.union(news)
        added = len(self.valids) - added
        for word in news:
            if self.Check.check(word):
                self.remains.add(word)
        if added == 0:
            print("0 words were added.")
        elif added == 1:
            print("1 word was added.")
            self.unsaved = True
        else:
            print(str(added) + " words were added.")
            self.unsaved = True

    def processRemove(self, args = None, forced = False):
        news = self.getWords(args)
        removed = len(self.valids)
        self.valids = self.valids.difference(news)
        removed -= len(self.valids)
        self.remains = self.remains.difference(news)
        if removed == 0:
            print("0 words were removed.")
        elif removed == 1:
            print("1 word was removed.")
            self.unsaved = True
        else:
            print(str(removed) + " words were removed.")
            self.unsaved = True

    def processSave(self, forced = False):
        if self.unsaved:
            OutHandle = open("valid-words.txt", "wt")
            for word in self.valids:
                OutHandle.write(word + " ")
            self.unsaved = False;
            print("All " + str(len(self.valids)) + " words have been saved in 'valid-words.txt'.")
            OutHandle.close()
        else:
            print("There are no changes to save!")

    # Solve functions

    Check = WordChecker()
    remains = set()

    def processMatch(self, args = None, forced = False):
        if len(args) == 0:
            if len(self.remains) >= 10:
                print("10 random words: ", end = "")
                chosen = sample(self.remains, 10)
                for word in chosen:
                    print(word, end = " ")
            else:
                print(str(len(self.remains)) + " random words: ", end = "")
                for word in self.remains:
                    print(word, end = " ")
            print("")
        else:
            print("The 'reset' command only accepts zero arguments!")

    def processHint(self, args = None, forced = False):
        if len(args) == 1:
            hint = args[0].upper()
            invalid = False
            for index in range(0, 10):
                if index & 1 == 0:
                    if hint[index] != '-' and hint[index] != '~' and hint[index] != '+':
                        invalid = True
                        break
                else:
                    if 'A' > hint[index] and hint[index] > 'Z':
                        invalid = True
                        break
            if invalid:
                print("Invalid hint was typed!")
            else:
                self.Hints.append(hint)
                self.Check.update(hint)
                newRemains = set()
                for word in self.remains:
                    if self.Check.check(word):
                        newRemains.add(word)
                self.remains = newRemains
                if len(self.remains) == 1:
                    print("Hint added, 1 word remains.")
                else:
                    print("Hint added, " + len(self.remains) + " words remain.")
        else:
            print("The 'hint' command only accepts one argument!")

    def processReset(self, args = None, forced = False):
        if len(args) == 1:
            if args[0] == "database":
                if not forced:
                    if str(input("Are you sure you want to clear the database? (Y/n)")) != "Y":
                        return
                self.valids = set()
                self.unsaved = True
                print("Database cleared.")
            elif args[0] == "hints":
                if not forced:
                    if str(input("Are you sure you want to reset hints? (Y/n)")) != "Y":
                        return
                self.Hints = []
                self.remains = self.valids
                print("Hints reset.")
            else:
                print("The 'reset' command only accepts as argument 'database' or 'hints'!")
        else:
            print("The 'reset' command only accepts one argument!")

if __name__ == "__main__":
    pass