# Wayne Kenney 2015

#_________   _________ _________           ________                                   __                
#\_   ___ \ /   _____//   _____/          /  _____/  ____   ____   ________________ _/  |_  ___________ 
#/    \  \/ \_____  \ \_____  \   ______ /   \  ____/ __ \ /    \_/ __ \_  __ \__  \\   __\/  _ \_  __ \
#\     \____/        \/        \ /_____/ \    \_\  \  ___/|   |  \  ___/|  | \// __ \|  | (  <_> )  | \/
# \______  /_______  /_______  /          \______  /\___  >___|  /\___  >__|  (____  /__|  \____/|__|   
#        \/        \/        \/                  \/     \/     \/     \/           \/                  


# Globalize help var
cmds = ("\n1. Start by entering class name"
			"\n2. Enter the type of styles to be included "
			"(seperated by commas)\n\nStyles:\n\ncenter.text"
			"\ncenter.div\nborder.round\n\nMore to be included...\n")

# Center div object inclusion code
centerdiv = ('\ndisplay: block;'
					'\nmargin-left: auto;'
					'\nmargin-right: auto;'
					'\nwidth: 100%%;\n')

# Center text object [suck as p element]
centertext = ('\ntext-align: center;\n')

def main():
	# Globalize initial class dec
	global cmd

	# Wait for class name
	while True:
		cmd = raw_input("Enter Class (? for list): ")
		# Display commands
		if cmd == "?":
			print cmds
		else:
			#go to styles
			styling()


def styling():
	# Wait for styles
	global inArr
	inArr = ['','']

	# Infinite loop
	while True:
		cmd2 = raw_input("\nClass = %s\n\nEnter styles seperated by comma (? for list): " % (cmd))
		# Re-display commands
		if cmd2 == "?":
			print cmds
		else:
			# Check for css command
			check = cmd2.find("center.div")
			check2 = cmd2.find("center.text")

			# If not found then..
			if check != -1:
				# Add to array space
				inArr[0] = centerdiv

			# Check fo second command
			if check2 != -1:
				# Include second command to array space
				inArr[1] = centertext

			# Open selector
			print ('\n.%s { ' % (cmd))

			# Generate according to input
			# Loop array length
			for i in inArr:
				# Include code
				print i
				# End loop

			# Close selector
			print ('}\n')

main()