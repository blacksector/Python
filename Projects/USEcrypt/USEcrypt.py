# Wayne Kenney
# 5/3/2016
# USE (Unique String Encryption)

import os

# [?] Function for copying encrypted text to clipboard
def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

def decr():
	# Declare input string
	x = raw_input("\nEnter Message to Decrypt: ")

	# Array declared
	ar = []

	# For every Character in input string
	for c in x:
		n = ord(c)
		# if 'a' contained in input string then..
		if c == "a":
			# then append to array
			ar.append("z")
		elif c == "b":
			ar.append('a')
		elif c == "c":
			ar.append("b")
		elif c == "d":
			ar.append("c")
		elif c == "e":
			ar.append("d")
		elif c == "f":
			ar.append("e")
		elif c == "g":
			ar.append("f")
		elif c == "h":
			ar.append("g")
		elif c == "i":
			ar.append("h")
		elif c == "j":
			ar.append("i")
		elif c == "k":
			ar.append("j")
		elif c == "l":
			ar.append("k")
		elif c == "m":
			ar.append("l")
		elif c == "n":
			ar.append("m")
		elif c == "o":
			ar.append("n")
		elif c == "p":
			ar.append("o")
		elif c == "q":
			ar.append("p")
		elif c == "r":
			ar.append("q")
		elif c == "s":
			ar.append("r")
		elif c == "t":
			ar.append("s")
		elif c == "u":
			ar.append("t")
		elif c == "v":
			ar.append("u")
		elif c == "w":
			ar.append("v")
		elif c == "x":
			ar.append("w")
		elif c == "y":
			ar.append("x")
		elif c == "z":
			ar.append("y")
		elif c == "0":
			ar.append(" ")
		elif c == "1":
			ar.append(",")
		elif c == "2":
			ar.append(".")
		elif c == "3":
			ar.append("'")
		elif c == "4":
			ar.append("?")
		elif c == "5":
			ar.append("!")


	# Display all appended in array
	decrypted = ''.join(ar)

	# Display encrypted Text
	print "\nYour decrypted text: %s" % (decrypted)



def encr():
	# Declare input string
	x = raw_input("\nEnter Message to Encrypt: ")

	# Array declared
	ar = []

	# For every Character in input string
	for c in x:
		n = ord(c)
		# if 'a' contained in input string then..
		if c == "a" or c == "A":
			# then append to array
			ar.append('b')
		elif c == "b" or c == "B":
			ar.append("c")
		elif c == "c" or c == "C":
			ar.append("d")
		elif c == "d" or c == "D":
			ar.append("e")
		elif c == "e" or c == "E":
			ar.append("f")
		elif c == "f" or c == "F":
			ar.append("g")
		elif c == "g" or c == "G":
			ar.append("h")
		elif c == "h" or c == "H":
			ar.append("i")
		elif c == "i" or c == "I":
			ar.append("j")
		elif c == "j" or c == "J":
			ar.append("k")
		elif c == "k" or c == "K":
			ar.append("l")
		elif c == "l" or c == "L":
			ar.append("m")
		elif c == "m" or c == "M":
			ar.append("n")
		elif c == "n" or c == "N":
			ar.append("o")
		elif c == "o" or c == "O":
			ar.append("p")
		elif c == "p" or c == "P":
			ar.append("q")
		elif c == "q" or c == "Q":
			ar.append("r")
		elif c == "r" or c == "R":
			ar.append("s")
		elif c == "s" or c == "S":
			ar.append("t")
		elif c == "t" or c == "T":
			ar.append("u")
		elif c == "u" or c == "U":
			ar.append("v")
		elif c == "v" or c == "V":
			ar.append("w")
		elif c == "w" or c == "W":
			ar.append("x")
		elif c == "x" or c == "X":
			ar.append("y")
		elif c == "y" or c == "Y":
			ar.append("z")
		elif c == "z" or c == "Z":
			ar.append("a")
		elif c == " ":
			ar.append("0")
		elif c == ",":
			ar.append("1")
		elif c == ".":
			ar.append("2")
		elif c == "'":
			ar.append("3")
		elif c == "?":
			ar.append("4")
		elif c == "!":
			ar.append("5")

	# Display all appended in array
	encrypted = ''.join(ar)

	# Display encrypted Text
	print "\nYour encrypted text: %s" % (encrypted)

	print "\nEncrypted text copied to clipboard.\n"
	# Copy text to clipboard
	addToClipBoard(encrypted)


while(True):
	
	cmd = raw_input("Enter command (? for help): ")

	if cmd == "encrypt":
		encr()
	elif cmd == "decrypt":
		decr()
	elif cmd == "?" or cmd == "help":
		print "\n Commands:\n\n encrypt (input for encryption)\n decrypt (input for decryption\n"
	else:	
		print "\n [!] Invalid command. Try again. \n"