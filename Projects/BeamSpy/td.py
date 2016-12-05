
# BeamSpy Prototype
# Wayne Kenney - 2015                                   
# By Pythogen

# ( This script is an experimental work in-progress as I slowly learn how Beam works.. )

# Frame.py:

#Modules
import requests
from random import randint
import time
from playsound import playsound
from pygame import mixer


#Program Information
print '\nPyAqua-1.0 - Requests Module Prototype\nBy Pythogen'

#Main Routine.
def main():

	#Enable access to variables ANYWHERE
	global USERNAME
	global PASSWORD
	global login_URL
	global page
	global landing
	global keyword
	global attempts

	#Site's Name (Banner)
	Service = 'Beam Status'
	#Login URL
	login_URL = 'https://beam.pro/api/v1/users/login?'
	#login_URL redirected to after login_URL containing keyword
	landing = 'https://beam.pro/api/v1/channels/'
	#The keyword that indicates successful login_URL detection
	keyword = 'Logout'

	#Display Banner
print ' _______  _______  _______  __   __    _______  _______  __   __ '
print ' |  _    ||       ||   _   ||  |_|  |  |       ||       ||  | |  |'
print ' | |_|   ||    ___||  |_|  ||       |  |  _____||    _  ||  |_|  |'
print ' |       ||   |___ |       ||       |  | |_____ |   |_| ||       |'
print ' |  _   | |    ___||       ||       |  |_____  ||    ___||_     _|'
print ' | |_|   ||   |___ |   _   || ||_|| |   _____| ||   |      |   |  '
print ' |_______||_______||__| |__||_|   |_|  |_______||___|      |___|  \n\n'


#Go to main 
main()

#Console prompt after successful login
def cpPrompt():

	#Command line Construct. Add commands here..
	while(True):

		#Listen for command input
		cmd = raw_input('%s>' % (USERNAME))

		#Command Construct
		if cmd == '?':
			#Show list of commands
			print '\n- who (Users Online)\n- quit\n'
		elif cmd == 'who':
			#Call function to extract data between tags. Function name included in var for global access
			print '\n' + find_between( processReq.page.content,"Online: (<strong>","</strong>)" ) + '\n'
		elif cmd == 'quit':
			quit()
			
	
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
	with requests.Session() as c:
	
		#POST Login data
		#Header data
		header_data = \
		{
			'x-csrf-token': 'undefined',
			'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36',
			'referer': 'https://beam.pro/anatlus89',
			'cookie': '__cfduid=d88f23e6e8cd85b8cb22893c24b1be5e21477517097; _gat=1; _ga=GA1.2.1606304139.1477517098; sid=Fe26.2**3605772755aaf1339645e6d78ecb0612d4222db118221c3640a8c24d59c358f4*8KHQh6aBVH_-boyMItg_Gw*3HtMWICAqM_f3tEItBfRY7s1dQbegeTOrXWao3JvmZcuyXmgP9fW8U2rcLIlbqFGIH1_RMzxbVYOs4fwBdIIvw0JsOOCpgit4T0GB2zazcOGUMO2I3JByXkUEU495Z18nm_Ov9nlqFqzjMh0Lwky1zQ4-UqMBPtfJGqnKvVIMD97jQNOvaYkbA8quLVsfPH0yZf6ICMbCKrJoKOImvzaxBQscGgxg7a-wr7hHabE6zfT-kYj_vx0i0neWQoX6n9TG4U0sU58QRAgBjKt7nJ9d6a95Nuj1ichF2tFCVWL5vJsxfBYkzWW3T2uX5KolCjgYL9iQSUG47fk8avvq-B3v6CzVqnqixpjhQGtXcGSSPkvZTOeDC_mhURA-6IpbVlm**850ef7668c9f4163cfb1bd78fd7e5d348c3da5ff337a72bc6861d21bc5671c90*vFge5XV6a3g5Odkk-IMVa2WJBn_iQSrzdBKtCdjAeNY; __bcsrf=91ec438779d99986339653f1c9d0341bcd2a4595',
			'accept-language': 'en-US,en;q=0.8',
			'accept-encoding': 'gzip, deflate, sdch, br',
			'accept': '*/*',
			'scheme': 'https',
			'path': '/api/v1/channels/anatlus89?',
			'method': 'GET',
			'authority': 'beam.pro',
		}

		login_data = '{"username":"chaotic","password":"passxz45690"}'

		p=0
		cnt = 0
		sparks = 0
		exp = 0

		while p != 1:
			control = raw_input("Enter command: ")

			# Check Details of Streamer
			if control == "user.check":
				p=1

			# Used to mine Spark points... [Under Construction]
			elif control == "mine":
				cmd = raw_input("Enter Username: ")
				while p != 1:
					time.sleep(1)
					# 3) Extract user data then print > Loop
					processReq.page = c.get(landing + cmd)
					#Check = processReq.page.content.find(keyword)
					onlineStatus = find_between( processReq.page.content,'online":',',"' )
					if onlineStatus=="true":
						ostat = "[!] This user is Online - "
					else:
						ostat = "[x] This user is Offline - "
						mixer.init() #you must initialize the mixer
						alert=mixer.Sound('alert.wav')
						alert.play()
					cnt = cnt + 1
					print ostat + str(cnt)
					if cnt%60 == 0:
						sparks = sparks + 2
						print "\nYou earned 2 more Spark points! - Total Earned: %s\n" % (sparks)
					elif cnt%300 == 0:
						exp = exp + 10
						print "\nYou earned 10 more experience points! - Total Earned: %s\n" % (exp)


		while True:

			cmd = raw_input("Enter Username: ")

			# 3) Extract user data then print > Loop
			processReq.page = c.get(landing + cmd)
			#Check = processReq.page.content.find(keyword)
			onlineStatus = find_between( processReq.page.content,'online":',',"' )
			if onlineStatus=="true":
				ostat = "[!] This user is Online."
			else:
				ostat = "[x] This user is Offline."

			followers = find_between( processReq.page.content,'numFollowers":',',"description' )
			mid = find_between( processReq.page.content,'id":',',"userId' )
			userid = find_between( processReq.page.content,'userId":',',"token' )
			followers = find_between( processReq.page.content,'numFollowers":',',"description' )
			totalView = find_between( processReq.page.content,'viewersTotal":',',"v' )
			viewers = find_between( processReq.page.content,'viewersCurrent":',',"numFo' )
			level = find_between( processReq.page.content,'level":',',"social' )
			#print "%s : %s" % (processReq.page.content, p)
			print "\n%s\n\n Level: %s\n Main ID: %s\n UserID: %s\n Number of Followers: %s\n Total Views: %s\n Current Views: %s\n" % (ostat, level ,mid, userid, followers, totalView, viewers)


#Process Auth Details
processReq()