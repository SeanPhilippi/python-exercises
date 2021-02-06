def is_pangram(sentence):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	alpha_map = {}
	pangram = True
	for ch in alphabet:
		alpha_map[ch] = 0

	for ch in sentence.lower():
		if ch in alpha_map:
			alpha_map[ch] += 1
	
	for count in list(alpha_map.values()):
		if count == 0:
			pangram = False
	return pangram
