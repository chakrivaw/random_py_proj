#Code for random password generator
import random
letters =  [i for i in 'abcdefghiklmnopqrstuvwxyz'] + [k for k in 'abcdefghiklmnopqrstuvwxyz'.upper()]#letters used 
numbers = [i for i in '1234567890']#numbers used and defined
symbols = [i for i in '!@#$%^&*()']#symbols used and defined

no_of_letters = int(input('how may letters required?'))
no_of_numbers = int(input('no of numbers required?'))
no_of_symbols = int(input('no of symbols required?'))

password = ''#initialising a empty string to store password
#generation of letters
for i in range(no_of_letters):
    lp = random.randint(0,len(letters)-1)
    password += letters[lp]
#generation of numbers
for i in range(no_of_numbers):
    np = random.randint(0,len(numbers)-1)
    password += numbers[np]
#genration of symbols
for i in range(no_of_symbols):
    np = random.randint(0,len(symbols)-1)
    password += symbols[np]

ran = [i for i in range(len(password))] #etraction of indexes of password
random.shuffle(ran) #shuffling of indexes of password to generate more random password
rand_pass = '' #initialising an empty string to store final random password
#generating an random password from already generated sequenced password
for i in ran:
    rand_pass += password[i]
print(rand_pass)
