# Wayne Kenney 2015 - Pythogen

# _________   _________ _________           ________                                   __                
# \_   ___ \ /   _____//   _____/          /  _____/  ____   ____   ________________ _/  |_  ___________ 
# /    \  \/ \_____  \ \_____  \   ______ /   \  ____/ __ \ /    \_/ __ \_  __ \__  \\   __\/  _ \_  __ \
# \     \____/        \/        \ /_____/ \    \_\  \  ___/|   |  \  ___/|  | \// __ \|  | (  <_> )  | \/
#  \______  /_______  /_______  /          \______  /\___  >___|  /\___  >__|  (____  /__|  \____/|__|   
#         \/        \/        \/                  \/     \/     \/     \/           \/                  

# Built for personal convenience.
# More commands to be added...

#  ___              ___                       _          _    ___ ___ ___   _ 
# | _ \_ _ ___ ___ / __|___ _ _  ___ _ _ __ _| |_ ___ __| |  / __/ __/ __| (_)
# |  _/ '_/ -_)___| (_ / -_) ' \/ -_) '_/ _` |  _/ -_) _` | | (__\__ \__ \  _ 
# |_| |_| \___|    \___\___|_||_\___|_| \__,_|\__\___\__,_|  \___|___/___/ (_)                                                                            


# Globalize help var
cmds = ("\n1. Start by entering class name"
			"\n2. Enter the type of styles to be included "
			"(seperated by commas)\n"
			"\nStyles:\n"
			"\ncenter.text"
			"\ncenter.div"
			"\nborder.round"
			"\nbgimg.center"
			"\nfix.footer"
			"\n\nMore to be included...\n")

# Center div object inclusion code
centerdiv = ('\ndisplay: block;'
					'\nmargin-left: auto;'
					'\nmargin-right: auto;'
					'\nwidth: 100%%;')

# Center text object [such as p element]
centertext = ('\ntext-align: center;')

# Round borders
roundbord = ('\nborder: 1px solid;'
				'\nborder-radius: 25px;')

# Fixed footer
fixfoot = ('\nposition:fixed;'
   '\nleft:0px;'
   '\nbottom:0px;'
   '\nheight:30px;'
   '\nwidth:100%;'
   '\nbackground:#999;')

# Empty bg name var
bgname = ""

def cssIndex():
	# Enter bg file name + format extension
	bgname = raw_input("The background image file: ")

	# Include that file in code
	bgimgcenter = ('\nbackground-image: url("%s");'
	'\nbackground-repeat: no-repeat;'
	'\nbackground-attachment: fixed;'
	'\nbackground-size: cover;' % (bgname))


#  ___                       _             _ 
# | _ \_ _ ___  __ ___ _____(_)_ _  __ _  (_)
# |  _/ '_/ _ \/ _/ -_|_-<_-< | ' \/ _` |  _ 
# |_| |_| \___/\__\___/__/__/_|_||_\__, | (_)
#                                  |___/     


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
			# Go to style method
			styling()


def styling():

	global fw
	global inArr
	global bgname

	# Occupy as many spaces as commands...
	inArr = ['','','','','']

	# Infinite loop
	while True:
		cmd2 = raw_input("\nClass = %s\n\nEnter styles seperated by comma (? for list): " % (cmd))
		# Re-display commands
		if cmd2 == "?":
			print cmds
		else:

			# File writing. Generate to text file
			fw = open('output.txt','w')
			
			# Check for css command
			check = cmd2.find("center.div")
			check2 = cmd2.find("center.text")
			check3 = cmd2.find("border.round")
			check4 = cmd2.find("bgimg.center")
			check5 = cmd2.find("fix.footer")

			# If not found then..
			if check != -1:
				# Add to array space
				inArr[0] = centerdiv

			# Check for second command
			if check2 != -1:
				# Include second command to array space
				inArr[1] = centertext

			# Check for third command
			if check3 != -1:
				# Include third command to array space
				inArr[2] = roundbord

			# Check for fourth command
			if check4 != -1:

				# Call function requiring input
				cssIndex()

				# Include fourth command to array space
				inArr[3] = bgimgcenter

			# Check for fifth command
			if check5 != -1:
				# Include fifth command to array space
				inArr[4] = fixfoot

			# Open selector
			print ('\n.%s { ' % (cmd))
			fw.writelines('\n.%s { ' % (cmd))

			# Generate according to input
			# Loop array length
			for i in inArr:
				# Include code
				fw.writelines(i)
				print i
				# End loop

			# Close selector
			print ('}\n')
			fw.writelines('}\n')
			fw.close()

# Call main routine
main()