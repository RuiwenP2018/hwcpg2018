#display the sentence word by word

##s = raw_input ("pleace put in one sentence? ")

##for word in s.split():

##	print (word)

s = raw_input ("pleace put in one sentence? ")

words = s.split()

sentence = "\n".join(words)

print (sentence)
