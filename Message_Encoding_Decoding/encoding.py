# Write a python program to translate a message into secret code language. 

# Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode
import string
import random

message = input("Enter a message:")
choose = int(input("For encoding the message press 1 & for decoding the message press 2:"))
list = message.split()
final = []
if choose == 1:
    for i in list:
        if len(i) < 3:
            reverse = i[::-1]
            final.append(reverse)
        elif len(i) >= 3:
            s1 = 3  # number of characters in the string.  
            s2 = 3
            # call random.choices() string module to find the string in lowercase .  
            ran1 = ''.join(random.choices(string.ascii_lowercase, k = s1))  
            ran2 = ''.join(random.choices(string.ascii_lowercase, k = s2))  
            i = i[1:] + i[0]   #1st letter will go to the end
            new = ran1+i+ran2
            final.append(new)

    encoded_message = ' '.join(final)
    print(encoded_message)
elif choose == 2:
    for i in list:
        if len(i) < 3:
            reverse = i[::-1]
            final.append(reverse)
        elif len(i) >= 3:
            i = i[-4]+ i[3:len(i)-4]
            final.append(i)
    decoded_message = ' '.join(final)
    print(decoded_message)
else:
    print("Enter a valid character...")