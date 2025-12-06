#Project_1: create a project which create random number and guess the number , ( guessing game)

#random number
import random

#give random no between 1 to 5
target = random.randint(1,5)

while True:
    userChoice = (input("Guess the target or Quit(Q): "))
    #if click Q , then Quit
    if(userChoice=="Q"):
        break
    #convert to integer
    userChoice= int(userChoice)

    if(userChoice==target):
        print("success : correct Guess !")
        break
    elif(userChoice<target):
        print("your number was too small. Take a bigger guess")
    else:
        print("your number is too big. Take a smaller guess.")
print("--------GAME OVER. NO WAS: ", target)

#=============================

#Project -2: Random Password Generator

import random
import string

print(string.ascii_letters)
#ans: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(type( string.ascii_letters))
#ans: <class 'str'>
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)
# print(string.capwords)
val =random.choice([1,3,5])
print(val)
val1 =random.choice(['a','g','d'])
print(val1)

# create password:
# we have : 'A' to 'Z' , "a" to "z", 0 to 9 , /,\,|,%,-,?,!.

# we give all character in a list  , then generate password:

charValues =string.ascii_letters +string.punctuation+string.digits
print(charValues)

password_len=12
password=""
print(random.choice(charValues))

for i in range(password_len):
    password+= random.choice(charValues)

print("your random password is: " , password)


# === another way: using list comprehension
# list comprehension: [function for i in range (n) ]
#means: n times function will be call and  store data in list .

length = 10
#list comprehension using:
res = [random.choice(charValues)  for i in range(length)]
print(res)
#ans:['D', '"', '%', 'O', 'd', '#', '2', 'p', 'N', 'R']

#  create this as a string using  .join
# .join : concatenation the all character .


password1 = "".join ([random.choice(charValues)  for i in range(length)])

print(password1)  #ans: 7MQ7ZF~w"Z


password2 = "*".join ([random.choice(charValues)  for i in range(length)])

print(password2)  #ans: A*'*K*"*'*`*u*J*x*f
