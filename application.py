import re
import urllib2
import sys

class Find(object):
    def search(self):
        """Asks the user for two urls and one word, searches for matches"""
        while True:
            self.word = raw_input("Enter a word to be searched: ")
            self.url1 = raw_input("Enter a valid URL (remember to add https://): ")
            self.url2 = raw_input("Enter the second valid URL (remember to add https://): ")

            self.word = self.word.lower()
            self.url1 = self.url1.lower()
            self.url2 = self.url2.lower()

            web = urllib2.urlopen(self.url1)
            web2 = urllib2.urlopen(self.url2)
            read = web.read()
            read2 = web2.read()

            s1 = len(re.findall(self.word, read))
            s2 = len(re.findall(self.word, read2))

            if s1 > s2:
                print "The URL with more repetitions is: ", self.url1
                print "The number of times the word was found is: ", s1
            elif s2 > s1:
                print "The URL with more repetitions is: ", self.url2
                print "The number of times the word was found is: ", s2
            elif s2 == s1:
                print "Both URL's have the word the same time: ", s1, "-", s2
            else:
                print "Wow, What is going on"

            PROOF.tryagain()


    def tryagain(self):
        while True:
            print "Do you want to search for another word? Y/N"
            user = raw_input(">")
            user = user.lower()
            if user == "y":
                PROOF.search()
            elif user == "n":
                print "Good-Bye"
                False
                sys.exit()
            else:
                print "Invalid option, enter only Y or N"



PROOF = Find()
PROOF.search()


