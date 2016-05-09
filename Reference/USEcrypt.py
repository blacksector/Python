# Wayne Kenney
# USE (Unique String Encryption)


def decr():
	# Declare input string
	x = raw_input("Enter Message to Decrypt: ")

	# Array declared
	ar = []

	# For every Character in input string
	for c in x:
		n = ord(c)
		# if 'a' contained in input string then..
		if c == "b":
			# then append to array
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

	# Display all appended in array
	decrypted = ''.join(ar)

	# Display encrypted Text
	print "Your decrypted text: %s" % (decrypted)

	d = raw_input("OK?")



def encr():
	# Declare input string
	x = raw_input("Enter Message to Encrypt: ")

	# Array declared
	ar = []

	# For every Character in input string
	for c in x:
		n = ord(c)
		# if 'a' contained in input string then..
		if c == "a":
			# then append to array
			ar.append('b')
		elif c == "b":
			ar.append("c")
		elif c == "c":
			ar.append("d")
		elif c == "d":
			ar.append("e")
		elif c == "e":
			ar.append("f")
		elif c == "f":
			ar.append("g")
		elif c == "g":
			ar.append("h")
		elif c == "h":
			ar.append("i")
		elif c == "i":
			ar.append("j")
		elif c == "j":
			ar.append("k")
		elif c == "k":
			ar.append("l")
		elif c == "l":
			ar.append("m")
		elif c == "m":
			ar.append("n")
		elif c == "n":
			ar.append("o")
		elif c == "o":
			ar.append("p")
		elif c == "p":
			ar.append("q")
		elif c == "q":
			ar.append("r")
		elif c == "r":
			ar.append("s")
		elif c == "s":
			ar.append("t")
		elif c == "t":
			ar.append("u")
		elif c == "u":
			ar.append("v")
		elif c == "v":
			ar.append("w")
		elif c == "w":
			ar.append("x")
		elif c == "x":
			ar.append("y")
		elif c == "y":
			ar.append("z")
		elif c == "z":
			ar.append("0")
		elif c == " ":
			ar.append("0")

	# Display all appended in array
	encrypted = ''.join(ar)

	# Display encrypted Text
	print "Your encrypted text: %s" % (encrypted)

	d = raw_input("OK?")


cmd = raw_input("Enter command: ")
if cmd == "encrypt":
	encr()
elif cmd == "decrypt":
	decr()