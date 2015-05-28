prompt = "> "
lyric_1 = "\nYou remind me of the babe\n"
lyric_2 = "\nThe babe with the power\n"
lyric_3 = "\nThe power of voodoo\n"
lyric_4 = "\nYou do\n"

# Oh god, make it stop.
while True:
	
	print lyric_1
	ans = raw_input(prompt)
	while (ans != "what babe"):
		print lyric_1
		ans = raw_input(prompt)

	print lyric_2
	ans = raw_input(prompt)
	while (ans != "what power"):

		print lyric_2
		ans = raw_input(prompt)

	print lyric_3
	ans = raw_input(prompt)
	while (ans != "who do"):
		print lyric_3
		ans = raw_input(prompt)
	
	print lyric_4
	ans = raw_input(prompt)
	while (ans != "do what"):
		print lyric_3
		ans = raw_input(prompt)