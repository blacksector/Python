
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

	#Enable access to variables ANYWHERE
	global USERNAME
	global PASSWORD
	global login_URL
	global page
	global land
	global keyword
	global attempts

	#Site's Name (Banner)
	Service = 'Toxic Steam'
	#login_URL redirected to after login_URL containing keyword
	land = ['http://steamcommunity.com/id/annephrank',
			'http://steamcommunity.com/profiles/76561198088067348/',
			'http://steamcommunity.com/profiles/76561198050674224/']
	#The keyword that indicates successful login_URL detection
	keyword = 'loggedin'
	#Define username
	USERNAME = raw_input("\nPlease enter a username: ")
	#Display Banner
	print '   ______                 ______       __          '
	print '  / __/ /____ ___ ___ _  / __/ /____ _/ /___ _____ '
	print ' _\ \/ __/ -_) _ `/    \_\ \/ __/ _ `/ __/ // (_-< '
	print '/___/\__/\__/\_,_/_/_/_/___/\__/\_,_/\__/\_,_/___/ '



#Go to main 
main()
def cmdList():
	#Call function to extract data between tags. Function name included in var for global access
	processReq.page = c.get(land[0])
	print '\n(1) - Annephrank (98.229.232.45): [ ' + find_between( processReq.page.content,'<div class="profile_in_game_header">','</div>' ) + ' ]'
	processReq.page = c.get(land[1])
	print '(2) - DarknessErupto (50.136.11.210): [ ' + find_between( processReq.page.content,'<div class="profile_in_game_header">','</div>' ) + ' ]'
	processReq.page = c.get(land[2])	
	print '(3) - Aniziel (107.3.41.121): [ ' + find_between( processReq.page.content,'<div class="profile_in_game_header">','</div>' ) + ' ]'
	print "(4) - Check user's status."
	print "(?) - Show commands."
	print '(quit) - Close the program.\n'


#Console prompt after successful login
def cpPrompt():

	#Command line Construct. Add commands here..

	cmdList()

	while(True):

		#Listen for command input
		cmd = raw_input('%s>' % (USERNAME))

		#Command Construct
		if cmd == '1':
			#Show list of commands
			print '\n- IP of Annephrank copied to clipboard...\n'
			addToClipBoard('98.229.232.45')

		elif cmd == '2':
			#Show list of commands
			print '\n- IP of DarknessErupto copied to clipboard...\n'
			addToClipBoard('50.136.11.210')		
				
		elif cmd == '3':
			#Show list of commands
			print '\n- IP of Aniziel copied to clipboard...\n'
			addToClipBoard('107.3.41.121')		

		elif cmd == '4':
			
			# First process request and get content
			processReq.page = c.get(land[0])
			print "\n- Checking user's status...\n"
			a = find_between( processReq.page.content,'<div class="profile_in_game_header">','</div>' )
			if a == "Currently Offline":
				print '  Annephrank (98.229.232.45): [ ' + find_between( processReq.page.content,'<div class="profile_in_game_header">','</div>' ) + ' ]'
			else:
				print '  Annephrank (98.229.232.45): [ ' + find_between( processReq.page.content,'<div class="profile_in_game_header">','</div>' ) + ' ]'
			
			# Second process request and get content
			processReq.page = c.get(land[1])
			a = find_between( processReq.page.content,'<div class="profile_in_game_header">','</div>' )
			if a == "Currently Offline":
				print '  DarknessErupto (50.136.11.210): [ ' + find_between( processReq.page.content,'<div class="profile_in_game_header">','</div>' ) + ' ]'
			else:
				print '  DarknessErupto (50.136.11.210): [ ' + find_between( processReq.page.content,'<div class="profile_in_game_header">','</div>' ) + ' ]'
			
			# Third process request and get content
			processReq.page = c.get(land[2])
			a = find_between( processReq.page.content,'<div class="profile_in_game_header">','</div>' )
			if a == "Currently Offline":
				print '  Aniziel (107.3.41.121): [ ' + find_between( processReq.page.content,'<div class="profile_in_game_header">','</div>' ) + ' ]\n'
			else:
				print '  Aniziel (107.3.41.121): [ ' + find_between( processReq.page.content,'<div class="profile_in_game_header">','</div>' ) + ' ]\n'

		elif cmd == "?":
			cmdList()

		elif cmd == 'quit':
			quit()
			
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