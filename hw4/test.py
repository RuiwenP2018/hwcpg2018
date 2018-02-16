name = raw_input('Please supply you whole name (first, middle, last): ')

upper_name = name.upper()
back_name = name[::-1]

names = name.split()
first = names[0]
middle = names[1]
last = names[2]

center = len(middle)/2
midfir = middle[0:center]
midlas = middle[-center:]
whole = (first + " " + midfir + "-BOB-" + midlas + " " + last)

print (upper_name)
print (back_name)
print (whole)
