sentence = raw_input ("Pleace enter a sentence that inclued upper and lower words in them. ")

upperWords = []

NonUpperWords = []

for i, word in enumerate (sentence.strip().split()):

	if word.isupper():

		upperWords.append(word)

	else:

		NonUpperWords.append(word)

print (upperWords)
