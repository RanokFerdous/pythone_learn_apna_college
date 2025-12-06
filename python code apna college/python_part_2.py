
#condition
#python is an indentation  take 4 space gap  before statement.


age =23
if( age>18):
    print("vote")
    print("hurrah, i can vote")
elif( age==18 ):
    print("can vote")
else :
    print("not give vote")

#traffic Light code

light =input("light color : ")

if(light=="red"):
    print("stop")
elif( light=="yellow"):
    print("look")
elif(light=="green"):
    print("go")
else:
    print("light is broken")

#another condition check
A=int( input("A : "))
G=input( "M/F :")

if( (A==1 or A ==2) and G=="M"):
    print("fee is 100")
elif(A==3 or A==4 or G=="F"):
    print("fee is 200")
elif( A==5 and G=="M"):
    print ("fee is 300")
else:
    print( "no fee")


# ternary operator
#process 1:
food =input("food : ")
eat="Yes" if food=="cake" else "no"
print(eat)

#process: 2

food1 =input("food1: ")

print("sweet") if food1=="cake" or food1=="jalebi" else print ("not sweet")

#**topic : clever if

# syntax : <var> =(false_val, ture_val) [<condition>]

age2 =int(input("age :"))

vote =("yes","not")[age<18]   # 4 line code now just in 1 line
print(vote)

#another example
sal=float (input("salary : "))
tax=sal*(0.1, 0.2)[sal>50000]
print(tax)

#relational operator
a=20
b=50
print(a==b) #ans: False
print(a!=b) #ans: True

#assignment operator : ==,!=, +=,%=
num=20
num+=40
print("num : ",num)  #ans: 60
num**=3
print("num : ",num)  #216000

#logical operator : and, or, not
print(not False)  # ans: True
print(not True) #ans: False

a=50
b=30
print (not (a>b))  # ans: False

val1=True
val2=True
print("and operator :", val1 and val2) # ans: True
print("or operator :", val1 or val2) # ans: True
print("OR operator: ", (a==b) or (a>b)) #ans: True


#==========================
#Type convertion : *** automatically will be in pythone

a=2
b=4.32
sum=a+b # ans: 6.32 (2.0+4.32=6.32) ( convert int to float)

#Type casting
c="2" # this is string
d=4.32
# print( a+b )  this is wrong
e=int(c)
print(d+e) # ans: 6.32

f=float("30")   # convert string to float
print(d+f)   #34.32

# but string can't work like
#g= float( "string")
#print( g+f)   it will be worng.

a=3.14
a1=str(a)
print(type(a))   #<class 'float'>
#====


#######  input taking
name2= input()
print(name2)

name3= input( "enter your name3:")
print( name3)
print( "my name3 is : ", name3)

# ***** always our input is an string ( if we not specify )

val= input( "enter some value : ") #24
print( type (val), val) # <class 'str'>24

#so , using type casting for specify the type


int_val = int(input("enter some value: "))  # 34   ( if give 43.32 , 43.6, 73.2  then give wrong)
print(type(int_val), int_val) # <class 'int'> 34

float_val=float(input("enter some value: "))   #25
print(type(float_val),float_val) # <class 'float'>25.0


#-----------------------------
name=input( "enter your name: ")
age= int( input( "enter your age : "))
marks =float(input( "enter your marks: "))

print( "welcome", name)
print("age is :", age)
print("marks is : ", marks)

