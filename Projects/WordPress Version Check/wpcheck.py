
# Authenticate Query Unification Application
# Wayne Kenney - 2015                                   
#  _____                 ___     ___ 
# |  _  |___ _ _ ___ ___|_  |   |   |
# |     | . | | | .'|___|_| |_ _| | |
# |__|__|_  |___|__,|   |_____|_|___|
#         |_|                        
# By Pythogen

# Frame.py:

#Modules
import requests
from random import randint
import time
import os

#Program Information
print '\n(Powered by PyAqua-1.0 Framework - Wayne Kenney)'

#Main Routine.
def main():

	#Enable access to variables anywhere
	global USERNAME
	global PASSWORD
	global login_URL
	global page
	global land
	global keyword
	global attempts

	#Site's Name (Banner)
	Service = 'WordPress Version - Check'

	#login_URL redirected to after login_URL containing keyword
	land = ['http://www.thatvideogameblog.com/',
			'http://ukresistance.co.uk/',
			'http://ohsheglows.com/',
			'http://www.runningonrealfood.com/']

	#The keyword that indicates successful login_URL detection
	keyword = 'loggedin'

	#Define username
	#USERNAME = raw_input("\nPlease enter a username: ")
	USERNAME = 'Pythogen'

	#Display Banner
print '__      _____  __   __                ___ _           _    '
print '\ \    / / _ \ \ \ / /__ _ _   ___   / __| |_  ___ __| |__ '
print ' \ \/\/ /|  _/  \ V / -_)  _| |___| | (__|   \/ -_) _| / / '
print '  \_/\_/ |_|     \_/\___|_|          \___|_||_\___\__|_\_\ '
                                                                                                

#Go to main 
main()
def cmdList():

	# Call function to extract data between tags. Function name included in var for global access
	# Cycle for loop from 0 to size of array
	for i in range(0, len(land)):

		# Check the proper directory that enables
		# version disclosure
		land[i] = land[i] + '/wp-login.php?'
		# Get from next link in array
		processReq.page = c.get(land[i])
		# Check and print
		print '\nSite: %s\nVersion: [ ' % (land[i]) + find_between( processReq.page.content,"buttons.min.css?ver=","' type='text/css'" ) + ' ]\n'

# Console prompt after successful login
def cpPrompt():

	# Command line Construct. Add commands here..

	cmdList()

	while(True):

		# Listen for command input
		cmd = raw_input('%s>' % (USERNAME))

		# Check
		if cmd == "?":
			cmdList()

		# Exit
		elif cmd == 'quit':
			quit()

# Clipboard function
def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)
	
#Used for finding values between tags
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""


def processReq():
	#Shorten method
	global c
	with requests.Session() as c:
	
		#Continuous auth checking. Line by line
		while(True):
			print '\nWelcome, ' + USERNAME + '\n'
			#Login success. Go to command console
			cpPrompt()


#Process Auth Details
processReq()