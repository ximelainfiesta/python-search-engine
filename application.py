"""Search Engine"""

import re
import urllib2
import sys
#We import some modules

class Find(object):
    """Class that searched for words in urls"""
    def search(self):
        """Asks the user for two urls and one word, searches for matches"""
        while True:
            try:
                word = raw_input("Enter a word to be searched: ")
                url1 = raw_input("Enter a valid URL (remember to add https://): ")
                url2 = raw_input("Enter the second valid URL (remember to add https://): ")

                word = word.lower()
                url1 = url1.lower()
                url2 = url2.lower()

                web = urllib2.urlopen(url1)#opens url
                web2 = urllib2.urlopen(url2)
                read = web.read() #reads the file
                read2 = web2.read()

                search1 = len(re.findall(word, read)) #searches the given word in the file
                search2 = len(re.findall(word, read2))

                web.close() #close the file
                web2.close()

                if search1 > search2:
                    print "The URL with more repetitions is: ", url1
                    print "The number of times the word was found is: ", search1
                elif search2 > search1:
                    print "The URL with more repetitions is: ", url2
                    print "The number of times the word was found is: ", search2
                elif search2 == search1:
                    print "Both URL's have the word the same time: ", search1, "-", search2
                else:
                    print "Wow, What is going on?"

                PROOF.tryagain() #initiates the try again method
            except ValueError:
                print "Enter a Valid URL with https:// included"
            except NameError:
                print "-Enter a Valid URL with https:// included"
            except TypeError:
                print "--Enter a Valid URL with https:// included"

    def tryagain(self):
        """Asks the user for another search"""
        while True:
            print "Do you want to search for another word? Y/N"
            user = raw_input(">")
            user = user.lower()
            if user == "y":
                PROOF.search()
            elif user == "n":
                print "Good-Bye"
                sys.exit()
            else:
                print "Invalid option, enter only Y or N"

PROOF = Find()
PROOF.search()


