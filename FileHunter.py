#Author: Bish0pQ
#Website: http://www.bish0pq.pw
#Proud member of Sinister.ly (IDE)
#Proud member of Criminal.cat

import urllib2
import argparse
import string
from random import randint
##Add arguments to the parser

##Variables
lstTriedIDS = []
opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')] #Set a useragent

#Ask for the amount of results to generate
strFullUri = raw_input("Please give in the URL of the website: ")
strExtension = raw_input("Please give in the type you want to search for (ex. .zip): ")
intResults = int(raw_input("Please give in the amount of results to generate: "))
intCharCount = int(raw_input("Please give in the character count of the string to generate: "))

def GenerateString(length):
	"""Generate the string that will be used in the request"""
	strID = ""
	letters = list(string.ascii_lowercase)
	for x in range(0, 6): ##Change the number 6 to increase string length
		strID = strID + letters[randint(0,25)]
	strID = strFullUri + strID + strExtension
	##Check if ID is in list
	if strID not in lstTriedIDS:
		return strID
	else:
		lstTriedIDS.append(strID)
		return ""
		

def CreateRequest(strLink):
	"""Create a request to the target site with the generated string"""
	if strLink == "":
		print 'Link was a duplicate, generating a new one...'
	else:
		try:
			strSource = opener.open(strLink) #Try downloading the URL as a string
			return strLink + ' does exist!'
		except urllib2.HTTPError as err: #Failed to download the string (FIX: handle 403 errors)
			if err.code == 404:
				return strLink + ' does not exist!'
			elif err.code == 403:
				return strFullUri + ' might be blocking requests.'
			else:
				return 'An unexpected error ocurred. Please make sure the website is online.'
	

for z in range(0, intResults):
	print '[+] ' + CreateRequest(GenerateString(intCharCount))
	
