thermometer = float(raw_input ("Pleace put in the number that you read on the thermometer? "))

if (thermometer < 96.0):

	thermometer = raw_input ("Are you cold? (yes/no) ")

	if (thermometer.lower() == "yes"):

		print ("Try dressing up for the winter to keep your temperature up.")

	elif (thermometer.lower() == "no"):

		print ("hmph, you must be cold blooded.")

elif (thermometer > 99.0):

	thermometer = raw_input ("Are you hot? (yes/no) ")

	if (thermometer.lower() == "yes"):

		print ("you might have a fever.")

	elif (thermometer.lower() == "no"):

		print ("you must be warm blooded.")

elif (thermometer == 98.5):

	print ("Congratulations, you are normal and healthy")

else:

	print ("pleace try a defarent number.")
