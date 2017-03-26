
# Authenticate Query Unification Application
# Wayne Kenney - 2017                                   
#  _____                 ___     ___ 
# |  _  |___ _ _ ___ ___|_  |   |   |
# |     | . | | | .'|___|_| |_ _| | |
# |__|__|_  |___|__,|   |_____|_|___|
#         |_|                        
# By Pythogen


# Toxic
# Purpose: The purpose of this script is confidential.
# Use: Personal use.
# Version: 1.3

# Frame.py:

#Modules
import requests
from random import randint
import time
import string
import random
from tqdm import tqdm

#Program Information
print '\nPyAqua-1.0 - Requests Module Prototype\nBy Pythogen'



def id_generator(size=500, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

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
	Service = 'Newgrounds - Login'
	#Login URL
	login_URL = 'https://www.newgrounds.com/passport/mode/iframe/appsession/812703283236516b81e11ed4ddac931b30b292034ba228'
	#login_URL redirected to after login_URL containing keyword
	landing = 'http://www.newgrounds.com/bbs'
	#The keyword that indicates successful login_URL detection
	keyword = 'loggedin'

	#Display Banner
	#print '\n%s\n' % (Service)
	USERNAME = raw_input("Enter Username: ")
	PASSWORD = raw_input("Enter Password: ")

# ASCII Font Name 'Big'
print ''
print '  _______        _      '
print ' |__   __|      (_)     '
print '    | | _____  ___  ___ '
print '    | |/ _ \ \/ / |/ __|'
print '    | | (_) >  <| | (__ '
print '    |_|\___/_/\_\_|\___|\n'


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
		elif cmd =='post':

			for i in tqdm(range(1,100000)):

				time.sleep(1)

				a = id_generator()

				#POST Login data
				data1 = \
				{
					'comment': a,
					'page': '1',
					'id': '983077',
					'userkey': 'e9d88%O205d996ffb7e%145aOc54097a11f%Pd358br9c%%682c14%7%9%14f%d956sca330e0bObe5dr574crs%907365%%s6%6%af3d35db18br2Pd27f%7erP6fd90ccr00e01eebf94f960be7babc022d95c1655%s%4d7P%%O%rr308135990235575496',
				}

				#Header data
				header_data2 = \
				{
					'X-Requested-With': 'XMLHttpRequest',
					'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36',
					'Referer': 'http://fearnova.newgrounds.com/news/post/983077',
					'Origin': 'http://fearnova.newgrounds.com',
					'Host': 'fearnova.newgrounds.com',
					'Cookie': '__cfduid=db3173c13b913db562a4ced4cb261393c1490501067; remember_me_checkbox=1; ng_adcode_country_id=2; __utma=158261541.1985287000.1490501068.1490501068.1490501068.1; __utmb=158261541.22.9.1490501544103; __utmc=158261541; __utmz=158261541.1490501068.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=132636953.309726048.1490501336.1490501336.1490501336.1; __utmb=132636953.4.10.1490501336; __utmc=132636953; __utmz=132636953.1490501336.1.1.utmcsr=wayne.newgrounds.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ng_user0=a%3A1%3A%7Bs%3A7%3A%22default%22%3Ba%3A0%3A%7B%7D%7D; vmkIdu5l8m=H1vgGJEM6EGFs6zk0TsTHgSuTr3f4f3HdF198ALMOCKCL%2FNVcWQI7PQbHwfIl7XLs5c70sG79kaZX0MmEysCeoO9snyMVS%2F1ym9zGn%2FwLvvKT3wraCKFoHaoUxmwoT37PiJsCiG8Sj7XJuxeA_0XtY4BQaWbUv9FE_Lz0lYCoIY%3D; NG_GG_username=fearnova',
					'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
					'Content-Length': '302',
					'Connection': 'keep-alive',
					'Accept-Language': 'en-US,en;q=0.8',
					'Accept-Encoding': 'gzip, deflate',
					'Accept': '*/*',
				}

				r = requests.get("http://fearnova.newgrounds.com/news/comment")
				r = requests.post("http://fearnova.newgrounds.com/news/comment", data=data1, headers=header_data2)


			
	
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
		login_data = \
		{
			'username' : USERNAME,
			'password' : PASSWORD,
			'remember' : 1,
			'login' : 1,
		}

		#Header data
		header_data = \
		{
			'Host': 'www.newgrounds.com',
			'Connection': 'keep-alive',
			'Content-Length': '455',
			'Accept': '*/*',
			'Origin': 'http://www.newgrounds.com',
			'X-Requested-With': 'XMLHttpRequest',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
			'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Referer': 'http://www.newgrounds.com/',
		}


		# 1) Direct to login url. Prepare for POST login
		c.get(login_URL)

		# 2) Submit POST data. Initialize login
		c.post(login_URL, data=login_data, headers=header_data)

		# 3) Landing page after login attempt. Function name as object. func.var = x
		processReq.page = c.get(landing)

		# 4) Looking for keyword indicating successful login
		Check = processReq.page.content.find(keyword)


		#Continuous auth checking. Line by line
		while(True):
			if Check == -1:
				print '\nlogin failed. (Try again)'
				#print processReq.page.content
				main()
				processReq()
			else:
				print '\nWelcome, ' + USERNAME + '\n'

				#Login success. Go to command console
				cpPrompt()


#Process Auth Details
processReq()