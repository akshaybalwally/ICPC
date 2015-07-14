def isPalindrome(word):
	for i in range(0,len(word)/2 + 1):
		if word[i] != word[len(word) - (i+1)]:
			return False
	return True

def run(words):
	for word1 in words:
		for word2 in words:
			if word1 != word2:
				if isPalindrome(word1+word2):
					return word1+word2
					
				elif isPalindrome(word2+word1):
					return word2+word1
	return '0'
					



f = open('input.txt', 'r')
cases = int(f.readline())
#print cases
for case in range(0,cases):
	
	wordNumber = int(f.readline())
	words = []
	for wordnum in range(0,wordNumber):
		string = f.readline()
		#print string
		x = len(string)
		if string[x-1] == '\n':
			string = string[0:x-1]
		words.append(string)
	print run(words)
	
	#print words	
