#!/usr/bin/python3

# This program says hello and asks for my name

print('Hello world.')
print('What is your name?')  #ask for their name
yourName = input()
print('Welcome to the machine ' + yourName)
print(yourName + ' is ' + str(len(yourName)) + ' characters long')
print('What is your age?') # ask for their age
yourAge = input()
print('You will be ' + str(int(yourAge) + 1) + ' in a year.')

