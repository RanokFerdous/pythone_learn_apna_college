# cheapter: 06 : function and recursion learning
# describe:
# function : block of statement that perform a specific task.

# def func_name ( param1, param2 ..) :   # function defination
# some call
# return val

# func_name ( arg1, arg2 ..) # function call

# ==================
# use function for : repeat /redundant reduce.
a =3
b=23

# def  -> define what work it will be done

# def sum ( param1, param2 ):
def sum ( a,b):
    sum= a+b
    print (sum)  # ans: 6
    return sum

print ( sum(2,4))  # ans: 6

# print ( sum( arg1, arg2,....))
print (sum(234,23))
print( sum(233,15))

# doing same work again and again .

#==========================

# another function example
# function defination
def cal_sum( a,b) :
    return a+b
# function call ,  3 and 2 are arguments.

sum1 = cal_sum(3,2)
print(sum1)  # ans: 05

#=========================

# without parameter function call

def print_hello ():
    print("hello")

print_hello()  # ANS: hello
print_hello()  # ANS: hello
print_hello()  # ANS: hello
print_hello()  # ANS: hello

# =================

# average of 3 number

def cal_avg (a,b,c):
    sum=a+b+c
    avg=(sum)/3
    print(avg)
    return avg

cal_avg(34,24,223)

#=============================

# some built in function are:
# 1. print(), 2.len() 3. type (), 4. range()

print ( "apnacollege")  # print is a function

# other type: user define function

print( "apnacollege","shradhakhapra")
# in function defination: sep=" " end="\n"
# sep -> take space between 2 object.
#o/p:  apnacollege shradhakhapra  ( space b/w 2 word for sep=" " property in defination)

#==================
#topic:  for print 2 print func in same line use: end=" "
print("apnacollege",end=" ") # sep=" "
print("shradhakhapra") #end="\n"

# o.p: apnacollege shradhakhapra
#===============
print("apnacollege",end="$") # sep="$"
print("shradhakhapra") #end="\n"
print("apnacollege",end=" ") # sep=" "
# o.p: apnacollege$shradhakhapra

#=========================

# topic : user define function , which we write , not built in .

#=====
# topic: default parameter

def cal_prod( a=1,b=3):
     print (a*b)
     return a*b
cal_prod()

def cal_prod( a,b=3):
     print (a*b)
     return a*b
cal_prod(1)

# we can write
def cal_prod( b,a=4):
     print (a*b)
     return a*b
cal_prod(1)

# but, below condition is wrong
# def cal_prod( a=2,b):  # it gives wrong
#      print (a*b)
#      return a*b
# cal_prod(1)
#================

# practie question on function topic:
# qs1 : WAF to print length of list. length is parameter
# qs2: WAF to print the elements of a list in a single line. ( list is the parameter)
# qs3: WAF to find the factorial of n . ( n is the parameter)
# qs4: WAF to eonvert USD to INR .

# ANS:
# ans: qs1:

cities =["delhi","gurgaon","noida","mumbai","chennai"]

def print_len(list) :   # here,pass a list
    print(len(list))

print_len(cities)  # ans: 05

# qs2: print all items in single line
heroes= ["thor","ironman","captain","shaktiman"]

def print_list1 (list):
    for item in list:
        print(item,end=" ")

print_list1(heroes)
#ans: thor ironman captain shaktiman

print()  # give : a new line
#qs 3: WAF to find the factorial of n .
# 5! = 5*4*3*2*1

def cal_fac( n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)  #ans: 120
cal_fac(5)

#================
# qs 4: USD to INR

def converter ( usd_val):
   inr_val = usd_val * 83
   print(usd_val,"USD =", inr_val,"INR")

converter(2)

#========================
