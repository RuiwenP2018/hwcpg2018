#problem for change the name.
##put all the name in upper case.

name = raw_input ("pleace enter you first, middle ,and the last name. ")

upper_name = name.upper()

print (upper_name)

##revers the name

#revers = name.split (" ")

#numberofwords = len(revers)

#newwords = revers[0,(numberofwords),-1]

#sentence = "".join(newwords)

#print (sentence)

newname = " ".join(word[::-1] for word in name.split())

print (newname)

##add a -BOB- in the middle.

names = name.split()

first = names[0]

middle = names[1]

last = names[2]

final = len(name)-1

middlename = len(middle)/2

midfir = middle[0:middlename]

midlas = middle[middlename:final+1]

finalname = (first +" "+ midfir + "-BOB-" + midlas +" "+ last)

print (finalname)
