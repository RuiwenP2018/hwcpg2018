sentence = raw_input ("Pleace enter a sentence and separate each letter with a comma? ")

lower = sentence.lower()

words = lower.split(',')

numOfWords = len(words)

if (numOfWords%2 == 1):

	if ("llama" in words):

		print (' '.join(words))

elif ((numOfWords%2 == 1) or ((words[0]%2 == 1) and (words[1]%2 == 1) and (words[2]%2 == 1) and (words[3]%2 == 1) and (words[4]%2 == 1))):

	print ("That is odd. ")
