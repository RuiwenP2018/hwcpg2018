uin = raw_input("Enter your text: ")

##create lists to hold upper and lower case words
up_words = []
no_up_words = []

for i, word in enumerate(uin.strip().split()):
    if word.islower():
        no_up_words.append(word)
    else: 
        up_words.append(word)

print(up_words, no_up_words)
