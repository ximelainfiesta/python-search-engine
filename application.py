import re
import urllib2 

class Find(object):
	def __init__(self, word, url1, url2):
		self.word = word
		self.url1 = url1
		self.url2 = url2




User = Find(raw_input("Enter a word to be searched: "), raw_input("Enter a valid URL: "), raw_input("Enter the second valid URL: "))