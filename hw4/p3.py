#Generate a random number from the two given numbers.

import random

print ("pleace give me two random numbers.")

min = raw_input("the smaller number ")

max = raw_input("the bigger number ")

number = random.randint (int(min), int(max))

print (number)

number2 = random.randint (int(min), int(max))

print (number2)
