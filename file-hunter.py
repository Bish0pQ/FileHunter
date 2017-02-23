# Authors: Bish0pQ, Inori
# Website: http://www.bish0pq.pw
# Proud member of Sinister.ly (IDE)

# try/catch for Python 3 compatability
try:
	from urllib2 import *
except ImportError:
	from urllib.request import *
	from urllib.error import *

from string import ascii_lowercase,digits	# strings with loweralpha + digit charsets
from argparse import ArgumentParser		# CLI argument parser
from random import choice			# random element selector

charset=ascii_lowercase+digits	# charset in use
attempted=[]			# list of last 16 attempted urls
successes=0			# number of successful downloads

# create a parser instance
parser=ArgumentParser(
	description="Hunt for files on hosting sites like pomf, mixtape.moe, or imgur. You can find a list of alternatives here: https://goo.gl/wPDXdV",
	usage="file-hunter.py [--help] [--verbose] [--ext ex] [--results n] [--length n]\n[--proxy adr] [--ssl] url"
)

# Add arguments to the parser
parser.add_argument('-v','--verbose',action="store_true",help='enable verbose logging')
parser.add_argument('-e','--ext',metavar='ex',default='zip',help='extension to look for (no .)')
parser.add_argument('-r','--results',metavar='n',type=int,default=5,help='number of results to download')
parser.add_argument('-l','--length',metavar='n',type=int,default=6,help='length of file names')
parser.add_argument('-p', '--proxy',metavar='adr',help='proxy to use in IP:PORT format')
parser.add_argument('-s', '--ssl',action="store_true",help='use SSL for proxies')
parser.add_argument('url',action="store",help='url of the search target')

# get arguments
args=parser.parse_args()

def generate_url():
	"""generate the random string to use for a url"""
	# generate a random string of the specified length
	rand_str=''.join(choice(charset) for _ in range(args.length))
	
	# if the url was generated recently (unlikely), return
	# a recursive method call
	if rand_str in attempted: return generate_url()

	if len(attempted)==16: attempted.pop(0)	# pop the list if it's already 16 items long
	attempted.append(rand_str)		# append the new url to the list
	return rand_str				# return the url
	
def create_req(url):
	"""create an http request for the target site using the generated url"""
	global successes	# scope the global successes counter

	full_path=args.url+'/'+url+'.'+args.ext	# full path of the link
	try:
		if args.proxy is not None:
			# initialize proxy handler with requested protocol
			if args.ssl: proxy_support = ProxyHandler({"https":"https://" + args.proxy})	#Add the proxy
			else: proxy_support = ProxyHandler({"http":"http://" + args.proxy})				#Add the proxy
			builder = build_opener(proxy_support)
			install_opener(builder) #Install the builder
			f=urlopen(full_path)			# attempt to download the file
			print("[+] downloading '%s'"%full_path)	# print a message
			successes+=1
		else:
			f=urlopen(full_path) #Attempt to download the file
			print("[+] downloading '%s'"%full_path)	# print a message
			successes+=1
		with open(url+'.'+args.ext,'w') as file:
			file.write(f.read())	# write the file locally
	except HTTPError as err:
		# report error if verbose logging is enabled
		if args.verbose:
			print("[-] %s returned HTTP error code %d (%s)"%(full_path,err.code,err.reason))
	except URLError as err:
		# report error if verbose logging is enabled
		if args.verbose:
			print("[-] %s threw a URL error: %s"%(full_path,err.reason))

# main loop
while successes<args.results:
	try:
		# generate a url and attempt to download it
		create_req(generate_url())
	except KeyboardInterrupt:
		print("successfully downloaded %d/%d files; quitting"%(successes,args.results))
		quit()
